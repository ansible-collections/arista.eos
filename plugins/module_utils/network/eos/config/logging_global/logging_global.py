#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The eos_logging_global config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.resource_module import (
    ResourceModule,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.facts.facts import (
    Facts,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.rm_templates.logging_global import (
    Logging_globalTemplate,
)

import q


class Logging_global(ResourceModule):
    """
    The eos_logging_global config class
    """

    def __init__(self, module):
        super(Logging_global, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="logging_global",
            tmplt=Logging_globalTemplate(),
        )
        self.parsers = [
            "buffered",
            "console",
            "event",
            "facility",
            "console",
            "format",
            "format.timestamp",
            "level",
            "monitor",
            "on",
            "persistent",
            "policy",
            "relogging_interval",
            "repeat_messages",
            "src_interface",
            "synchronous",
            "trap",
        ]

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """ Generate configuration commands to send based on
            want, have and desired state.
        """

        wantd = {"logging_global": self.want}
        haved = {"logging_global": self.have}
        # turn all lists of dicts into dicts prior to merge
        for entry in wantd["logging_global"], haved["logging_global"]:
            self._logging_global_list_to_dict(entry)
        q(wantd, haved)
        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            wantd = dict_merge(haved, wantd)

        # if state is deleted, empty out wantd and set haved to wantd
        if self.state == "deleted":
            haved = {
                k: v for k, v in iteritems(haved) if k in wantd or not wantd
            }
            wantd = {}

        # remove superfluous config for overridden and deleted
        if self.state in ["overridden", "deleted"]:
            for k, have in iteritems(haved):
                if k not in wantd:
                    self._compare(want={}, have=have)

        for k, want in iteritems(wantd):
            q(k, want)
            self._compare(want=want, have=haved.pop(k, {}))

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Logging_global network resource.
        """
        self._hosts_compare(want=want, have=have)
        self._vrfs_compare(want=want, have=have)
        self.compare(parsers=self.parsers, want=want, have=have)

    def _hosts_compare(self, want, have):
        host_want = want.get("hosts", {})
        host_have = have.get("hosts", {})
        q(host_want, host_have)
        for name, entry in iteritems(host_want):

            h = {}
            if host_have:
                h = {"hosts": {name: host_have.pop(name, {})}}
            self.compare(parsers="host", want={"hosts": {name: entry}}, have=h)
        for name, entry in iteritems(host_have):
            self.compare(parsers="host", want={}, have=entry)

    def _vrfs_hosts_compare(self, vrf, want, have):
        host_want = want.get("hosts", {})
        host_have = have.get("hosts", {})
        for name, entry in iteritems(host_want):
            h = {}
            if host_have:
                h = {
                    "vrfs": {
                        "name": vrf,
                        "hosts": {name: host_have.pop(name, {})},
                    }
                }
            w = {"vrfs": {"name": vrf, "hosts": {name: entry}}}
            self.compare(parsers="vrf.host", want=w, have=h)
        for name, entry in iteritems(host_have):
            self.compare(
                parsers="vrf.host",
                want={},
                have={"vrfs": {"name": vrf, "hosts": {name: entry}}},
            )

    def _vrfs_compare(self, want, have):
        vrf_want = want.get("vrfs", {})
        vrf_have = have.get("vrfs", {})
        for name, entry in iteritems(vrf_want):
            self._vrfs_hosts_compare(
                name, want=entry, have=vrf_have.pop(name, {})
            )
            if entry.get("source_interface"):
                if vrf_have.get(name):
                    h = {
                        "vrfs": {
                            "name": name,
                            "source_interface": vrf_have[name].pop(
                                "source_interface", ""
                            ),
                        }
                    }
                w = {
                    "vrfs": {
                        "name": name,
                        "source_interface": entry["source_interface"],
                    }
                }
            self.compare(
                parsers="vrf.source_interface",
                want={"hosts": {name: entry}},
                have=h,
            )
        for name, entry in iteritems(vrf_have):
            self.compare(want={}, have=entry)

    def _logging_global_list_to_dict(self, entry):
        q(entry)
        if "hosts" in entry:
            hosts_dict = {}
            for el in entry["hosts"]:
                hosts_dict.update({el["name"]: el})
            entry["hosts"] = hosts_dict

        if "vrfs" in entry:
            vrf_dict = {}
            for el in entry["vrfs"]:
                vrf_dict.update({el["name"]: el})
            entry["vrfs"] = vrf_dict
            self._logging_global_list_to_dict(entry["vrfs"])
