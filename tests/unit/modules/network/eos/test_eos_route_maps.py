#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.arista.eos.plugins.modules import eos_route_maps
from ansible_collections.arista.eos.tests.unit.modules.utils import set_module_args

from .eos_module import TestEosModule, load_fixture


class TestEosRoute_MapsModule(TestEosModule):
    module = eos_route_maps

    def setUp(self):
        super(TestEosRoute_MapsModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.arista.eos.plugins.module_utils.network.eos.facts.route_maps.route_maps.Route_mapsFacts.get_config",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestEosRoute_MapsModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, transport="cli", filename=None):
        if filename is None:
            filename = "eos_route_maps_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_eos_route_maps_merged_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        route_map="mapmerge",
                        entries=[
                            dict(
                                description="merged_map",
                                action="permit",
                                sequence=10,
                                match=dict(router_id=22),
                            ),
                            dict(
                                description="newmap",
                                action="deny",
                                sequence=25,
                                continue_sequence=45,
                                match=dict(interface="Ethernet1"),
                            ),
                        ],
                    ),
                    dict(
                        route_map="mapmerge2",
                        entries=[
                            dict(
                                sub_route_map=dict(name="mapmerge"),
                                action="deny",
                                match=dict(
                                    ipv6=dict(resolved_next_hop="list1"),
                                ),
                                sequence=45,
                                set=dict(
                                    metric=dict(value=25, add="igp-metric"),
                                    as_path=dict(prepend=dict(last_as=2)),
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_route_maps_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        route_map="mapmerge_new",
                        entries=[
                            dict(
                                action="permit",
                                match=dict(
                                    invert_result=dict(
                                        aggregate_role=dict(route_map="map01"),
                                    ),
                                    isis_level="level-1",
                                    route_type="local",
                                ),
                                set=dict(
                                    nexthop=dict(max_metric=True),
                                    segment_index=25,
                                    distance=55,
                                    tag=3,
                                    local_preference=51,
                                    evpn=True,
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )
        commands = [
            "route-map mapmerge_new permit",
            "match invert-result as-path aggregate-role contributor aggregator-attributes map01",
            "match isis level level-1",
            "match route-type local",
            "set next-hop igp-metric max-metric",
            "set segment-index 25",
            "set distance 55",
            "set tag 3",
            "set local-preference 51",
            "set evpn next-hop unchanged",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_route_maps_replaced_idempotent(self):
        set_module_args(
            dict(
                state="replaced",
                config=[
                    dict(
                        route_map="mapmerge",
                        entries=[
                            dict(
                                description="merged_map",
                                action="permit",
                                sequence=10,
                                set=dict(bgp=20),
                                match=dict(router_id=22),
                            ),
                            dict(
                                description="newmap",
                                action="deny",
                                sequence=25,
                                continue_sequence=45,
                                match=dict(interface="Ethernet1"),
                            ),
                        ],
                    ),
                    dict(
                        route_map="mapmerge2",
                        entries=[
                            dict(
                                sub_route_map=dict(name="mapmerge"),
                                action="deny",
                                match=dict(
                                    ipv6=dict(resolved_next_hop="list1"),
                                ),
                                sequence=45,
                                set=dict(
                                    metric=dict(value=25, add="igp-metric"),
                                    as_path=dict(prepend=dict(last_as=2)),
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_route_maps_replaced(self):
        set_module_args(
            dict(
                state="replaced",
                config=[
                    dict(
                        route_map="mapmerge",
                        entries=[
                            dict(
                                action="permit",
                                match=dict(
                                    ipv6=dict(resolved_next_hop="listr"),
                                ),
                                sequence=10,
                            ),
                            dict(
                                action="deny",
                                sequence=90,
                                set=dict(
                                    extcommunity=dict(
                                        rt=dict(vpn="22:11", delete=True),
                                    ),
                                    ip=dict(unchanged=True),
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )
        commands = [
            "route-map mapmerge permit 10",
            "match ipv6 resolved-next-hop prefix-list listr",
            "no match router-id prefix-list 22",
            "no set bgp bestpath as-path weight 20",
            "no description",
            "route-map mapmerge deny 90",
            "set extcommunity rt 22:11 delete",
            "set ip next-hop unchanged",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_route_maps_overridden_idempotent(self):
        set_module_args(
            dict(
                state="overridden",
                config=[
                    dict(
                        route_map="mapmerge",
                        entries=[
                            dict(
                                description="merged_map",
                                action="permit",
                                sequence=10,
                                match=dict(router_id=22),
                                set=dict(bgp=20),
                            ),
                            dict(
                                description="newmap",
                                action="deny",
                                sequence=25,
                                continue_sequence=45,
                                match=dict(interface="Ethernet1"),
                            ),
                        ],
                    ),
                    dict(
                        route_map="mapmerge2",
                        entries=[
                            dict(
                                sub_route_map=dict(name="mapmerge"),
                                action="deny",
                                match=dict(
                                    ipv6=dict(resolved_next_hop="list1"),
                                ),
                                sequence=45,
                                set=dict(
                                    metric=dict(value=25, add="igp-metric"),
                                    as_path=dict(prepend=dict(last_as=2)),
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_route_maps_overridden(self):
        set_module_args(
            dict(
                state="overridden",
                config=[
                    dict(
                        route_map="mapmerge",
                        entries=[
                            dict(
                                action="permit",
                                match=dict(
                                    ipv6=dict(
                                        address=dict(
                                            prefix_list="test_prefix",
                                        ),
                                    ),
                                ),
                                set=dict(
                                    metric=dict(igp_param="igp-nexthop-cost"),
                                ),
                                sequence=10,
                            ),
                            dict(
                                action="deny",
                                sequence=90,
                                match=dict(
                                    ip=dict(
                                        address=dict(
                                            prefix_list="test_prefix",
                                        ),
                                    ),
                                ),
                                set=dict(
                                    extcommunity=dict(
                                        rt=dict(vpn="22:11", delete=True),
                                    ),
                                    ip=dict(unchanged=True),
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )
        commands = [
            "no route-map mapmerge deny 25",
            "no route-map mapmerge2 deny 45",
            "route-map mapmerge permit 10",
            "match ipv6 address prefix-list test_prefix",
            "set metric igp-nexthop-cost",
            "no match router-id prefix-list 22",
            "no set bgp bestpath as-path weight 20",
            "no description",
            "route-map mapmerge deny 90",
            "match ip address prefix-list test_prefix",
            "set extcommunity rt 22:11 delete",
            "set ip next-hop unchanged",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_route_maps_delete(self):
        set_module_args(
            dict(state="deleted", config=[dict(route_map="mapmerge")]),
        )
        commands = ["no route-map mapmerge"]
        self.execute_module(changed=True, commands=commands)

    def test_eos_route_maps_delete_all(self):
        set_module_args(dict(state="deleted"))
        commands = ["no route-map mapmerge", "no route-map mapmerge2"]
        self.execute_module(changed=True, commands=commands)

    def test_eos_route_maps_render(self):
        set_module_args(
            dict(
                state="rendered",
                config=[
                    dict(
                        route_map="mapmerge",
                        entries=[
                            dict(
                                description="merged_map",
                                action="permit",
                                sequence=10,
                                match=dict(router_id=22),
                            ),
                            dict(
                                description="newmap",
                                action="deny",
                                sequence=25,
                                continue_sequence=45,
                                match=dict(interface="Ethernet1"),
                            ),
                        ],
                    ),
                    dict(
                        route_map="mapmerge2",
                        entries=[
                            dict(
                                action="deny",
                                match=dict(
                                    ipv6=dict(resolved_next_hop="list1"),
                                ),
                                sequence=45,
                                set=dict(
                                    metric=dict(value=25, add="igp-metric"),
                                    as_path=dict(prepend=dict(last_as=2)),
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )
        commands = [
            "route-map mapmerge permit 10",
            "description merged_map",
            "match router-id prefix-list 22",
            "route-map mapmerge deny 25",
            "description newmap",
            "match interface Ethernet1",
            "continue 45",
            "route-map mapmerge2 deny 45",
            "match ipv6 resolved-next-hop prefix-list list1",
            "set metric 25 +igp-metric",
            "set as-path prepend last-as 2",
        ]

        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(commands),
            result["rendered"],
        )

    def test_vyos_route_maps_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(
            changed=False,
            filename="eos_route_maps_config.cfg",
        )
        gathered_list = {
            "mapmerge": [
                {
                    "action": "permit",
                    "description": "merged_map",
                    "match": {"router_id": "22"},
                    "sequence": 10,
                    "set": {"bgp": 20},
                },
                {
                    "action": "deny",
                    "continue_sequence": 45,
                    "description": "newmap",
                    "match": {"interface": "Ethernet1"},
                    "sequence": 25,
                },
            ],
            "mapmerge2": [
                {
                    "action": "deny",
                    "match": {"ipv6": {"resolved_next_hop": "list1"}},
                    "sequence": 45,
                    "set": {
                        "as_path": {"prepend": {"last_as": 2}},
                        "metric": {"value": "25", "add": "igp-metric"},
                    },
                    "sub_route_map": {"name": "mapmerge"},
                },
            ],
        }
        for entry in result["gathered"]:
            if entry.get("route_map") in ["mapmerge", "mapmerge2"]:
                self.assertEqual(
                    gathered_list[entry["route_map"]],
                    entry["entries"],
                )

    def test_vyos_route_maps_parsed(self):
        commands = [
            "route-map mapmerge permit 10",
            "description merged_map",
            "match router-id prefix-list 22",
            "route-map mapmerge deny 25",
            "description newmap",
            "match interface Ethernet1",
            "continue 45",
            "route-map mapmerge2 deny 45",
            "match ipv6 resolved-next-hop prefix-list list1",
            "sub-route-map mapmerge",
            "set metric 25 +igp-metric",
            "set as-path prepend last-as 2",
        ]

        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "entries": [
                    {
                        "action": "permit",
                        "description": "merged_map",
                        "match": {"router_id": "22"},
                        "sequence": 10,
                    },
                    {
                        "action": "deny",
                        "continue_sequence": 45,
                        "description": "newmap",
                        "match": {"interface": "Ethernet1"},
                        "sequence": 25,
                    },
                ],
                "route_map": "mapmerge",
            },
            {
                "entries": [
                    {
                        "action": "deny",
                        "match": {"ipv6": {"resolved_next_hop": "list1"}},
                        "sequence": 45,
                        "set": {
                            "as_path": {"prepend": {"last_as": 2}},
                            "metric": {"value": "25", "add": "igp-metric"},
                        },
                        "sub_route_map": {"name": "mapmerge"},
                    },
                ],
                "route_map": "mapmerge2",
            },
        ]
        self.assertEqual(parsed_list, result["parsed"])
