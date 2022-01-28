#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.arista.eos.tests.unit.compat.mock import patch
from ansible_collections.arista.eos.plugins.modules import eos_hostname
from ansible_collections.arista.eos.tests.unit.modules.utils import (
    set_module_args,
)
from .eos_module import TestEosModule, load_fixture


class TestEosHostnameModule(TestEosModule):
    module = eos_hostname

    def setUp(self):
        super(TestEosHostnameModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection"
        )
        self.get_resource_connection_config = (
            self.mock_get_resource_connection_config.start()
        )

        self.mock_execute_show_command = patch(
            "ansible_collections.arista.eos.plugins.module_utils.network.eos.facts.hostname.hostname.HostnameFacts.get_config"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestEosHostnameModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, transport="cli", filename=None):
        if filename is None:
            filename = "eos_hostname_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_eos_hostname_merged_idempotent(self):
        set_module_args(dict(config=dict(hostname="eos_test")))
        self.execute_module(changed=False, commands=[])

    def test_eos_hostname_replaced_idempotent(self):
        set_module_args(
            dict(config=dict(hostname="eos_test"), state="replaced")
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_hostname_overridden_idempotent(self):
        set_module_args(
            dict(config=dict(hostname="eos_test"), state="overridden")
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_hostname_merged(self):
        set_module_args(dict(config=dict(hostname="eos")))
        self.execute_module(changed=True, commands=["hostname eos"])

    def test_eos_hostname_replaced(self):
        set_module_args(dict(config=dict(hostname="eos"), state="replaced"))
        self.execute_module(changed=True, commands=["hostname eos"])

    def test_eos_hostname_overridden(self):
        set_module_args(dict(config=dict(hostname="eos"), state="overridden"))

    def test_eos_hostname_deleted(self):
        set_module_args(dict(state="deleted"))
        self.execute_module(changed=True, commands=["no hostname eos_test"])

    def test_eos_hostname_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(
            changed=False, filename="eos_hostname_config.cfg"
        )
        gathered_list = {"hostname": "eos_test"}
        self.assertEqual(sorted(gathered_list), sorted(result["gathered"]))

    def test_eos_hostname_parsed(self):
        parsed_str = "hostname eos_test"
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {"hostname": "eos_test"}
        self.assertEqual(sorted(parsed_list), sorted(result["parsed"]))

    def test_eos_hostname_rendered(self):
        set_module_args(
            dict(state="rendered", config=dict(hostname="eos_test"))
        )
        commands = ["hostname eos_test"]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]), sorted(commands), result["rendered"]
        )
