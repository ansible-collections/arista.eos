.. _arista.eos.eos_prefix_lists_module:


***************************
arista.eos.eos_prefix_lists
***************************

**Manages Prefix lists resource module**


Version added: 2.2.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module configures and manages the attributes of Prefix lists on Arista EOS platforms.




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
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of dictionary of prefix-list options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>The Address Family Indicator (AFI) for the  prefix list.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix_lists</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of prefix-lists.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>entries</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of prefix-lists</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>deny</li>
                                    <li>permit</li>
                        </ul>
                </td>
                <td>
                        <div>action to be performed on the specified path</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>ipv4/v6 address in prefix-mask or address-masklen format</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>match masklen</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>masklen</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Mask Length.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>eq</li>
                                    <li>le</li>
                                    <li>ge</li>
                        </ul>
                </td>
                <td>
                        <div>equalto/greater than/lesser than</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>resequence</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Resequence the list.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default</b>
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
                        <div>Resequence with default values (10).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>start_seq</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Starting sequence number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>step</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Step to increment the sequence number.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sequence</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>sequence number</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Name of the prefix-list</div>
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
                        <div>The value of this option should be the output received from the EOS device by executing the command <b>show running-config | section access-list</b>.</div>
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
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Arista EOS 4.24.6F
   - This module works with connection ``network_cli``. See the `EOS Platform Options <eos_platform_options>`_.



Examples
--------

.. code-block:: yaml

    # Using merged


    # Before state
    # veos#show running-config | section prefix-lists
    # veos#

    - name: Merge provided configuration with device configuration
      arista.eos.eos_prefix_lists:
        config:
          - afi: "ipv4"
            prefix_lists:
              - name: "v401"
                entries:
                  - sequence: 25
                    action: "deny"
                    address: "45.55.4.0/24"
                  - sequence: 100
                    action: "permit"
                    address: "11.11.2.0/24"
                    match:
                      masklen: 32
                      operator: "ge"
              - name: "v402"
                entries:
                  - action: "deny"
                    address: "10.1.1.0/24"
                    sequence: 10
                    match:
                      masklen: 32
                      operator: "ge"
          - afi: "ipv6"
            prefix_lists:
              - name: "v601"
                entries:
                  - sequence: 125
                    action: "deny"
                    address: "5000:1::/64"

    # Task Output
    # -------------
    # before: {}
    # commands:
    # - ipv6 prefix-list v601
    # - seq 125 deny 5000:1::/64
    # - ip prefix-list v401
    # - seq 25 deny 45.55.4.0/24
    # - seq 100 permit 11.11.2.0/24 ge 32
    # - ip prefix-list v402
    # - seq 10 deny 10.1.1.0/24 ge 32
    # after:
    # - afi: ipv4
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 45.55.4.0/24
    #       sequence: 25
    #     - action: permit
    #       address: 11.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 100
    #     name: v401
    #   - entries:
    #     - action: deny
    #       address: 10.1.1.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 10
    #     name: v402
    # - afi: ipv6
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 5000:1::/64
    #       sequence: 125
    #     name: v601


    # After state:
    # ------------
    # veos#
    # veos#show running-config | section prefix-list
    # ip prefix-list v401
    #    seq 25 deny 45.55.4.0/24
    #    seq 100 permit 11.11.2.0/24 ge 32
    # !
    # ip prefix-list v402
    #    seq 10 deny 10.1.1.0/24 ge 32
    # !
    # ipv6 prefix-list v601
    #    seq 125 deny 5000:1::/64
    # veos#


    # Using merged:
    # Failure scenario : 'merged' should not be used when an existing prefix-list (sequence number)
    # is to be modified.


    # veos#show running-config | section prefix-list
    # ip prefix-list v401
    #    seq 25 deny 45.55.4.0/24
    #    seq 100 permit 11.11.2.0/24 ge 32
    # !
    # ip prefix-list v402
    #    seq 10 deny 10.1.1.0/24 ge 32
    # !
    # ipv6 prefix-list v601
    #    seq 125 deny 5000:1::/64
    # veos#

    - name: Merge provided configuration with device configuration
      arista.eos.eos_prefix_lists:
        config:
          - afi: "ipv4"
            prefix_lists:
              - name: "v401"
                entries:
                  - sequence: 25
                    action: "deny"
                    address: "45.55.4.0/24"
                    match:
                      masklen: 32
                      operator: "ge"
                  - sequence: 100
                    action: "permit"
                    address: "11.11.2.0/24"
                    match:
                      masklen: 32
                      operator: "ge"
              - name: "v402"
                entries:
                  - action: "deny"
                    address: "10.1.1.0/24"
                    sequence: 10
                    match:
                      masklen: 32
                      operator: "ge"
          - afi: "ipv6"
            prefix_lists:
              - name: "v601"
                entries:
                  - sequence: 125
                    action: "deny"
                    address: "5000:1::/64"
        state: merged

    # Task Output
    # -------------
    # changed: false
    # invocation:
    #   module_args:
    #     config:
    #     - afi: ipv4
    #       prefix_lists:
    #       - entries:
    #         - action: deny
    #           address: 45.55.4.0/24
    #           match:
    #             masklen: 32
    #             operator: ge
    #           resequence:
    #           sequence: 25
    #         - action: permit
    #           address: 11.11.2.0/24
    #           match:
    #             masklen: 32
    #             operator: ge
    #           resequence:
    #           sequence: 100
    #         name: v401
    #       - entries:
    #         - action: deny
    #           address: 10.1.1.0/24
    #           match:
    #             masklen: 32
    #             operator: ge
    #           resequence:
    #           sequence: 10
    #         name: v402
    #     - afi: ipv6
    #       prefix_lists:
    #       - entries:
    #         - action: deny
    #           address: 5000:1::/64
    #           match:
    #           resequence:
    #           sequence: 125
    #         name: v601
    #     running_config:
    #     state: merged
    # msg: Sequence number 25 is already present. Use replaced/overridden operation to change
    #   the configuration


    # Using Replaced:

    # Before state:
    # veos#show running-config | section prefix-list
    # ip prefix-list v401
    #    seq 25 deny 45.55.4.0/24
    #    seq 100 permit 11.11.2.0/24 ge 32
    # !
    # ip prefix-list v402
    #    seq 10 deny 10.1.1.0/24 ge 32
    # !
    # ipv6 prefix-list v601
    #    seq 125 deny 5000:1::/64
    # veos#


    - name: Replace Provided configuration with given configuration
      arista.eos.eos_prefix_lists:
        config:
          - afi: "ipv4"
            prefix_lists:
              - name: "v401"
                entries:
                  - sequence: 25
                    action: "deny"
                    address: "45.55.4.0/24"
                    match:
                      masklen: 32
                      operator: "ge"
                  - sequence: 200
                    action: "permit"
                    address: "200.11.2.0/24"
                    match:
                      masklen: 32
                      operator: "ge"
        state: replaced


    # Task Output
    # -------------
    # before:
    # - afi: ipv4
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 45.55.4.0/24
    #       sequence: 25
    #     - action: permit
    #       address: 11.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 100
    #     name: v401
    #   - entries:
    #     - action: deny
    #       address: 10.1.1.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 10
    #     name: v402
    # - afi: ipv6
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 5000:1::/64
    #       sequence: 125
    #     name: v601
    # commands:
    # - ip prefix-list v401
    # - no seq 25
    # - seq 25 deny 45.55.4.0/24 ge 32
    # - seq 200 permit 200.11.2.0/24 ge 32
    # - no seq 100
    # - no ip prefix-list v402
    # after:
    # - afi: ipv4
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 45.55.4.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 25
    #     - action: permit
    #       address: 200.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 200
    #     name: v401
    # - afi: ipv6
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 5000:1::/64
    #       sequence: 125
    #     name: v601


    # After State:
    # veos#show running-config | section prefix-list
    # ip prefix-list v401
    #    seq 25 deny 45.55.4.0/24 ge 32
    #    seq 200 permit 200.11.2.0/24 ge 32
    # !
    # ipv6 prefix-list v601
    #    seq 125 deny 5000:1::/64
    # veos#
    #
    #


    # Using overridden:


    # Before State:
    # veos#show running-config | section prefix-list
    # ip prefix-list v401
    #    seq 25 deny 45.55.4.0/24 ge 32
    #    seq 100 permit 11.11.2.0/24 ge 32
    #    seq 200 permit 200.11.2.0/24 ge 32
    # !
    # ip prefix-list v402
    #    seq 10 deny 10.1.1.0/24 ge 32
    # !
    # ipv6 prefix-list v601
    #    seq 125 deny 5000:1::/64
    # veos#

    - name: Override
      arista.eos.eos_prefix_lists:
        config:
          - afi: "ipv4"
            prefix_lists:
              - name: "v401"
                entries:
                  - sequence: 25
                    action: "deny"
                    address: "45.55.4.0/24"
                  - sequence: 300
                    action: "permit"
                    address: "30.11.2.0/24"
                    match:
                      masklen: 32
                      operator: "ge"
              - name: "v403"
                entries:
                  - action: "deny"
                    address: "10.1.1.0/24"
                    sequence: 10
        state: overridden


    # Task Output
    # -------------
    # before:
    # - afi: ipv4
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 45.55.4.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 25
    #     - action: permit
    #       address: 11.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 100
    #     - action: permit
    #       address: 200.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 200
    #     name: v401
    #   - entries:
    #     - action: deny
    #       address: 10.1.1.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 10
    #     name: v402
    # - afi: ipv6
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 5000:1::/64
    #       sequence: 125
    #     name: v601
    # commands:
    # - no ipv6 prefix-list v601
    # - ip prefix-list v401
    # - seq 25 deny 45.55.4.0/24
    # - seq 300 permit 30.11.2.0/24 ge 32
    # - no seq 100
    # - no seq 200
    # - ip prefix-list v403
    # - seq 10 deny 10.1.1.0/24
    # - no ip prefix-list v402
    # after:
    # - afi: ipv4
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 45.55.4.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 25
    #     - action: permit
    #       address: 30.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 300
    #     name: v401
    #   - entries:
    #     - action: deny
    #       address: 10.1.1.0/24
    #       sequence: 10
    #     name: v403


    # After State
    # veos#
    # veos#show running-config | section prefix-list
    # ip prefix-list v401
    #    seq 25 deny 45.55.4.0/24 ge 32
    #    seq 300 permit 30.11.2.0/24 ge 32
    # !
    # ip prefix-list v403
    #    seq 10 deny 10.1.1.0/24
    # veos#

    # Using deleted:

    # Before State:
    # veos#show running-config | section prefix-list
    # ip prefix-list v401
    #    seq 25 deny 45.55.4.0/24 ge 32
    #    seq 100 permit 11.11.2.0/24 ge 32
    #    seq 300 permit 30.11.2.0/24 ge 32
    # !
    # ip prefix-list v402
    #    seq 10 deny 10.1.1.0/24 ge 32
    # !
    # ip prefix-list v403
    #    seq 10 deny 10.1.1.0/24
    # !
    # ipv6 prefix-list v601
    #    seq 125 deny 5000:1::/64
    # veos#

    - name: Delete device configuration
      arista.eos.eos_prefix_lists:
        config:
          - afi: "ipv6"
        state: deleted

    # Task Output
    # -------------
    # before:
    # - afi: ipv4
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 45.55.4.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 25
    #     - action: permit
    #       address: 11.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 100
    #     - action: permit
    #       address: 30.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 300
    #     name: v401
    #   - entries:
    #     - action: deny
    #       address: 10.1.1.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 10
    #     name: v402
    #   - entries:
    #     - action: deny
    #       address: 10.1.1.0/24
    #       sequence: 10
    #     name: v403
    # - afi: ipv6
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 5000:1::/64
    #       sequence: 125
    #     name: v601
    # commands:
    # - no ipv6 prefix-list v601
    # after:
    # - afi: ipv4
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 45.55.4.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 25
    #     - action: permit
    #       address: 11.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 100
    #     - action: permit
    #       address: 30.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 300
    #     name: v401
    #   - entries:
    #     - action: deny
    #       address: 10.1.1.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 10
    #     name: v402
    #   - entries:
    #     - action: deny
    #       address: 10.1.1.0/24
    #       sequence: 10
    #     name: v403

    # after State:
    # veos#show running-config | section prefix-list
    # ip prefix-list v401
    #    seq 25 deny 45.55.4.0/24 ge 32
    #    seq 100 permit 11.11.2.0/24 ge 32
    #    seq 300 permit 30.11.2.0/24 ge 32
    # !
    # ip prefix-list v402
    #    seq 10 deny 10.1.1.0/24 ge 32
    # !
    # ip prefix-list v403
    #    seq 10 deny 10.1.1.0/24
    #


    # Using deleted


    # Before state:
    # veos#show running-config | section prefix-list
    # ip prefix-list v401
    #    seq 25 deny 45.55.4.0/24 ge 32
    #    seq 100 permit 11.11.2.0/24 ge 32
    #    seq 300 permit 30.11.2.0/24 ge 32
    # !
    # ip prefix-list v402
    #    seq 10 deny 10.1.1.0/24 ge 32
    # !
    # ip prefix-list v403
    #    seq 10 deny 10.1.1.0/24
    # veos#

    - name: Delete device configuration
      arista.eos.eos_prefix_lists:
        state: deleted


    # Task Output
    # -------------
    # before:
    # - afi: ipv4
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 45.55.4.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 25
    #     - action: permit
    #       address: 11.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 100
    #     - action: permit
    #       address: 30.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 300
    #     name: v401
    #   - entries:
    #     - action: deny
    #       address: 10.1.1.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 10
    #     name: v402
    #   - entries:
    #     - action: deny
    #       address: 10.1.1.0/24
    #       sequence: 10
    #     name: v403
    # commands:
    # - no ip prefix-list v401
    # - no ip prefix-list v402
    # - no ip prefix-list v403
    # after: {}

    # After State:
    # veos#show running-config | section prefix-list
    # veos#


    # Using parsed:


    # parse_prefix_lists.cfg
    # ip prefix-list v401
    #    seq 25 deny 45.55.4.0/24
    #    seq 100 permit 11.11.2.0/24 ge 32
    # !
    # ip prefix-list v402
    #    seq 10 deny 10.1.1.0/24
    # !
    # ipv6 prefix-list v601
    #    seq 125 deny 5000:1::/64
    #


    - name: parse configs
      arista.eos.eos_prefix_lists:
        running_config: "{{ lookup('file', './parsed_prefix_lists.cfg') }}"
        state: parsed


    # Task Output
    # -------------
    # parsed:
    # - afi: ipv4
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 45.55.4.0/24
    #       sequence: 25
    #     - action: permit
    #       address: 11.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 100
    #     name: v401
    #   - entries:
    #     - action: deny
    #       address: 10.1.1.0/24
    #       sequence: 10
    #     name: v402
    # - afi: ipv6
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 5000:1::/64
    #       sequence: 125
    #     name: v601


    # Using rendered:

    - name: Render provided configuration
      arista.eos.eos_prefix_lists:
        config:
          - afi: "ipv4"
            prefix_lists:
              - name: "v401"
                entries:
                  - sequence: 25
                    action: "deny"
                    address: "45.55.4.0/24"
                  - sequence: 200
                    action: "permit"
                    address: "200.11.2.0/24"
                    match:
                      masklen: 32
                      operator: "ge"
              - name: "v403"
                entries:
                  - action: "deny"
                    address: "10.1.1.0/24"
                    sequence: 10
        state: rendered

    # Task Output
    # -------------
    # rendered:
    # - ip prefix-list v401
    # - seq 25 deny 45.55.4.0/24
    # - seq 200 permit 200.11.2.0/24 ge 32
    # - ip prefix-list v403
    # - seq 10 deny 10.1.1.0/24

    # using gathered:


    # Device config:
    # veos#show running-config | section prefix-list
    # ip prefix-list v401
    #    seq 25 deny 45.55.4.0/24
    #    seq 100 permit 11.11.2.0/24 ge 32
    # !
    # ip prefix-list v402
    #    seq 10 deny 10.1.1.0/24 ge 32
    # !
    # ipv6 prefix-list v601
    #    seq 125 deny 5000:1::/64
    # veos#

    - name: gather configs
      arista.eos.eos_prefix_lists:
        state: gathered

    # Task Output
    # -------------
    # gathered:
    # - afi: ipv4
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 45.55.4.0/24
    #       sequence: 25
    #     - action: permit
    #       address: 11.11.2.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 100
    #     name: v401
    #   - entries:
    #     - action: deny
    #       address: 10.1.1.0/24
    #       match:
    #         masklen: 32
    #         operator: ge
    #       sequence: 10
    #     name: v402
    # - afi: ipv6
    #   prefix_lists:
    #   - entries:
    #     - action: deny
    #       address: 5000:1::/64
    #       sequence: 125
    #     name: v601



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
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The resulting configuration model invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration prior to the model invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
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
                <td>always</td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;ip prefix-list v401&#x27;, &#x27;seq 25 deny 45.55.4.0/24&#x27;, &#x27;seq 200 permit 200.11.2.0/24 ge 32&#x27;, &#x27;ip prefix-list v403&#x27;, &#x27;seq 10 deny 10.1.1.0/24&#x27;]</div>
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
                <td>When <code>state</code> is <em>gathered</em></td>
                <td>
                            <div>The configuration as structured data transformed for the running configuration fetched from remote host</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
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
                <td>When <code>state</code> is <em>parsed</em></td>
                <td>
                            <div>The configuration as structured data transformed for the value of <code>running_config</code> option</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
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
                <td>When <code>state</code> is <em>rendered</em></td>
                <td>
                            <div>The set of CLI commands generated from the value in <code>config</code> option</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">- ip prefix-list v401 - seq 25 deny 45.55.4.0/24 - seq 200 permit 200.11.2.0/24 ge 32 - ip prefix-list v403 - seq 10 deny 10.1.1.0/24</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Gomathi Selvi Srinivasan (@GomathiselviS)
