# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the
# cli_rm_builder.
#
# Manually editing this file is not advised.
#
# To update the argspec make the desired changes
# in the module docstring and re-run
# cli_rm_builder.
#
#############################################

"""
The arg spec for the eos_logging_global module
"""


class Logging_globalArgs(object):  # pylint: disable=R0903
    """The arg spec for the eos_logging_global module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "type": "dict",
            "options": {
                "buffered": {
                    "type": "dict",
                    "options": {
                        "severity": {
                            "type": "str",
                            "choices": [
                                "alerts",
                                "critical",
                                "debugging",
                                "emergencies",
                                "errors",
                                "informational",
                                "notifications",
                                "warnings",
                            ],
                        },
                        "buffer_size": {"type": "int"},
                    },
                },
                "console": {
                    "type": "dict",
                    "options": {
                        "severity": {
                            "type": "str",
                            "choices": [
                                "alerts",
                                "critical",
                                "debugging",
                                "emergencies",
                                "errors",
                                "informational",
                                "notifications",
                                "warnings",
                            ],
                        },
                    },
                },
                "event": {
                    "type": "str",
                    "choices": [
                        "link-status",
                        "port-channel",
                        "spanning-tree",
                    ],
                },
                "facility": {
                    "type": "str",
                    "choices": [
                        "auth",
                        "cron",
                        "daemon",
                        "kern",
                        "local0",
                        "local1",
                        "local2",
                        "local3",
                        "local4",
                        "local5",
                        "local6",
                        "local7",
                        "lpr",
                        "mail",
                        "news",
                        "sys10",
                        "sys11",
                        "sys12",
                        "sys13",
                        "sys14",
                        "sys9",
                        "syslog",
                        "user",
                        "uucp",
                    ],
                },
                "format": {
                    "type": "dict",
                    "options": {
                        "hostname": {"type": "str"},
                        "timestamp": {
                            "type": "dict",
                            "options": {
                                "high_resolution": {"type": "bool"},
                                "traditional": {
                                    "type": "dict",
                                    "options": {
                                        "state": {
                                            "type": "str",
                                            "choices": ["enabled", "disabled"],
                                        },
                                        "timezone": {"type": "bool"},
                                        "year": {"type": "bool"},
                                    },
                                },
                            },
                        },
                        "sequence_numbers": {"type": "bool"},
                    },
                },
                "hosts": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "name": {"type": "str"},
                        "add": {"type": "bool"},
                        "remove": {"type": "bool"},
                        "protocol": {"type": "str", "choices": ["tcp", "udp"]},
                        "port": {"type": "int", "default": 514},
                    },
                },
                "level": {
                    "type": "dict",
                    "options": {
                        "facility": {"type": "str"},
                        "severity": {
                            "type": "str",
                            "choices": [
                                "alerts",
                                "critical",
                                "debugging",
                                "emergencies",
                                "errors",
                                "informational",
                                "notifications",
                                "warnings",
                            ],
                        },
                    },
                },
                "monitor": {"type": "str"},
                "turn_on": {"type": "bool"},
                "persistent": {
                    "type": "dict",
                    "options": {
                        "set": {"type": "bool"},
                        "size": {"type": "int"},
                    },
                },
                "policy": {
                    "type": "dict",
                    "options": {
                        "invert_result": {"type": "bool"},
                        "match_list": {"type": "str"},
                    },
                },
                "qos": {"type": "int"},
                "relogging_interval": {"type": "int"},
                "repeat_messages": {"type": "bool"},
                "source_interface": {"type": "str"},
                "synchronous": {
                    "type": "dict",
                    "options": {
                        "set": {"type": "bool"},
                        "level": {"type": "str"},
                    },
                },
                "trap": {
                    "type": "dict",
                    "options": {
                        "set": {"type": "bool"},
                        "severity": {
                            "type": "str",
                            "choices": [
                                "alerts",
                                "critical",
                                "debugging",
                                "emergencies",
                                "errors",
                                "informational",
                                "notifications",
                                "warnings",
                            ],
                        },
                    },
                },
                "vrfs": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "name": {"type": "str"},
                        "hosts": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "name": {"type": "str"},
                                "add": {"type": "bool"},
                                "remove": {"type": "bool"},
                                "protocol": {
                                    "type": "str",
                                    "choices": ["tcp", "udp"],
                                },
                                "port": {"type": "int", "default": 514},
                            },
                        },
                        "source_interface": {"type": "str"},
                    },
                },
            },
        },
        "running_config": {"type": "str"},
        "state": {
            "type": "str",
            "choices": [
                "deleted",
                "merged",
                "overridden",
                "replaced",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
        },
    }  # pylint: disable=C0301
