# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The eos vlans fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

import re

from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.vlans.vlans import (
    VlansArgs,
)


class VlansFacts(object):
    """The eos vlans fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = VlansArgs.argument_spec
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
        """Populate the facts for vlans
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not data:
            data = connection.get("show running-config | section ^vlan")

        # split the config into instances of the resource
        resource_delim = "vlan"
        find_pattern = r"(?:^|\n)%s.*?(?=(?:^|\n)%s|$)" % (
            resource_delim,
            resource_delim,
        )
        resources = [p.strip() for p in re.findall(find_pattern, data, re.DOTALL)]

        objs = []
        for resource in resources:
            if resource:
                obj = self.render_config(self.generated_spec, resource)
                if obj:
                    objs.extend(obj)

        ansible_facts["ansible_network_resources"].pop("vlans", None)
        facts = {"vlans": []}
        if objs:
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )
            facts["vlans"] = [utils.remove_empties(cfg) for cfg in params["config"]]

        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        config = deepcopy(spec)
        vlans = []

        parse_result = utils.parse_conf_arg(conf, "vlan")
        if not parse_result.split(" ")[0].isalpha():
            vlan_list = vlan_to_list(parse_result)
            for vlan in vlan_list:
                config["vlan_id"] = vlan
                config["name"] = utils.parse_conf_arg(conf, "name")
                config["state"] = utils.parse_conf_arg(conf, "state")
                if config["state"] is None:
                    config["state"] = "active"
                vlans.append(utils.remove_empties(config))

        return vlans


def vlan_to_list(vlan_str):
    vlans = []
    for vlan in vlan_str.split(","):
        if "-" in vlan:
            start, stop = vlan.split("-")
            vlans.extend(range(int(start), int(stop) + 1))
        else:
            vlans.append(int(vlan))

    return vlans
