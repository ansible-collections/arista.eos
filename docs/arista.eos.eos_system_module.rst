.. _arista.eos.eos_system_module:


*********************
arista.eos.eos_system
*********************

**Manage the system attributes on Arista EOS devices**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides declarative management of node system attributes on Arista EOS devices.  It provides an option to configure host system parameters or remove those parameters from the device active configuration.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>domain_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provides the list of domain suffixes to append to the hostname for the purpose of doing name resolution. This argument accepts a list of names and will be reconciled with the current active configuration on the running node.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: domain_search</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>domain_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure the IP domain name on the remote device to the provided value. Value should be in the dotted name form and will be appended to the <code>hostname</code> to create a fully-qualified domain name.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure the device hostname parameter. This option takes an ASCII string value.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>lookup_source</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=raw</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provides one or more source interfaces to use for performing DNS lookups.  The interface provided in <code>lookup_source</code> can only exist in a single VRF.  This argument accepts either a list of interface names or a list of hashes that configure the interface name and VRF name.  See examples.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name_servers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=raw</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of DNS name servers by IP address to use to perform name resolution lookups.  This argument accepts either a list of DNS servers or a list of hashes that configure the name server and VRF name.  See examples.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                    <li>absent</li>
                        </ul>
                </td>
                <td>
                        <div>State of the configuration values in the device&#x27;s current active configuration.  When set to <em>present</em>, the values should be configured in the device active configuration and when set to <em>absent</em> the values should not be in the device active configuration</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Arista EOS 4.24.6F



Examples
--------

.. code-block:: yaml

    - name: configure hostname and domain-name
      arista.eos.eos_system:
        hostname: eos01
        domain_name: test.example.com

    - name: remove configuration
      arista.eos.eos_system:
        state: absent

    - name: configure DNS lookup sources
      arista.eos.eos_system:
        lookup_source: Management1

    - name: configure DNS lookup sources with VRF support
      arista.eos.eos_system:
        lookup_source:
          - interface: Management1
            vrf: mgmt
          - interface: Ethernet1
            vrf: myvrf

    - name: configure name servers
      arista.eos.eos_system:
        name_servers:
          - 8.8.8.8
          - 8.8.4.4

    - name: configure name servers with VRF support
      arista.eos.eos_system:
        name_servers:
          - {server: 8.8.8.8, vrf: mgmt}
          - {server: 8.8.4.4, vrf: mgmt}



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
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The list of configuration mode commands to send to the device</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;hostname eos01&#x27;, &#x27;dns domain test.example.com&#x27;]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>session_name</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>changed</td>
                <td>
                            <div>The EOS config session name used to load the configuration</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ansible_1479315771</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Peter Sprygada (@privateip)
