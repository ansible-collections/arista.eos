#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for eos_ntp_global
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: eos_ntp_global
short_description: Manages ntp resource module
description: This module configures and manages the attributes of  ntp on Arista
  EOS platforms.
version_added: 3.1.0
author: Gomathi Selvi Srinivasan (@GomathiselviS)
notes:
- Tested against Arista EOS 4.24.60M
- This module works with connection C(network_cli). See the L(EOS Platform Options,eos_platform_options).
options:
    config:
      description: A dictionary of ntp options
      type: dict
      suboptions:
        authenticate:
          description:
          - Require authentication for NTP synchronization.
          type: dict
          suboptions:
            enable:
              description: Enable authentication for NTP synchronization.
              type: bool
            servers:
              description: Authentication required only for incoming NTP server responses.
              type: bool
        authentication_keys:
          description:
          - Define a key to use for authentication.
          type: list
          elements: dict
          suboptions:
            id:
              description: key identifier.
              type: int
            algorithm:
              description: hash algorithm,
              type: str
              choices: ["md5", "sha1"]
            encryption:
              description: key type
              type: int
              choices: [0, 1]
            key:
              description: Unobfuscated key string.
              type: str
              no_log: True
        local_interface:
          description: Configure the interface from which the IP source address is taken.
          type: str
        qos_dscp:
          description: Set DSCP value in IP header
          type: int
        serve:
          description: Configure the switch as an NTP server.
          type: dict
          suboptions:
            all:
              description: Service NTP requests received on any interface.
              type: bool
            access_lists:
              description: Configure access control list.
              type: list
              elements: dict
              suboptions:
                afi:
                  description: ip/ipv6 config commands.
                  type: str
                acls:
                  description: Access lists to be configured under the afi
                  type: list
                  elements: dict
                  suboptions:
                    acl_name:
                      description: Name of the access list.
                      type: str
                    direction:
                      description: direction for the packets.
                      type: str
                      choices: ["in", "out"]
                    vrf:
                      description: VRF in which to apply the access control list.
                      type: str
        servers:
          description: Configure NTP server to synchronize to.
          type: list
          elements: dict
          suboptions:
            vrf:
              description: vrf name.
              type: str
            server:
              description: Hostname or A.B.C.D or A:B:C:D:E:F:G:H.
              type: str
              required: True
            burst:
              description: Send a burst of packets instead of the usual one.
              type: bool
            iburst:
              description: Send bursts of packets until the server is reached
              type: bool
            key:
              description: Set a key to use for authentication.
              type: int
            local_interface:
              description: Configure the interface from which the IP source address is taken.
              type: str
            maxpoll:
              description: Maximum poll interval.
              type: int
            minpoll:
              description: Minimum poll interval.
              type: int
            prefer:
              description: Mark this server as preferred.
              type: bool
            version:
              description: NTP version.
              type: int
        trusted_key:
          description: Configure the set of keys that are accepted for incoming messages
          type: str
    running_config:
      description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the EOS device by
        executing the command B(show running-config | section ntp).
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
from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.ntp_global.ntp_global import (
    Ntp_globalArgs,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.config.ntp_global.ntp_global import (
    Ntp_global,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Ntp_globalArgs.argument_spec,
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

    result = Ntp_global(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()