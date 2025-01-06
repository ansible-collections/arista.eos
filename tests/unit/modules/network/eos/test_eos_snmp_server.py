#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.arista.eos.plugins.modules import eos_snmp_server
from ansible_collections.arista.eos.tests.unit.modules.utils import set_module_args

from .eos_module import TestEosModule, load_fixture


class TestEosSnmp_ServerModule(TestEosModule):
    module = eos_snmp_server

    def setUp(self):
        super(TestEosSnmp_ServerModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.arista.eos.plugins.module_utils.network.eos.facts.snmp_server.snmp_server.Snmp_serverFacts.get_config",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestEosSnmp_ServerModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, transport="cli", filename=None):
        if filename is None:
            filename = "eos_snmp_server_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_eos_snmp_server_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(name="comm3", acl_v6="list1", view="view1"),
                        dict(
                            name="comm4",
                            acl_v4="list3",
                            view="view1",
                            ro=True,
                        ),
                        dict(name="comm5", acl_v4="list4"),
                    ],
                    contact="admin",
                    vrfs=[dict(vrf="vrf01", local_interface="Ethernet1")],
                    groups=[
                        dict(group="group1", version="v1", read="view1"),
                        dict(
                            group="group2",
                            version="v3",
                            auth_privacy="priv",
                            notify="view1",
                            write="view2",
                        ),
                    ],
                    hosts=[
                        dict(
                            host="host01",
                            version="3 priv",
                            user="user01",
                            udp_port=23,
                        ),
                        dict(
                            host="host02",
                            version="2c",
                            user="user01",
                            udp_port=23,
                        ),
                    ],
                    traps=dict(
                        bgp=dict(enabled=True),
                        capacity=dict(arista_hardware_utilization_alert=True),
                        external_alarm=dict(
                            arista_external_alarm_deasserted_notif=True,
                            arista_external_alarm_asserted_notif=True,
                        ),
                    ),
                ),
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_snmp_server_merged(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(
                            name="comm01",
                            acl_v6="list1",
                            view="view3",
                            ro=True,
                        ),
                        dict(name="comm6", rw=True),
                    ],
                    engineid=dict(
                        local="123456",
                        remote=dict(host="1.1.1.1", udp_port=23, id="abc123"),
                    ),
                    extension=dict(
                        root_oid="123456",
                        script_location="flash:",
                        oneshot=True,
                    ),
                    hosts=[
                        dict(
                            host="host01",
                            version="3 priv",
                            user="user01",
                            udp_port=23,
                            informs=True,
                        ),
                        dict(
                            host="host02",
                            version="2c",
                            user="user01",
                            udp_port=23,
                            traps=True,
                        ),
                        dict(
                            host="host01",
                            version="3 priv",
                            user="user01",
                            informs=True,
                        ),
                    ],
                    acls=[dict(afi="ipv4", acl="acl01", vrf="vrf01")],
                ),
            ),
        )

        commands = [
            "snmp-server host host01 informs version 3 priv user01 udp-port 23",
            "snmp-server host host02 traps version 2c user01 udp-port 23",
            "snmp-server host host01 informs version 3 priv user01",
            "snmp-server community comm6 rw",
            "snmp-server community comm01 view view3 ro ipv6 list1",
            "snmp-server ipv4 access-list acl01 vrf vrf01",
            "snmp-server engineID local 123456",
            "snmp-server engineID remote 1.1.1.1 udp-port 23 abc123",
            "snmp-server extension 123456 flash: one-shot",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_snmp_server_replaced_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(name="comm3", acl_v6="list1", view="view1"),
                        dict(
                            name="comm4",
                            acl_v4="list3",
                            view="view1",
                            ro=True,
                        ),
                        dict(name="comm5", acl_v4="list4"),
                    ],
                    contact="admin",
                    vrfs=[dict(vrf="vrf01", local_interface="Ethernet1")],
                    groups=[
                        dict(group="group1", version="v1", read="view1"),
                        dict(
                            group="group2",
                            version="v3",
                            auth_privacy="priv",
                            notify="view1",
                            write="view2",
                        ),
                    ],
                    hosts=[
                        dict(
                            host="host01",
                            version="3 priv",
                            user="user01",
                            udp_port=23,
                        ),
                        dict(
                            host="host02",
                            version="2c",
                            user="user01",
                            udp_port=23,
                        ),
                    ],
                    traps=dict(
                        bgp=dict(enabled=True),
                        capacity=dict(arista_hardware_utilization_alert=True),
                        external_alarm=dict(
                            arista_external_alarm_deasserted_notif=True,
                            arista_external_alarm_asserted_notif=True,
                        ),
                    ),
                ),
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_snmp_server_overridden_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(name="comm3", acl_v6="list1", view="view1"),
                        dict(
                            name="comm4",
                            acl_v4="list3",
                            view="view1",
                            ro=True,
                        ),
                        dict(name="comm5", acl_v4="list4"),
                    ],
                    contact="admin",
                    vrfs=[dict(vrf="vrf01", local_interface="Ethernet1")],
                    groups=[
                        dict(group="group1", version="v1", read="view1"),
                        dict(
                            group="group2",
                            version="v3",
                            auth_privacy="priv",
                            notify="view1",
                            write="view2",
                        ),
                    ],
                    hosts=[
                        dict(
                            host="host01",
                            version="3 priv",
                            user="user01",
                            udp_port=23,
                        ),
                        dict(
                            host="host02",
                            version="2c",
                            user="user01",
                            udp_port=23,
                        ),
                    ],
                    traps=dict(
                        bgp=dict(enabled=True),
                        capacity=dict(arista_hardware_utilization_alert=True),
                        external_alarm=dict(
                            arista_external_alarm_deasserted_notif=True,
                            arista_external_alarm_asserted_notif=True,
                        ),
                    ),
                ),
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_snmp_server_merged_traps(self):
        set_module_args(
            dict(
                config=dict(
                    traps=dict(
                        bgp=dict(
                            arista_backward_transition=True,
                            arista_established=True,
                            backward_transition=True,
                            established=True,
                        ),
                        vrrp=dict(trap_new_master=True),
                        test=dict(arista_test_notification=True),
                        switchover=dict(
                            arista_redundancy_switch_over_notif=True,
                        ),
                        snmpConfigManEvent=dict(arista_config_man_event=True),
                        snmp=dict(
                            authentication=True,
                            link_down=True,
                            link_up=True,
                        ),
                        pim=dict(neighbor_loss=True),
                        ospfv3=dict(
                            if_config_error=True,
                            if_rx_bad_packet=True,
                            if_state_change=True,
                            nbr_state_change=True,
                            nbr_restart_helper_status_change=True,
                            nssa_translator_status_change=True,
                            restart_status_change=True,
                        ),
                        ospf=dict(
                            if_config_error=True,
                            if_auth_failure=True,
                            if_state_change=True,
                            nbr_state_change=True,
                        ),
                        msdp=dict(backward_transition=True, established=True),
                        mpls_ldp=dict(
                            mpls_ldp_session_down=True,
                            mpls_ldp_session_up=True,
                        ),
                        lldp=dict(rem_tables_change=True),
                        isis=dict(
                            adjacency_change=True,
                            area_mismatch=True,
                            attempt_to_exceed_max_sequence=True,
                            authentication_type_failure=True,
                            database_overload=True,
                            own_lsp_purge=True,
                            rejected_adjacency=True,
                            sequence_number_skip=True,
                        ),
                        external_alarm=dict(
                            arista_external_alarm_asserted_notif=True,
                            arista_external_alarm_deasserted_notif=True,
                        ),
                        entity=dict(
                            arista_ent_sensor_alarm=True,
                            ent_config_change=True,
                            ent_state_oper=True,
                            ent_state_oper_disabled=True,
                            ent_state_oper_enabled=True,
                        ),
                        capacity=dict(arista_hardware_utilization_alert=True),
                        bridge=dict(
                            arista_mac_age=True,
                            arista_mac_learn=True,
                            arista_mac_move=True,
                        ),
                    ),
                ),
            ),
        )
        commands = [
            "snmp-server enable traps bgp arista-backward-transition arista-established backward-transition established",
            "snmp-server enable traps bridge arista-mac-age arista-mac-learn arista-mac-move",
            "snmp-server enable traps entity arista-ent-sensor-alarm ent-config-change ent-state-oper ent-state-oper-disabled ent-state-oper-enabled",
            "snmp-server enable traps isis adjacency-change area-mismatch attempt-to-exceed-max-sequence authentication-type-failure database-overload own-lsp-purge rejected-adjacency sequence-number-skip",  # noqa: E501
            "snmp-server enable traps lldp rem-tables-change",
            "snmp-server enable traps mpls-ldp mpls-ldp-session-down mpls-ldp-session-up",
            "snmp-server enable traps msdp backward-transition established",
            "snmp-server enable traps ospf if-auth-failure if-config-error if-state-change nbr-state-change",
            "snmp-server enable traps ospfv3 if-config-error if-rx-bad-packet if-state-change nbr-state-change nbr-restart-helper-status-change nssa-translator-status-change restart-status-change",  # noqa: E501
            "snmp-server enable traps pim neighbor-loss",
            "snmp-server enable traps snmp authentication link-down link-up",
            "snmp-server enable traps snmpConfigManEvent arista-config-man-event",
            "snmp-server enable traps switchover arista-redundancy-switch-over-notif",
            "snmp-server enable traps test arista-test-notification",
            "snmp-server enable traps vrrp trap-new-master",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_eos_snmp_server_overridden(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(name="replacecomm", acl_v6="list4", rw=True),
                    ],
                    chassis_id="123456",
                    vrfs=[dict(vrf="replacevrf")],
                    users=[
                        dict(
                            user="user01",
                            group="grp01",
                            remote="1.1.1.1",
                            version="v3",
                            auth=dict(
                                algorithm="md5",
                                auth_passphrase="password123",
                                encryption="aes",
                                priv_passphrase="abcdef",
                            ),
                            udp_port=100,
                        ),
                    ],
                ),
                state="overridden",
            ),
        )
        commands = [
            "snmp-server community replacecomm rw ipv6 list4",
            "no snmp-server community comm3 view view1 ipv6 list1",
            "no snmp-server community comm4 view view1 ro list3",
            "no snmp-server community comm5 list4",
            "no snmp-server group group1 v1 read view1",
            "no snmp-server group group2 v3 priv write view2 notify view1",
            "no snmp-server host host01 version 3 priv user01 udp-port 23",
            "no snmp-server host host02 version 2c user01 udp-port 23",
            "snmp-server user user01 grp01 remote 1.1.1.1 udp-port 100 v3 auth md5 password123 priv aes abcdef",
            "no snmp-server vrf vrf01 local-interface Ethernet1",
            "snmp-server vrf replacevrf",
            "snmp-server chassis-id 123456",
            "no snmp-server contact admin",
            "default snmp-server enable traps bgp",
            "default snmp-server enable traps capacity arista-hardware-utilization-alert",
            "default snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_eos_snmp_server_replaced(self):
        set_module_args(
            dict(
                config=dict(
                    users=[
                        dict(
                            user="user01",
                            group="grp01",
                            remote="1.1.1.1",
                            version="v3",
                            localized=dict(
                                engineid="abcdef",
                                algorithm="md5",
                                auth_passphrase="password123",
                                encryption="aes",
                                priv_passphrase="abcdef",
                            ),
                            udp_port=100,
                        ),
                    ],
                    views=[dict(view="view1", mib="mib1", action="excluded")],
                    transport="tcp",
                    transmit=25,
                    qosmib=41,
                    qos=20,
                    objects=dict(route_tables=True),
                ),
                state="replaced",
            ),
        )
        commands = [
            "no snmp-server community comm3 view view1 ipv6 list1",
            "no snmp-server community comm4 view view1 ro list3",
            "no snmp-server community comm5 list4",
            "no snmp-server group group1 v1 read view1",
            "no snmp-server group group2 v3 priv write view2 notify view1",
            "no snmp-server host host01 version 3 priv user01 udp-port 23",
            "no snmp-server host host02 version 2c user01 udp-port 23",
            "snmp-server user user01 grp01 remote 1.1.1.1 udp-port 100 v3 localized abcdef auth md5 password123 priv aes abcdef",
            "snmp-server view view1 mib1 excluded",
            "no snmp-server vrf vrf01 local-interface Ethernet1",
            "snmp-server transport tcp",
            "snmp-server transmit max-size 25",
            "snmp-server qosmib counter-interval 41",
            "snmp-server qos dscp 20",
            "snmp-server objects mac-address-tables disable",
            "snmp-server objects route-tables disable",
            "no snmp-server contact admin",
            "default snmp-server enable traps bgp",
            "default snmp-server enable traps capacity arista-hardware-utilization-alert",
            "default snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_eos_snmp_server_deleted(self):
        set_module_args(dict(state="deleted"))
        commands = [
            "no snmp-server community comm3 view view1 ipv6 list1",
            "no snmp-server community comm4 view view1 ro list3",
            "no snmp-server community comm5 list4",
            "no snmp-server group group1 v1 read view1",
            "no snmp-server group group2 v3 priv write view2 notify view1",
            "no snmp-server host host01 version 3 priv user01 udp-port 23",
            "no snmp-server host host02 version 2c user01 udp-port 23",
            "no snmp-server contact admin",
            "no snmp-server vrf vrf01 local-interface Ethernet1",
            "default snmp-server enable traps bgp",
            "default snmp-server enable traps capacity arista-hardware-utilization-alert",
            "default snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_eos_snmp_server_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(
            changed=False,
            filename="eos_snmp_server_config.cfg",
        )
        gathered_list = {
            "communities": [
                {"acl_v6": "list1", "name": "comm3", "view": "view1"},
                {
                    "acl_v4": "list3",
                    "name": "comm4",
                    "ro": True,
                    "view": "view1",
                },
                {"acl_v4": "list4", "name": "comm5"},
            ],
            "contact": "admin",
            "groups": [
                {"group": "group1", "read": "view1", "version": "v1"},
                {
                    "auth_privacy": "priv",
                    "group": "group2",
                    "notify": "view1",
                    "version": "v3",
                    "write": "view2",
                },
            ],
            "hosts": [
                {
                    "host": "host01",
                    "udp_port": 23,
                    "user": "user01",
                    "version": "3 priv",
                },
                {
                    "host": "host02",
                    "udp_port": 23,
                    "user": "user01",
                    "version": "2c",
                },
            ],
            "traps": {
                "bgp": {"enabled": True},
                "capacity": {"arista_hardware_utilization_alert": True},
                "external_alarm": {
                    "arista_external_alarm_asserted_notif": True,
                    "arista_external_alarm_deasserted_notif": True,
                },
            },
            "vrfs": [{"local_interface": "Ethernet1", "vrf": "vrf01"}],
        }
        self.assertEqual(sorted(gathered_list), sorted(result["gathered"]))

    def test_eos_logging_global_parsed(self):
        commands = [
            "snmp-server contact admin",
            "snmp-server vrf vrf01 local-interface Ethernet1",
            "snmp-server community comm3 view view1 ipv6 list1",
            "snmp-server community comm4 view view1 ro list3",
            "snmp-server community comm5 list4",
            "snmp-server group group1 v1 read view1",
            "snmp-server group group2 v3 priv write view2 notify view1",
            "snmp-server host host01 version 3 priv user01 udp-port 23",
            "snmp-server host host02 version 2c user01 udp-port 23",
            "snmp-server enable traps bgp",
            "snmp-server enable traps capacity arista-hardware-utilization-alert",
            "snmp-server enable traps external-alarm arista-external-alarm-asserted-notif",
            "snmp-server enable traps external-alarm arista-external-alarm-deasserted-notif",
        ]
        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {
            "communities": [
                {"acl_v6": "list1", "name": "comm3", "view": "view1"},
                {
                    "acl_v4": "list3",
                    "name": "comm4",
                    "ro": True,
                    "view": "view1",
                },
                {"acl_v4": "list4", "name": "comm5"},
            ],
            "contact": "admin",
            "groups": [
                {"group": "group1", "read": "view1", "version": "v1"},
                {
                    "auth_privacy": "priv",
                    "group": "group2",
                    "notify": "view1",
                    "version": "v3",
                    "write": "view2",
                },
            ],
            "hosts": [
                {
                    "host": "host01",
                    "udp_port": 23,
                    "user": "user01",
                    "version": "3 priv",
                },
                {
                    "host": "host02",
                    "udp_port": 23,
                    "user": "user01",
                    "version": "2c",
                },
            ],
            "traps": {
                "bgp": {"enabled": True},
                "capacity": {"arista_hardware_utilization_alert": True},
                "external_alarm": {
                    "arista_external_alarm_asserted_notif": True,
                    "arista_external_alarm_deasserted_notif": True,
                },
            },
            "vrfs": [{"local_interface": "Ethernet1", "vrf": "vrf01"}],
        }
        self.assertEqual(sorted(parsed_list), sorted(result["parsed"]))

    def test_eos_logging_global_rendered(self):
        set_module_args(
            dict(
                state="rendered",
                config=dict(
                    communities=[
                        dict(name="comm3", acl_v6="list1", view="view1"),
                        dict(
                            name="comm4",
                            acl_v4="list3",
                            view="view1",
                            ro=True,
                        ),
                        dict(name="comm5", acl_v4="list4"),
                    ],
                    contact="admin",
                    vrfs=[dict(vrf="vrf01", local_interface="Ethernet1")],
                    groups=[
                        dict(group="group1", version="v1", read="view1"),
                        dict(
                            group="group2",
                            version="v3",
                            auth_privacy="priv",
                            notify="view1",
                            write="view2",
                        ),
                    ],
                    hosts=[
                        dict(
                            host="host01",
                            version="3 priv",
                            user="user01",
                            udp_port=23,
                        ),
                        dict(
                            host="host02",
                            version="2c",
                            user="user01",
                            udp_port=23,
                        ),
                    ],
                    traps=dict(
                        bgp=dict(enabled=True),
                        capacity=dict(arista_hardware_utilization_alert=True),
                        external_alarm=dict(
                            arista_external_alarm_deasserted_notif=True,
                            arista_external_alarm_asserted_notif=True,
                        ),
                    ),
                ),
            ),
        )
        commands = [
            "snmp-server contact admin",
            "snmp-server vrf vrf01 local-interface Ethernet1",
            "snmp-server community comm3 view view1 ipv6 list1",
            "snmp-server community comm4 view view1 ro list3",
            "snmp-server community comm5 list4",
            "snmp-server group group1 v1 read view1",
            "snmp-server group group2 v3 priv write view2 notify view1",
            "snmp-server host host01 version 3 priv user01 udp-port 23",
            "snmp-server host host02 version 2c user01 udp-port 23",
            "snmp-server enable traps bgp",
            "snmp-server enable traps capacity arista-hardware-utilization-alert",
            "snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(commands),
            result["rendered"],
        )
