#
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function
__metaclass__ = type

"""
The eos_bgp_global config file.
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
from ansible_collections.arista.eos.plugins.module_utils.network.eos.rm_templates.bgp_global import (
    Bgp_globalTemplate,
)


class Bgp_global(ResourceModule):
    """
    The eos_bgp_global config class
    """

    def __init__(self, module):
        super(Bgp_global, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="bgp_global",
            tmplt=Bgp_globalTemplate(),
        )
        self.parsers = [
            "router",
            "vrf",
            "aggregate_address",
            "bgp_params_additional_paths",
            "bgp_params_advertise_inactive",
            "bgp_params_allowas_in",
            "bgp_params_always_compare_med",
            "bgp_params_asn",
            "bgp_params_auto_local_addr",
            "bgp_params_bestpath_as_path",
            "bgp_params_bestpath_ecmp_fast",
            "bgp_params_bestpath_med",
            "bgp_params_bestpath_skip",
            "bgp_params_tie_break",
            "bgp_params_client_to_client",
            "bgp_params_cluster_id",
            "bgp_params_confederation",
            "bgp_params_control_plane_filter",
            "bgp_params_convergence",
            "bgp_params_default",
            "bgp_params.enforce_first_as",
            "bgp_params.host_routes",
            "bgp_params.labelled_unicast",
            "bgp_params.listen_limit",
            "bgp_params.listen_range",
            "bgp_params.log_neighbor_changes",
            "bgp_params.missing_policy",
            "bgp_params.monitoring",
            "bgp_params.nexthop_unchanged",
            "bgp_params.redistribute_internal",
            "bgp_params.route",
            "bgp_params.route_reflector",
            "bgp_params.transport",
            "default_metric",
            "distance",
            "graceful_restart",
            "graceful_restart_helper",
            "acccess_group",
            "maximum_paths",
            "monitoring",
            "neighbor.additional_paths",
            "neighbor.allowas_in",
            "neighbor.auto_local_addr",
            "neighbor.default_originate",
            "neighbor.description",
            "neighbor.dont_capability_negotiate",
            "neighbor.ebgp_multihop",
            "neighbor.enforce_first_as",
            "neighbor.export_localpref",
            "neighbor.fall_over",
            "neighbor.graceful_restart",
            "neighbor.graceful_restart_helper",
            "neighbor.idle_restart_timer",
            "neighbor.import_localpref",
            "neighbor.link_bandwidth",
            "neighbor.local_as",
            "neighbor.local_v6_addr",
            "neighbor.maximum_accepted_routes",
            "neighbor.maximum_received_routes",
            "neighbor.metric_out",
            "neighbor.monitoring",
            "neighbor.next_hop_self",
            "neighbor.next_hop_unchanged",
            "neighbor.next_hop_v6_addr",
            "neighbor.out_delay",
            "neighbor.remote_as",
            "neighbor.remove_private_as",
            "neighbor.peer_group",
            "neighbor.prefix_list",
            "neighbor.route_map",
            "neighbor.route_reflector_client",
            "neighbor.route_to_peer",
            "neighbor.send_community_add",
            "neighbor.send_community_link_bandwidth",
            "neighbor.send_community_extended",
            "neighbor.send_community_remove",
            "neighbor.send_community_standard",
            "neighbor.send_community",
            "neighbor.shutdown",
            "neighbor.soft_reconfiguration",
            "neighbor.transport",
            "neighbor.timers",
            "neighbor.ttl",
            "neighbor.update_source",
            "neighbor.weight",
            "network",
            "route_target",
            "router_id",
            "shutdown",
            "timers",
            "ucmp_fec",
            "ucmp_link_bandwidth",
            "ucmp_mode",
            "update",
            "vlan",
            "vlan_aware_bundle"
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
            self._bgp_global_list_to_dict(entry)

        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            wantd = dict_merge(haved, wantd)

        # if state is deleted, empty out wantd and set haved to wantd
        if self.state == "deleted":
            haved = {
                k: v for k, v in iteritems(haved) if k in wantd or not wantd
            }
            wantd = {}

            data = self._connection.get("show running-config | section bgp ")
            for config_line in data.splitlines():
                if 'address-family' in config_line:
                    self._module.warn(" Please use bgp_af module to delete the address family\
                        configurations before deleting the instance ")
                    haved = {}
                    break
            for num, entry in iteritems(haved):
                self.commands.append(
                    self._tmplt.render({"as_number": num}, "router", True)
                )


        # remove superfluous config for overridden
        # if self.state in ["overridden"]:
        #    for k, have in iteritems(haved):
        #        if have.get('address_family'):
        #            self._module.warn(" Please use bgp_af module to override the address family configurations")
        #            haved = {}
        #        elif have.get('vrfs'):
        #            for name, vrf_entry in iteritems(have['vrfs']):
        #                q(vrf_entry)
        #                if vrf_entry.get('address_family'):
        #                    self._module.warn(" Please use bgp_af module to override the address family configurations")
        #                    haved = {}
        #                    break
        #        else:
        #            if k not in wantd:
        #                self._compare(want={}, have=have)


        for k, want in iteritems(wantd):
            self._compare(want=want, have=haved.pop(k, {}))

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Bgp_global network resource.
        """
        for name, entry in iteritems(want):

            self.compare(parsers=self.parsers, want={name: entry}, have={name: have.pop(name, None)})

        for name, entry in iteritems(have):
            self.compare(parsers=self.parsers, want={}, have={name: have.get(name)})

        if self.commands and "router bgp" not in self.commands[0]:
            self.commands.insert(
                0, self._tmplt.render({"as_number": want['as_number']}, "router", False)
            )

    def _bgp_global_list_to_dict(self, entry):
        for name, proc in iteritems(entry):
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

            if "aggregate_address" in proc:
                proc["aggregate_address"] = {
                    entry["address"]: entry
                    for entry in proc.get("aggregate_address", [])
                }

                        
            if "vrfs" in proc:
                proc["vrfs"] = {
                    entry["vrf"]: entry
                    for entry in proc.get("vrfs", [])
                }
                self._bgp_global_list_to_dict(proc["vrfs"])

                
