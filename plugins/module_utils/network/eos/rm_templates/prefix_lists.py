# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Prefix_lists parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network_template import (
    NetworkTemplate,
)


class Prefix_listsTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(Prefix_listsTemplate, self).__init__(
            lines=lines, tmplt=self, module=module
        )

    def _tmplt_prefix_list_ip(config_data):
        import q

        q(config_data)
        command = ""

    # fmt: off
    PARSERS = [
        {
            "name": "prefixlist.name",
            "getval": re.compile(
                r"""
                ^(?P<afi>ip|ipv6)\sprefix-list\s(?P<name>\S+)
                *$""",
                re.VERBOSE,
            ),
            "setval": "{{ afi }} prefix-list {{ name }}",
            "compval": "prefix_lists",
            "result": {
                '{{ afi  }}': {
                    "afi": '{{ "ipv4" if afi == "ip" else afi }}',
                    "prefix_lists": {
                        "{{ name }}": {
                            "name": "{{ name }}"
                        }
                    }
                }
            },
            "shared": True,
        },
        {
            "name": "prefixlist.ip",
            "getval": re.compile(
                r"""
                \s*seq
                \s(?P<num>\d+)
                \s+(?P<action>permit|deny)
                \s+(?P<ip>\S+)
                \s*(?P<oper>eq|ge|le)*
                \s*(?P<len>\d+)*
                $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_prefix_list_ip,
            "result": {
                "{{ afi }}": {
                    "prefix_lists": {
                        "{{ name }}": {
                             "entries": {
                                 '{{ num|d("seq") }}': {
                                    "sequence": "{{ num }}",
                                    "action": "{{ action }}",
                                    "address": "{{ ip }}",
                                    "match": {
                                        "operator": "{{ oper }}",
                                        "masklen": "{{ len }}"
                                    }
                                }
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "prefixlist.resequence",
            "getval": re.compile(
                r"""
                \s*resequence
                \s*(?P<start>\d+)*
                \*(?P<step>\d+)*
                $""",
                re.VERBOSE,
            ),
            "setval": "resequnce {{ start }} {{ step }}",
            "result": {
                 '{{ num|d("seq") }}': {
                     "entries": {
                        "resequnce": {
                            "default": "{{ True if start_seq is undefined and step is undefined }}",
                            "start_seq": "{{ start }}",
                            "step": "{{ step }}"
                        }
                    }
                }
            },
        },
    ]
    # fmt: on
