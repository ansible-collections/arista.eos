#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for eos_prefix_lists
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: eos_prefix_lists
short_description: Manages Prefix lists resource module
description: This module configures and manages the attributes of Prefix lists on Arista
  EOS platforms.
version_added: 2.1.1
author: Gomathi Selvi Srinivasan (@GomathiselviS)
notes:
- Tested against Arista EOS 4.20.10M
- This module works with connection C(network_cli). See the L(EOS Platform Options,eos_platform_options).
options:
   config:
      description: A list of dictionary of prefix-list options
      type: list
      elements: dict
      suboptions:
        afi:
          description:
          - The Address Family Indicator (AFI) for the  prefix list.
          type: str
          required: true
          choices:
          - ipv4
          - ipv6
        prefix_lists:
          description:
          - A list of prefix-lists.
          type: list
          elements: dict
          suboptions:
            name:
              description: Name of the prefix-list
              type: str
              required: true
            entries:
              description: List of prefix-lists
              type: list
              elements: dict
              suboptions:
                action:
                  description: action to be performed on the specified path
                  type: str
                  choices: ['deny', 'permit']
                address:
                  description: ipv4/v6 address in prefix-mask or address-masklen format
                  type: str
                match:
                  description: match masklen
                  type: dict
                  suboptions:
                    operator:
                      description: equalto/greater than/lesser than
                      type: str
                      choices: ['eq', 'le', 'ge']
                    masklen:
                      description: Mask Length.
                      type: int
                sequence:
                  description: sequence number
                  type: int
                resequence:
                  description: Resequence the list.
                  type: dict
                  suboptions:
                    default:
                      description: Resequence with default values (10).
                      type: bool
                    start_seq:
                      description: Starting sequence number.
                      type: int
                    step:
                      description: Step to increment the sequence number.
                      type: int
   running_config:
      description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the EOS device by
        executing the command B(show running-config | section access-list).
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
from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.prefix_lists.prefix_lists import (
    Prefix_listsArgs,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.config.prefix_lists.prefix_lists import (
    Prefix_lists,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Prefix_listsArgs.argument_spec,
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

    result = Prefix_lists(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
