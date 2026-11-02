# (c) 2026 Red Hat, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest.mock import patch

from ansible_collections.arista.eos.plugins.modules import eos_lldp
from ansible_collections.arista.eos.tests.unit.modules.utils import set_module_args

from .eos_module import TestEosModule


class TestEosLldpModule(TestEosModule):
    module = eos_lldp

    def setUp(self):
        super(TestEosLldpModule, self).setUp()
        self.mock_get_config = patch(
            "ansible_collections.arista.eos.plugins.modules.eos_lldp.get_config",
        )
        self.get_config = self.mock_get_config.start()
        self.get_config.return_value = "lldp run"

        self.mock_load_config = patch(
            "ansible_collections.arista.eos.plugins.modules.eos_lldp.load_config",
        )
        self.load_config = self.mock_load_config.start()
        self.load_config.return_value = dict(diff=None, session="session")

    def tearDown(self):
        super(TestEosLldpModule, self).tearDown()
        self.mock_get_config.stop()
        self.mock_load_config.stop()

    def load_fixtures(self, commands=None, transport="cli"):
        pass

    def test_eos_lldp_present_idempotent(self):
        set_module_args(dict(state="present"))
        result = self.execute_module(changed=False)
        self.assertEqual(result.get("commands"), [])
        self.assertNotIn("warnings", result)

    def test_eos_lldp_absent(self):
        self.get_config.return_value = "lldp run"
        set_module_args(dict(state="absent"))
        self.execute_module(changed=True, commands=["no lldp run"])

    def test_eos_lldp_present_enable(self):
        self.get_config.return_value = "no lldp run"
        set_module_args(dict(state="present"))
        self.execute_module(changed=True, commands=["lldp run"])

    def test_eos_lldp_absent_idempotent(self):
        self.get_config.return_value = "no lldp run"
        set_module_args(dict(state="absent"))
        self.execute_module(changed=False, commands=[])

    def test_eos_lldp_check_mode_and_diff(self):
        self.get_config.return_value = "no lldp run"
        self.load_config.return_value = dict(
            diff="+lldp run",
            session="sess1",
        )
        set_module_args(
            dict(state="present", _ansible_check_mode=True, _ansible_diff=True),
        )
        result = self.execute_module(changed=True)
        self.assertEqual(result["session_name"], "sess1")
        self.assertIn("diff", result)
        _args, kwargs = self.load_config.call_args
        self.assertFalse(kwargs.get("commit"))
