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
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.resource_module.get_resource_connection"
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
        commands = [
            "router bgp 65535",
            "vrf vrf01",
            "neighbor peer1 peer-group",
            "neighbor peer1 maximum-routes 12000",
            "neighbor peer1 send-community link-bandwidth divide ratio",
            "neighbor peer2 peer-group",
            "neighbor peer2 maximum-routes 12000",
            "timers bgp 44 100",
            "ucmp link-bandwidth recursive",
            "exit",
            "redistribute isis level-2",
            "network 6.6.6.0/24 route-map netmap1",
            "network 10.1.0.0/16",
            "default-metric 433",
            "route-target export 44:22",
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
            "neighbor peer2 maximum-routes 12000",
            "timers bgp 44 100",
            "ucmp link-bandwidth recursive",
            "exit",
            "redistribute isis level-2",
            "network 6.6.6.0/24 route-map netmap1",
            "network 10.1.0.0/16",
            "default-metric 433",
            "route-target export 44:22",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(rendered_cmds),
            result["rendered"],
        )
