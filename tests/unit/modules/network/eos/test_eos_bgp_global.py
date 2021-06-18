#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.arista.eos.tests.unit.compat.mock import patch
from ansible_collections.arista.eos.plugins.modules import eos_bgp_global
from ansible_collections.arista.eos.tests.unit.modules.utils import (
    set_module_args,
)
from .eos_module import TestEosModule, load_fixture


class TestEosBgpglobalModule(TestEosModule):
    module = eos_bgp_global

    def setUp(self):
        super(TestEosBgpglobalModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection"
        )
        self.get_resource_connection_config = (
            self.mock_get_resource_connection_config.start()
        )

        self.mock_execute_show_command = patch(
            "ansible_collections.arista.eos.plugins.module_utils.network.eos.facts.bgp_global.bgp_global.Bgp_globalFacts.get_config"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

        self.mock_execute_show_command_config = patch(
            "ansible_collections.arista.eos.plugins.module_utils.network.eos.config.bgp_global.bgp_global.Bgp_global._get_config"
        )
        self.execute_show_command_config = (
            self.mock_execute_show_command_config.start()
        )

    def tearDown(self):
        super(TestEosBgpglobalModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_execute_show_command.stop()
        self.mock_execute_show_command_config.stop()

    def load_fixtures(self, commands=None, transport="cli", filename=None):
        if filename is None:
            filename = "eos_bgp_global_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file
        self.execute_show_command_config.side_effect = load_from_file

    def test_eos_bgp_global_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65535",
                    timers=dict(keepalive=44, holdtime=100),
                    ucmp=dict(link_bandwidth=dict(mode="recursive")),
                    neighbor=[
                        dict(
                            peer="peer1",
                            peer_group="peer1",
                            maximum_received_routes=dict(count=12000),
                            send_community=dict(
                                community_attribute="link-bandwidth",
                                link_bandwidth_attribute="divide",
                                divide="ratio",
                            ),
                        ),
                        dict(
                            peer="peer2",
                            peer_group="peer2",
                            maximum_received_routes=dict(count=12000),
                        ),
                    ],
                    aggregate_address=[
                        dict(
                            address="1.1.1.0/24",
                            as_set=True,
                            summary_only=True,
                        ),
                        dict(address="5.1.0.0/16", attribute_map="attrmap"),
                    ],
                    redistribute=[
                        dict(protocol="ospf", ospf_route="nssa_external_2"),
                        dict(protocol="static"),
                        dict(protocol="rip", route_map="MAP01"),
                    ],
                    vlan_aware_bundle="bundle1 bundle3",
                    vrfs=[
                        dict(
                            vrf="vrf01",
                            default_metric=433,
                            network=[
                                dict(
                                    address="6.6.6.0/24", route_map="netmap1"
                                ),
                                dict(address="10.1.0.0/16"),
                            ],
                            redistribute=[
                                dict(protocol="isis", isis_level="level-2")
                            ],
                            route_target=dict(action="export", target="44:22"),
                        )
                    ],
                ),
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_bgp_global_merged(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65535",
                    vrfs=[
                        dict(
                            vrf="vrf01",
                            bgp_params=dict(
                                listen=dict(limit=20),
                                log_neighbor_changes=True,
                                missing_policy=dict(
                                    direction="in", action="deny"
                                ),
                                monitoring=True,
                                next_hop_unchanged=True,
                                redistribute_internal=True,
                                route="map01",
                                route_reflector=dict(preserve=True),
                                transport=33,
                            ),
                            timers=dict(keepalive=44, holdtime=100),
                            ucmp=dict(
                                link_bandwidth=dict(
                                    mode="update_delay", update_delay=10
                                )
                            ),
                            neighbors=[
                                dict(
                                    peer="peer1",
                                    peer_group="peer1",
                                    maximum_received_routes=dict(count=12000),
                                    send_community=dict(
                                        community_attribute="link-bandwidth",
                                        link_bandwidth_attribute="divide",
                                        divide="ratio",
                                    ),
                                    transport=dict(remote_port=20),
                                    timers=dict(keepalive=5, holdtime=10),
                                    ttl=33,
                                    update_source="Ethernet1",
                                    weight=43,
                                ),
                                dict(
                                    peer="peer2",
                                    peer_group="peer2",
                                    maximum_received_routes=dict(count=12000),
                                    shutdown=True,
                                ),
                            ],
                        )
                    ],
                    default_metric=433,
                    networks=[
                        dict(address="6.6.6.0/24", route_map="netmap1"),
                        dict(address="10.1.0.0/16"),
                    ],
                    redistribute=[dict(protocol="isis", isis_level="level-2")],
                    route_target=dict(action="export", target="44:22"),
                    ucmp=dict(mode=dict(nexthops=55)),
                    update=dict(
                        wait_for="wait_for_convergence", batch_size=50
                    ),
                ),
                state="merged",
            )
        )
        commands = [
            "router bgp 65535",
            "vrf vrf01",
            "neighbor peer1 peer-group",
            "neighbor peer1 maximum-routes 12000",
            "neighbor peer1 send-community link-bandwidth divide ratio",
            "neighbor peer1 timers 5 10",
            "neighbor peer1 ttl maximum-hops 33",
            "neighbor peer1 update-source Ethernet1",
            "neighbor peer1 weight 43",
            "neighbor peer1 transport remote-port 20",
            "neighbor peer2 peer-group",
            "neighbor peer2 maximum-routes 12000",
            "neighbor peer2 shutdown",
            "bgp route-reflector preserve-attributes always",
            "bgp listen limit 20",
            "bgp log-neighbor-changes",
            "bgp missing-policy direction in action deny",
            "bgp monitoring",
            "bgp next-hop-unchanged",
            "bgp redistribute-internal",
            "bgp route install-map map01",
            "bgp transport listen-port 33",
            "timers bgp 44 100",
            "ucmp link-bandwidth update_delay 10",
            "exit",
            "redistribute isis level-2",
            "network 6.6.6.0/24 route-map netmap1",
            "network 10.1.0.0/16",
            "default-metric 433",
            "route-target export 44:22",
            "ucmp link-bandwidth recursive mode 1 55",
            "update wait_for_convergence 50",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_bgp_global_replaced_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65535",
                    timers=dict(keepalive=44, holdtime=100),
                    ucmp=dict(link_bandwidth=dict(mode="recursive")),
                    neighbor=[
                        dict(
                            peer="peer1",
                            peer_group="peer1",
                            maximum_received_routes=dict(count=12000),
                            send_community=dict(
                                community_attribute="link-bandwidth",
                                link_bandwidth_attribute="divide",
                                divide="ratio",
                            ),
                        ),
                        dict(
                            peer="peer2",
                            peer_group="peer2",
                            maximum_received_routes=dict(count=12000),
                        ),
                    ],
                    aggregate_address=[
                        dict(
                            address="1.1.1.0/24",
                            as_set=True,
                            summary_only=True,
                        ),
                        dict(address="5.1.0.0/16", attribute_map="attrmap"),
                    ],
                    redistribute=[
                        dict(protocol="ospf", ospf_route="nssa_external_2"),
                        dict(protocol="static"),
                        dict(protocol="rip", route_map="MAP01"),
                    ],
                    vlan_aware_bundle="bundle1 bundle3",
                    vrfs=[
                        dict(
                            vrf="vrf01",
                            default_metric=433,
                            network=[
                                dict(
                                    address="6.6.6.0/24", route_map="netmap1"
                                ),
                                dict(address="10.1.0.0/16"),
                            ],
                            redistribute=[
                                dict(protocol="isis", isis_level="level-2")
                            ],
                            route_target=dict(action="export", target="44:22"),
                        )
                    ],
                ),
                state="replaced",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_bgp_global_replaced_novrf(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65535",
                    default_metric=433,
                    network=[
                        dict(address="6.6.6.0/24", route_map="netmap1"),
                        dict(address="10.1.0.0/16"),
                    ],
                    redistribute=[dict(protocol="isis", isis_level="level-2")],
                    route_target=dict(action="export", target="44:22"),
                ),
                state="replaced",
            )
        )
        commands = [
            "router bgp 65535",
            "no vrf vrf01",
            "redistribute isis level-2",
            "network 6.6.6.0/24 route-map netmap1",
            "network 10.1.0.0/16",
            "default-metric 433",
            "route-target export 44:22",
            "no timers bgp 44 100",
            "no ucmp link-bandwidth recursive",
            "no neighbor peer1 peer-group",
            "no neighbor peer1 send-community link-bandwidth divide ratio",
            "no neighbor peer1 maximum-routes 12000",
            "no neighbor peer2 peer-group",
            "no neighbor peer2 maximum-routes 12000",
            "no aggregate-address 1.1.1.0/24 as-set summary-only",
            "no aggregate-address 5.1.0.0/16 attribute-map attrmap",
            "no redistribute ospf match nssa-external 2",
            "no redistribute static",
            "no vlan-aware-bundle bundle1 bundle3",
            "no redistribute rip route-map MAP01",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_bgp_global_replaced_vrf(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65535",
                    vrfs=[
                        dict(
                            vrf="vrf01",
                            default_metric=433,
                            aggregate_address=[
                                dict(
                                    address="1.1.1.0/24",
                                    as_set=True,
                                    summary_only=True,
                                ),
                                dict(
                                    address="5.1.0.0/16",
                                    attribute_map="attrmap",
                                ),
                            ],
                            redistribute=[
                                dict(
                                    protocol="ospf",
                                    ospf_route="nssa_external_2",
                                ),
                                dict(protocol="static"),
                                dict(protocol="rip", route_map="MAP01"),
                            ],
                        )
                    ],
                ),
                state="replaced",
            )
        )
        commands = [
            "router bgp 65535",
            "vrf vrf01",
            "no route-target export 44:22",
            "redistribute ospf match nssa-external 2",
            "redistribute static",
            "redistribute rip route-map MAP01",
            "no redistribute isis level-2",
            "no network 6.6.6.0/24 route-map netmap1",
            "no network 10.1.0.0/16",
            "aggregate-address 1.1.1.0/24 as-set summary-only",
            "aggregate-address 5.1.0.0/16 attribute-map attrmap",
            "exit",
            "no neighbor peer1 peer-group",
            "no neighbor peer1 send-community link-bandwidth divide ratio",
            "no neighbor peer1 maximum-routes 12000",
            "no neighbor peer2 peer-group",
            "no neighbor peer2 maximum-routes 12000",
            "no redistribute ospf match nssa-external 2",
            "no redistribute static",
            "no redistribute rip route-map MAP01",
            "no aggregate-address 1.1.1.0/24 as-set summary-only",
            "no aggregate-address 5.1.0.0/16 attribute-map attrmap",
            "no timers bgp 44 100",
            "no ucmp link-bandwidth recursive",
            "no vlan-aware-bundle bundle1 bundle3",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_bgp_global_deleted(self):
        set_module_args(dict(config=dict(as_number="65535"), state="deleted"))
        commands = [
            "router bgp 65535",
            "no vrf vrf01",
            "no neighbor peer1 peer-group",
            "no neighbor peer1 send-community link-bandwidth divide ratio",
            "no neighbor peer1 maximum-routes 12000",
            "no neighbor peer2 peer-group",
            "no neighbor peer2 maximum-routes 12000",
            "no redistribute ospf match nssa-external 2",
            "no redistribute static",
            "no redistribute rip route-map MAP01",
            "no aggregate-address 1.1.1.0/24 as-set summary-only",
            "no aggregate-address 5.1.0.0/16 attribute-map attrmap",
            "no timers bgp 44 100",
            "no ucmp link-bandwidth recursive",
            "no vlan-aware-bundle bundle1 bundle3",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_bgp_global_purged(self):
        set_module_args(dict(config=dict(as_number="65535"), state="purged"))
        commands = ["no router bgp 65535"]
        self.execute_module(changed=True, commands=commands)

    def test_eos_bgp_global_merged_incorrect_instance(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="100",
                    vrfs=[
                        dict(
                            vrf="vrf02",
                            timers=dict(keepalive=44, holdtime=100),
                            ucmp=dict(link_bandwidth=dict(mode="recursive")),
                            neighbor=[
                                dict(
                                    peer="peer1",
                                    peer_group="peer1",
                                    maximum_received_routes=dict(count=12000),
                                    send_community=dict(
                                        community_attribute="link-bandwidth",
                                        link_bandwidth_attribute="divide",
                                        divide="ratio",
                                    ),
                                ),
                                dict(
                                    peer="peer2",
                                    peer_group="peer2",
                                    maximum_received_routes=dict(count=12000),
                                ),
                            ],
                        )
                    ],
                    default_metric=433,
                    network=[
                        dict(address="6.6.6.0/24", route_map="netmap1"),
                        dict(address="10.1.0.0/16"),
                    ],
                    redistribute=[dict(protocol="isis", isis_level="level-2")],
                    route_target=dict(action="export", target="44:22"),
                ),
                state="merged",
            )
        )
        result = self.execute_module(failed=True)
        self.assertIn(
            "Only one bgp instance is allowed per device", result["msg"]
        )

    def test_eos_bgp_global_replaced_with_af(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65535",
                    default_metric=433,
                    network=[
                        dict(address="6.6.6.0/24", route_map="netmap1"),
                        dict(address="10.1.0.0/16"),
                    ],
                    redistribute=[dict(protocol="isis", isis_level="level-2")],
                    route_target=dict(action="export", target="44:22"),
                ),
                state="replaced",
            )
        )
        result = self.execute_module(
            failed=True, filename="eos_bgp_global_af_config.cfg"
        )
        self.assertIn(
            "Use the _bgp_address_family module to delete the address_family under vrf, before replacing/deleting the vrf.",
            result["msg"],
        )

    def test_eos_bgp_global_deleted_with_af(self):
        set_module_args(dict(config=dict(as_number="65535"), state="deleted"))
        result = self.execute_module(
            failed=True, filename="eos_bgp_global_af_config.cfg"
        )
        self.assertIn(
            "Use the _bgp_address_family module to delete the address_family under vrf, before replacing/deleting the vrf.",
            result["msg"],
        )

    def test_eos_bgp_global_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(
            changed=False, filename="eos_bgp_global_config.cfg"
        )
        gather_list = {
            "aggregate_address": [
                {
                    "address": "1.1.1.0/24",
                    "as_set": True,
                    "summary_only": True,
                },
                {"address": "5.1.0.0/16", "attribute_map": "attrmap"},
            ],
            "as_number": "65535",
            "neighbor": [
                {
                    "maximum_received_routes": {"count": 12000},
                    "peer": "peer1",
                    "peer_group": "peer1",
                    "send_community": {
                        "community_attribute": "link-bandwidth",
                        "divide": "ratio",
                        "link_bandwidth_attribute": "divide",
                    },
                },
                {
                    "maximum_received_routes": {"count": 12000},
                    "peer": "peer2",
                    "peer_group": "peer2",
                },
            ],
            "redistribute": [
                {"ospf_route": "nssa_external_2", "protocol": "ospf"},
                {"protocol": "static"},
                {"protocol": "rip", "route_map": "MAP01"},
            ],
            "timers": {"holdtime": 100, "keepalive": 44},
            "ucmp": {"link_bandwidth": {"mode": "recursive"}},
            "vlan_aware_bundle": "bundle1 bundle3",
            "vrfs": [
                {
                    "default_metric": 433,
                    "network": [
                        {"address": "6.6.6.0/24", "route_map": "netmap1"},
                        {"address": "10.1.0.0/16"},
                    ],
                    "redistribute": [
                        {"isis_level": "level-2", "protocol": "isis"}
                    ],
                    "route_target": {"action": "export", "target": "44:22"},
                    "vrf": "vrf01",
                }
            ],
        }
        self.assertEqual(sorted(gather_list), sorted(result["gathered"]))

    def test_eos_bgp_global_parsed(self):
        commands = [
            "router bgp 65535",
            "timers bgp 44 100",
            "ucmp link-bandwidth recursive",
            "neighbor peer1 peer-group",
            "neighbor peer1 send-community link-bandwidth divide ratio",
            "neighbor peer1 maximum-routes 12000",
            "neighbor peer2 peer-group",
            "neighbor peer2 maximum-routes 12000",
            "aggregate-address 1.1.1.0/24 as-set summary-only",
            "aggregate-address 5.1.0.0/16 attribute-map attrmap",
            "redistribute ospf match nssa-external 2",
            "redistribute static",
            "redistribute rip route-map MAP01",
            "!",
            "vlan-aware-bundle bundle1 bundle3",
            "!",
            "vrf vrf01",
            "route-target export 44:22",
            "default-metric 433",
            "network 6.6.6.0/24 route-map netmap1",
            "network 10.1.0.0/16",
            "redistribute isis level-2",
        ]

        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(
            changed=False, filename="eos_bgp_global_config.cfg"
        )
        parsed_list = {
            "aggregate_address": [
                {
                    "address": "1.1.1.0/24",
                    "as_set": True,
                    "summary_only": True,
                },
                {"address": "5.1.0.0/16", "attribute_map": "attrmap"},
            ],
            "as_number": "65535",
            "neighbor": [
                {
                    "maximum_received_routes": {"count": 12000},
                    "peer": "peer1",
                    "peer_group": "peer1",
                    "send_community": {
                        "community_attribute": "link-bandwidth",
                        "divide": "ratio",
                        "link_bandwidth_attribute": "divide",
                    },
                },
                {
                    "maximum_received_routes": {"count": 12000},
                    "peer": "peer2",
                    "peer_group": "peer2",
                },
            ],
            "redistribute": [
                {"ospf_route": "nssa_external_2", "protocol": "ospf"},
                {"protocol": "static"},
                {"protocol": "rip", "route_map": "MAP01"},
            ],
            "timers": {"holdtime": 100, "keepalive": 44},
            "ucmp": {"link_bandwidth": {"mode": "recursive"}},
            "vlan_aware_bundle": "bundle1 bundle3",
            "vrfs": [
                {
                    "default_metric": 433,
                    "network": [
                        {"address": "6.6.6.0/24", "route_map": "netmap1"},
                        {"address": "10.1.0.0/16"},
                    ],
                    "redistribute": [
                        {"isis_level": "level-2", "protocol": "isis"}
                    ],
                    "route_target": {"action": "export", "target": "44:22"},
                    "vrf": "vrf01",
                }
            ],
        }
        self.assertEqual(sorted(parsed_list), sorted(result["parsed"]))

    def test_eos_bgp_global_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65535",
                    vrfs=[
                        dict(
                            vrf="vrf02",
                            timers=dict(keepalive=44, holdtime=100),
                            ucmp=dict(link_bandwidth=dict(mode="recursive")),
                            neighbor=[
                                dict(
                                    peer="peer1",
                                    peer_group="peer1",
                                    maximum_received_routes=dict(count=12000),
                                    send_community=dict(
                                        community_attribute="link-bandwidth",
                                        link_bandwidth_attribute="divide",
                                        divide="ratio",
                                    ),
                                ),
                                dict(
                                    peer="peer2",
                                    peer_group="peer2",
                                    ebgp_multihop=dict(ttl=10),
                                    enforce_first_as=True,
                                    fall_over=True,
                                    graceful_restart_helper=True,
                                    idle_restart_timer=5,
                                    link_bandwidth=dict(auto=True),
                                    local_as=dict(as_number=55, fallback=True),
                                    maximum_accepted_routes=dict(
                                        count=6, warning_limit=4
                                    ),
                                    maximum_received_routes=dict(
                                        count=6,
                                        warning_limit=dict(limit_percent=25),
                                        warning_only=True,
                                    ),
                                    metric_out=5,
                                    monitoring=True,
                                    next_hop_self=True,
                                    next_hop_unchanged=True,
                                    next_hop_v6_address="5001::/64",
                                    out_delay=15,
                                    remote_as=55,
                                    remove_private_as=dict(replace_as=True),
                                    prefix_list=dict(
                                        name="list01", direction="in"
                                    ),
                                    route_map=dict(
                                        name="map01", direction="out"
                                    ),
                                    route_reflector_client=True,
                                    route_to_peer=True,
                                ),
                            ],
                        )
                    ],
                    default_metric=433,
                    network=[
                        dict(address="6.6.6.0/24", route_map="netmap1"),
                        dict(address="10.1.0.0/16"),
                    ],
                    redistribute=[dict(protocol="isis", isis_level="level-2")],
                    route_target=dict(action="export", target="44:22"),
                    bgp_params=dict(
                        additional_paths="send",
                        advertise_inactive=True,
                        allowas_in=dict(count=4),
                        always_compare_med=True,
                        auto_local_addr=True,
                        bestpath=dict(
                            as_path="ignore",
                            ecmp_fast=True,
                            med=dict(confed=True),
                        ),
                        client_to_client=True,
                        cluster_id=2,
                        control_plane_filter=True,
                        convergence=dict(slow_peer=True, time=5),
                        enforce_first_as=True,
                        host_routes=True,
                    ),
                    access_group=dict(
                        afi="ipv6", acl_name="acl01", direction="out"
                    ),
                ),
                state="rendered",
            )
        )
        rendered_cmds = [
            "router bgp 65535",
            "vrf vrf02",
            "neighbor peer1 peer-group",
            "neighbor peer1 maximum-routes 12000",
            "neighbor peer1 send-community link-bandwidth divide ratio",
            "neighbor peer2 peer-group",
            "neighbor peer2 local-as 55 no-prepend replace-as fallback",
            "neighbor peer2 next-hop-v6-addr 5001::/64 in",
            "neighbor peer2 ebgp-multiphop 10",
            "neighbor peer2 enforce-first-as",
            "neighbor peer2 fall-over bfd",
            "neighbor peer2 graceful-restart-helper",
            "neighbor peer2 idle-restart-timer 5",
            "neighbor peer2 link-bandwidth auto",
            "neighbor peer2 maximum-accepted-routes 6 warning-limit 4",
            "neighbor peer2 maximum-routes 6 warning-limit 25 percent warning-only",
            "neighbor peer2 metric-out 5",
            "neighbor peer2 monitoring",
            "neighbor peer2 next-hop-self",
            "neighbor peer2 next-hop-unchanged",
            "neighbor peer2 out-delay 15",
            "neighbor peer2 remote-as 55",
            "neighbor peer2 remove-private-as replace-as",
            "neighbor peer2 prefix-list list01 in",
            "neighbor peer2 route-map map01 out",
            "neighbor peer2 route-reflector-client",
            "neighbor peer2 route-to-peer",
            "timers bgp 44 100",
            "ucmp link-bandwidth recursive",
            "exit",
            "bgp additional-paths send any",
            "bgp advertise-inactive",
            "bgp allowas-in 4",
            "bgp always-comapre-med",
            "bgp auto-local-addr",
            "redistribute isis level-2",
            "network 6.6.6.0/24 route-map netmap1",
            "network 10.1.0.0/16",
            "default-metric 433",
            "route-target export 44:22",
            "bgp bestpath ecmp-fast",
            "bgp bestpath med confed",
            "bgp client-to-client",
            "bgp cluster-id 2",
            "bgp control-plane-filter default-allow",
            "bgp convergence slow-peer time 5",
            "bgp enforce-first-as",
            "bgp host-routes fib direct-install",
            "bgp bestpath as-path ignore",
            "ipv6 access-group acl01 out",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(rendered_cmds),
            result["rendered"],
        )
