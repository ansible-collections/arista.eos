#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.arista.eos.tests.unit.compat.mock import patch
from ansible_collections.arista.eos.plugins.modules import (
    eos_bgp_address_family,
)
from ansible_collections.arista.eos.tests.unit.modules.utils import (
    set_module_args,
)
from .eos_module import TestEosModule, load_fixture


class TestEosBgpafModule(TestEosModule):
    module = eos_bgp_address_family

    def setUp(self):
        super(TestEosBgpafModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection"
        )
        self.get_resource_connection_config = (
            self.mock_get_resource_connection_config.start()
        )

        self.mock_execute_show_command = patch(
            "ansible_collections.arista.eos.plugins.module_utils.network.eos.facts.bgp_address_family.bgp_address_family.Bgp_afFacts.get_config"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestEosBgpafModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, transport="cli", filename=None):
        if filename is None:
            filename = "eos_bgp_af_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_eos_bgp_af_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    as_number=10,
                    address_family=[
                        dict(
                            afi="ipv4",
                            redistribute=[
                                dict(protocol="ospfv3", ospf_route="external")
                            ],
                            network=[
                                dict(address="1.1.1.0/24"),
                                dict(address="1.5.1.0/24", route_map="MAP01"),
                            ],
                            neighbor=[
                                dict(
                                    peer="peer2",
                                    default_originate=dict(always=True),
                                )
                            ],
                            bgp_params=dict(additional_paths="receive"),
                        ),
                        dict(
                            afi="ipv4",
                            vrf="vrft",
                            bgp_params=dict(additional_paths="receive"),
                        ),
                        dict(
                            afi="ipv6",
                            vrf="vrft",
                            redistribute=[
                                dict(protocol="isis", isis_level="level-2")
                            ],
                        ),
                    ],
                ),
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_bgp_af_merged(self):
        set_module_args(
            dict(
                config=dict(
                    as_number=10,
                    address_family=[
                        dict(
                            afi="ipv4",
                            redistribute=[
                                dict(protocol="ospfv3", ospf_route="external")
                            ],
                            neighbor=[
                                dict(
                                    peer="peer2",
                                    default_originate=dict(always=True),
                                )
                            ],
                        ),
                        dict(afi="ipv6", graceful_restart=True),
                        dict(
                            afi="ipv4",
                            vrf="vrft",
                            route_target=dict(
                                action="both", type="evpn", target="465:11"
                            ),
                        ),
                    ],
                ),
                state="merged",
            )
        )
        commands = [
            "router bgp 10",
            "vrf vrft",
            "address-family ipv4",
            "route-target both evpn 465:11",
            "exit",
            "exit",
            "address-family ipv6",
            "graceful-restart",
            "exit",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_eos_bgp_af_replaced(self):
        set_module_args(
            dict(
                config=dict(
                    as_number=10,
                    address_family=[
                        dict(
                            afi="ipv4",
                            redistribute=[
                                dict(protocol="ospfv3", ospf_route="external")
                            ],
                            neighbor=[
                                dict(
                                    peer="peer2",
                                    default_originate=dict(always=True),
                                )
                            ],
                        ),
                        dict(afi="ipv6", graceful_restart=True),
                        dict(
                            afi="ipv4",
                            vrf="vrft",
                            route_target=dict(
                                action="both", type="vpn-ipv4", target="465:11"
                            ),
                        ),
                    ],
                ),
                state="replaced",
            )
        )
        commands = [
            "router bgp 10",
            "address-family ipv4",
            "no network 1.1.1.0/24",
            "no network 1.5.1.0/24 route-map MAP01",
            "no bgp additional-paths receive",
            "exit",
            "address-family ipv6",
            "graceful-restart",
            "exit",
            "vrf vrft",
            "address-family ipv4",
            "no bgp additional-paths receive",
            "route-target both vpn-ipv4 465:11",
            "exit",
            "exit",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_eos_bgp_af_replaced_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    as_number=10,
                    address_family=[
                        dict(
                            afi="ipv4",
                            redistribute=[
                                dict(protocol="ospfv3", ospf_route="external")
                            ],
                            network=[
                                dict(address="1.1.1.0/24"),
                                dict(address="1.5.1.0/24", route_map="MAP01"),
                            ],
                            neighbor=[
                                dict(
                                    peer="peer2",
                                    default_originate=dict(always=True),
                                )
                            ],
                            bgp_params=dict(additional_paths="receive"),
                        ),
                        dict(
                            afi="ipv4",
                            vrf="vrft",
                            bgp_params=dict(additional_paths="receive"),
                        ),
                        dict(
                            afi="ipv6",
                            vrf="vrft",
                            redistribute=[
                                dict(protocol="isis", isis_level="level-2")
                            ],
                        ),
                    ],
                ),
                state="replaced",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_bgp_af_overridden(self):
        set_module_args(
            dict(
                config=dict(
                    as_number=10,
                    address_family=[
                        dict(
                            afi="ipv4",
                            redistribute=[
                                dict(protocol="ospfv3", ospf_route="external")
                            ],
                            neighbor=[
                                dict(
                                    peer="peer2",
                                    default_originate=dict(always=True),
                                )
                            ],
                        ),
                        dict(afi="ipv6", graceful_restart=True),
                        dict(
                            afi="ipv4",
                            vrf="vrft",
                            route_target=dict(
                                action="both", type="vpn-ipv6", target="465:11"
                            ),
                        ),
                    ],
                ),
                state="overridden",
            )
        )
        commands = [
            "router bgp 10",
            "address-family ipv4",
            "no network 1.1.1.0/24",
            "no network 1.5.1.0/24 route-map MAP01",
            "no bgp additional-paths receive",
            "exit",
            "address-family ipv6",
            "graceful-restart",
            "exit",
            "vrf vrft",
            "address-family ipv4",
            "no bgp additional-paths receive",
            "route-target both vpn-ipv6 465:11",
            "exit",
            "exit",
            "vrf vrft",
            "no address-family ipv6",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_eos_bgp_af_overridden_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    as_number=10,
                    address_family=[
                        dict(
                            afi="ipv4",
                            redistribute=[
                                dict(protocol="ospfv3", ospf_route="external")
                            ],
                            network=[
                                dict(address="1.1.1.0/24"),
                                dict(address="1.5.1.0/24", route_map="MAP01"),
                            ],
                            neighbor=[
                                dict(
                                    peer="peer2",
                                    default_originate=dict(always=True),
                                )
                            ],
                            bgp_params=dict(additional_paths="receive"),
                        ),
                        dict(
                            afi="ipv4",
                            vrf="vrft",
                            bgp_params=dict(additional_paths="receive"),
                        ),
                        dict(
                            afi="ipv6",
                            vrf="vrft",
                            redistribute=[
                                dict(protocol="isis", isis_level="level-2")
                            ],
                        ),
                    ],
                ),
                state="overridden",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_bgp_af_deleted(self):
        set_module_args(
            dict(
                config=dict(
                    as_number=10,
                    address_family=[
                        dict(afi="ipv4"),
                        dict(afi="ipv4", vrf="vrft"),
                    ],
                ),
                state="deleted",
            )
        )
        commands = [
            "router bgp 10",
            "no address-family ipv4",
            "vrf vrft",
            "no address-family ipv4",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_eos_bgp_af_parsed(self):

        commands = [
            "router bgp 10",
            "address-family ipv4",
            "network 1.5.1.0/24 route-map MAP01",
            "!",
            "address-family ipv6",
            "graceful-restart",
            "redistribute isis level-1",
            "bgp additional-paths receive",
            "!",
            "vrf vrft",
            "address-family ipv4",
            "redistribute ospfv3 match external",
            "route-target both vpn-ipv4 465:11",
            "!",
        ]

        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {
            "as_number": "10",
            "address_family": [
                {
                    "afi": "ipv4",
                    "network": [
                        {"address": "1.5.1.0/24", "route_map": "MAP01"}
                    ],
                },
                {
                    "afi": "ipv6",
                    "redistribute": [
                        {"protocol": "isis", "isis_level": "level-1"}
                    ],
                    "graceful_restart": True,
                    "bgp_params": {"additional_paths": "receive"},
                },
                {
                    "afi": "ipv4",
                    "vrf": "vrft",
                    "redistribute": [
                        {"protocol": "ospfv3", "ospf_route": "external`"}
                    ],
                    "route_target": {
                        "action": "both",
                        "type": "vpn-ipv4",
                        "target": "465:11",
                    },
                },
            ],
        }
        self.assertEqual(sorted(parsed_list), sorted(result["parsed"]))

    def test_eos_bgp_af_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(
            changed=False, filename="eos_bgp_af_config.cfg"
        )
        gather_list = {
            "address_family": [
                {
                    "afi": "ipv4",
                    "bgp_params": {"additional_paths": "receive"},
                    "neighbor": [
                        {
                            "default_originate": {"always": True},
                            "peer": "peer2",
                        }
                    ],
                    "network": [
                        {"address": "1.1.1.0/24"},
                        {"address": "1.5.1.0/24", "route_map": "MAP01"},
                    ],
                    "redistribute": [
                        {"ospf_route": "external", "protocol": "ospfv3"}
                    ],
                },
                {
                    "afi": "ipv4",
                    "bgp_params": {"additional_paths": "receive"},
                    "vrf": "vrft",
                },
                {
                    "afi": "ipv6",
                    "redistribute": [
                        {"isis_level": "level-2", "protocol": "isis"}
                    ],
                    "vrf": "vrft",
                },
            ],
            "as_number": "10",
        }
        self.assertEqual(sorted(gather_list), sorted(result["gathered"]))

    def test_eos_bgp_af_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    as_number=10,
                    address_family=[
                        dict(
                            afi="ipv4",
                            redistribute=[
                                dict(protocol="ospfv3", ospf_route="external")
                            ],
                            network=[
                                dict(address="1.1.1.0/24"),
                                dict(address="1.5.1.0/24", route_map="MAP01"),
                            ],
                            neighbor=[
                                dict(
                                    peer="peer2",
                                    default_originate=dict(always=True),
                                )
                            ],
                            bgp_params=dict(additional_paths="receive"),
                        ),
                        dict(
                            afi="ipv4",
                            vrf="vrft",
                            bgp_params=dict(additional_paths="receive"),
                        ),
                    ],
                ),
                state="rendered",
            )
        )
        self.execute_module(changed=False)
        rendered_cmds = [
            "router bgp 10",
            "address-family ipv4",
            "redistribute ospfv3 match external",
            "network 1.1.1.0/24",
            "network 1.5.1.0/24 route-map MAP01",
            "neighbor peer2 default-originate always",
            "bgp additional-paths receive",
            "exit",
            "vrf vrft",
            "address-family ipv4",
            "bgp additional-paths receive",
            "exit",
            "exit",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(rendered_cmds),
            result["rendered"],
        )
