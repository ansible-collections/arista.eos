# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Logging_global parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network_template import (
    NetworkTemplate,
)

class Logging_globalTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(Logging_globalTemplate, self).__init__(lines=lines, tmplt=self, module=module)

    # fmt: off
    PARSERS = [
        {
            "name": "buffered",
            "getval": re.compile(
                r"""
                \s*logging\sbuffered
                \s*(?P<sev>[0-7])*
                \s*(?P<size>\d{2,})*
                \s*(?P<msg>\w+)*
                $""",
                re.VERBOSE,
            ),
            "setval": 'logging buffered {{ buffered.severity}} {{ buffered.buffer_size }} {{ buffered.message_type}}',
            "result": {
                "buffered": {
                    "message_type": "{{ msg }}",
                    "buffer_size": "{{ size }}",
                    "severity": "{{ sev }}"
                }
            },
        },
        {
            "name": "console",
            "getval": re.compile(
                r"""
                \s*logging\sconsole
                \s*(?P<sev>[0-7])*
                \s*(?P<msg>\w+)*
                $""",
                re.VERBOSE,
            ),
            "setval": 'logging console {{ console.severity}} {{ console.message_type}}',
            "result": {
                "console": {
                    "message_type": "{{ msg }}",
                    "severity": "{{ sev }}"
                }
            },
        },
        {
            "name": "event",
            "getval": re.compile(
                r"""
                \s*logging\sevent
                \s(?P<event>link-status|port-channel|spanning-tree)
                \s*(?P<mem>member-status)*
                \sglobal
                *$""",
                re.VERBOSE,
            ),
            "setval": 'logging event {{ event }} {{ mem }} global',
            "result": {
                "event": "{{ event }}"
            },
        },
        {
            "name": "facility",
            "getval": re.compile(
                r"""
                \s*logging\sfacility
                \s(?P<facility>\S+)
                *$""",
                re.VERBOSE,
            ),
            "setval": 'logging facility {{ facility }}',
            "result": {
                "facility": "{{ facility }}"
            },
        },
        {
            "name": "console",
            "getval": re.compile(
                r"""
                \s*logging\sconsole
                \s*(?P<sev>[0-7])*
                \s*(?P<msg>\w+)*
                $""",
                re.VERBOSE,
            ),
            "setval": 'logging console {{ console.severity}} {{ console.message_type}}',
            "result": {
                "console": {
                    "message_type": "{{ msg }}",
                    "severity": "{{ sev }}"
                }
            },
        },
        {
            "name": "format",
            "getval": re.compile(
                r"""
                \s*logging\sformat
                \s*(?P<param>hostname\s\S+|sequence-numbers)*
                $""",
                re.VERBOSE,
            ),
            "setval": 'logging format {{ param.split(" ")[0] }} {{ param.split(" ")[1] if "hostname" in param }}',
            "result": {
                "format": {
                    '{{ param.split(" ")[0] }}': '{{ param.split(" ")[1] if "hostname" in param else True }}',
                }
            },
        },
        {
            "name": "format.timestamp",
            "getval": re.compile(
                r"""
                \s*logging\sformat\stimestamp
                \s*(?P<highresol>high-resolution)*
                \s*(?P<year>year)*
                \s*(?P<zone>timezone)*
                $""",
                re.VERBOSE,
            ),
            "setval": 'logging format timestamp {{ year if year is defined }} {{ timezone if timezone is defined }}',
            "result": {
                "format": {
                    "timestamp": {
                        "year": "{{ True if year is defined}}",
                        "timezone": "{{ True if timezone is defined}}",
                        "state": "{{ enabled if year and timezone is undefined}}",
                }
            },
        },

        {
            "name": "key_a",
            "getval": re.compile(
                r"""
                ^key_a\s(?P<key_a>\S+)
                $""", re.VERBOSE),
            "setval": "",
            "result": {
            },
            "shared": True
        },
        {
            "name": "key_b",
            "getval": re.compile(
                r"""
                \s+key_b\s(?P<key_b>\S+)
                $""", re.VERBOSE),
            "setval": "",
            "result": {
            },
        },
    ]
    # fmt: on
