.. _arista.eos.eos_interfaces_module:


*************************
arista.eos.eos_interfaces
*************************

**Interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages the interface attributes of Arista EOS interfaces.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="2">
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
                        <div>The provided configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface description</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>duplex</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface link status. Applicable for Ethernet interfaces only.</div>
                        <div>Values other than <code>auto</code> must also set <em>speed</em>.</div>
                        <div>Ignored when <em>speed</em> is set above <code>1000</code>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Administrative state of the interface.</div>
                        <div>Set the value to <code>true</code> to administratively enable the interface or <code>false</code> to disable it.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>layer2</li>
                                    <li>layer3</li>
                        </ul>
                </td>
                <td>
                        <div>Manage Layer2 or Layer3 state of the interface. Applicable for Ethernet and port channel interfaces only.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mtu</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MTU for a specific interface. Must be an even number between 576 and 9216. Applicable for Ethernet interfaces only.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Full name of the interface, e.g. GigabitEthernet1.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>speed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface link speed. Applicable for Ethernet interfaces only.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
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
                <td colspan="2">
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
                                    <li>rendered</li>
                                    <li>gathered</li>
                        </ul>
                </td>
                <td>
                        <div>The state of the configuration after module completion.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Arista EOS 4.24.6F
   - This module works with connection ``network_cli``. See https://docs.ansible.com/ansible/latest/network/user_guide/platform_eos.html



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
    # !
    # interface Management1
    #    ip address dhcp
    #    dhcp client accept default-route

    - name: Merge provided configuration with device configuration
      arista.eos.eos_interfaces:
        config:
          - name: Ethernet1
            enabled: true
            mode: layer3
          - name: Ethernet2
            description: Configured by Ansible
            enabled: false
        state: merged

    # Task Output
    # -----------
    #
    # before:
    # - enabled: true
    #   name: Ethernet1
    # - enabled: true
    #   name: Ethernet2
    # - enabled: true
    #   name: Management1
    # commands:
    # - interface Ethernet1
    # - no switchport
    # - interface Ethernet2
    # - shutdown
    # - description Configured by Ansible
    # after:
    # - enabled: true
    #   mode: layer3
    #   name: Ethernet1
    # - description: Configured by Ansible
    #   enabled: false
    #   name: Ethernet2
    # - enabled: true
    #   name: Management1

    # After state:
    # ------------
    #
    # test#show running-config | section interface
    # interface Ethernet1
    #    no switchport
    # !
    # interface Ethernet2
    #    description Configured by Ansible
    #    shutdown
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
    #    no switchport
    # !
    # interface Ethernet2
    #    description Configured by Ansible
    #    shutdown
    # !
    # interface Management1
    #    ip address dhcp
    #    dhcp client accept default-route

    - name: Replaces device configuration of listed interfaces with provided configuration
      arista.eos.eos_interfaces:
        config:
          - name: Ethernet1
            enabled: true
          - name: Ethernet2
            description: Configured by Ansible
            enabled: false
        state: replaced

    # Task Output
    # -----------
    #
    # before:
    # - enabled: true
    #   mode: layer3
    #   name: Ethernet1
    # - description: Configured by Ansible
    #   enabled: false
    #   name: Ethernet2
    # - enabled: true
    #   name: Management1
    # commands:
    # - interface Ethernet1
    # - switchport
    # after:
    # - enabled: true
    #   name: Ethernet1
    # - description: Configured by Ansible
    #   enabled: false
    #   name: Ethernet2
    # - enabled: true
    #   name: Management1

    # After state:
    # ------------
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

    # Using overridden

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

    - name: Overrides all device configuration with provided configuration
      arista.eos.eos_interfaces:
        config:
          - name: Ethernet1
            enabled: true
          - name: Ethernet2
            description: Configured by Ansible
            enabled: false
        state: overridden

    # Task Output
    # -----------
    #
    # before:
    # - enabled: true
    #   name: Ethernet1
    # - description: Configured by Ansible
    #   enabled: false
    #   name: Ethernet2
    # - enabled: true
    #   name: Management1
    # commands:
    # - interface Management1
    # - no shutdown
    # after:
    # - enabled: true
    #   name: Ethernet1
    # - description: Configured by Ansible
    #   enabled: false
    #   name: Ethernet2
    # - enabled: true
    #   name: Management1

    # After state:
    # ------------
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

    # Using deleted

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

    - name: Delete or return interface parameters to default settings
      arista.eos.eos_interfaces:
        config:
          - name: Ethernet1
        state: deleted

    # Task Output
    # -----------
    #
    # before:
    # - enabled: true
    #   name: Ethernet1
    # - description: Configured by Ansible
    #   enabled: false
    #   name: Ethernet2
    # - enabled: true
    #   name: Management1
    # commands:
    # - interface Ethernet1
    # - no shutdown
    # after:
    # - enabled: true
    #   name: Ethernet1
    # - description: Configured by Ansible
    #   enabled: false
    #   name: Ethernet2
    # - enabled: true
    #   name: Management1

    # After state:
    # ------------
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

    # Using rendered

    - name: Render the provided configuration into platform specific configuration lines
      arista.eos.eos_interfaces:
        config:
          - name: Ethernet1
            enabled: true
            mode: layer3
          - name: Ethernet2
            description: Configured by Ansible
            enabled: false
        state: rendered

    # Module Execution Result:
    # ------------------------
    #
    # rendered:
    # - interface Ethernet1
    # - no shutdown
    # - no switchport
    # - interface Ethernet2
    # - shutdown
    # - description Configured by Ansible

    # Using Parsed

    # File: parsed.cfg
    # ----------------
    #
    # interface Ethernet1
    #    description "Interface 1"
    # !
    # interface Ethernet2
    #    description "Configured by Ansible"
    #    shutdown
    # !

    - name: Parse the commands for provided configuration
      arista.eos.interfaces:
        running_config: "{{ lookup('file', 'parsed.cfg') }}"
        state: parsed

    # Module Execution Result:
    # ------------------------
    #
    # parsed:
    #  - name: Ethernet1
    #    enabled: True
    #    mode: layer2
    #  - name: Ethernet2
    #    description: 'Configured by Ansible'
    #    enabled: False
    #    mode: layer2

    # Using Gathered

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

    - name: Gather interfaces facts from the device
      arista.eos.interfaces:
        state: gathered

    # Module Execution Result:
    # ------------------------
    #
    # gathered:
    # - enabled: true
    #   name: Ethernet1
    # - description: Configured by Ansible
    #   enabled: false
    #   name: Ethernet2
    # - enabled: true
    #   name: Management1



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface Ethernet1&#x27;, &#x27;no shutdown&#x27;, &#x27;no switchport&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface Ethernet1&#x27;, &#x27;no shutdown&#x27;, &#x27;no switchport&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Nathaniel Case (@Qalthos)
