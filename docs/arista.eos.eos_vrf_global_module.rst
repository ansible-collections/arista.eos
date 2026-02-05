.. _arista.eos.eos_vrf_global_module:


*************************
arista.eos.eos_vrf_global
*************************

**Resource module to configure VRF definitions.**


Version added: 10.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides declarative management of VRF definitions on Arista EOS platforms.




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
                        <div>A list of dictionaries containing device configurations for VRF definitions.</div>
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
                        <div>A description for the VRF.</div>
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
                        <div>Name of the VRF Instance.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rd</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP Route Distinguisher (RD).</div>
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
                        <div>The value of this option should be the output received from the EOS device by executing the command <b>show running-config vrf</b>.</div>
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
                                    <li>parsed</li>
                                    <li>gathered</li>
                                    <li>deleted</li>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>replaced</li>
                                    <li>rendered</li>
                                    <li>overridden</li>
                                    <li>purged</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in</div>
                        <div>The states <em>rendered</em>, <em>gathered</em> and <em>parsed</em> does not perform any change on the device.</div>
                        <div>The state <em>rendered</em> will transform the configuration in <code>config</code> option to platform specific CLI commands which will be returned in the <em>rendered</em> key within the result. For state <em>rendered</em> active connection to remote host is not required.</div>
                        <div>The state <em>gathered</em> will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the <em>gathered</em> key within the result.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into JSON format as per the resource module parameters and the value is returned in the <em>parsed</em> key within the result. The value of <code>running_config</code> option should be the same format as the output of command <em>show running-config vrf</em>. connection to remote host is not required.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Arista EOS 4.23.0F
   - This module works with connection ``network_cli``. See the `EOS Platform Options <eos_platform_options>`_.



Examples
--------

.. code-block:: yaml

    # Using merged
    #
    # Before state:
    # -------------
    #
    # test#show running-config | section ^vrf

    - name: Merge provided configuration with device configuration
      arista.eos.eos_vrf_global:
        config:
          - name: VRF4
            description: VRF4 Description
            rd: "3:4"
        state: merged

    # Task Output:
    # ------------
    #
    # before: []
    #
    # commands:
    # - vrf instance VRF4
    # - description VRF4 Description
    # - rd 3:4
    #
    # after:
    # - name: VRF4
    #   description: VRF4 Description
    #   rd: "3:4"
    #
    # After state:
    # ------------
    #
    # test#show running-config | section ^vrf
    # vrf instance VRF4
    #  description "VRF4 Description"
    #  rd "3:4"

    # Using replaced
    #
    # Before state:
    # -------------
    #
    # test#show running-config | section ^vrf
    # vrf instance VRF4
    #  description "VRF4 Description"
    #  rd "3:4"

    - name: Replace the provided configuration with the existing running configuration
      arista.eos.eos_vrf_global:
        config:
          - name: VRF7
            description: VRF7 description
            rd: "67:9"
        state: replaced

    # Task Output:
    # ------------
    #
    # before:
    # - name: VRF4
    #   description: VRF4 Description
    #   rd: "3:4"
    #
    # commands:
    # - vrf instance VRF7
    # - description VRF7 description
    # - rd 6:9
    #
    # after:
    #   - name: VRF4
    #     description: VRF4 Description
    #     rd: "3:4"
    #   - name: VRF7
    #     description: VRF7 description
    #     rd: "6:9"
    #
    # After state:
    # ------------
    #
    # test#show running-config | section ^vrf
    # vrf instance VRF4
    #  description VRF4 Description
    #  rd 3:4
    # !
    # vrf instance VRF7
    #  description VRF7 description
    #  rd 6:9
    #  !
    # !

    # Using overridden
    #
    # Before state:
    # -------------
    #
    # test#show running-config | section ^vrf
    # vrf instance VRF4
    #  description VRF4 Description
    #  rd 3:4
    # !
    # vrf instance VRF7
    #  description VRF7 description
    #  rd 6:9
    #  !
    # !

    - name: Override the provided configuration with the existing running configuration
      arista.eos.eos_vrf_global:
        state: overridden
        config:
          - name: VRF6
            description: VRF6 Description
            rd: "9:8"

    # Task Output:
    # ------------
    #
    # before:
    # - name: VRF4
    #   description: VRF4 Description
    #   rd: "3:4"
    # - name: VRF7
    #   description: VRF7 description
    #   rd: "6:9"
    #
    # commands:
    # - vrf instance VRF4
    # - no description VRF4 Description
    # - no rd 3:4
    # - vrf instance VRF7
    # - no description VRF7 description
    # - no rd 67:9
    # - vrf instance VRF6
    # - description VRF6 Description
    # - rd 9:8
    #
    # after:
    # - name: VRF4
    # - name: VRF6
    #   description: VRF6 Description
    #   rd: "9:8"
    # - name: VRF7
    #
    # After state:
    # -------------
    # test#show running-config | section ^vrf
    # vrf instance VRF4
    # vrf instance VRF6
    #  description VRF6 Description
    #  rd 9:8
    # vrf instance VRF7

    # Using deleted
    #
    # Before state:
    # -------------
    #
    # test#show running-config | section ^vrf
    # vrf instance VRF4
    # vrf instance VRF6
    #  description VRF6 Description
    #  rd 9:8
    # vrf instance VRF7

    - name: Delete the provided configuration
      arista.eos.eos_vrf_global:
        config:
        state: deleted

    # Task Output:
    # ------------
    #
    # before:
    # - name: VRF4
    # - name: VRF6
    #   description: VRF6 Description
    #   rd: "9:8"
    # - name: VRF7

    # commands:
    # - vrf instance VRF4
    # - vrf instance VRF6
    # - no description VRF6 Description
    # - no rd 9:8
    # - vrf instance VRF7
    #
    # after:
    # - name: VRF4
    # - name: VRF6
    # - name: VRF7
    #
    # After state:
    # ------------
    #
    # test#show running-config | section ^vrf
    # vrf instance VRF4
    # vrf instance VRF6
    # vrf instance VRF7

    # Using purged
    #
    # Before state:
    # -------------
    #
    # test#show running-config | section ^vrf
    # vrf instance VRF4
    # vrf instance VRF6
    # vrf instance VRF7

    - name: Purge all the configuration from the device
      arista.eos.eos_vrf_global:
        state: purged

    # Task Output:
    # ------------
    #
    # before:
    # - name: VRF4
    # - name: VRF6
    # - name: VRF7
    #
    # commands:
    # - no vrf instance VRF4
    # - no vrf instance VRF6
    # - no vrf instance VRF7
    #
    # after: []
    #
    # After state:
    # -------------
    # test#show running-config | section ^vrf
    # -

    # Using rendered
    #
    - name: Render provided configuration with device configuration
      arista.eos.eos_vrf_global:
        config:
          - name: VRF4
            description: VRF4 Description
            rd: "3:4"
        state: rendered

    # Task Output:
    # ------------
    #
    # rendered:
    # - vrf instance VRF4
    # - description VRF4 Description
    # - rd 3:4

    # Using gathered
    #
    # Before state:
    # -------------
    #
    # test#show running-config | section ^vrf
    # vrf instance VRF4
    #  description "VRF4 Description"
    #  rd "3:4"

    - name: Gather existing running configuration
      arista.eos.eos_vrf_global:
        state: gathered

    # Task Output:
    # ------------
    #
    # gathered:
    # - name: VRF4
    #   description: VRF4 Description
    #   rd: "3:4"

    # Using parsed
    #
    # File: parsed.cfg
    # ----------------
    #
    # vrf instance test
    #  description "This is test VRF"
    #  rd "testing"
    #  !
    # !
    # vrf my_vrf
    #  description "this is sample vrf for feature testing"
    #  rd "2:3"
    #  !
    # !

    - name: Parse the provided configuration
      arista.eos.eos_vrf_global:
        running_config: "{{ lookup('file', 'parsed.cfg') }}"
        state: parsed

    # Task Output:
    # ------------
    #
    # parsed:
    # - description: This is test VRF
    #   name: test
    #   rd: testing
    # - description: this is sample vrf for feature testing
    #   name: my_vrf
    #   rd: '2:3'



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
                            <div>The resulting configuration after module execution.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
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
                <td>when <em>state</em> is <code>merged</code>, <code>replaced</code>, <code>overridden</code>, <code>deleted</code> or <code>purged</code></td>
                <td>
                            <div>The configuration prior to the module execution.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;vrf instance test&#x27;, &#x27;description &quot;This is test VRF&quot;&#x27;, &#x27;rd 3:4&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;vrf instance test&#x27;, &#x27;description &quot;This is test VRF&quot;&#x27;, &#x27;rd 3:4&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ruchi Pakhle (@Ruchip16)
