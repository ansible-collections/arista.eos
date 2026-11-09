# (c) 2026 Red Hat, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest.mock import patch

from ansible_collections.arista.eos.plugins.modules import eos_vrf
from ansible_collections.arista.eos.tests.unit.modules.utils import set_module_args

from .eos_module import TestEosModule, load_fixture


class TestEosVrfModule(TestEosModule):
    module = eos_vrf

    def setUp(self):
        super(TestEosVrfModule, self).setUp()
        self.mock_run_commands = patch(
            "ansible_collections.arista.eos.plugins.modules.eos_vrf.run_commands",
        )
        self.run_commands = self.mock_run_commands.start()

        self.mock_load_config = patch(
            "ansible_collections.arista.eos.plugins.modules.eos_vrf.load_config",
        )
        self.load_config = self.mock_load_config.start()
        self.load_config.return_value = dict(diff=None, session="session")

        self.mock_sleep = patch(
            "ansible_collections.arista.eos.plugins.modules.eos_vrf.time.sleep",
        )
        self.sleep = self.mock_sleep.start()

    def tearDown(self):
        super(TestEosVrfModule, self).tearDown()
        self.mock_run_commands.stop()
        self.mock_load_config.stop()
        self.mock_sleep.stop()

    def load_fixtures(self, commands=None, transport="cli"):
        self.run_commands.return_value = [load_fixture("eos_vrf_show_vrf.text")]

    def test_eos_vrf_create(self):
        set_module_args(dict(name="red", rd="1:200", state="present"))
        commands = ["vrf instance red", "rd 1:200"]
        self.execute_module(changed=True, commands=commands)

    def test_eos_vrf_create_with_interfaces(self):
        set_module_args(
            dict(
                name="red",
                interfaces=["Ethernet1", "Ethernet2"],
                state="present",
            ),
        )
        commands = [
            "vrf instance red",
            "interface ethernet1",
            "vrf red",
            "interface ethernet2",
            "vrf red",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_vrf_idempotent(self):
        set_module_args(dict(name="mgmt", rd="1:101", state="present"))
        self.execute_module(changed=False, commands=[])

    def test_eos_vrf_update_rd(self):
        set_module_args(dict(name="mgmt", rd="1:999", state="present"))
        commands = ["vrf instance mgmt", "rd 1:999"]
        self.execute_module(changed=True, commands=commands)

    def test_eos_vrf_add_missing_interfaces(self):
        set_module_args(
            dict(
                name="test",
                interfaces=["Ethernet5", "Ethernet6", "Ethernet7", "Ethernet8"],
                state="present",
            ),
        )
        commands = ["interface ethernet8", "vrf test"]
        self.execute_module(changed=True, commands=commands)

    def test_eos_vrf_add_interfaces_when_none(self):
        set_module_args(
            dict(name="blue", interfaces=["Ethernet1"], state="present"),
        )
        commands = ["interface ethernet1", "vrf blue"]
        self.execute_module(changed=True, commands=commands)

    def test_eos_vrf_absent(self):
        set_module_args(dict(name="mgmt", state="absent"))
        commands = ["no vrf instance mgmt"]
        self.execute_module(changed=True, commands=commands)

    def test_eos_vrf_absent_noop(self):
        set_module_args(dict(name="missing", state="absent"))
        self.execute_module(changed=False, commands=[])

    def test_eos_vrf_purge(self):
        set_module_args(dict(name="mgmt", purge=True, state="present"))
        result = self.execute_module(changed=True)
        self.assertIn("no vrf instance test", result["commands"])
        self.assertIn("no vrf instance blue", result["commands"])

    def test_eos_vrf_aggregate(self):
        set_module_args(
            dict(
                aggregate=[
                    dict(name="red", rd="2:2"),
                    dict(name="green", state="absent"),
                ],
            ),
        )
        result = self.execute_module(changed=True)
        self.assertIn("vrf instance red", result["commands"])
        self.assertIn("rd 2:2", result["commands"])

    def test_eos_vrf_check_mode(self):
        set_module_args(
            dict(name="red", state="present", _ansible_check_mode=True),
        )
        self.execute_module(changed=True)
        _args, kwargs = self.load_config.call_args
        self.assertFalse(kwargs.get("commit"))

    def test_eos_vrf_diff(self):
        self.load_config.return_value = dict(
            diff="@@ -0 +1 @@\n+vrf instance red",
            session="session",
        )
        set_module_args(
            dict(name="red", state="present", _ansible_diff=True),
        )
        result = self.execute_module(changed=True)
        self.assertIn("diff", result)
        self.assertEqual(result["session_name"], "session")

    def test_eos_vrf_associated_interfaces_ok(self):
        set_module_args(
            dict(
                name="test",
                associated_interfaces=["Ethernet5"],
                delay=0,
                state="present",
            ),
        )
        self.execute_module(changed=False)

    def test_eos_vrf_associated_interfaces_fail(self):
        set_module_args(
            dict(
                name="test",
                associated_interfaces=["Ethernet99"],
                delay=0,
                state="present",
            ),
        )
        self.execute_module(failed=True)

    def test_eos_vrf_associated_interfaces_on_change(self):
        set_module_args(
            dict(
                name="red",
                associated_interfaces=["Ethernet1"],
                interfaces=["Ethernet1"],
                delay=0,
                state="present",
            ),
        )
        # New VRF is created (changed); intent check re-reads show vrf and does not
        # fail when the VRF is absent from the refreshed config.
        self.execute_module(changed=True)
        self.sleep.assert_called()
