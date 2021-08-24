#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.arista.eos.tests.unit.compat.mock import patch
from ansible_collections.arista.eos.plugins.modules import eos_prefix_lists
from ansible_collections.arista.eos.tests.unit.modules.utils import (
    set_module_args,
)
from .eos_module import TestEosModule, load_fixture


class TestEosPrefix_ListsModule(TestEosModule):
    module = eos_prefix_lists

    def setUp(self):
        super(TestEosPrefix_ListsModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection"
        )
        self.get_resource_connection_config = (
            self.mock_get_resource_connection_config.start()
        )

        self.mock_execute_show_command = patch(
            "ansible_collections.arista.eos.plugins.module_utils.network.eos.facts.prefix_lists.prefix_lists.Prefix_listsFacts.get_config"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestEosPrefix_ListsModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, transport="cli", filename=None):
        if filename is None:
            filename = "eos_prefix_lists_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_eos_prefix_lists_mergede_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="v401",
                                entries=[
                                    dict(
                                        sequence=25,
                                        action="deny",
                                        address="45.55.4.0/24",
                                    ),
                                    dict(
                                        sequence=100,
                                        action="permit",
                                        address="11.11.2.0/24",
                                        match=dict(masklen=32, operator="ge"),
                                    ),
                                ],
                            ),
                            dict(
                                name="v402",
                                entries=[
                                    dict(
                                        sequence=10,
                                        action="deny",
                                        address="10.1.1.0/24",
                                    )
                                ],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        prefix_lists=[
                            dict(
                                name="v601",
                                entries=[
                                    dict(
                                        sequence=125,
                                        action="deny",
                                        address="5000:1::/64",
                                    )
                                ],
                            )
                        ],
                    ),
                ]
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_prefix_lists_merged_error(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="v401",
                                entries=[
                                    dict(
                                        sequence=25,
                                        action="deny",
                                        address="45.55.4.0/24",
                                        match=dict(masklen=32, operator="ge"),
                                    )
                                ],
                            )
                        ],
                    )
                ]
            )
        )
        result = self.execute_module(failed=True)
        self.assertIn(
            "Sequence number 25 is already present. Use replaced/overridden operation to change the configuration",
            result["msg"],
        )

    def test_eos_prefix_lists_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="v401",
                                entries=[
                                    dict(
                                        sequence=300,
                                        action="permit",
                                        address="192.11.2.0/24",
                                    ),
                                    dict(
                                        resequence=dict(start_seq=20, step=2)
                                    ),
                                ],
                            ),
                            dict(
                                name="v403",
                                entries=[
                                    dict(
                                        sequence=100,
                                        action="deny",
                                        address="192.0.2.0/24",
                                        match=dict(masklen=32, operator="le"),
                                    )
                                ],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        prefix_lists=[
                            dict(
                                name="v601",
                                entries=[
                                    dict(
                                        sequence=125,
                                        action="deny",
                                        address="5000:1::/64",
                                    )
                                ],
                            )
                        ],
                    ),
                ]
            )
        )
        commands = [
            "ip prefix-list v401",
            "seq 300 permit 192.11.2.0/24",
            "ip prefix-list v403",
            "seq 100 deny 192.0.2.0/24 le 32",
            "resequence 20 2",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_prefix_lists_replaced_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="v401",
                                entries=[
                                    dict(
                                        sequence=25,
                                        action="deny",
                                        address="45.55.4.0/24",
                                    ),
                                    dict(
                                        sequence=100,
                                        action="permit",
                                        address="11.11.2.0/24",
                                        match=dict(masklen=32, operator="ge"),
                                    ),
                                ],
                            ),
                            dict(
                                name="v402",
                                entries=[
                                    dict(
                                        sequence=10,
                                        action="deny",
                                        address="10.1.1.0/24",
                                    )
                                ],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        prefix_lists=[
                            dict(
                                name="v601",
                                entries=[
                                    dict(
                                        sequence=125,
                                        action="deny",
                                        address="5000:1::/64",
                                    )
                                ],
                            )
                        ],
                    ),
                ],
                state="replaced",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_prefix_lists_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="v401",
                                entries=[
                                    dict(
                                        sequence=300,
                                        action="permit",
                                        address="192.11.2.0/24",
                                    ),
                                    dict(resequence=dict(default=True)),
                                ],
                            ),
                            dict(
                                name="v403",
                                entries=[
                                    dict(
                                        sequence=100,
                                        action="deny",
                                        address="192.0.2.0/24",
                                        match=dict(masklen=32, operator="le"),
                                    )
                                ],
                            ),
                        ],
                    )
                ],
                state="replaced",
            )
        )
        commands = [
            "ip prefix-list v401",
            "seq 300 permit 192.11.2.0/24",
            "resequence",
            "no seq 25",
            "no seq 100",
            "no ip prefix-list v402",
            "ip prefix-list v403",
            "seq 100 deny 192.0.2.0/24 le 32",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_prefix_lists_overridden_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="v401",
                                entries=[
                                    dict(
                                        sequence=25,
                                        action="deny",
                                        address="45.55.4.0/24",
                                    ),
                                    dict(
                                        sequence=100,
                                        action="permit",
                                        address="11.11.2.0/24",
                                        match=dict(masklen=32, operator="ge"),
                                    ),
                                ],
                            ),
                            dict(
                                name="v402",
                                entries=[
                                    dict(
                                        sequence=10,
                                        action="deny",
                                        address="10.1.1.0/24",
                                    )
                                ],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        prefix_lists=[
                            dict(
                                name="v601",
                                entries=[
                                    dict(
                                        sequence=125,
                                        action="deny",
                                        address="5000:1::/64",
                                    )
                                ],
                            )
                        ],
                    ),
                ],
                state="overridden",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_prefix_lists_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="v401",
                                entries=[
                                    dict(
                                        sequence=300,
                                        action="permit",
                                        address="192.11.2.0/24",
                                    ),
                                    dict(resequence=dict(default=True)),
                                ],
                            ),
                            dict(
                                name="v403",
                                entries=[
                                    dict(
                                        sequence=100,
                                        action="deny",
                                        address="192.0.2.0/24",
                                        match=dict(masklen=32, operator="le"),
                                    )
                                ],
                            ),
                        ],
                    )
                ],
                state="overridden",
            )
        )
        commands = [
            "ip prefix-list v401",
            "seq 300 permit 192.11.2.0/24",
            "resequence",
            "no seq 25",
            "no seq 100",
            "no ip prefix-list v402",
            "ip prefix-list v403",
            "seq 100 deny 192.0.2.0/24 le 32",
            "no ipv6 prefix-list v601",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_prefix_lists_delete_afi(self):
        set_module_args(dict(config=[dict(afi="ipv4")], state="deleted"))
        commands = ["no ip prefix-list v401", "no ip prefix-list v402"]
        self.execute_module(changed=True, commands=commands)

    def test_eos_prefix_lists_delete_all(self):
        set_module_args(dict(state="deleted"))
        commands = [
            "no ip prefix-list v401",
            "no ip prefix-list v402",
            "no ipv6 prefix-list v601",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_prefix_lists_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="v401",
                                entries=[
                                    dict(
                                        sequence=300,
                                        action="permit",
                                        address="192.11.2.0/24",
                                    ),
                                    dict(
                                        resequence=dict(start_seq=20, step=2)
                                    ),
                                ],
                            ),
                            dict(
                                name="v403",
                                entries=[
                                    dict(
                                        sequence=100,
                                        action="deny",
                                        address="192.0.2.0/24",
                                        match=dict(masklen=32, operator="le"),
                                    )
                                ],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        prefix_lists=[
                            dict(
                                name="v601",
                                entries=[
                                    dict(
                                        sequence=125,
                                        action="deny",
                                        address="5000:1::/64",
                                    )
                                ],
                            )
                        ],
                    ),
                ],
                state="rendered",
            )
        )
        commands = [
            "ip prefix-list v401",
            "seq 300 permit 192.11.2.0/24",
            "resequence 20 2",
            "ip prefix-list v403",
            "seq 100 deny 192.0.2.0/24 le 32",
            "ipv6 prefix-list v601",
            "seq 125 deny 5000:1::/64",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]), sorted(commands), result["rendered"]
        )

    def test_eos_prefix_lists_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(
            changed=False, filename="eos_prefix_lists_config.cfg"
        )
        gathered_list = {
            "ipv4": [
                {
                    "entries": [
                        {
                            "action": "deny",
                            "address": "45.55.4.0/24",
                            "sequence": 25,
                        },
                        {
                            "action": "permit",
                            "address": "11.11.2.0/24",
                            "match": {"masklen": 32, "operator": "ge"},
                            "sequence": 100,
                        },
                    ],
                    "name": "v401",
                },
                {
                    "entries": [
                        {
                            "action": "deny",
                            "address": "10.1.1.0/24",
                            "sequence": 10,
                        }
                    ],
                    "name": "v402",
                },
            ],
            "ipv6": [
                {
                    "entries": [
                        {
                            "action": "deny",
                            "address": "5000:1::/64",
                            "sequence": 125,
                        }
                    ],
                    "name": "v601",
                }
            ],
        }
        for entry in result["gathered"]:
            if entry.get("afi") in ["ipv4", "ipv6"]:
                self.assertEqual(
                    gathered_list[entry["afi"]], entry["prefix_lists"]
                )

    def test_eos_route_maps_parsed(self):
        commands = [
            "ip prefix-list v401",
            "seq 25 deny 45.55.4.0/24",
            "seq 100 permit 11.11.2.0/24 ge 32",
            "ip prefix-list v402",
            "seq 10 deny 10.1.1.0/24",
            "ipv6 prefix-list v601",
            "seq 125 deny 5000:1::/64",
        ]
        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "afi": "ipv4",
                "prefix_lists": [
                    {
                        "entries": [
                            {
                                "action": "deny",
                                "address": "45.55.4.0/24",
                                "sequence": 25,
                            },
                            {
                                "action": "permit",
                                "address": "11.11.2.0/24",
                                "match": {"masklen": 32, "operator": "ge"},
                                "sequence": 100,
                            },
                        ],
                        "name": "v401",
                    },
                    {
                        "entries": [
                            {
                                "action": "deny",
                                "address": "10.1.1.0/24",
                                "sequence": 10,
                            }
                        ],
                        "name": "v402",
                    },
                ],
            },
            {
                "afi": "ipv6",
                "prefix_lists": [
                    {
                        "entries": [
                            {
                                "action": "deny",
                                "address": "5000:1::/64",
                                "sequence": 125,
                            }
                        ],
                        "name": "v601",
                    }
                ],
            },
        ]
        self.assertEqual(parsed_list, result["parsed"])
