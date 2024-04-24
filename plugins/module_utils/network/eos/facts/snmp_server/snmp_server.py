# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The eos snmp_server fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.snmp_server.snmp_server import (
    Snmp_serverArgs,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.rm_templates.snmp_server import (
    Snmp_serverTemplate,
)


class Snmp_serverFacts(object):
    """The eos snmp_server facts class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Snmp_serverArgs.argument_spec

    def get_config(self, connection):
        """Wrapper method for `connection.get()`
        This method exists solely to allow the unit test framework to mock device connection calls.
        """
        return connection.get("show running-config | section snmp-server")

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for Snmp_server network resource

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

        # parse native config using the Snmp_server template
        snmp_server_parser = Snmp_serverTemplate(
            lines=data.splitlines(),
            module=self._module,
        )
        objs = snmp_server_parser.parse()
        if objs:
            if "communities" in objs:
                objs["communities"] = sorted(
                    list(objs["communities"].values()),
                    key=lambda k, sk="name": k[sk],
                )
            if "groups" in objs:
                objs["groups"] = sorted(
                    list(objs["groups"].values()),
                    key=lambda k, sk="group": k[sk],
                )
            if "hosts" in objs:
                objs["hosts"] = sorted(
                    list(objs["hosts"].values()),
                    key=lambda k, sk="host": k[sk],
                )
            if "acls" in objs:
                objs["acls"] = sorted(
                    list(objs["acls"].values()),
                    key=lambda k, sk="afi": k[sk],
                )
            if "users" in objs:
                objs["users"] = sorted(
                    list(objs["users"].values()),
                    key=lambda k, sk="user": k[sk],
                )
            if "views" in objs:
                objs["views"] = sorted(
                    list(objs["views"].values()),
                    key=lambda k, sk="view": k[sk],
                )
            if "vrfs" in objs:
                objs["vrfs"] = sorted(
                    list(objs["vrfs"].values()),
                    key=lambda k, sk="vrf": k[sk],
                )
        else:
            objs = {}

        ansible_facts["ansible_network_resources"].pop("snmp_server", None)

        params = utils.remove_empties(
            snmp_server_parser.validate_config(
                self.argument_spec,
                {"config": objs},
                redact=True,
            ),
        )

        facts["snmp_server"] = params.get("config", {})
        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts
