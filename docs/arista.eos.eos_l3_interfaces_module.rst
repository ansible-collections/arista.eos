.. _arista.eos.eos_l3_interfaces_module:


****************************
arista.eos.eos_l3_interfaces
****************************

**L3 interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides declarative management of Layer 3 interfaces on Arista EOS devices.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary of Layer 3 interface options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv4</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of IPv4 addresses to be set for the Layer 3 interface mentioned in <em>name</em> option.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4 address to be set in the format &lt;ipv4 address&gt;/&lt;mask&gt; eg. 192.0.2.1/24, or <code>dhcp</code> to query DHCP for an IP address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>secondary</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Whether or not this address is a secondary address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>virtual</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Whether or not this address is a virtual address.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of IPv6 addresses to be set for the Layer 3 interface mentioned in <em>name</em> option.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 address to be set in the address format is &lt;ipv6 address&gt;/&lt;mask&gt; eg. 2001:db8:2201:1::1/64 or <code>auto-config</code> to use SLAAC to chose an address.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Full name of the interface, i.e. Ethernet1.</div>
                </td>
            </tr>

            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>running_config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This option is used only with state <em>parsed</em>.</div>
                        <div>The value of this option should be the output received from the EOS device by executing the command <b>show running-config | section ^interface</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
                </td>
            </tr>
            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
                                    <li>parsed</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                        </ul>
                </td>
                <td>
                        <div>The state of the configuration after module completion</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Arista EOS 4.24.6F
   - This module works with connection ``network_cli``. See https://docs.ansible.com/ansible/latest/network/user_guide/platform_eos.html 'eos_l2_interfaces/eos_interfaces' should be used for preparing the interfaces, before applying L3 configurations using this module (eos_l3_interfaces).



Examples
--------

.. code-block:: yaml

    # Using merged

    # Before state:
    # -------------
    #
    # test#show running-config | section interface
    # interface Ethernet1
    # !
    # interface Ethernet2
    #    description Configured by Ansible
    #    shutdown
    # !
    # interface Management1
    #    ip address dhcp
    #    dhcp client accept default-route

    - name: Merge provided configuration with device configuration.
      arista.eos.eos_l3_interfaces:
        config:
          - name: Ethernet1
            ipv4:
              - address: 198.51.100.14/24
          - name: Ethernet2
            ipv4:
              - address: 203.0.113.27/24
        state: merged

    # Task Output
    # -----------
    #
    # before:
    # - name: Ethernet1
    # - name: Ethernet2
    # - ipv4:
    #   - address: dhcp
    #   name: Management1
    # commands:
    # - interface Ethernet1
    # - ip address 198.51.100.14/24
    # - interface Ethernet2
    #   - ip address 203.0.113.27/24
    # after:
    # - ipv4:
    #   - address: 198.51.100.14/24
    #   name: Ethernet1
    # - ipv4:
    #   - address: 203.0.113.27/24
    #   name: Ethernet2
    # - ipv4:
    #   - address: dhcp
    #   name: Management1

    # After state:
    # ------------
    #
    # test#show running-config | section interface
    # interface Ethernet1
    #    ip address 198.51.100.14/24
    # !
    # interface Ethernet2
    #    description Configured by Ansible
    #    shutdown
    #    ip address 203.0.113.27/24
    # !
    # interface Management1
    #    ip address dhcp
    #    dhcp client accept default-route

    # Using overridden

    # Before state:
    # -------------
    #
    # test#show running-config | section interface
    # interface Ethernet1
    #    ip address 198.51.100.14/24
    # !
    # interface Ethernet2
    #    ip address 203.0.113.27/24
    # !
    # interface Management1
    #    ip address dhcp
    #    dhcp client accept default-route

    - name: Override device configuration of all L2 interfaces on device with provided
        configuration.
      arista.eos.eos_l3_interfaces:
        config:
          - name: Ethernet1
            ipv6:
              - address: 2001:db8:feed::1/96
          - name: Ethernet2
            ipv4:
              - address: 203.0.113.27/24
          - ipv4:
              - address: dhcp
            name: Management1
        state: overridden

    # Task Output
    # -----------
    #
    # before:
    # - ipv4:
    #   - address: 198.51.100.14/24
    #   name: Ethernet1
    # - ipv4:
    #   - address: 203.0.113.27/24
    #   name: Ethernet2
    # - ipv4:
    #   - address: dhcp
    #   name: Management1
    # commands:
    # - interface Ethernet1
    # - ipv6 address 2001:db8:feed::1/96
    # - no ip address
    # after:
    # - ipv6:
    #   - address: 2001:db8:feed::1/96
    #   name: Ethernet1
    # - ipv4:
    #   - address: 203.0.113.27/24
    #   name: Ethernet2
    # - ipv4:
    #   - address: dhcp
    #   name: Management1

    # After state:
    # ------------
    #
    # test#show running-config | section interface
    # interface Ethernet1
    #    ipv6 address 2001:db8:feed::1/96
    # !
    # interface Ethernet2
    #    ip address 203.0.113.27/24
    # !
    # interface Management1
    #    ip address dhcp
    #    dhcp client accept default-route

    # Using replaced

    # Before state:
    # -------------
    #
    # test#show running-config | section interface
    # interface Ethernet1
    #    ipv6 address 2001:db8:feed::1/96
    # !
    # interface Ethernet2
    #    ip address 203.0.113.27/24
    # !
    # interface Management1
    #    ip address dhcp
    #    dhcp client accept default-route

    - name: Replace device configuration of specified L2 interfaces with provided configuration.
      arista.eos.eos_l3_interfaces:
        config:
          - name: Ethernet2
            ipv4:
              - address: 203.0.113.27/24
        state: replaced

    # Task Output
    # -----------
    #
    # before:
    # - ipv6:
    #   - address: 2001:db8:feed::1/96
    #   name: Ethernet1
    # - ipv4:
    #   - address: 203.0.113.27/24
    #   name: Ethernet2
    # - ipv4:
    #   - address: dhcp
    #   name: Management1
    # commands:
    # - interface Ethernet2
    # - ip address 203.0.113.28/24
    # after:
    # - ipv6:
    #   - address: 2001:db8:feed::1/96
    #   name: Ethernet1
    # - ipv4:
    #   - address: 203.0.113.28/24
    #   name: Ethernet2
    # - ipv4:
    #   - address: dhcp
    #   name: Management1

    # After state:
    # ------------
    #
    # test#show running-config | section interface
    # interface Ethernet1
    #    ipv6 address 2001:db8:feed::1/96
    # !
    # interface Ethernet2
    #    ip address 203.0.113.28/24
    # !
    # interface Management1
    #    ip address dhcp
    #    dhcp client accept default-route

    # Using deleted

    # Before state:
    # -------------
    #
    # test#show running-config | section interface
    # interface Ethernet1
    #    ipv6 address 2001:db8:feed::1/96
    # !
    # interface Ethernet2
    #    ip address 203.0.113.28/24
    # !
    # interface Management1
    #    ip address dhcp
    #    dhcp client accept default-route

    - name: Delete L3 attributes of given interfaces.
      arista.eos.eos_l3_interfaces:
        config:
          - name: Ethernet1
          - name: Ethernet2
        state: deleted

    # Task Output
    # -----------
    #
    # before:
    # - ipv6:
    #   - address: 2001:db8:feed::1/96
    #   name: Ethernet1
    # - ipv4:
    #   - address: 203.0.113.28/24
    #   name: Ethernet2
    # - ipv4:
    #   - address: dhcp
    #   name: Management1
    # commands:
    # - interface Ethernet1
    # - no ipv6 address 2001:db8:feed::1/96
    # - interface Ethernet2
    # - no ip address
    # after:
    # - name: Ethernet1
    # - name: Ethernet2
    # - ipv4:
    #   - address: dhcp
    #   name: Management1

    # After state:
    # ------------
    #
    # test#show running-config | section interface
    # interface Ethernet1
    # !
    # interface Ethernet2
    # !
    # interface Management1
    #    ip address dhcp
    #    dhcp client accept default-route

    # Using Parsed

    # File: parsed.cfg
    # ----------------
    #
    # veos#show running-config | section interface
    # interface Ethernet1
    #    ip address 198.51.100.14/24
    # !
    # interface Ethernet2
    #    ip address 203.0.113.27/24
    # !

    - name: Use parsed to convert native configs to structured data
      arista.eos.interfaces:
        running_config: "{{ lookup('file', 'parsed.cfg') }}"
        state: parsed

    # Module Execution Result:
    # ------------------------
    #
    # parsed:
    #  - name: Ethernet1
    #    ipv4:
    #      - address: 198.51.100.14/24
    #  - name: Ethernet2
    #    ipv4:
    #      - address: 203.0.113.27/24

    # Using rendered:

    - name: Use Rendered to convert the structured data to native config
      arista.eos.eos_l3_interfaces:
        config:
          - name: Ethernet1
            ipv4:
              - address: 198.51.100.14/24
          - name: Ethernet2
            ipv4:
              - address: 203.0.113.27/24
        state: rendered

    # Module Execution Result:
    # ------------------------
    #
    # rendered:
    # - interface Ethernet1
    # - ip address 198.51.100.14/24
    # - interface Ethernet2
    # - ip address 203.0.113.27/24

    # using gathered:

    # Before state:
    # -------------
    #
    # test#show running-config | section interface
    # interface Ethernet1
    #    ip address 198.51.100.14/24
    # !
    # interface Ethernet2
    #    ip address 203.0.113.27/24
    # !

    - name: Gather l3 interfaces facts from the device
      arista.eos.l3_interfaces:
        state: gathered

    # Module Execution Result:
    # ------------------------
    #
    # gathered:
    #  - name: Ethernet1
    #    ipv4:
    #      - address: 198.51.100.14/24
    #  - name: Ethernet2
    #    ipv4:
    #      - address: 203.0.113.27/24



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>after</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The resulting configuration after module execution.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>merged</code>, <code>replaced</code>, <code>overridden</code>, <code>deleted</code> or <code>purged</code></td>
                <td>
                            <div>The configuration prior to the module execution.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>merged</code>, <code>replaced</code>, <code>overridden</code>, <code>deleted</code> or <code>purged</code></td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface Ethernet1&#x27;, &#x27;ip address 198.51.100.14/24&#x27;, &#x27;ipv6 address 2001:db8:feed::1/96&#x27;]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>gathered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>gathered</code></td>
                <td>
                            <div>Facts about the network resource gathered from the remote device as structured data.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>parsed</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>parsed</code></td>
                <td>
                            <div>The device native config provided in <em>running_config</em> option parsed into structured data as per module argspec.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>rendered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>rendered</code></td>
                <td>
                            <div>The provided configuration in the task rendered in device-native format (offline).</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface Ethernet1&#x27;, &#x27;ip address 198.51.100.14/24&#x27;, &#x27;ipv6 address 2001:db8:feed::1/96&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Nathaniel Case (@Qalthos)
