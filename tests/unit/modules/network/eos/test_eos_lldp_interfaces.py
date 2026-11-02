# (c) 2026 Red Hat, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest.mock import patch

from ansible_collections.arista.eos.plugins.modules import eos_lldp_interfaces
from ansible_collections.arista.eos.tests.unit.modules.utils import set_module_args

from .eos_module import TestEosModule


class TestEosLldpInterfacesModule(TestEosModule):
    module = eos_lldp_interfaces

    def setUp(self):
        super(TestEosLldpInterfacesModule, self).setUp()

        self.mock_execute_module = patch(
            "ansible_collections.arista.eos.plugins.modules.eos_lldp_interfaces.Lldp_interfaces.execute_module",
        )
        self.execute_rm = self.mock_execute_module.start()
        self.execute_rm.return_value = {
            "changed": False,
            "commands": [],
            "before": [],
            "after": [],
        }

    def tearDown(self):
        super(TestEosLldpInterfacesModule, self).tearDown()
        self.mock_execute_module.stop()

    def test_eos_lldp_interfaces_exit_emits_warnings(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        self.assertNotIn("warnings", result)
        self.execute_rm.assert_called_once()
