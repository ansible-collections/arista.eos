#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for eos_logging_global
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: eos_logging_global
short_description: Manages logging resource module
description: This module configures and manages the attributes of  logging on Arista
  EOS platforms.
version_added: 3.0.0
author: Gomathi Selvi Srinivasan (@GomathiselviS)
notes:
- Tested against Arista EOS 4.24.6M
- This module works with connection C(network_cli). See the L(EOS Platform Options,eos_platform_options).
options:
   config:
      description: A dictionary of logging options
      type: dict
      suboptions:
        buffered:
          description:
          - Set buffered logging parameters.
          type: dict
          suboptions: &message_options
          severity:
            description: Severity level .
            type: str
          buffer_size:
            description: Logging buffer size
            type: int
        console:
          description:
          - Set console logging parameters.
          type: dict
          suboptions:
          severity:
            description: Severity level .
            type: str
        event:
          description: Global events
          type: str
          choices: ["link-status", "port-channel", "spanning-tree"]
        facility:
          description: Set logging facility.
          type: str
        format:
          description: Set logging format parameters
          type: dict
          suboptions:
            hostname:
              description: Specify hostname logging format.
              type: str
            timestamp:
              description: Set timestamp logging parameters.
              type: dict
              suboptions:
                high_resolution:
                  description: RFC3339 timestamps.
                  type: bool
                traditional:
                  description: Traditional syslog timestamp format as specified in RFC3164.
                  type: dict
                  suboptions:
                    state:
                      description: When enabled traditional timestamp format is set.
                      type: str
                      choices: ["enabled", "disabled"]
                    timezone:
                      description: Show timezone in traditional format timestamp
                      type: bool
                    year:
                      description: Show year in traditional format timestamp
                      type: bool
            sequence_numbers:
              description:  No. of log messages.
              type: bool
        host: &host
          description: Set syslog server IP address and parameters.
          type: dict
          suboptions:
            name:
              description: Hostname or IP address of the syslog server.
              type: str
            add:
              description: Configure ports on the given host.
              type: bool
            remove:
              description: Remove configured ports from the given host
              type: bool
            protocol:
              description: Set syslog server transport protocol
              type: str
              choices: ["type", "udp"]
            port:
              description: Port of the syslog server.
              type: int
        level:
          description: Configure logging severity
          type: dict
          suboptions:
            facility:
              description: Facility level
              type: str
            severity:
              description: Severity level
              type: str
        monitor:
          description: Set terminal monitor severity
          type: str
        turn_on:
          description: Turn on logging.
          type: bool
        persistent:
          description: Save logging messages to the flash disk.
          type: dict
          suboptions:
            set:
              description: Save logging messages to the flash dis.
              type: bool
            size:
              description: The maximum size (in bytes) of logging file stored on flash disk.
              type: int
        policy:
          description: Configure logging policies.
          type: dict
          suboptions:
            invert_result:
              description: Invert the match of match-list.
              type: bool
            match_list:
              description: Configure logging message filtering.
              type: str
        qos:
          description: Set DSCP value in IP header.
          type: int
        relogging_interval:
          description: Configure relogging-interval for critical log messages
          type: int
        repeat_messages:
          description: Repeat messages instead of summarizing number of repeats
          type: bool
        source_interface: &srcint
          description: Use IP Address of interface as source IP of log messages.
          type: str
        synchronous:
          description: Set synchronizing unsolicited with solicited messages
          type: dict
          suboptions:
            set:
              description: Set synchronizing unsolicited with solicited messages.
              type: bool
            level:
              description: Configure logging severity
              type: str
        trap:
          description: Severity of messages sent to the syslog server.
          type: dict
          suboptions:
            set:
              description: Severity of messages sent to the syslog server.
              type: bool
            severity:
              description: severity level
              type: str
        vrf:
          description: Specify vrf
          type: dict
          suboptions:
            name:
              description: vrf name.
              type: str
            host: *host
            source_interface: *srcint
   running_config:
      description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the EOS device by
        executing the command B(show running-config | section access-list).
      - The states I(replaced) and I(overridden) have identical
        behaviour for this module.
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
      type: str
   state:
      description:
      - The state the configuration should be left in.
      type: str
      choices:
      - deleted
      - merged
      - overridden
      - replaced
      - gathered
      - rendered
      - parsed
      default: merged
EXAMPLES:
- merged_example_01.txt
- replaced_example_01.txt
- overridden_example_01.txt
- deleted_example_01.txt
- gathered_example_01.txt
- parsed_example_01.txt
- rendered_example_01.txt
"""
EXAMPLES = """

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.logging_global.logging_global import (
    Logging_globalArgs,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.config.logging_global.logging_global import (
    Logging_global,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Logging_globalArgs.argument_spec,
        mutually_exclusive=[["config", "running_config"]],
        required_if=[
            ["state", "merged", ["config"]],
            ["state", "replaced", ["config"]],
            ["state", "overridden", ["config"]],
            ["state", "rendered", ["config"]],
            ["state", "parsed", ["running_config"]],
        ],
        supports_check_mode=True,
    )

    result = Logging_global(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
