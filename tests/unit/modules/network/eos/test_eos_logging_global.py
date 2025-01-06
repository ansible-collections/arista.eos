#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.arista.eos.plugins.modules import eos_logging_global
from ansible_collections.arista.eos.tests.unit.modules.utils import set_module_args

from .eos_module import TestEosModule, load_fixture


class TestEosLogging_GlobalModule(TestEosModule):
    module = eos_logging_global

    def setUp(self):
        super(TestEosLogging_GlobalModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.arista.eos.plugins.module_utils.network.eos.facts.logging_global.logging_global.Logging_globalFacts.get_config",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestEosLogging_GlobalModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, transport="cli", filename=None):
        if filename is None:
            filename = "eos_logging_global_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_eos_logging_global_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    buffered=dict(buffer_size=50000, severity="informational"),
                    console=dict(severity="warnings"),
                    facility="local7",
                    format=dict(
                        timestamp=dict(traditional=dict(timezone=True)),
                    ),
                    hosts=[
                        dict(name="11.11.11.1", port=25),
                        dict(name="host01", port=514, protocol="tcp"),
                    ],
                    level=dict(facility="AAA", severity="alerts"),
                    persistent=dict(size=4096),
                    policy=dict(invert_result=True, match_list="list01"),
                    vrfs=[
                        dict(name="vrf01", source_interface="Ethernet1"),
                        dict(
                            name="vrf02",
                            hosts=[
                                dict(name="24.1.1.1", port=33),
                                dict(
                                    name="hostvrf1",
                                    port=514,
                                    protocol="tcp",
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_logging_global_replaced_idempotent(self):
        set_module_args(
            dict(
                state="replaced",
                config=dict(
                    buffered=dict(buffer_size=50000, severity="informational"),
                    console=dict(severity="warnings"),
                    facility="local7",
                    format=dict(
                        timestamp=dict(traditional=dict(timezone=True)),
                    ),
                    hosts=[
                        dict(name="11.11.11.1", port=25),
                        dict(name="host01", port=514, protocol="tcp"),
                    ],
                    level=dict(facility="AAA", severity="alerts"),
                    persistent=dict(size=4096),
                    policy=dict(invert_result=True, match_list="list01"),
                    vrfs=[
                        dict(name="vrf01", source_interface="Ethernet1"),
                        dict(
                            name="vrf02",
                            hosts=[
                                dict(name="24.1.1.1", port=33),
                                dict(
                                    name="hostvrf1",
                                    port=514,
                                    protocol="tcp",
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_logging_global_overridden_idempotent(self):
        set_module_args(
            dict(
                state="overridden",
                config=dict(
                    buffered=dict(buffer_size=50000, severity="informational"),
                    console=dict(severity="warnings"),
                    facility="local7",
                    format=dict(
                        timestamp=dict(traditional=dict(timezone=True)),
                    ),
                    hosts=[
                        dict(name="11.11.11.1", port=25),
                        dict(name="host01", port=514, protocol="tcp"),
                    ],
                    level=dict(facility="AAA", severity="alerts"),
                    persistent=dict(size=4096),
                    policy=dict(invert_result=True, match_list="list01"),
                    vrfs=[
                        dict(name="vrf01", source_interface="Ethernet1"),
                        dict(
                            name="vrf02",
                            hosts=[
                                dict(name="24.1.1.1", port=33),
                                dict(
                                    name="hostvrf1",
                                    port=514,
                                    protocol="tcp",
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_logging_global_merged(self):
        set_module_args(
            dict(
                config=dict(
                    synchronous=dict(set=True),
                    trap=dict(severity="critical"),
                    source_interface="Loopback6",
                    hosts=[dict(name="host02", protocol="tcp")],
                    vrfs=[
                        dict(name="vrf03", source_interface="vlan100"),
                        dict(
                            name="vrf04",
                            hosts=[
                                dict(
                                    name="hostvrf1",
                                    protocol="tcp",
                                    add=True,
                                ),
                                dict(
                                    name="hostvrf2",
                                    protocol="tcp",
                                    remove=True,
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        )
        commands = [
            "logging host host02 protocol tcp",
            "logging vrf vrf04 host hostvrf1 add protocol tcp",
            "logging vrf vrf04 host hostvrf2 remove protocol tcp",
            "logging vrf vrf03 source-interface vlan100",
            "logging synchronous",
            "logging trap critical",
            "logging source-interface Loopback6",
        ]
        self.execute_module(changed=True, commands=sorted(commands))

    def test_eos_logging_global_replaced(self):
        set_module_args(
            dict(
                state="replaced",
                config=dict(
                    format=dict(sequence_numbers=True),
                    synchronous=dict(level="informational"),
                    trap=dict(severity="critical"),
                    hosts=[
                        dict(name="host02", protocol="tcp", add=True),
                        dict(name="host03", protocol="tcp", remove=True),
                    ],
                    vrfs=[
                        dict(name="vrf03", source_interface="vlan100"),
                        dict(
                            name="vrf04",
                            hosts=[dict(name="hostvrf1", protocol="tcp")],
                        ),
                    ],
                ),
            ),
        )
        commands = [
            "logging host host02 add protocol tcp",
            "logging host host03 remove protocol tcp",
            "no logging host 11.11.11.1 25",
            "no logging host host01 514 protocol tcp",
            "logging vrf vrf03 source-interface vlan100",
            "logging vrf vrf04 host hostvrf1 protocol tcp",
            "no logging vrf vrf01 source-interface Ethernet1",
            "no logging vrf vrf02 host 24.1.1.1 33",
            "no logging vrf vrf02 host hostvrf1 514 protocol tcp",
            "no logging buffered 50000 informational",
            "no logging facility local7",
            "no logging console warnings",
            "no logging format timestamp traditional timezone",
            "no logging level AAA alerts",
            "no logging persistent 4096",
            "no logging policy match invert-result match-list list01 discard",
            "logging format sequence-numbers",
            "logging synchronous level informational",
            "logging trap critical",
        ]
        self.execute_module(changed=True, commands=sorted(commands))

    def test_eos_logging_global_overridden(self):
        set_module_args(
            dict(
                state="overridden",
                config=dict(
                    format=dict(hostname="host01"),
                    synchronous=dict(set=True),
                    trap=dict(severity="critical"),
                    hosts=[dict(name="host02", protocol="tcp")],
                    vrfs=[
                        dict(name="vrf03", source_interface="vlan100"),
                        dict(
                            name="vrf04",
                            hosts=[dict(name="hostvrf1", protocol="tcp")],
                        ),
                    ],
                ),
            ),
        )
        commands = [
            "logging host host02 protocol tcp",
            "no logging host 11.11.11.1 25",
            "no logging host host01 514 protocol tcp",
            "logging vrf vrf03 source-interface vlan100",
            "logging vrf vrf04 host hostvrf1 protocol tcp",
            "no logging vrf vrf01 source-interface Ethernet1",
            "no logging vrf vrf02 host 24.1.1.1 33",
            "no logging vrf vrf02 host hostvrf1 514 protocol tcp",
            "no logging buffered 50000 informational",
            "no logging facility local7",
            "no logging console warnings",
            "no logging format timestamp traditional timezone",
            "no logging level AAA alerts",
            "no logging persistent 4096",
            "no logging policy match invert-result match-list list01 discard",
            "logging format hostname host01",
            "logging synchronous",
            "logging trap critical",
        ]
        self.execute_module(changed=True, commands=sorted(commands))

    def test_eos_logging_global_deleted(self):
        set_module_args(
            dict(
                state="deleted",
            ),
        )
        commands = [
            "no logging host 11.11.11.1 25",
            "no logging host host01 514 protocol tcp",
            "no logging vrf vrf01 source-interface Ethernet1",
            "no logging vrf vrf02 host 24.1.1.1 33",
            "no logging vrf vrf02 host hostvrf1 514 protocol tcp",
            "no logging buffered 50000 informational",
            "no logging facility local7",
            "no logging console warnings",
            "no logging format timestamp traditional timezone",
            "no logging level AAA alerts",
            "no logging persistent 4096",
            "no logging policy match invert-result match-list list01 discard",
        ]
        self.execute_module(changed=True, commands=sorted(commands))

    def test_eos_logging_global_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(
            changed=False,
            filename="eos_logging_global_config.cfg",
        )
        gathered_list = {
            "buffered": {"buffer_size": "50000", "severity": "informational"},
            "console": {"severity": "warnings"},
            "facility": "local7",
            "format": {"timestamp": {"traditional": {"timezone": "True"}}},
            "hosts": [
                {"name": "11.11.11.1", "port": 25},
                {"name": "host01", "port": 514, "protocol": "tcp"},
            ],
            "level": {"facility": "AAA", "severity": "alerts"},
            "persistent": {"size": 4096},
            "policy": {"invert_result": "True", "match_list": "list01"},
            "vrfs": [
                {"name": "vrf01", "source_interface": "Ethernet1"},
                {
                    "name": "vrf02",
                    "hosts": [
                        {"name": "24.1.1.1", "port": 33},
                        {"name": "hostvrf1", "port": 514, "protocol": "tcp"},
                    ],
                },
            ],
        }
        self.assertEqual(sorted(gathered_list), sorted(result["gathered"]))

    def test_eos_logging_global_parsed(self):
        commands = [
            "logging console warnings",
            "logging buffered 50000 informational",
            "logging facility local7",
            "logging host 11.11.11.1 25",
            "logging host host01 514 protocol tcp",
            "logging vrf vrf02 host 24.1.1.1 33",
            "logging vrf vrf02 host hostvrf1 514 protocol tcp",
            "logging format timestamp traditional timezone",
            "logging vrf vrf01 source-interface Ethernet1",
            "logging policy match inverse-result match-list list01 discard",
            "logging persistent 4096",
            "logging level AAA alerts",
        ]
        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {
            "buffered": {"buffer_size": "50000", "severity": "informational"},
            "console": {"severity": "warnings"},
            "facility": "local7",
            "format": {"timestamp": {"traditional": {"timezone": True}}},
            "hosts": [
                {"name": "11.11.11.1", "port": 25},
                {"name": "host01", "port": 514, "protocol": "tcp"},
            ],
            "level": {"facility": "AAA", "severity": "alerts"},
            "persistent": {"size": 4096},
            "policy": {"invert_result": True, "match_list": "list01"},
            "vrfs": [
                {"name": "vrf01", "source_interface": "Ethernet1"},
                {
                    "name": "vrf02",
                    "hosts": [
                        {"name": "24.1.1.1", "port": 33},
                        {"name": "hostvrf1", "port": 514, "protocol": "tcp"},
                    ],
                },
            ],
        }
        self.assertEqual(sorted(parsed_list), sorted(result["parsed"]))

    def test_eos_logging_global_rendered(self):
        set_module_args(
            dict(
                state="rendered",
                config=dict(
                    buffered=dict(buffer_size=50000, severity="informational"),
                    console=dict(severity="warnings"),
                    facility="local7",
                    format=dict(
                        timestamp=dict(traditional=dict(timezone=True)),
                    ),
                    hosts=[
                        dict(name="11.11.11.1", port=25),
                        dict(name="host01", port=514, protocol="tcp"),
                    ],
                    level=dict(facility="AAA", severity="alerts"),
                    persistent=dict(size=4096),
                    policy=dict(invert_result=True, match_list="list01"),
                    vrfs=[
                        dict(name="vrf01", source_interface="Ethernet1"),
                        dict(
                            name="vrf02",
                            hosts=[
                                dict(name="24.1.1.1", port=33),
                                dict(
                                    name="hostvrf1",
                                    port=514,
                                    protocol="tcp",
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        )
        commands = [
            "logging console warnings",
            "logging buffered 50000 informational",
            "logging facility local7",
            "logging host 11.11.11.1 25",
            "logging host host01 514 protocol tcp",
            "logging vrf vrf02 host 24.1.1.1 33",
            "logging vrf vrf02 host hostvrf1 514 protocol tcp",
            "logging format timestamp traditional timezone",
            "logging vrf vrf01 source-interface Ethernet1",
            "logging policy match invert-result match-list list01 discard",
            "logging persistent 4096",
            "logging level AAA alerts",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(commands),
            result["rendered"],
        )
