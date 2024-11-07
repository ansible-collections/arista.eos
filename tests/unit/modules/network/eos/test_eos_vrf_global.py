#
# (c) 2024, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from textwrap import dedent
from unittest.mock import patch

from ansible_collections.arista.eos.plugins.modules import eos_vrf_global
from ansible_collections.arista.eos.tests.unit.modules.utils import set_module_args

from .eos_module import TestEosModule


class TestEosVrfGlobalModule(TestEosModule):
    """Tests the eos_vrf_global module."""

    module = eos_vrf_global

    def setUp(self):
        """Setup for eos_vrf module tests."""
        super(TestEosVrfGlobalModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        self.mock_get_config = patch(
            "ansible_collections.arista.eos.plugins.module_utils.network.eos.facts.vrf_global.vrf_global."
            "Vrf_globalFacts.get_config",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        """Tear down for eos_vrf_global module tests."""
        super(TestEosVrfGlobalModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_eos_vrf_global_merged_idempotent(self):
        """Test the idempotent nature of the eos_vrf_global module in merged state."""
        run_cfg = dedent(
            """\
            vrf instance test
             description "this is sample vrf for feature testing"
             rd "2:3"
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=[
                    dict(
                        name="test",
                        description="this is sample vrf for feature testing",
                        rd="2:3",
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_vrf_global_merged(self):
        """Test the merged state of the eos_vrf_global module."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                        description="VRF4 Description",
                        rd="3:4",
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "vrf instance VRF4",
            "description VRF4 Description",
            "rd 3:4",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_eos_vrf_global_replaced(self):
        """Test the replaced state of the eos_vrf_global module."""
        run_cfg = dedent(
            """\
            vrf instance VRF4
             description VRF4 description
             rd 3:4
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                        description="VRF4 description",
                        rd="3:4",
                    ),
                    dict(
                        name="VRF7",
                        description="VRF7 description",
                        rd="67:9",
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "vrf instance VRF7",
            "description VRF7 description",
            "rd 67:9",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_eos_vrf_global_replaced_idempotent(self):
        """Test the idempotent nature of the eos_vrf_global module in replaced state."""
        run_cfg = dedent(
            """\
            vrf instance VRF4
             description VRF4 description
             rd 3:4
            vrf instance VRF7
             description VRF7 description
             rd 67:9
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                        description="VRF4 description",
                        rd="3:4",
                    ),
                    dict(
                        name="VRF7",
                        description="VRF7 description",
                        rd="67:9",
                    ),
                ],
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_vrf_global_overridden(self):
        """Test the overridden state of the eos_vrf_global module."""
        run_cfg = dedent(
            """\
            vrf instance VRF4
             description VRF4 description
             rd 3:4
            vrf instance VRF7
             description VRF7 description
             rd 6:9
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                    ),
                    dict(
                        name="VRF6",
                        description="VRF6 description",
                        rd="9:8",
                    ),
                    dict(
                        name="VRF7",
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "vrf instance VRF4",
            "no description VRF4 description",
            "no rd 3:4",
            "vrf instance VRF7",
            "no description VRF7 description",
            "no rd 6:9",
            "vrf instance VRF6",
            "description VRF6 description",
            "rd 9:8",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_eos_vrf_global_overridden_idempotent(self):
        """Test the idempotent nature of the eos_vrf_global module in overridden state."""
        run_cfg = dedent(
            """\
            vrf instance VRF4
            vrf instance VRF6
             description VRF6 description
             rd 67:9
            vrf instance VRF7
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                    ),
                    dict(
                        name="VRF6",
                        description="VRF6 description",
                        rd="67:9",
                    ),
                    dict(
                        name="VRF7",
                    ),
                ],
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_vrf_global_deleted(self):
        """Test the deleted state of the eos_vrf_global module."""
        run_cfg = dedent(
            """\
            vrf instance VRF4
            vrf instance VRF6
             description VRF6 description
             rd 9:8
            vrf instance VRF7
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                    ),
                    dict(
                        name="VRF6",
                    ),
                    dict(
                        name="VRF7",
                    ),
                ],
                state="deleted",
            ),
        )

        commands = [
            "vrf instance VRF6",
            "no description VRF6 description",
            "no rd 9:8",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_eos_vrf_global_deleted_idempotent(self):
        """Test the idempotent nature of the eos_vrf_global module in deleted state."""
        run_cfg = dedent(
            """\
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=[], state="deleted"))

        result = self.execute_module(changed=False)
        self.assertEqual(result["commands"], [])

    def test_eos_vrf_global_purged(self):
        """Test the purged state of the eos_vrf_global module."""
        run_cfg = dedent(
            """\
            vrf instance VRF4
            vrf instance VRF6
            vrf instance VRF7
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(state="purged"))
        commands = [
            "no vrf instance VRF4",
            "no vrf instance VRF6",
            "no vrf instance VRF7",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_eos_vrf_global_rendered(self):
        """Test the rendered state of the eos_vrf_global module."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                        description="VRF4 Description",
                        rd="3:4",
                    ),
                ],
                state="rendered",
            ),
        )
        commands = [
            "vrf instance VRF4",
            "description VRF4 Description",
            "rd 3:4",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_eos_vrf_global_parsed(self):
        """Test the parsed state of the eos_vrf_global module."""
        run_cfg = dedent(
            """\
            vrf instance my_vrf
             description "this is sample vrf for feature testing"
             rd "2:3"
            """,
        )
        set_module_args(dict(running_config=run_cfg, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "name": "my_vrf",
                "description": "this is sample vrf for feature testing",
                "rd": "2:3",
            },
        ]

        self.assertEqual(parsed_list, result["parsed"])
