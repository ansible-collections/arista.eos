#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function
__metaclass__ = type

"""
The eos_bgp_af config file.
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
from ansible_collections.arista.eos.plugins.module_utils.network.eos.rm_templates.bgp_af import (
    Bgp_afTemplate,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    get_from_dict,
)

import q
class Bgp_af(ResourceModule):
    """
    The eos_bgp_af config class
    """

    def __init__(self, module):
        super(Bgp_af, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="bgp_af",
            tmplt=Bgp_afTemplate(),
        )
        self.parsers = [
            "router",
            "address_family",
            "vrf",
            "bgp_params_additional_paths",
            "bgp_params.nexthop_address_family",
            "bgp_params.nexthop_unchanged",
            "bgp_params.redistribute_internal",
            "bgp_params.route",
            "graceful_restart",
            "neighbor.activate",
            "neighbor.additional_paths",
            "neighbor.default_originate",
            "neighbor.graceful_restart",
            "neighbor.next_hop_unchanged",
            "neighbor.next_hop_address_family",
            "neighbor.prefix_list",
            "neighbor.route_map",
            "neighbor.weight",
            "neighbor.encapsulation",
            "network",
            "redistribute"
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
        wantd = {}
        haved = {}

        if self.want:
            wantd = { self.want["as_number"]: self.want }
        if self.have:
            haved = { self.have["as_number"]: self.have }

        # turn all lists of dicts into dicts prior to merge
        for entry in wantd, haved:
            self._bgp_af_list_to_dict(entry)
        
        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            wantd = dict_merge(haved, wantd)
            if len(wantd.keys()) > 1:
                self._module.fail_json(
                    msg="Only one bgp instance is allowed per device"
                )
                wantd = {}
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
            self._compare(want=want, have=haved.pop(k, {}))

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Bgp_af network resource.
        """
        q("COM", want, have)
        for name, entry in iteritems(want):
            q(have.get(name))
            if name != "as_number":
                self._compare_vrfs({name: entry}, {name: have.get(name, {})})
                self._compare_af({name: entry}, {name: have.get(name, {})})
            # self.compare(parsers=self.parsers, want={name: entry}, have={name: have.pop(name, None)})

        #for name, entry in iteritems(have):
        #    self.compare(parsers=self.parsers, want={}, have={name: have.get(name)})

        if self.commands and "router bgp" not in self.commands[0]:
            self.commands.insert(
                0, self._tmplt.render({"as_number": want['as_number']}, "router", False)
            )

    def _compare_vrfs(self, want, have):
        wvrfs = want.get("vrfs", {})
        hvrfs = have.get("vrfs", {})
        q('VRF', wvrfs, hvrfs)
        for name, entry in iteritems(wvrfs):
            begin = len(self.commands)
            self._compare_af(entry, hvrfs.pop(name, {}))
            q(self.commands)
            if (
                len(self.commands) != begin
            ):
                self.commands.insert(
                    begin, self._tmplt.render(entry, "vrf", False)
                )
                self.commands.append("exit")
        #for name, entry in iteritems(haf):
        #    self.addcmd(entry, "network", True)
        #    have.pop("network", {})

    def _compare_af(self, want, have):
        waf = want.get("address_family", {})
        haf = have.get("address_family", {})
        q("AF" , waf, haf, have)
        for name, entry in iteritems(waf):
            begin = len(self.commands)
            self._compare_lists(entry, have=haf.get(name, {}))
            self._compare_neighbor(entry, have=haf.get(name, {}))
            self.compare(
                parsers=self.parsers, want=entry, have=haf.pop(name, {})
            )
            if (
                len(self.commands) != begin
            ):
                self.commands.insert(
                    begin, self._tmplt.render(entry, "address_family", False)
                )
                self.commands.append("exit")
            
        #for name, entry in iteritems(haf):
        #    self.addcmd(entry, "network", True)
        #    have.pop("network", {})

    def _compare_neighbor(self, want, have):
        parsers = [
            "neighbor.activate",
            "neighbor.additional_paths",
            "neighbor.default_originate",
            "neighbor.graceful_restart",
            "neighbor.next_hop_unchanged",
            "neighbor.next_hop_address_family",
            "neighbor.prefix_list",
            "neighbor.route_map",
            "neighbor.weight",
            "neighbor.encapsulation",
        ]
        wneigh = want.get("neighbor", {})
        hneigh = have.get("neighbor", {})
        for name, entry in iteritems(wneigh):
            self.compare(parsers=parsers, want={"neighbor": entry}, have={"neighbor": hneigh.pop(name, {})})
        for name, entry in iteritems(hneigh):
            self.compare(parsers=parsers, want={}, have=entry)


    def _compare_lists(self, want, have):
        parsers = [
            "network",
            "redistribute",
        ]
        q("***********************")
        q(want, have)

        for attrib in ["redistribute", "network"]:
            wdict = get_from_dict(want, attrib) or {}
            hdict = get_from_dict(have, attrib) or {}
            q(attrib, wdict, hdict)
            for key, entry in iteritems(wdict):
              q(key, entry)
              #  if entry != hdict.pop(key, {}):
              #      self.addcmd(entry, attrib, False)
              # self.compare(parsers=parsers, want={ attrib: entry }, have=hdict.pop(key, {}))
              if entry != hdict.pop(key, {}):
                self.addcmd(entry, attrib, False)
            # remove remaining items in have for replaced
            for entry in hdict.values():
                self.addcmd(entry, attrib, True)
                #self.compare(parsers=parsers, want={}, have=entry)
        q("**************")

    def _bgp_af_list_to_dict(self, entry):
        for name, proc in iteritems(entry):
            if "address_family" in proc:
                proc["address_family"] = {
                    entry["afi"]: entry
                    for entry in proc.get("address_family", [])
                }
                self._bgp_af_list_to_dict(proc["address_family"])

            if "vrfs" in proc:
                proc["vrfs"] = {
                    entry["name"]: entry
                    for entry in proc.get("vrfs", [])
                }
                self._bgp_af_list_to_dict(proc["vrfs"])

            if "neighbor" in proc:
                proc["neighbor"] = {
                    entry["peer"]: entry
                    for entry in proc.get("neighbor", [])
                }
            if "network" in proc:
                proc["network"] = {
                    entry["address"]: entry
                    for entry in proc.get("network", [])
                }
            if "redistribute" in proc:
                proc["redistribute"] = {
                    entry["protocol"]: entry
                    for entry in proc.get("redistribute", [])
                }

