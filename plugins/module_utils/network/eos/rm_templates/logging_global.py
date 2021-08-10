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
        super(Logging_globalTemplate, self).__init__(
            lines=lines, tmplt=self, module=module
        )

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
                }
            },
        },
        {
            "name": "host",
            "getval": re.compile(
                r"""
                \s*logging\shost
                \s(?P<name>\S+)
                \s*(?P<oper>add|remove)*
                \s*(?P<port>\d+)*
                \s*(?P<proto>protocol \S+)*
                $""",
                re.VERBOSE,
            ),
            "setval": 'logging host {{ hosts.name}} {{ oper }} {{ hosts.port }} {{ hosts.protocol }}',
            "result": {
                "hosts": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "add": '{{ True if oper == "add" }}',
                        "remove": '{{ True if oper == "remove" }}',
                        "port": "{{ port }}",
                        "protocol": "{{ protocol }}"
                    }
                }
            },
        },
        {
            "name": "level",
            "getval": re.compile(
                r"""
                \s*logging\slevel
                \s(?P<level>\S+)
                *$""",
                re.VERBOSE,
            ),
            "setval": 'logging level {{ level }}',
            "result": {
                "level": "{{ level }}"
            },
        },
        {
            "name": "monitor",
            "getval": re.compile(
                r"""
                \s*logging\smonitor
                \s(?P<val>\S+)
                *$""",
                re.VERBOSE,
            ),
            "setval": 'logging monitor {{ val }}',
            "result": {
                "level": "{{ val }}"
            },
        },
        {
            "name": "on",
            "getval": re.compile(
                r"""
                \s*logging\son
                *$""",
                re.VERBOSE,
            ),
            "setval": 'logging on',
            "result": {
                "on": "{{ True }}"
            },
        },
        {
            "name": "persistent",
            "getval": re.compile(
                r"""
                \s*logging\spersistent
                \s*(?P<size>\d+)*
                $""",
                re.VERBOSE,
            ),
            "setval": 'logging persistent {{ persistent.size }}',
            "result": {
                "persistent": {
                    "size": "{{ size }}",
                    "set": '{{ True if size is not defined }}',
                }
            },
        },
        {
            "name": "policy",
            "getval": re.compile(
                r"""
                \s*logging\spolicy\smatch
                \s*(?P<inv>invert-result)*
                \s+match-list
                \s+(?P<match>\S+)
                \s+discard
                $""",
                re.VERBOSE,
            ),
            "setval": 'logging policy match {{ inv if policy.invert_result is defined }} match {{ policy.match_list }} discard',
            "result": {
                "policy": {
                    "invert_result": "{{ True if inv is defined }}",
                    "match_list": '{{ match }}',
                }
            },
        },
        {
            "name": "relogging_interval",
            "getval": re.compile(
                r"""
                \s*logging\srelogging-interval
                \s(?P<val>\d+)
                *$""",
                re.VERBOSE,
            ),
            "setval": 'logging relogging-interval {{ relogging_interval }}',
            "result": {
                "relogging_interval": "{{ val }}"
            },
        },
        {
            "name": "repeat_messages",
            "getval": re.compile(
                r"""
                \s*logging\srepeat-messages
                *$""",
                re.VERBOSE,
            ),
            "setval": 'logging repeat-messages',
            "result": {
                "repeat_messages": "{{ True }}"
            },
        },
        {
            "name": "src_interface",
            "getval": re.compile(
                r"""
                \s*logging\ssource-interface
                \s(?P<val>.+)
                *$""",
                re.VERBOSE,
            ),
            "setval": 'logging source-interface {{ source_interface }}',
            "result": {
                "source_interface": "{{ val }}"
            },
        },
        {
            "name": "synchronous",
            "getval": re.compile(
                r"""
                \s*logging\ssynchronous
                \s*(?P<level>level\s\S+)*
                $""",
                re.VERBOSE,
            ),
            "setval": 'logging synchronous {{ synchronous.level if level is defined }}',
            "result": {
                "synchronous": {
                    "set": "{{ True if level is not defined }}",
                    "level": "{{ level.split(" ")[1] if level is defined }}"
                }
            },
        },
        {
            "name": "trap",
            "getval": re.compile(
                r"""
                \s*logging\strap
                \s*(?P<level>\S+)*
                $""",
                re.VERBOSE,
            ),
            "setval": 'logging trap {{ trap.level if level is defined }}',
            "result": {
                "trap": {
                    "set": "{{ True if level is not defined }}",
                    "level": "{{ level }}"
                }
            },
        },
        {
            "name": "vrf.host",
            "getval": re.compile(
                r"""
                \s*logging\svrf
                \s+(?P<vrf>\S+)
                \s+host
                \s(?P<name>\S+)
                \s*(?P<oper>add|remove)*
                \s*(?P<port>\d+)*
                \s*(?P<proto>protocol \S+)*
                $""",
                re.VERBOSE,
            ),
            "setval": 'logging vrf {{ vrfs.name }} host {{ vrfs.hosts.name}} {{ oper if oper is defined }} {{ vrfs.hosts.port }} {{ vrfs.hosts.protocol }}',
            "compval": "vrfs.hosts",
            "shared": True,
            "result": {
                "vrfs": {
                   "{{ vrf }}": {
                        "name": "{{ vrf }}",
                        "hosts": {
                            "{{ name }}": {
                                "name": "{{ name }}",
                                "add": '{{ True if oper == "add" }}',
                                "remove": '{{ True if oper == "remove" }}',
                                "port": "{{ port }}",
                                "protocol": "{{ protocol }}"
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "vrf.source_interface",
            "getval": re.compile(
                r"""
                \s*logging\svrf
                \s+(?P<vrf>\S+)
                \s+source-interface
                \s(?P<val>.+)
                *$""",
                re.VERBOSE,
            ),
            "setval": 'logging vrf {{ vrfs.name }} source-interface {{ vrf.source_interface }}',
            "compval": "vrfs.source_interface",
            "shared": True,
            "result": {
                "vrfs": {
                   "{{ vrf }}": {
                        "name": "{{ vrf }}",
                        "source_interface": "{{ val }}"
                    }
                }
            },
        },
    ]
    # fmt: on
