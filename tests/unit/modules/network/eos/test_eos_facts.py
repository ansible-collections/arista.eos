# (c) 2026 Red Hat, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest.mock import patch

from ansible_collections.arista.eos.plugins.modules import eos_facts
from ansible_collections.arista.eos.tests.unit.modules.utils import set_module_args

from .eos_module import TestEosModule


class TestEosFactsModule(TestEosModule):
    module = eos_facts

    def setUp(self):
        super(TestEosFactsModule, self).setUp()
        self.mock_get_facts = patch(
            "ansible_collections.arista.eos.plugins.modules.eos_facts.Facts.get_facts",
        )
        self.get_facts = self.mock_get_facts.start()
        self.get_facts.return_value = ({}, [])

    def tearDown(self):
        super(TestEosFactsModule, self).tearDown()
        self.mock_get_facts.stop()

    def test_eos_facts_exit_emits_warnings(self):
        set_module_args(dict(gather_subset="min"))
        result = self.execute_module(changed=False)
        self.assertIn("ansible_facts", result)
        self.assertNotIn("warnings", result)

    def test_eos_facts_available_network_resources(self):
        set_module_args(dict(available_network_resources=True, gather_subset="min"))
        result = self.execute_module(changed=False)
        self.assertIn(
            "available_network_resources",
            result["ansible_facts"],
        )
        self.assertTrue(result["ansible_facts"]["available_network_resources"])

    def test_eos_facts_merges_warnings(self):
        self.get_facts.return_value = ({"ansible_net_hostname": "eos1"}, ["warn1"])
        set_module_args(dict(gather_subset="min"))
        result = self.execute_module(changed=False)
        self.assertEqual(result["ansible_facts"]["ansible_net_hostname"], "eos1")
        self.assertNotIn("warnings", result)
