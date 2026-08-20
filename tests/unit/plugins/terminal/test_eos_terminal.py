from __future__ import absolute_import, division, print_function


__metaclass__ = type

import importlib.util
import json
import os
import re

from unittest.mock import MagicMock

import pytest

from ansible.errors import AnsibleConnectionFailure


@pytest.fixture(scope="module")
def terminal_cls():
    """Import TerminalModule from the local source tree, not the venv install."""
    eos_path = os.path.normpath(
        os.path.join(os.path.dirname(__file__), *[os.pardir] * 4, "plugins", "terminal", "eos.py"),
    )
    spec = importlib.util.spec_from_file_location("eos_terminal_local", eos_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.TerminalModule


@pytest.fixture
def terminal(terminal_cls):
    conn = MagicMock()
    return terminal_cls(conn)


class TestOnBecomePromptRegex:
    """Verify the password prompt regex in on_become handles
    both local auth (trailing space) and TACACS+ auth (no trailing space).
    """

    def _extract_prompt_regex(self, terminal, passwd="secret"):
        """Call on_become and capture the prompt regex from the command JSON."""
        commands = []

        def capture_command(cmd, check_rc=True):
            commands.append(cmd)

        terminal._get_prompt = MagicMock(return_value=b"switch>")
        terminal._exec_cli_command = capture_command

        try:
            terminal.on_become(passwd=passwd)
        except (AnsibleConnectionFailure, AttributeError):
            pass

        cmd_data = json.loads(commands[0])
        return re.compile(cmd_data["prompt"])

    @pytest.mark.parametrize(
        "prompt_text,description",
        [
            ("Password: ", "local auth - trailing space"),
            ("Password:", "TACACS+ auth - no trailing space"),
            ("\nPassword: ", "local auth with leading newline"),
            ("\nPassword:", "TACACS+ auth with leading newline"),
            ("\r\nPassword: ", "local auth with CRLF"),
            ("\r\nPassword:", "TACACS+ auth with CRLF"),
            ("password: ", "lowercase local auth"),
            ("password:", "lowercase TACACS+ auth"),
        ],
    )
    def test_password_prompt_matches(self, terminal, prompt_text, description):
        regex = self._extract_prompt_regex(terminal)
        assert regex.search(
            prompt_text,
        ), f"Prompt regex should match '{prompt_text!r}' ({description})"

    @pytest.mark.parametrize(
        "prompt_text",
        [
            "Username: ",
            "Login: ",
            "Enter password for key: ",
        ],
    )
    def test_password_prompt_rejects_non_password(self, terminal, prompt_text):
        regex = self._extract_prompt_regex(terminal)
        assert not regex.search(prompt_text)


class TestOnBecome:

    def test_already_privileged(self, terminal):
        terminal._get_prompt = MagicMock(return_value=b"switch#")
        terminal._exec_cli_command = MagicMock()
        terminal.on_become(passwd="secret")
        terminal._exec_cli_command.assert_not_called()

    def test_no_password_sends_enable_only(self, terminal):
        terminal._get_prompt = MagicMock(side_effect=[b"switch>", b"switch#"])
        terminal._exec_cli_command = MagicMock()
        terminal.on_become()
        cmd_data = json.loads(terminal._exec_cli_command.call_args[0][0])
        assert cmd_data == {"command": "enable"}

    def test_with_password_includes_prompt_and_retry(self, terminal):
        terminal._get_prompt = MagicMock(side_effect=[b"switch>", b"switch#"])
        terminal._exec_cli_command = MagicMock()
        terminal.on_become(passwd="secret")
        cmd_data = json.loads(terminal._exec_cli_command.call_args[0][0])
        assert cmd_data["command"] == "enable"
        assert cmd_data["answer"] == "secret"
        assert cmd_data["prompt_retry_check"] is True
        assert "prompt" in cmd_data

    def test_failed_elevation_raises(self, terminal):
        terminal._get_prompt = MagicMock(
            side_effect=[b"switch>", b"switch>", b"switch>"],
        )
        terminal._exec_cli_command = MagicMock()
        with pytest.raises(AnsibleConnectionFailure, match="unable to elevate"):
            terminal.on_become(passwd="secret")
