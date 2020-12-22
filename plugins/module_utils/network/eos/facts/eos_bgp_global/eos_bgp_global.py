# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

"""
The eos eos_bgp_global fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.rm_templates.eos_bgp_global import (
    Eos_bgp_globalTemplate,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.eos_bgp_global.eos_bgp_global import (
    Eos_bgp_globalArgs,
)

class Eos_bgp_globalFacts(object):
    """ The eos eos_bgp_global facts class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Eos_bgp_globalArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for Eos_bgp_global network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        objs = []

        if not data:
            data = connection.get()

        # parse native config using the Eos_bgp_global template
        eos_bgp_global_parser = Eos_bgp_globalTemplate(lines=data.splitlines())
        objs = eos_bgp_global_parser.parse()

        ansible_facts['ansible_network_resources'].pop('eos_bgp_global', None)

        params = utils.remove_empties(
            utils.validate_config(self.argument_spec, {"config": objs})
        )

        facts['eos_bgp_global'] = params['config']
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts
