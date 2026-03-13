#
# (c) 2026, Sonic.net, LLC
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

import unittest

from unittest.mock import MagicMock, patch

from ansible_collections.arista.eos.plugins.module_utils.network.eos.eos import (
    HttpApi,
)


def _make_api():
    """Return an HttpApi instance with a mocked connection."""
    module = MagicMock()
    api = HttpApi(module)
    mock_conn = MagicMock()
    # edit_config calls send_request twice:
    #   1. push the session config commands (return value unused)
    #   2. show session-config diffs / commit / abort (response[1] is the diff)
    mock_conn.send_request.side_effect = [
        ["{}"],
        ["", "", ""],
    ]
    api._connection_obj = mock_conn
    return api, mock_conn


# ---------------------------------------------------------------------------
# HttpApi.get_diff  —  diff_replace="config" path
# ---------------------------------------------------------------------------


class TestHttpApiGetDiff(unittest.TestCase):
    def _get_diff(self, candidate, diff_replace="config", running=""):
        api, _conn = _make_api()
        return api.get_diff(
            candidate=candidate,
            running=running,
            diff_replace=diff_replace,
        )

    # --- diff_replace="config" bypasses NetworkConfig ---

    def test_config_replace_returns_candidate_lines(self):
        """Regular config lines are returned verbatim."""
        result = self._get_diff("hostname switch\nip routing\n")
        self.assertIn("hostname switch", result["config_diff"])
        self.assertIn("ip routing", result["config_diff"])

    def test_config_replace_preserves_closing_braces(self):
        """} lines are NOT dropped"""
        candidate = (
            "router general\n"
            "   control-functions\n"
            "      code unit RCF\n"
            "         function foo() {\n"
            "             return true;\n"
            "         }\n"
            "      EOF\n"
        )
        result = self._get_diff(candidate)
        self.assertIn("         }", result["config_diff"])

    def test_config_replace_preserves_semicolons(self):
        """Lines ending with ; are not dropped."""
        candidate = (
            "      code unit RCF\n"
            "         function foo() {\n"
            "             return true;\n"
            "         }\n"
            "      EOF\n"
        )
        result = self._get_diff(candidate)
        self.assertIn("             return true;", result["config_diff"])

    def test_config_replace_filters_blank_lines(self):
        result = self._get_diff("hostname switch\n\n\nip routing\n")
        lines = result["config_diff"].split("\n")
        self.assertNotIn("", lines)

    def test_config_replace_filters_indented_bang_lines(self):
        """! separators that appear with leading whitespace are also filtered."""
        result = self._get_diff("router general\n   !\n   hardware next-hop fast-failover\n")
        lines = result["config_diff"].split("\n")
        self.assertFalse(any(line.strip().startswith("!") for line in lines))

    # --- diff_replace="line" still uses NetworkConfig ---

    def test_line_replace_uses_networkconfig_diff(self):
        """Non-config replace mode still computes a NetworkConfig diff."""
        running = "hostname localhost\n"
        candidate = "hostname switch01\n"
        api, _conn = _make_api()
        result = api.get_diff(
            candidate=candidate,
            running=running,
            diff_replace="line",
        )
        self.assertIn("hostname switch01", result["config_diff"])
        self.assertNotIn("hostname localhost", result["config_diff"])


# ---------------------------------------------------------------------------
# HttpApi.edit_config  —  multiline block assembly
# ---------------------------------------------------------------------------


class TestHttpApiEditConfig(unittest.TestCase):
    def setUp(self):
        self.mock_session = patch(
            "ansible_collections.arista.eos.plugins.module_utils.network.eos.eos.session_name",
            return_value="ansible_test",
        )
        self.mock_session.start()

    def tearDown(self):
        self.mock_session.stop()

    def _sent_commands(self, config, replace=False):
        """Run edit_config and return the commands list from the first send_request call."""
        api, mock_conn = _make_api()
        api.edit_config(config, replace=replace)
        return mock_conn.send_request.call_args_list[0][0][0]

    def _dict_commands(self, commands):
        """Return only the dict entries from a commands list (i.e. multiline eAPI blocks)."""
        return [c for c in commands if isinstance(c, dict)]

    # --- banner block (regression — existing behaviour must be unchanged) ---

    def test_banner_assembled_as_dict(self):
        config = [
            "banner login",
            "line one",
            "line two",
            "EOF",
        ]
        commands = self._sent_commands(config)
        dict_cmds = self._dict_commands(commands)
        self.assertEqual(len(dict_cmds), 1)
        self.assertEqual(dict_cmds[0]["cmd"], "banner login")
        self.assertEqual(dict_cmds[0]["input"], "line one\nline two")

    # --- code unit block ---

    def test_code_unit_assembled_as_dict_with_correct_input(self):
        """code unit block produces one dict with the correct cmd and verbatim input,
        including closing braces which NetworkConfig previously dropped."""
        config = [
            "router general",
            "   control-functions",
            "      code unit RCF",
            "         function foo() {",
            "             return true;",
            "         }",
            "      EOF",
        ]
        commands = self._sent_commands(config)
        dict_cmds = self._dict_commands(commands)
        self.assertEqual(len(dict_cmds), 1)
        self.assertEqual(dict_cmds[0]["cmd"], "code unit RCF")
        self.assertEqual(
            dict_cmds[0]["input"],
            "         function foo() {\n" "             return true;\n" "         }",
        )

    def test_multiple_code_unit_blocks(self):
        config = [
            "router general",
            "   control-functions",
            "      code unit BLOCK1",
            "         function a() { return true; }",
            "      EOF",
            "      code unit BLOCK2",
            "         function b() { return false; }",
            "      EOF",
        ]
        commands = self._sent_commands(config)
        dict_cmds = self._dict_commands(commands)
        self.assertEqual(len(dict_cmds), 2)
        self.assertEqual(dict_cmds[0]["cmd"], "code unit BLOCK1")
        self.assertEqual(dict_cmds[0]["input"], "         function a() { return true; }")
        self.assertEqual(dict_cmds[1]["cmd"], "code unit BLOCK2")
        self.assertEqual(dict_cmds[1]["input"], "         function b() { return false; }")

    def test_plain_code_inside_control_functions_assembled_as_dict(self):
        """Plain 'code' (without 'unit') inside control-functions is also a multiline block."""
        config = [
            "router general",
            "   control-functions",
            "      code",
            "         function foo() {",
            "             return true;",
            "         }",
            "      EOF",
        ]
        commands = self._sent_commands(config)
        dict_cmds = self._dict_commands(commands)
        self.assertEqual(len(dict_cmds), 1)
        self.assertEqual(dict_cmds[0]["cmd"], "code")

    def test_code_outside_control_functions_not_treated_as_multiline(self):
        """A line starting with 'code' outside control-functions is a plain command."""
        config = [
            "code command",
            "some other command",
        ]
        commands = self._sent_commands(config)
        dict_cmds = self._dict_commands(commands)
        self.assertEqual(len(dict_cmds), 0)
        self.assertIn("code command", commands)

    def test_context_exits_after_last_code_block(self):
        """After the final EOF in control-functions, subsequent 'code' lines elsewhere
        in the config are not treated as multiline blocks."""
        config = [
            "router general",
            "   control-functions",
            "      code unit RCF",
            "         function f() { return true; }",
            "      EOF",
            "some top level command",
        ]
        commands = self._sent_commands(config)
        dict_cmds = self._dict_commands(commands)
        self.assertEqual(len(dict_cmds), 1)
        self.assertEqual(dict_cmds[0]["cmd"], "code unit RCF")
        self.assertIn("some top level command", commands)

    # --- banner + code unit together ---

    def test_mixed_banner_and_code_unit_blocks(self):
        """A config containing both block types produces two dicts in the correct order."""
        config = [
            "banner login",
            "Welcome to this device",
            "EOF",
            "router general",
            "   control-functions",
            "      code unit RCF",
            "         function f() {",
            "             return true;",
            "         }",
            "      EOF",
        ]
        commands = self._sent_commands(config)
        dict_cmds = self._dict_commands(commands)
        self.assertEqual(len(dict_cmds), 2)
        self.assertEqual(dict_cmds[0]["cmd"], "banner login")
        self.assertEqual(dict_cmds[1]["cmd"], "code unit RCF")


if __name__ == "__main__":
    unittest.main()
