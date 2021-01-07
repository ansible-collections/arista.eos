# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

"""
The eos bgp_af fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.rm_templates.bgp_af import (
    Bgp_afTemplate,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.bgp_af.bgp_af import (
    Bgp_afArgs,
)
import re

import q

class Bgp_afFacts(object):
    """ The eos bgp_af facts class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Bgp_afArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_config(self, connection):
        """Wrapper method for `connection.get()`
        This method exists solely to allow the unit test framework to mock device connection calls.
        """
        return connection.get("show running-config | section bgp ")

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for Bgp_af network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        objs = []

        if not data:
            data = self.get_config(connection)

        # remove global configs from bgp_af
        bgp_af_config = []
        start = False
        for bgp_line in data.splitlines():
            if re.search(r'router bgp \S+|vrf \S+', bgp_line):
                bgp_af_config.append(bgp_line)
            if start:
                bgp_af_config.append(bgp_line)
            if "address-family" in bgp_line:
                bgp_af_config.append(bgp_line)
                start = True
            if start and '!' in bgp_line:
                start = False

        q(bgp_af_config)
        # parse native config using the Bgp_af template
        bgp_af_parser = Bgp_afTemplate(lines=bgp_af_config)
        objs = bgp_af_parser.parse()
        q(objs)
        if objs:
            global_vals = objs.get("vrfs", {}).pop("vrf_", {})
            for key, value in iteritems(global_vals):
                objs[key] = value
            if "vrfs" in objs:
                q(objs["vrfs"])
                objs["vrfs"] = list(objs["vrfs"].values())
                for vrf in objs["vrfs"]:
                    if "address_family" in vrf:
                        vrf["address_family"] = list(vrf["address_family"].values())
                        for af in vrf["address_family"]:
                            if "neighbor" in af:
                                af["neighbor"] = list(af["neighbor"].values())
                            if "network" in af:
                                af["network"] = list(af["network"].values())

            if "address_family" in objs:
                objs["address_family"] = list(objs["address_family"].values())
                for af in objs["address_family"]:
                    if "neighbor" in af:
                        af["neighbor"] = list(af["neighbor"].values())
                    if "network" in af:
                        af["network"] = list(af["network"].values())



        ansible_facts['ansible_network_resources'].pop('bgp_af', None)

        params = utils.remove_empties(
            utils.validate_config(self.argument_spec, {"config": objs})
        )

        facts['bgp_af'] = params.get("config", [])
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts
