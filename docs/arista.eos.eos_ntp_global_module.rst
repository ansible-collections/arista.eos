.. _arista.eos.eos_ntp_global_module:


*************************
arista.eos.eos_ntp_global
*************************

**Manages ntp resource module**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module configures and manages the attributes of  ntp on Arista EOS platforms.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="5">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary of ntp options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authenticate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Require authentication for NTP synchronization.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable</b>
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
                        <div>Enable authentication for NTP synchronization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>servers</b>
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
                        <div>Authentication required only for incoming NTP server responses.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authentication_keys</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Define a key to use for authentication.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>algorithm</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>md5</li>
                                    <li>sha1</li>
                        </ul>
                </td>
                <td>
                        <div>hash algorithm,</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>encryption</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>0</li>
                                    <li>7</li>
                        </ul>
                </td>
                <td>
                        <div>key type</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>key identifier.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Unobfuscated key string.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>local_interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure the interface from which the IP source address is taken.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>qos_dscp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set DSCP value in IP header</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>serve</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure the switch as an NTP server.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>access_lists</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure access control list.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>acls</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Access lists to be configured under the afi</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>acl_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the access list.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>direction</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>in</li>
                                    <li>out</li>
                        </ul>
                </td>
                <td>
                        <div>direction for the packets.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRF in which to apply the access control list.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ip/ipv6 config commands.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>all</b>
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
                        <div>Service NTP requests received on any interface.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>servers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure NTP server to synchronize to.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>burst</b>
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
                        <div>Send a burst of packets instead of the usual one.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>iburst</b>
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
                        <div>Send bursts of packets until the server is reached</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set a key to use for authentication.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>local_interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure the interface from which the IP source address is taken.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>maxpoll</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum poll interval.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>minpoll</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum poll interval.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefer</b>
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
                        <div>Mark this server as preferred.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>server</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Hostname or A.B.C.D or A:B:C:D:E:F:G:H.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure the interface from which the IP source address is taken.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>NTP version.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>vrf name.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trusted_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure the set of keys that are accepted for incoming messages</div>
                </td>
            </tr>

            <tr>
                <td colspan="5">
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
                        <div>The value of this option should be the output received from the EOS device by executing the command <b>show running-config | section ntp</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
                </td>
            </tr>
            <tr>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>deleted</li>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>overridden</li>
                                    <li>replaced</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in.</div>
                        <div>The states <em>replaced</em> and <em>overridden</em> have identical behaviour for this module.</div>
                        <div>Please refer to examples for more details.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Arista EOS 4.24.60M
   - This module works with connection ``network_cli``. See the https://docs.ansible.com/ansible/latest/network/user_guide/platform_eos.html.



Examples
--------

.. code-block:: yaml

    # Using merged

    # Before state:
    # -------------
    # localhost(config)#show running-config | section ntp
    # localhost(config)#

    - name: Merge provided configuration with device configuration
      arista.eos.eos_ntp_global:
        config:
          authenticate:
            enable: true
          authentication_keys:
            - id: 2
              algorithm: "sha1"
              encryption: 7
              key: "123456"
            - id: 23
              algorithm: "md5"
              encryption: 7
              key: "123456"
          local_interface: "Ethernet1"
          qos_dscp: 10
          trusted_key: 23
          servers:
            - server: "10.1.1.1"
              vrf: "vrf01"
              burst: true
              prefer: true
            - server: "25.1.1.1"
              vrf: "vrf01"
              maxpoll: 15
              key_id: 2
          serve:
            access_lists:
              - afi: "ip"
                acls:
                  - acl_name: "acl01"
                    direction: "in"
              - afi: "ipv6"
                acls:
                  - acl_name: "acl02"
                    direction: "in"

    # After State

    # localhost(config)#show running-config | section ntp
    # ntp authentication-key 2 sha1 7 123456
    # ntp authentication-key 23 md5 7 123456
    # ntp trusted-key 23
    # ntp authenticate
    # ntp local-interface Ethernet1
    # ntp qos dscp 10
    # ntp server vrf vrf01 10.1.1.1 prefer burst
    # ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2
    # ntp serve ip access-group acl01 in
    # ntp serve ipv6 access-group acl02 in
    # localhost(config)#
    #
    #
    # Module Execution:
    # "after": {
    #         "authenticate": {
    #             "enable": true
    #         },
    #         "authentication_keys": [
    #             {
    #                 "algorithm": "sha1",
    #                 "encryption": 7,
    #                 "id": 2,
    #                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #             },
    #             {
    #                 "algorithm": "md5",
    #                 "encryption": 7,
    #                 "id": 23,
    #                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #             }
    #         ],
    #         "local_interface": "Ethernet1",
    #         "qos_dscp": 10,
    #         "serve": {
    #             "access_lists": [
    #                 {
    #                     "acls": [
    #                         {
    #                             "acl_name": "acl01",
    #                             "direction": "in"
    #                         }
    #                     ],
    #                     "afi": "ip"
    #                 },
    #                 {
    #                     "acls": [
    #                         {
    #                             "acl_name": "acl02",
    #                             "direction": "in"
    #                         }
    #                     ],
    #                     "afi": "ipv6"
    #                 }
    #             ]
    #         },
    #         "servers": [
    #             {
    #                 "burst": true,
    #                 "prefer": true,
    #                 "server": "10.1.1.1",
    #                 "vrf": "vrf01"
    #             },
    #             {
    #                 "key_id": 2,
    #                 "maxpoll": 15,
    #                 "server": "25.1.1.1",
    #                 "vrf": "vrf01"
    #             }
    #         ],
    #         "trusted_key": "23"
    #     },
    #     "before": {},
    #     "changed": true,
    #     "commands": [
    #         "ntp serve ip access-group acl01 in",
    #         "ntp serve ipv6 access-group acl02 in",
    #         "ntp authentication-key 2 sha1 7 ********",
    #         "ntp authentication-key 23 md5 7 ********",
    #         "ntp server vrf vrf01 10.1.1.1 burst prefer",
    #         "ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
    #         "ntp authenticate",
    #         "ntp local-interface Ethernet1",
    #         "ntp qos dscp 10",
    #         "ntp trusted-key 23"
    #     ],

    # Using Replaced

    # Before State

    # localhost(config)#show running-config | section ntp
    # ntp authentication-key 2 sha1 7 123456
    # ntp authentication-key 23 md5 7 123456
    # ntp trusted-key 23
    # ntp authenticate
    # ntp local-interface Ethernet1
    # ntp qos dscp 10
    # ntp server vrf vrf01 10.1.1.1 prefer burst
    # ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2
    # ntp serve ip access-group acl01 in
    # ntp serve ipv6 access-group acl02 in
    # localhost(config)#

    - name: Replace
      arista.eos.eos_ntp_global:
        config:
          qos_dscp: 15
          authentication_keys:
            - id: 2
              algorithm: "md5"
              encryption: 7
              key: "123456"
          servers:
            - server: "11.21.1.1"
              vrf: "vrf01"
              burst: true
              prefer: true
              minpoll: 13
          serve:
            access_lists:
              - afi: "ip"
                acls:
                  - acl_name: "acl03"
                    direction: "in"
        state: replaced

    # After State:
    # localhost(config)#show running-config | section ntp
    # ntp authentication-key 2 md5 7 123456
    # ntp qos dscp 15
    # ntp server vrf vrf01 11.21.1.1 prefer burst minpoll 13
    # ntp serve ip access-group acl03 in
    # localhost(config)#
    #
    #
    # Module Execution:
    # "after": {
    #        "authentication_keys": [
    #            {
    #                "algorithm": "md5",
    #                "encryption": 7,
    #                "id": 2,
    #                "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #            }
    #        ],
    #        "qos_dscp": 15,
    #        "serve": {
    #            "access_lists": [
    #                {
    #                    "acls": [
    #                        {
    #                            "acl_name": "acl03",
    #                            "direction": "in"
    #                        }
    #                    ],
    #                    "afi": "ip"
    #                }
    #            ]
    #        },
    #        "servers": [
    #            {
    #                "burst": true,
    #                "minpoll": 13,
    #                "prefer": true,
    #                "server": "11.21.1.1",
    #                "vrf": "vrf01"
    #            }
    #        ]
    #    },
    #    "before": {
    #        "authenticate": {
    #            "enable": true
    #        },
    #        "authentication_keys": [
    #            {
    #                "algorithm": "sha1",
    #                "encryption": 7,
    #                "id": 2,
    #                "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #            },
    #            {
    #                "algorithm": "md5",
    #                "encryption": 7,
    #                "id": 23,
    #                "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #            }
    #        ],
    #        "local_interface": "Ethernet1",
    #        "qos_dscp": 10,
    #        "serve": {
    #            "access_lists": [
    #                {
    #                    "acls": [
    #                        {
    #                            "acl_name": "acl01",
    #                            "direction": "in"
    #                        }
    #                    ],
    #                    "afi": "ip"
    #                },
    #                {
    #                    "acls": [
    #                        {
    #                            "acl_name": "acl02",
    #                            "direction": "in"
    #                        }
    #                    ],
    #                    "afi": "ipv6"
    #                }
    #            ]
    #        },
    #        "servers": [
    #            {
    #                "burst": true,
    #                "prefer": true,
    #                "server": "10.1.1.1",
    #                "vrf": "vrf01"
    #            },
    #            {
    #                "key_id": 2,
    #                "maxpoll": 15,
    #                "server": "25.1.1.1",
    #                "vrf": "vrf01"
    #            }
    #        ],
    #        "trusted_key": "23"
    #    },
    #    "changed": true,
    #    "commands": [
    #        "no ntp serve ip access-group acl01 in",
    #        "no ntp serve ipv6 access-group acl02 in",
    #        "no ntp authentication-key 23 md5 7 ********",
    #        "no ntp server vrf vrf01 10.1.1.1 burst prefer",
    #        "no ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
    #        "no ntp authenticate",
    #        "no ntp local-interface Ethernet1",
    #        "no ntp trusted-key 23",
    #        "ntp serve ip access-group acl03 in",
    #        "ntp authentication-key 2 md5 7 ********",
    #        "ntp server vrf vrf01 11.21.1.1 burst minpoll 13 prefer",
    #        "ntp qos dscp 15"
    #    ],
    #
    # Using Overridden

    # Before State

    # localhost(config)#show running-config | section ntp
    # ntp authentication-key 2 sha1 7 123456
    # ntp authentication-key 23 md5 7 123456
    # ntp trusted-key 23
    # ntp authenticate
    # ntp local-interface Ethernet1
    # ntp qos dscp 10
    # ntp server vrf vrf01 10.1.1.1 prefer burst
    # ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2
    # ntp serve ip access-group acl01 in
    # ntp serve ipv6 access-group acl02 in
    # localhost(config)#

    - name: Replace
      arista.eos.eos_ntp_global:
        config:
          qos_dscp: 15
          authentication_keys:
            - id: 2
              algorithm: "md5"
              encryption: 7
              key: "123456"
          servers:
            - server: "11.21.1.1"
              vrf: "vrf01"
              burst: true
              prefer: true
              minpoll: 13
          serve:
            access_lists:
              - afi: "ip"
                acls:
                  - acl_name: "acl03"
                    direction: "in"
        state: overridden

    # After State:
    # localhost(config)#show running-config | section ntp
    # ntp authentication-key 2 md5 7 123456
    # ntp qos dscp 15
    # ntp server vrf vrf01 11.21.1.1 prefer burst minpoll 13
    # ntp serve ip access-group acl03 in
    # localhost(config)#
    #
    #
    # Module Execution:
    # "after": {
    #        "authentication_keys": [
    #            {
    #                "algorithm": "md5",
    #                "encryption": 7,
    #                "id": 2,
    #                "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #            }
    #        ],
    #        "qos_dscp": 15,
    #        "serve": {
    #            "access_lists": [
    #                {
    #                    "acls": [
    #                        {
    #                            "acl_name": "acl03",
    #                            "direction": "in"
    #                        }
    #                    ],
    #                    "afi": "ip"
    #                }
    #            ]
    #        },
    #        "servers": [
    #            {
    #                "burst": true,
    #                "minpoll": 13,
    #                "prefer": true,
    #                "server": "11.21.1.1",
    #                "vrf": "vrf01"
    #            }
    #        ]
    #    },
    #    "before": {
    #        "authenticate": {
    #            "enable": true
    #        },
    #        "authentication_keys": [
    #            {
    #                "algorithm": "sha1",
    #                "encryption": 7,
    #                "id": 2,
    #                "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #            },
    #            {
    #                "algorithm": "md5",
    #                "encryption": 7,
    #                "id": 23,
    #                "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #            }
    #        ],
    #        "local_interface": "Ethernet1",
    #        "qos_dscp": 10,
    #        "serve": {
    #            "access_lists": [
    #                {
    #                    "acls": [
    #                        {
    #                            "acl_name": "acl01",
    #                            "direction": "in"
    #                        }
    #                    ],
    #                    "afi": "ip"
    #                },
    #                {
    #                    "acls": [
    #                        {
    #                            "acl_name": "acl02",
    #                            "direction": "in"
    #                        }
    #                    ],
    #                    "afi": "ipv6"
    #                }
    #            ]
    #        },
    #        "servers": [
    #            {
    #                "burst": true,
    #                "prefer": true,
    #                "server": "10.1.1.1",
    #                "vrf": "vrf01"
    #            },
    #            {
    #                "key_id": 2,
    #                "maxpoll": 15,
    #                "server": "25.1.1.1",
    #                "vrf": "vrf01"
    #            }
    #        ],
    #        "trusted_key": "23"
    #    },
    #    "changed": true,
    #    "commands": [
    #        "no ntp serve ip access-group acl01 in",
    #        "no ntp serve ipv6 access-group acl02 in",
    #        "no ntp authentication-key 23 md5 7 ********",
    #        "no ntp server vrf vrf01 10.1.1.1 burst prefer",
    #        "no ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
    #        "no ntp authenticate",
    #        "no ntp local-interface Ethernet1",
    #        "no ntp trusted-key 23",
    #        "ntp serve ip access-group acl03 in",
    #        "ntp authentication-key 2 md5 7 ********",
    #        "ntp server vrf vrf01 11.21.1.1 burst minpoll 13 prefer",
    #        "ntp qos dscp 15"
    #    ],
    #

    # using deleted:
    # Before State

    # localhost(config)#show running-config | section ntp
    # ntp authentication-key 2 sha1 7 123456
    # ntp authentication-key 23 md5 7 123456
    # ntp trusted-key 23
    # ntp authenticate
    # ntp local-interface Ethernet1
    # ntp qos dscp 10
    # ntp server vrf vrf01 10.1.1.1 prefer burst
    # ntp server vrf vrf01 11.21.1.1 prefer burst minpoll 13
    # ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2
    # ntp serve ip access-group acl01 in
    # ntp serve ipv6 access-group acl02 in
    # localhost(config)#

    - name: Delete  ntp-global
      arista.eos.eos_ntp_global:
        state: deleted

    # After State:
    #  localhost(config)#show running-config | section ntp
    # localhost(config)#
    #
    #
    # # Module Execution
    # "after": {},
    #     "before": {
    #         "authenticate": {
    #             "enable": true
    #         },
    #         "authentication_keys": [
    #             {
    #                 "algorithm": "sha1",
    #                 "encryption": 7,
    #                 "id": 2,
    #                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #             },
    #             {
    #                 "algorithm": "md5",
    #                 "encryption": 7,
    #                 "id": 23,
    #                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #             }
    #         ],
    #         "local_interface": "Ethernet1",
    #         "qos_dscp": 10,
    #         "serve": {
    #             "access_lists": [
    #                 {
    #                     "acls": [
    #                         {
    #                             "acl_name": "acl01",
    #                             "direction": "in"
    #                         }
    #                     ],
    #                     "afi": "ip"
    #                 },
    #                 {
    #                     "acls": [
    #                         {
    #                             "acl_name": "acl02",
    #                             "direction": "in"
    #                         }
    #                     ],
    #                     "afi": "ipv6"
    #                 }
    #             ]
    #         },
    #         "servers": [
    #             {
    #                 "burst": true,
    #                 "prefer": true,
    #                 "server": "10.1.1.1",
    #                 "vrf": "vrf01"
    #             },
    #             {
    #                 "burst": true,
    #                 "minpoll": 13,
    #                 "prefer": true,
    #                 "server": "11.21.1.1",
    #                 "vrf": "vrf01"
    #             },
    #             {
    #                 "key": 2,
    #                 "maxpoll": 15,
    #                 "server": "25.1.1.1",
    #                 "vrf": "vrf01"
    #             }
    #         ],
    #         "trusted_key": "23"
    #     },
    #     "changed": true,
    #     "commands": [
    #         "no ntp serve ip access-group acl01 in",
    #         "no ntp serve ipv6 access-group acl02 in",
    #         "no ntp authentication-key 2 sha1 7 ********",
    #         "no ntp authentication-key 23 md5 7 ********",
    #         "no ntp server vrf vrf01 10.1.1.1 burst prefer",
    #         "no ntp server vrf vrf01 11.21.1.1 burst minpoll 13 prefer",
    #         "no ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
    #         "no ntp authenticate",
    #         "no ntp local-interface Ethernet1",
    #         "no ntp qos dscp 10",
    #         "no ntp trusted-key 23"
    #     ],
    #

    # Using parsed:
    # parsed.cfg
    # ntp authentication-key 2 sha1 7 123456
    # ntp authentication-key 23 md5 7 123456
    # ntp trusted-key 23
    # ntp authenticate
    # ntp local-interface Ethernet1
    # ntp qos dscp 10
    # ntp server vrf vrf01 10.1.1.1 prefer burst
    # ntp server vrf vrf01 11.21.1.1 prefer burst minpoll 13
    # ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2
    # ntp serve ip access-group acl01 in
    # ntp serve ipv6 access-group acl02 in

    - name: parse configs
      arista.eos.eos_ntp_global:
        running_config: "{{ lookup('file', './parsed_ntp_global.cfg') }}"
        state: parsed
      tags:
        - parsed

    # Module Execution
    # "parsed": {
    #         "authenticate": {
    #             "enable": true
    #         },
    #         "authentication_keys": [
    #             {
    #                 "algorithm": "sha1",
    #                 "encryption": 7,
    #                 "id": 2,
    #                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #             },
    #             {
    #                 "algorithm": "md5",
    #                 "encryption": 7,
    #                 "id": 23,
    #                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #             }
    #         ],
    #         "local_interface": "Ethernet1",
    #         "qos_dscp": 10,
    #         "serve": {
    #             "access_lists": [
    #                 {
    #                     "acls": [
    #                         {
    #                             "acl_name": "acl01",
    #                             "direction": "in"
    #                         }
    #                     ],
    #                     "afi": "ip"
    #                 },
    #                 {
    #                     "acls": [
    #                         {
    #                             "acl_name": "acl02",
    #                             "direction": "in"
    #                         }
    #                     ],
    #                     "afi": "ipv6"
    #                 }
    #             ]
    #         },
    #         "servers": [
    #             {
    #                 "burst": true,
    #                 "prefer": true,
    #                 "server": "10.1.1.1",
    #                 "vrf": "vrf01"
    #             },
    #             {
    #                 "burst": true,
    #                 "minpoll": 13,
    #                 "prefer": true,
    #                 "server": "11.21.1.1",
    #                 "vrf": "vrf01"
    #             },
    #             {
    #                 "key": 2,
    #                 "maxpoll": 15,
    #                 "server": "25.1.1.1",
    #                 "vrf": "vrf01"
    #             }
    #         ],
    #         "trusted_key": "23"
    #     }
    # }

    # using Gathered
    # Device config:
    # localhost(config)#show running-config | section ntp
    # ntp authentication-key 2 sha1 7 123456
    # ntp authentication-key 23 md5 7 123456
    # ntp trusted-key 23
    # ntp authenticate
    # ntp local-interface Ethernet1
    # ntp qos dscp 10
    # ntp server vrf vrf01 10.1.1.1 prefer burst
    # ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2
    # ntp serve ip access-group acl01 in
    # ntp serve ipv6 access-group acl02 in
    # localhost(config)#

    - name: gather configs
      arista.eos.eos_ntp_global:
        state: gathered
      tags:
        - gathered

    # Module Execution

    #   "gathered": {
    #         "authenticate": {
    #             "enable": true
    #         },
    #         "authentication_keys": [
    #             {
    #                 "algorithm": "sha1",
    #                 "encryption": 7,
    #                 "id": 2,
    #                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #             },
    #             {
    #                 "algorithm": "md5",
    #                 "encryption": 7,
    #                 "id": 23,
    #                 "key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    #             }
    #         ],
    #         "local_interface": "Ethernet1",
    #         "qos_dscp": 10,
    #         "serve": {
    #             "access_lists": [
    #                 {
    #                     "acls": [
    #                         {
    #                             "acl_name": "acl01",
    #                             "direction": "in"
    #                         }
    #                     ],
    #                     "afi": "ip"
    #                 },
    #                 {
    #                     "acls": [
    #                         {
    #                             "acl_name": "acl02",
    #                             "direction": "in"
    #                         }
    #                     ],
    #                     "afi": "ipv6"
    #                 }
    #             ]
    #         },
    #         "servers": [
    #             {
    #                 "burst": true,
    #                 "prefer": true,
    #                 "server": "10.1.1.1",
    #                 "vrf": "vrf01"
    #             },
    #             {
    #                 "key_id": 2,
    #                 "maxpoll": 15,
    #                 "server": "25.1.1.1",
    #                 "vrf": "vrf01"
    #             }
    #         ],
    #         "trusted_key": "23"
    #     },
    #     "invocation": {
    #         "module_args": {
    #             "config": null,
    #             "running_config": null,
    #             "state": "gathered"
    #         }
    #     }
    # }

    # using rendered:

    - name: Render provided configuration
      arista.eos.eos_ntp_global:
        config:
          authenticate:
            enable: true
          authentication_keys:
            - id: 2
              algorithm: "sha1"
              encryption: 7
              key: "123456"
            - id: 23
              algorithm: "md5"
              encryption: 7
              key: "123456"
          local_interface: "Ethernet1"
          qos_dscp: 10
          trusted_key: 23
          servers:
            - server: "10.1.1.1"
              vrf: "vrf01"
              burst: true
              prefer: true
            - server: "25.1.1.1"
              vrf: "vrf01"
              maxpoll: 15
              key_id: 2
          serve:
            access_lists:
              - afi: "ip"
                acls:
                  - acl_name: "acl01"
                    direction: "in"
              - afi: "ipv6"
                acls:
                  - acl_name: "acl02"
                    direction: "in"
        state: rendered

    # Module Execution:
    # "rendered": [
    #         "ntp serve ip access-group acl01 in",
    #         "ntp serve ipv6 access-group acl02 in",
    #         "ntp authentication-key 2 sha1 7 ********",
    #         "ntp authentication-key 23 md5 7 ********",
    #         "ntp server vrf vrf01 10.1.1.1 burst prefer",
    #         "ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
    #         "ntp authenticate",
    #         "ntp local-interface Ethernet1",
    #         "ntp qos dscp 10",
    #         "ntp trusted-key 23"
    #     ]
    #



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;ntp master stratum 2&#x27;, &#x27;ntp peer 198.51.100.1 use-vrf test maxpoll 7&#x27;, &#x27;ntp authentication-key 10 md5 wawyhanx2 7&#x27;, &#x27;ntp access-group peer PeerAcl1&#x27;, &#x27;ntp access-group peer PeerAcl2&#x27;, &#x27;ntp access-group query-only QueryAcl1&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;ntp authentication-key 2 sha1 7 123456&#x27;, &#x27;ntp authentication-key 23 md5 7 123456&#x27;, &#x27;ntp trusted-key 23&#x27;, &#x27;ntp authenticate&#x27;, &#x27;ntp local-interface Ethernet1&#x27;, &#x27;ntp qos dscp 10&#x27;, &#x27;ntp server vrf vrf01 10.1.1.1 prefer burst&#x27;, &#x27;ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2&#x27;, &#x27;ntp serve ip access-group acl01 in&#x27;, &#x27;ntp serve ipv6 access-group acl02 in&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Gomathi Selvi Srinivasan (@GomathiselviS)
