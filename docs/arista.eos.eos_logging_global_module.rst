.. _arista.eos.eos_logging_global_module:


*****************************
arista.eos.eos_logging_global
*****************************

**Manages logging resource module**


Version added: 3.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module configures and manages the attributes of  logging on Arista EOS platforms.




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
                        <div>A dictionary of logging options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>buffered</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set buffered logging parameters.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>buffer_size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Logging buffer size</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>emergencies</li>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>errors</li>
                                    <li>warnings</li>
                                    <li>notifications</li>
                                    <li>informational</li>
                                    <li>debugging</li>
                        </ul>
                </td>
                <td>
                        <div>Severity level .</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>console</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set console logging parameters.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>emergencies</li>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>errors</li>
                                    <li>warnings</li>
                                    <li>notifications</li>
                                    <li>informational</li>
                                    <li>debugging</li>
                        </ul>
                </td>
                <td>
                        <div>Severity level .</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>event</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>link-status</li>
                                    <li>port-channel</li>
                                    <li>spanning-tree</li>
                        </ul>
                </td>
                <td>
                        <div>Global events</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facility</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>auth</li>
                                    <li>cron</li>
                                    <li>daemon</li>
                                    <li>kern</li>
                                    <li>local0</li>
                                    <li>local1</li>
                                    <li>local2</li>
                                    <li>local3</li>
                                    <li>local4</li>
                                    <li>local5</li>
                                    <li>local6</li>
                                    <li>local7</li>
                                    <li>lpr</li>
                                    <li>mail</li>
                                    <li>news</li>
                                    <li>sys10</li>
                                    <li>sys11</li>
                                    <li>sys12</li>
                                    <li>sys13</li>
                                    <li>sys14</li>
                                    <li>sys9</li>
                                    <li>syslog</li>
                                    <li>user</li>
                                    <li>uucp</li>
                        </ul>
                </td>
                <td>
                        <div>Set logging facility.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>format</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set logging format parameters</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specify hostname logging format.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sequence_numbers</b>
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
                        <div>No. of log messages.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timestamp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set timestamp logging parameters.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>high_resolution</b>
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
                        <div>RFC3339 timestamps.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>traditional</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Traditional syslog timestamp format as specified in RFC3164.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                                    <li>enabled</li>
                                    <li>disabled</li>
                        </ul>
                </td>
                <td>
                        <div>When enabled traditional timestamp format is set.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timezone</b>
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
                        <div>Show timezone in traditional format timestamp</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>year</b>
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
                        <div>Show year in traditional format timestamp</div>
                </td>
            </tr>



            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hosts</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set syslog server IP address and parameters.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>add</b>
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
                        <div>Configure ports on the given host.</div>
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
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Hostname or IP address of the syslog server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port of the syslog server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>tcp</li>
                                    <li>udp</li>
                        </ul>
                </td>
                <td>
                        <div>Set syslog server transport protocol</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>remove</b>
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
                        <div>Remove configured ports from the given host</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure logging severity</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facility</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Facility level</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>emergencies</li>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>errors</li>
                                    <li>warnings</li>
                                    <li>notifications</li>
                                    <li>informational</li>
                                    <li>debugging</li>
                        </ul>
                </td>
                <td>
                        <div>Severity level .</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>monitor</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set terminal monitor severity</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>persistent</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Save logging messages to the flash disk.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>set</b>
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
                        <div>Save logging messages to the flash dis.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The maximum size (in bytes) of logging file stored on flash disk.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>policy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure logging policies.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>invert_result</b>
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
                        <div>Invert the match of match-list.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure logging message filtering.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>qos</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set DSCP value in IP header.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>relogging_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure relogging-interval for critical log messages</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>repeat_messages</b>
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
                        <div>Repeat messages instead of summarizing number of repeats</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                        <div>Use IP Address of interface as source IP of log messages.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>synchronous</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set synchronizing unsolicited with solicited messages</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure logging severity</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>set</b>
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
                        <div>Set synchronizing unsolicited with solicited messages.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trap</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Severity of messages sent to the syslog server.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>set</b>
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
                        <div>Severity of messages sent to the syslog server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>emergencies</li>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>errors</li>
                                    <li>warnings</li>
                                    <li>notifications</li>
                                    <li>informational</li>
                                    <li>debugging</li>
                        </ul>
                </td>
                <td>
                        <div>Severity level .</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>turn_on</b>
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
                        <div>Turn on logging.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrfs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify vrf</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hosts</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set syslog server IP address and parameters.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>add</b>
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
                        <div>Configure ports on the given host.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Hostname or IP address of the syslog server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port of the syslog server.</div>
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
                                    <li>tcp</li>
                                    <li>udp</li>
                        </ul>
                </td>
                <td>
                        <div>Set syslog server transport protocol</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>remove</b>
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
                        <div>Remove configured ports from the given host</div>
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
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Use IP Address of interface as source IP of log messages.</div>
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
                        <div>The states <em>replaced</em> and <em>overridden</em> have identical behaviour for this module.</div>
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
   - Tested against Arista EOS 4.24.6M
   - This module works with connection ``network_cli``. See the `EOS Platform Options <eos_platform_options>`_.



Examples
--------

.. code-block:: yaml

    # Using merged
    # Before state

    # test(config)#show running-config | section logging
    # test(config)#

    - name: Merge provided configuration with device configuration
      arista.eos.eos_logging_global:
        config:
          hosts:
            - name: "host01"
              protocol: "tcp"
            - name: "11.11.11.1"
              port: 25
          vrfs:
            - name: "vrf01"
              source_interface: "Ethernet1"
            - name: "vrf02"
              hosts:
                - name: "hostvrf1"
                  protocol: "tcp"
                - name: "24.1.1.1"
                  port: "33"

    # After State:

    # test(config)#show running-config | section logging
    # logging host 11.11.11.1 25
    # logging host host01 514 protocol tcp
    # logging vrf vrf02 host 24.1.1.1 33
    # logging vrf vrf02 host hostvrf1 514 protocol tcp
    # logging vrf vrf01 source-interface Ethernet1
    # test(config)#
    #
    #
    # Module Execution:
    # "after": {
    #         "hosts": [
    #             {
    #                 "name": "11.11.11.1",
    #                 "port": 25
    #             },
    #             {
    #                 "name": "host01",
    #                 "port": 514,
    #                 "protocol": "tcp"
    #             }
    #         ],
    #         "vrfs": [
    #             {
    #                 "name": "vrf01",
    #                 "source_interface": "Ethernet1"
    #             },
    #             {
    #                 "hosts": [
    #                     {
    #                         "name": "24.1.1.1",
    #                         "port": 33
    #                     },
    #                     {
    #                         "name": "hostvrf1",
    #                         "port": 514,
    #                         "protocol": "tcp"
    #                     }
    #                 ],
    #                 "name": "vrf02"
    #             }
    #         ]
    #     },
    #     "before": {},
    #     "changed": true,
    #     "commands": [
    #         "logging host host01 protocol tcp",
    #         "logging host 11.11.11.1 25",
    #         "logging vrf vrf01 source-interface Ethernet1",
    #         "logging vrf vrf02 host hostvrf1 protocol tcp",
    #         "logging vrf vrf02 host 24.1.1.1 33"
    #     ],
    #

    # Using replaced:
    # Before State:

    # test(config)#show running-config | section logging
    # logging host 11.11.11.1 25
    # logging host host01 514 protocol tcp
    # logging vrf vrf02 host 24.1.1.1 33
    # logging vrf vrf02 host hostvrf1 514 protocol tcp
    # logging format timestamp traditional timezone
    # logging vrf vrf01 source-interface Ethernet1
    # logging policy match inverse-result match-list                           list01 discard
    # logging persistent 4096
    # !
    # logging level AAA alerts
    # test(config)#

    - name: Repalce
      arista.eos.eos_logging_global:
        config:
          synchronous:
            set: true
          trap:
            severity: "critical"
          hosts:
            - name: "host02"
              protocol: "tcp"
          vrfs:
            - name: "vrf03"
              source_interface: "Vlan100"
            - name: "vrf04"
              hosts:
                - name: "hostvrf1"
                  protocol: "tcp"

        state: replaced

    # After State:
    # test(config)#show running-config | section logging
    # logging synchronous
    # logging trap critical
    # logging host host02 514 protocol tcp
    # logging vrf vrf04 host hostvrf1 514 protocol tcp
    # logging vrf vrf03 source-interface Vlan100
    # test(config)#
    #
    # Module Execution:
    # "after": {
    #         "hosts": [
    #             {
    #                 "name": "host02",
    #                 "port": 514,
    #                 "protocol": "tcp"
    #             }
    #         ],
    #         "synchronous": {
    #             "set": true
    #         },
    #         "trap": {
    #            "severity": "critical"
    #         },
    #         "vrfs": [
    #             {
    #                 "name": "vrf03",
    #                 "source_interface": "Vlan100"
    #             },
    #             {
    #                 "hosts": [
    #                     {
    #                         "name": "hostvrf1",
    #                         "port": 514,
    #                         "protocol": "tcp"
    #                     }
    #                 ],
    #                 "name": "vrf04"
    #             }
    #         ]
    #     },
    #     "before": {
    #         "format": {
    #             "timestamp": {
    #                 "traditional": {
    #                     "timezone": true
    #                 }
    #             }
    #         },
    #         "hosts": [
    #             {
    #                 "name": "11.11.11.1",
    #                 "port": 25
    #             },
    #             {
    #                 "name": "host01",
    #                 "port": 514,
    #                 "protocol": "tcp"
    #             }
    #         ],
    #         "level": {
    #             "facility": "AAA",
    #             "severity": "alerts"
    #         },
    #         "persistent": {
    #             "size": 4096
    #         },
    #         "policy": {
    #             "invert_result": true,
    #             "match_list": "list01"
    #         },
    #         "vrfs": [
    #             {
    #                 "name": "vrf01",
    #                 "source_interface": "Ethernet1"
    #             },
    #             {
    #                 "hosts": [
    #                     {
    #                         "name": "24.1.1.1",
    #                         "port": 33
    #                     },
    #                     {
    #                         "name": "hostvrf1",
    #                         "port": 514,
    #                         "protocol": "tcp"
    #                     }
    #                 ],
    #                 "name": "vrf02"
    #             }
    #         ]
    #     },
    #     "changed": true,
    #     "commands": [
    #         "logging host host02 protocol tcp",
    #         "no logging host 11.11.11.1 25",
    #         "no logging host host01 514 protocol tcp",
    #         "logging vrf vrf03 source-interface Vlan100",
    #         "logging vrf vrf04 host hostvrf1 protocol tcp",
    #         "no logging vrf vrf01 source-interface Ethernet1",
    #         "no logging vrf vrf02 host 24.1.1.1 33",
    #         "no logging vrf vrf02 host hostvrf1 514 protocol tcp",
    #         "no logging format timestamp traditional timezone",
    #         "no logging level AAA alerts",
    #         "no logging persistent 4096",
    #         "no logging policy match invert-result match-list list01 discard",
    #         "logging synchronous",
    #         "logging trap critical"
    #     ],
    #
    #


    # Using overridden:
    # Before State:

    # test(config)#show running-config | section logging
    # logging host 11.11.11.1 25
    # logging host host01 514 protocol tcp
    # logging vrf vrf02 host 24.1.1.1 33
    # logging vrf vrf02 host hostvrf1 514 protocol tcp
    # logging format timestamp traditional timezone
    # logging vrf vrf01 source-interface Ethernet1
    # logging policy match inverse-result match-list                           list01 discard
    # logging persistent 4096
    # !
    # logging level AAA alerts
    # test(config)#

    - name: Repalce
      arista.eos.eos_logging_global:
        config:
          synchronous:
            set: true
          trap:
            severity: "critical"
          hosts:
            - name: "host02"
              protocol: "tcp"
          vrfs:
            - name: "vrf03"
              source_interface: "Vlan100"
            - name: "vrf04"
              hosts:
                - name: "hostvrf1"
                  protocol: "tcp"

        state: overridden

    # After State:
    # test(config)#show running-config | section logging
    # logging synchronous
    # logging trap critical
    # logging host host02 514 protocol tcp
    # logging vrf vrf04 host hostvrf1 514 protocol tcp
    # logging vrf vrf03 source-interface Vlan100
    # test(config)#
    #
    # Module Execution:
    # "after": {
    #         "hosts": [
    #             {
    #                 "name": "host02",
    #                 "port": 514,
    #                 "protocol": "tcp"
    #             }
    #         ],
    #         "synchronous": {
    #             "set": true
    #         },
    #         "trap": {
    #            "severity": "critical"
    #         },
    #         "vrfs": [
    #             {
    #                 "name": "vrf03",
    #                 "source_interface": "Vlan100"
    #             },
    #             {
    #                 "hosts": [
    #                     {
    #                         "name": "hostvrf1",
    #                         "port": 514,
    #                         "protocol": "tcp"
    #                     }
    #                 ],
    #                 "name": "vrf04"
    #             }
    #         ]
    #     },
    #     "before": {
    #         "format": {
    #             "timestamp": {
    #                 "traditional": {
    #                     "timezone": true
    #                 }
    #             }
    #         },
    #         "hosts": [
    #             {
    #                 "name": "11.11.11.1",
    #                 "port": 25
    #             },
    #             {
    #                 "name": "host01",
    #                 "port": 514,
    #                 "protocol": "tcp"
    #             }
    #         ],
    #         "level": {
    #             "facility": "AAA",
    #             "severity": "alerts"
    #         },
    #         "persistent": {
    #             "size": 4096
    #         },
    #         "policy": {
    #             "invert_result": true,
    #             "match_list": "list01"
    #         },
    #         "vrfs": [
    #             {
    #                 "name": "vrf01",
    #                 "source_interface": "Ethernet1"
    #             },
    #             {
    #                 "hosts": [
    #                     {
    #                         "name": "24.1.1.1",
    #                         "port": 33
    #                     },
    #                     {
    #                         "name": "hostvrf1",
    #                         "port": 514,
    #                         "protocol": "tcp"
    #                     }
    #                 ],
    #                 "name": "vrf02"
    #             }
    #         ]
    #     },
    #     "changed": true,
    #     "commands": [
    #         "logging host host02 protocol tcp",
    #         "no logging host 11.11.11.1 25",
    #         "no logging host host01 514 protocol tcp",
    #         "logging vrf vrf03 source-interface Vlan100",
    #         "logging vrf vrf04 host hostvrf1 protocol tcp",
    #         "no logging vrf vrf01 source-interface Ethernet1",
    #         "no logging vrf vrf02 host 24.1.1.1 33",
    #         "no logging vrf vrf02 host hostvrf1 514 protocol tcp",
    #         "no logging format timestamp traditional timezone",
    #         "no logging level AAA alerts",
    #         "no logging persistent 4096",
    #         "no logging policy match invert-result match-list list01 discard",
    #         "logging synchronous",
    #         "logging trap critical"
    #     ],
    #
    #

    # Using deleted:

    # Before State:
    # test(config)#show running-config | section logging
    # logging synchronous level critical
    # logging host 11.11.11.1 25
    # logging host host01 514 protocol tcp
    # logging host host02 514 protocol tcp
    # logging vrf vrf02 host 24.1.1.1 33
    # logging vrf vrf02 host hostvrf1 514 protocol tcp
    # logging vrf vrf04 host hostvrf1 514 protocol tcp
    # logging vrf vrf01 source-interface Ethernet1
    # logging vrf vrf03 source-interface Vlan100
    # test(config)#

    - name: Delete all logging configs
      arista.eos.eos_logging_global:
        state: deleted
      become: true

    # After state:
    # test(config)#show running-config | section logging
    # test(config)#
    #
    # "after": {},
    #     "before": {
    #         "hosts": [
    #             {
    #                 "name": "11.11.11.1",
    #                 "port": 25
    #             },
    #             {
    #                 "name": "host01",
    #                 "port": 514,
    #                 "protocol": "tcp"
    #             },
    #             {
    #                 "name": "host02",
    #                 "port": 514,
    #                 "protocol": "tcp"
    #             }
    #         ],
    #         "synchronous": {
    #             "level": "critical"
    #         },
    #         "vrfs": [
    #             {
    #                 "name": "vrf01",
    #                 "source_interface": "Ethernet1"
    #             },
    #             {
    #                 "hosts": [
    #                     {
    #                         "name": "24.1.1.1",
    #                         "port": 33
    #                     },
    #                     {
    #                         "name": "hostvrf1",
    #                         "port": 514,
    #                         "protocol": "tcp"
    #                     }
    #                 ],
    #                 "name": "vrf02"
    #             },
    #             {
    #                 "name": "vrf03",
    #                 "source_interface": "Vlan100"
    #             },
    #             {
    #                 "hosts": [
    #                     {
    #                         "name": "hostvrf1",
    #                         "port": 514,
    #                         "protocol": "tcp"
    #                     }
    #                 ],
    #                 "name": "vrf04"
    #             }
    #         ]
    #     },
    #     "changed": true,
    #     "commands": [
    #         "no logging host 11.11.11.1 25",
    #         "no logging host host01 514 protocol tcp",
    #         "no logging host host02 514 protocol tcp",
    #         "no logging vrf vrf01 source-interface Ethernet1",
    #         "no logging vrf vrf02 host 24.1.1.1 33",
    #         "no logging vrf vrf02 host hostvrf1 514 protocol tcp",
    #         "no logging vrf vrf03 source-interface Vlan100",
    #         "no logging vrf vrf04 host hostvrf1 514 protocol tcp",
    #         "no logging synchronous level critical"
    #     ],

    # Using parsed:
    # parsed.cfg

    # logging host 11.11.11.1 25
    # logging host host01 514 protocol tcp
    # logging vrf vrf02 host 24.1.1.1 33
    # logging vrf vrf02 host hostvrf1 514 protocol tcp
    # logging format timestamp traditional timezone
    # logging vrf vrf01 source-interface Ethernet1
    # logging policy match inverse-result match-list                           list01 discard
    # logging persistent 4096
    # !
    # logging level AAA alerts

    - name: parse configs
      arista.eos.eos_logging_global:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed

    # Module Execution
    # "parsed": {
    #         "format": {
    #             "timestamp": {
    #                 "traditional": {
    #                     "timezone": true
    #                 }
    #             }
    #         },
    #         "hosts": [
    #             {
    #                 "name": "11.11.11.1",
    #                 "port": 25
    #             },
    #             {
    #                 "name": "host01",
    #                 "port": 514,
    #                 "protocol": "tcp"
    #             }
    #         ],
    #         "level": {
    #             "facility": "AAA",
    #             "severity": "alerts"
    #         },
    #         "persistent": {
    #             "size": 4096
    #         },
    #         "policy": {
    #             "invert_result": true,
    #             "match_list": "list01"
    #         },
    #         "vrfs": [
    #             {
    #                 "name": "vrf01",
    #                 "source_interface": "Ethernet1"
    #             },
    #             {
    #                 "hosts": [
    #                     {
    #                         "name": "24.1.1.1",
    #                         "port": 33
    #                     },
    #                     {
    #                         "name": "hostvrf1",
    #                         "port": 514,
    #                         "protocol": "tcp"
    #                     }
    #                 ],
    #                 "name": "vrf02"
    #             }
    #         ]
    #     }
    #

    # Using gathered:
    # Before State:
    # test(config)#show running-config | section logging
    # logging host 11.11.11.1 25
    # logging host host01 514 protocol tcp
    # logging vrf vrf02 host 24.1.1.1 33
    # logging vrf vrf02 host hostvrf1 514 protocol tcp
    # logging format timestamp traditional timezone
    # logging vrf vrf01 source-interface Ethernet1
    # logging policy match inverse-result match-list                           list01 discard
    # logging persistent 4096
    # !
    # logging level AAA alerts
    # test(config)#

    - name: gather configs
      arista.eos.eos_logging_global:
        state: gathered

    # Module Execution:
    # "gathered": {
    #         "format": {
    #             "timestamp": {
    #                 "traditional": {
    #                     "timezone": true
    #                 }
    #             }
    #         },
    #         "hosts": [
    #             {
    #                 "name": "11.11.11.1",
    #                 "port": 25
    #             },
    #             {
    #                 "name": "host01",
    #                 "port": 514,
    #                 "protocol": "tcp"
    #             }
    #         ],
    #         "level": {
    #             "facility": "AAA",
    #             "severity": "alerts"
    #         },
    #         "persistent": {
    #             "size": 4096
    #         },
    #         "policy": {
    #             "invert_result": true,
    #             "match_list": "list01"
    #         },
    #         "vrfs": [
    #             {
    #                 "name": "vrf01",
    #                 "source_interface": "Ethernet1"
    #             },
    #             {
    #                 "hosts": [
    #                     {
    #                         "name": "24.1.1.1",
    #                         "port": 33
    #                     },
    #                     {
    #                         "name": "hostvrf1",
    #                         "port": 514,
    #                         "protocol": "tcp"
    #                     }
    #                 ],
    #                 "name": "vrf02"
    #             }
    #         ]
    #     },
    #

    # Using rendered:
    - name: Render provided configuration
      arista.eos.eos_logging_global:
        config:
          format:
            timestamp:
              traditional:
                timezone: true
          level:
            facility: "AAA"
            severity: "alerts"
          persistent:
            size: 4096
          policy:
            invert_result: true
            match_list: "list01"
          hosts:
            - name: "host01"
              protocol: "tcp"
            - name: "11.11.11.1"
              port: 25
          vrfs:
            - name: "vrf01"
              source_interface: "Ethernet1"
            - name: "vrf02"
              hosts:
                - name: "hostvrf1"
                  protocol: "tcp"
                - name: "24.1.1.1"
                  port: "33"
    # Module Execution:

    # "rendered": [
    #         "logging host host01 protocol tcp",
    #         "logging host 11.11.11.1 25",
    #         "logging vrf vrf01 source-interface Ethernet1",
    #         "logging vrf vrf02 host hostvrf1 protocol tcp",
    #         "logging vrf vrf02 host 24.1.1.1 33",
    #         "logging format timestamp traditional timezone",
    #         "logging level AAA alerts",
    #         "logging persistent 4096",
    #         "logging policy match invert-result match-list list01 discard"
    #     ]
    #




Status
------


Authors
~~~~~~~

- Gomathi Selvi Srinivasan (@GomathiselviS)
