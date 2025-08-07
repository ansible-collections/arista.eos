.. _arista.eos.eos_bgp_address_family_module:


*********************************
arista.eos.eos_bgp_address_family
*********************************

**Manages BGP address family resource module**


Version added: 1.4.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module configures and manages the attributes of BGP AF on Arista EOS platforms.




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
                        <div>Configurations for BGP address family.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address_family</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enable address family and enter its config mode</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                                    <li>evpn</li>
                        </ul>
                </td>
                <td>
                        <div>address family.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bgp_params</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP parameters.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>additional_paths</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>install</li>
                                    <li>send</li>
                                    <li>receive</li>
                        </ul>
                </td>
                <td>
                        <div>BGP additional-paths commands</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hop_address_family</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>Next-hop address-family configuration</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hop_unchanged</b>
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
                        <div>Preserve original nexthop while advertising routes to eBGP peers.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>redistribute_internal</b>
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
                        <div>Redistribute internal BGP routes.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure route-map for route installation.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>graceful_restart</b>
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
                        <div>Enable graceful restart mode.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>neighbor</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure routing for a network.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>activate</b>
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
                        <div>Activate neighbor in the address family.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>additional_paths</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>send</li>
                                    <li>receive</li>
                        </ul>
                </td>
                <td>
                        <div>BGP additional-paths commands.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_originate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Originate default route to this neighbor.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>always</b>
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
                        <div>Always originate default route to this neighbor.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route map reference.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>encapsulation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Default transport encapsulation for neighbor. Applicable for evpn address-family.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source interface to update BGP next hop address. Applicable for mpls transport.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transport</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>mpls</li>
                                    <li>vxlan</li>
                        </ul>
                </td>
                <td>
                        <div>MPLS/VXLAN transport.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>graceful_restart</b>
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
                        <div>Enable graceful restart mode.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hop_address_family</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>Next-hop address-family configuration</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hop_unchanged</b>
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
                        <div>Preserve original nexthop while advertising routes to eBGP peers.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Neighbor address/ peer group name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Prefix list reference.</div>
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
                        <div>Configure an inbound/outbound prefix-list.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>prefix list name.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route map reference.</div>
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
                        <div>Configure an inbound/outbound route-map.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route map name.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>weight</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Weight to assign.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>network</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configure routing for network.</div>
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
                        <div>network address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route map reference.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>redistribute</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Redistribute routes in to BGP.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>isis_level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>level-1</li>
                                    <li>level-2</li>
                                    <li>level-1-2</li>
                        </ul>
                </td>
                <td>
                        <div>Applicable for isis routes. Specify isis route level.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ospf_route</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>internal</li>
                                    <li>external</li>
                                    <li>nssa_external_1</li>
                                    <li>nssa_external_2</li>
                        </ul>
                </td>
                <td>
                        <div>ospf route options.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>isis</li>
                                    <li>ospfv3</li>
                                    <li>dhcp</li>
                        </ul>
                </td>
                <td>
                        <div>Routes to be redistributed.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route map reference.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_target</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route target.</div>
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
                                    <li>both</li>
                                    <li>import</li>
                                    <li>export</li>
                        </ul>
                </td>
                <td>
                        <div>Route action.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: mode</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>imported_route</b>
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
                        <div>Export routes imported from the same Afi/Safi</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of a route map.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>target</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route Target.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>evpn</li>
                                    <li>vpn-ipv4</li>
                                    <li>vpn-ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>Type of address fmaily</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>safi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>labeled-unicast</li>
                                    <li>multicast</li>
                        </ul>
                </td>
                <td>
                        <div>Address family type for ipv4.</div>
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
                        <div>name of the VRF in which BGP will be configured.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Autonomous system number.</div>
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
                        <div>The value of this option should be the output received from the EOS device by executing the command <b>show running-config | section bgp</b>.</div>
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

    # Using Merged

    # Before state:
    # -------------
    # veos(config)#show running-config | section bgp
    # veos(config)#

    - name: Merge provided configuration with device configuration
      arista.eos.eos_bgp_address_family:
        config:
          as_number: "10"
          address_family:
            - afi: "ipv4"
              redistribute:
                - protocol: "ospfv3"
                  ospf_route: "external"
              network:
                - address: "1.1.1.0/24"
                - address: "1.5.1.0/24"
                  route_map: "MAP01"
            - afi: "ipv6"
              bgp_params:
                additional_paths: "receive"
              neighbor:
                - peer: "peer2"
                  default_originate:
                    always: true
            - afi: "ipv6"
              redistribute:
                - protocol: "isis"
                  isis_level: "level-2"
              route_target:
                mode: "export"
                target: "33:11"
              vrf: "vrft"
        state: merged


    # Task output:
    # ------------
    # before: {}
    #
    # commands:
    # - router bgp 10
    # - address-family ipv4
    # - redistribute ospfv3 match external
    # - network 1.1.1.0/24
    # - network 1.5.1.0/24 route-map MAP01
    # - exit
    # - address-family ipv6
    # - neighbor peer2 default-originate always
    # - bgp additional-paths receive
    # - exit
    # - vrf vrft
    # - address-family ipv6
    # - redistribute isis level-2
    # - route-target export 33:11
    # - exit
    # - exit
    #
    # after:
    #     address_family:
    #     - afi: ipv4
    #       neighbor:
    #       - activate: true
    #         peer: 1.1.1.1
    #       network:
    #       - address: 1.1.1.0/24
    #       - address: 1.5.1.0/24
    #         route_map: MAP01
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #     - afi: ipv6
    #       bgp_params:
    #         additional_paths: receive
    #       neighbor:
    #       - activate: true
    #         default_originate:
    #           always: true
    #         peer: peer2
    #     - afi: ipv6
    #       redistribute:
    #       - isis_level: level-2
    #         protocol: isis
    #       route_target:
    #         action: export
    #         target: '33:11'
    #       vrf: vrft
    #     as_number: '10'
    #     "before": {},
    #     "changed": true,

    # After state:
    # ------------
    # veos(config-router-bgp)#show running-config | section bgp
    # router bgp 10
    #    neighbor peer2 peer group
    #    neighbor peer2 maximum-routes 12000
    #    neighbor 1.1.1.1 maximum-routes 12000
    #    !
    #    address-family ipv4
    #       neighbor 1.1.1.1 activate
    #       network 1.1.1.0/24
    #       network 1.5.1.0/24 route-map MAP01
    #       redistribute ospfv3 match external
    #    !
    #    address-family ipv6
    #       bgp additional-paths receive
    #       neighbor peer2 activate
    #       neighbor peer2 default-originate always
    #    !
    #    vrf vrft
    #       address-family ipv6
    #          route-target export 33:11
    #          redistribute isis level-2

    # Using replaced

    # Before state:
    # -------------
    # veos(config-router-bgp)#show running-config | section bgp
    # router bgp 10
    #    neighbor peer2 peer group
    #    neighbor peer2 maximum-routes 12000
    #    neighbor 1.1.1.1 maximum-routes 12000
    #    !
    #    address-family ipv4
    #       neighbor 1.1.1.1 activate
    #       network 1.1.1.0/24
    #       network 1.5.1.0/24 route-map MAP01
    #       redistribute ospfv3 match external
    #    !
    #    address-family ipv6
    #       bgp additional-paths receive
    #       neighbor peer2 activate
    #       neighbor peer2 default-originate always
    #    !
    #    vrf vrft
    #       address-family ipv6
    #          route-target export 33:11
    #          redistribute isis level-2

    - name: Replace running config section with provided config
      arista.eos.eos_bgp_address_family:
        config:
          as_number: "10"
          address_family:
            - afi: "ipv6"
              vrf: "vrft"
              redistribute:
                - protocol: "ospfv3"
                  ospf_route: "external"
            - afi: "ipv6"
              redistribute:
                - protocol: "isis"
                  isis_level: "level-2"
        state: replaced

    # Task output:
    # ------------
    # before:
    #     address_family:
    #     - afi: ipv4
    #       neighbor:
    #       - activate: true
    #         peer: 1.1.1.1
    #       network:
    #       - address: 1.1.1.0/24
    #       - address: 1.5.1.0/24
    #         route_map: MAP01
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #     - afi: ipv6
    #       bgp_params:
    #         additional_paths: receive
    #       neighbor:
    #       - activate: true
    #         default_originate:
    #           always: true
    #         peer: peer2
    #     - afi: ipv6
    #       redistribute:
    #       - isis_level: level-2
    #         protocol: isis
    #       route_target:
    #         action: export
    #         target: '33:11'
    #       vrf: vrft
    #     as_number: '10'
    #
    # commands:
    # - router bgp 10
    # - vrf vrft
    # - address-family ipv6
    # - redistribute ospfv3 match external
    # - no redistribute isis level-2
    # - no route-target export 33:11
    # - exit
    # - exit
    # - address-family ipv6
    # - redistribute isis level-2
    # - no neighbor peer2 activate
    # - no bgp additional-paths receive
    # - exit
    #
    # after:
    #     address_family:
    #     - afi: ipv4
    #       neighbor:
    #       - activate: true
    #         peer: 1.1.1.1
    #       network:
    #       - address: 1.1.1.0/24
    #       - address: 1.5.1.0/24
    #         route_map: MAP01
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #     - afi: ipv6
    #       neighbor:
    #       - default_originate:
    #           always: true
    #         peer: peer2
    #       redistribute:
    #       - isis_level: level-2
    #         protocol: isis
    #     - afi: ipv6
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #       vrf: vrft
    #     as_number: '10'

    # After state:
    # ------------
    # veos(config-router-bgp)#show running-config | section bgp
    # router bgp 10
    #    neighbor peer2 peer group
    #    neighbor peer2 maximum-routes 12000
    #    neighbor 1.1.1.1 maximum-routes 12000
    #    !
    #    address-family ipv4
    #       neighbor 1.1.1.1 activate
    #       network 1.1.1.0/24
    #       network 1.5.1.0/24 route-map MAP01
    #       redistribute ospfv3 match external
    #    !
    #    address-family ipv6
    #       neighbor peer2 default-originate always
    #       redistribute isis level-2
    #    !
    #    vrf vrft
    #       address-family ipv6
    #          redistribute ospfv3 match external

    # Using overridden (overriding af at global context):

    # Before state:
    # -------------
    # veos(config-router-bgp)#show running-config | section bgp
    # router bgp 10
    #    neighbor peer2 peer group
    #    neighbor peer2 maximum-routes 12000
    #    neighbor 1.1.1.1 maximum-routes 12000
    #    !
    #    address-family ipv4
    #       neighbor 1.1.1.1 activate
    #       network 1.1.1.0/24
    #       network 1.5.1.0/24 route-map MAP01
    #       redistribute ospfv3 match external
    #    !
    #    address-family ipv6
    #       neighbor peer2 default-originate always
    #       redistribute isis level-2
    #    !
    #    vrf vrft
    #       address-family ipv6
    #          redistribute ospfv3 match external

    - name: Override running config with provided config
      arista.eos.eos_bgp_address_family:
        config:
          as_number: "10"
          address_family:
            - afi: "ipv4"
              bgp_params:
                additional_paths: "receive"
              neighbor:
                - peer: "peer2"
                  default_originate:
                    always: true
        state: overridden


    #
    # Task output:
    # ------------
    # before:
    #     address_family:
    #     - afi: ipv4
    #       neighbor:
    #       - activate: true
    #         peer: 1.1.1.1
    #       network:
    #       - address: 1.1.1.0/24
    #       - address: 1.5.1.0/24
    #         route_map: MAP01
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #     - afi: ipv6
    #       neighbor:
    #       - default_originate:
    #           always: true
    #         peer: peer2
    #       redistribute:
    #       - isis_level: level-2
    #         protocol: isis
    #     - afi: ipv6
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #       vrf: vrft
    #     as_number: '10'
    #
    # commands:
    # - router bgp 10
    # - address-family ipv4
    # - no redistribute ospfv3 match external
    # - no network 1.1.1.0/24
    # - no network 1.5.1.0/24 route-map MAP01
    # - neighbor peer2 default-originate always
    # - no neighbor 1.1.1.1 activate
    # - bgp additional-paths receive
    # - exit
    # - no address-family ipv6
    #
    # after:
    #     address_family:
    #     - afi: ipv4
    #       bgp_params:
    #         additional_paths: receive
    #       neighbor:
    #       - default_originate:
    #           always: true
    #         peer: peer2
    #     - afi: ipv6
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #       vrf: vrft
    #     as_number: '10'

    # After state:
    # ------------
    # veos(config-router-bgp)#show running-config | section bgp
    # router bgp 10
    #    neighbor peer2 peer group
    #    neighbor peer2 maximum-routes 12000
    #    neighbor 1.1.1.1 maximum-routes 12000
    #    !
    #    address-family ipv4
    #       bgp additional-paths receive
    #       neighbor peer2 default-originate always
    #    !
    #    vrf vrft
    #       address-family ipv6
    #          redistribute ospfv3 match external

    # using Overridden (overridding af in vrf context):

    # Before state:
    # -------------
    # veos(config-router-bgp)#show running-config | section bgp
    # router bgp 10
    #    neighbor peer2 peer group
    #    neighbor peer2 maximum-routes 12000
    #    neighbor 1.1.1.1 maximum-routes 12000
    #    !
    #    address-family ipv4
    #       bgp additional-paths receive
    #       neighbor peer2 default-originate always
    #       no neighbor 1.1.1.1 activate
    #       network 1.1.1.0/24
    #       network 1.5.1.0/24 route-map MAP01
    #       redistribute ospfv3 match external
    #    !
    #    address-family ipv6
    #       bgp additional-paths receive
    #       neighbor peer2 default-originate always
    #    !
    #    vrf vrft
    #       address-family ipv6
    #          route-target export 33:11
    #          redistribute isis level-2
    #          redistribute ospfv3 match external

    - name: Override running config with provided config
      arista.eos.eos_bgp_address_family:
        config:
          as_number: "10"
          address_family:
            - afi: "ipv4"
              bgp_params:
                additional_paths: "receive"
              neighbor:
                - peer: "peer2"
                  default_originate:
                    always: true
              vrf: vrft
        state: overridden

    # Task output:
    # ------------
    # before:
    #     address_family:
    #     - afi: ipv4
    #       bgp_params:
    #         additional_paths: receive
    #       neighbor:
    #       - default_originate:
    #           always: true
    #         peer: peer2
    #       network:
    #       - address: 1.1.1.0/24
    #       - address: 1.5.1.0/24
    #         route_map: MAP01
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #     - afi: ipv6
    #       bgp_params:
    #         additional_paths: receive
    #       neighbor:
    #       - default_originate:
    #           always: true
    #         peer: peer2
    #     - afi: ipv6
    #       redistribute:
    #       - isis_level: level-2
    #         protocol: isis
    #       - ospf_route: external
    #         protocol: ospfv3
    #       route_target:
    #         action: export
    #         target: '33:11'
    #       vrf: vrft
    #     as_number: '10'
    #
    # commands:
    # - router bgp 10
    # - vrf vrft
    # - address-family ipv4
    # - neighbor peer2 default-originate always
    # - bgp additional-paths receive
    # - exit
    # - exit
    # - vrf vrft
    # - no address-family ipv6
    #
    # after:
    #     address_family:
    #     - afi: ipv4
    #       bgp_params:
    #         additional_paths: receive
    #       neighbor:
    #       - default_originate:
    #           always: true
    #         peer: peer2
    #       network:
    #       - address: 1.1.1.0/24
    #       - address: 1.5.1.0/24
    #         route_map: MAP01
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #     - afi: ipv6
    #       bgp_params:
    #         additional_paths: receive
    #       neighbor:
    #       - default_originate:
    #           always: true
    #         peer: peer2
    #     - afi: ipv4
    #       bgp_params:
    #         additional_paths: receive
    #       vrf: vrft
    #     as_number: '10'

    # After state:
    # ------------
    # veos(config-router-bgp)#show running-config | section bgp
    # router bgp 10
    #    neighbor peer2 peer group
    #    neighbor peer2 maximum-routes 12000
    #    neighbor 1.1.1.1 maximum-routes 12000
    #    !
    #    address-family ipv4
    #       bgp additional-paths receive
    #       neighbor peer2 default-originate always
    #       network 1.1.1.0/24
    #       network 1.5.1.0/24 route-map MAP01
    #       redistribute ospfv3 match external
    #    !
    #    address-family ipv6
    #       bgp additional-paths receive
    #       neighbor peer2 default-originate always
    #    !
    #    vrf vrft
    #       address-family ipv4
    #          bgp additional-paths receive

    # Using deleted

    # Before state:
    # -------------
    # veos(config-router-bgp)#show running-config | section bgp
    # router bgp 10
    #    neighbor peer2 peer group
    #    neighbor peer2 maximum-routes 12000
    #    neighbor 1.1.1.1 maximum-routes 12000
    #    !
    #    address-family ipv4
    #       bgp additional-paths receive
    #       neighbor peer2 default-originate always
    #       no neighbor 1.1.1.1 activate
    #       network 1.1.1.0/24
    #       network 1.5.1.0/24 route-map MAP01
    #       redistribute ospfv3 match external
    #    !
    #    address-family ipv6
    #       bgp additional-paths receive
    #       neighbor peer2 default-originate always
    #    !
    #    vrf vrft
    #       address-family ipv4
    #          bgp additional-paths receive

    - name: Delete running config for provided afi
      arista.eos.eos_bgp_address_family:
        config:
          as_number: "10"
          address_family:
            - afi: "ipv6"
              vrf: "vrft"
            - afi: "ipv6"
        state: deleted

    # Task output:
    # ------------
    # before:
    #     address_family:
    #     - afi: ipv4
    #       bgp_params:
    #         additional_paths: receive
    #       neighbor:
    #       - default_originate:
    #           always: true
    #         peer: peer2
    #       network:
    #       - address: 1.1.1.0/24
    #       - address: 1.5.1.0/24
    #         route_map: MAP01
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #     - afi: ipv6
    #       bgp_params:
    #         additional_paths: receive
    #       neighbor:
    #       - default_originate:
    #           always: true
    #         peer: peer2
    #     - afi: ipv4
    #       bgp_params:
    #         additional_paths: receive
    #       vrf: vrft
    #     as_number: '10'
    #
    # after:
    #     address_family:
    #     - afi: ipv4
    #       bgp_params:
    #         additional_paths: receive
    #       neighbor:
    #       - default_originate:
    #           always: true
    #         peer: peer2
    #       network:
    #       - address: 1.1.1.0/24
    #       - address: 1.5.1.0/24
    #         route_map: MAP01
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #     - afi: ipv4
    #       bgp_params:
    #         additional_paths: receive
    #       vrf: vrft
    #     as_number: '10'

    # After state:
    # ------------
    # veos(config-router-bgp)#show running-config | section bgp
    # router bgp 10
    #    neighbor peer2 peer group
    #    neighbor peer2 maximum-routes 12000
    #    neighbor 1.1.1.1 maximum-routes 12000
    #    !
    #    address-family ipv4
    #       bgp additional-paths receive
    #       neighbor peer2 default-originate always
    #       no neighbor 1.1.1.1 activate
    #       network 1.1.1.0/24
    #       network 1.5.1.0/24 route-map MAP01
    #       redistribute ospfv3 match external
    #    !
    #    vrf vrft
    #       address-family ipv4
    #          bgp additional-paths receive


    # Using parsed

    # parsed.cfg
    # ----------
    # router bgp 10
    #    neighbor n2 peer group
    #    neighbor n2 next-hop-unchanged
    #    neighbor n2 maximum-routes 12000
    #    neighbor peer2 peer group
    #    neighbor peer2 maximum-routes 12000
    #    network 1.1.1.0/24
    #    network 1.5.1.0/24 route-map MAP01
    #    !
    #    address-family ipv4
    #       bgp additional-paths receive
    #       neighbor peer2 default-originate always
    #       redistribute ospfv3 match external
    #    !
    #    address-family ipv6
    #       no bgp additional-paths receive
    #       neighbor n2 next-hop-unchanged
    #       redistribute isis level-2
    #    !
    #    vrf bgp_10
    #       ip access-group acl01
    #       ucmp fec threshold trigger 33 clear 22 warning-only
    #       !
    #       address-family ipv4
    #          route-target import 20:11
    #    !
    #    vrf vrft
    #       address-family ipv4
    #          bgp additional-paths receive
    #       !
    #       address-family ipv6
    #          redistribute ospfv3 match external

    - name: parse running config and generate structred facts
      arista.eos.eos_bgp_address_family:
        running_config: "{{ lookup('file', './parsed_bgp_address_family.cfg') }}"
        state: parsed

    # Task output:
    # ------------
    # parsed:
    #     address_family:
    #     - afi: ipv4
    #       bgp_params:
    #         additional_paths: receive
    #       neighbor:
    #       - default_originate:
    #           always: true
    #         peer: peer2
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #     - afi: ipv6
    #       neighbor:
    #       - next_hop_unchanged: true
    #         peer: n2
    #       redistribute:
    #       - isis_level: level-2
    #         protocol: isis
    #     - afi: ipv4
    #       route_target:
    #         action: import
    #         target: '20:11'
    #       vrf: bgp_10
    #     - afi: ipv4
    #       bgp_params:
    #         additional_paths: receive
    #       vrf: vrft
    #     - afi: ipv6
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #       vrf: vrft
    #     as_number: '10'

    # Using gathered

    # running config
    # --------------
    # veos(config-router-bgp)#show running-config | section bgp
    # router bgp 10
    #    neighbor peer2 peer group
    #    neighbor peer2 maximum-routes 12000
    #    neighbor 1.1.1.1 maximum-routes 12000
    #    !
    #    address-family ipv4
    #       bgp additional-paths receive
    #       neighbor peer2 default-originate always
    #       no neighbor 1.1.1.1 activate
    #       network 1.1.1.0/24
    #       network 1.5.1.0/24 route-map MAP01
    #       redistribute ospfv3 match external
    #    !
    #    vrf vrft
    #       address-family ipv4
    #          bgp additional-paths receive

    - name: gather running config
      arista.eos.eos_bgp_address_family:
        state: gathered

    # Task output:
    # ------------
    # gathered:
    #     address_family:
    #     - afi: ipv4
    #       bgp_params:
    #         additional_paths: receive
    #       neighbor:
    #       - default_originate:
    #           always: true
    #         peer: peer2
    #       network:
    #       - address: 1.1.1.0/24
    #       - address: 1.5.1.0/24
    #         route_map: MAP01
    #       redistribute:
    #       - ospf_route: external
    #         protocol: ospfv3
    #     - afi: ipv4
    #       bgp_params:
    #         additional_paths: receive
    #       vrf: vrft
    #     as_number: '10'

    # using rendered

    - name: Render CLI commands for provided config
      arista.eos.eos_bgp_address_family:
        config:
          as_number: "10"
          address_family:
            - afi: "ipv4"
              redistribute:
                - protocol: "ospfv3"
                  ospf_route: "external"
              network:
                - address: "1.1.1.0/24"
                - address: "1.5.1.0/24"
                  route_map: "MAP01"
            - afi: "ipv6"
              bgp_params:
                additional_paths: "receive"
              neighbor:
                - peer: "peer2"
                  default_originate:
                    always: true
            - afi: "ipv6"
              redistribute:
                - protocol: "isis"
                  isis_level: "level-2"
              route_target:
                mode: "export"
                target: "33:11"
              vrf: "vrft"
        state: rendered

    # Task output:
    # ------------
    # rendered:
    # - router bgp 10
    # - address-family ipv4
    # - redistribute ospfv3 match external
    # - network 1.1.1.0/24
    # - network 1.5.1.0/24 route-map MAP01
    # - exit
    # - address-family ipv6
    # - neighbor peer2 default-originate always
    # - bgp additional-paths receive
    # - exit
    # - vrf vrft
    # - address-family ipv6
    # - redistribute isis level-2
    # - route-target export 33:11
    # - exit
    # - exit



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;router bgp 10&#x27;, &#x27;address-family ipv4&#x27;, &#x27;redistribute ospfv3 match external&#x27;, &#x27;network 1.1.1.0/24&#x27;]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>gathered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
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
                      <span style="color: purple">dictionary</span>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;router bgp 10&#x27;, &#x27;address-family ipv4&#x27;, &#x27;redistribute ospfv3 match external&#x27;, &#x27;network 1.1.1.0/24&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Gomathi Selvi Srinivasan (@GomathiselviS)
