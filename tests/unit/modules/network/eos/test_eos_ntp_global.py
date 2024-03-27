#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.arista.eos.plugins.modules import eos_ntp_global
from ansible_collections.arista.eos.tests.unit.modules.utils import set_module_args

from .eos_module import TestEosModule, load_fixture


class TestEosNtp_GlobalModule(TestEosModule):
    module = eos_ntp_global

    def setUp(self):
        super(TestEosNtp_GlobalModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.arista.eos.plugins.module_utils.network.eos.facts.ntp_global.ntp_global.Ntp_globalFacts.get_config",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestEosNtp_GlobalModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, transport="cli", filename=None):
        if filename is None:
            filename = "eos_ntp_global_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_eos_ntp_global_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    authenticate=dict(enable=True),
                    authentication_keys=[
                        dict(
                            id=2,
                            algorithm="sha1",
                            encryption=7,
                            key="123456",
                        ),
                        dict(
                            id=23,
                            algorithm="md5",
                            encryption=7,
                            key="123456",
                        ),
                    ],
                    local_interface="Ethernet1",
                    qos_dscp=10,
                    trusted_key=23,
                    servers=[
                        dict(
                            server="25.1.1.1",
                            vrf="vrf01",
                            maxpoll=15,
                            key_id=2,
                        ),
                        dict(
                            server="11.21.1.1",
                            vrf="vrf01",
                            minpoll=13,
                            burst=True,
                            prefer=True,
                        ),
                    ],
                    serve=dict(
                        access_lists=[
                            dict(
                                afi="ip",
                                acls=[dict(acl_name="acl01", direction="in")],
                            ),
                            dict(
                                afi="ipv6",
                                acls=[dict(acl_name="acl02", direction="in")],
                            ),
                        ],
                    ),
                ),
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_ntp_global_replaced_idempotent(self):
        set_module_args(
            dict(
                state="replaced",
                config=dict(
                    authenticate=dict(enable=True),
                    authentication_keys=[
                        dict(
                            id=2,
                            algorithm="sha1",
                            encryption=7,
                            key="123456",
                        ),
                        dict(
                            id=23,
                            algorithm="md5",
                            encryption=7,
                            key="123456",
                        ),
                    ],
                    local_interface="Ethernet1",
                    qos_dscp=10,
                    trusted_key=23,
                    servers=[
                        dict(
                            server="25.1.1.1",
                            vrf="vrf01",
                            maxpoll=15,
                            key_id=2,
                        ),
                        dict(
                            server="11.21.1.1",
                            vrf="vrf01",
                            minpoll=13,
                            burst=True,
                            prefer=True,
                        ),
                    ],
                    serve=dict(
                        access_lists=[
                            dict(
                                afi="ip",
                                acls=[dict(acl_name="acl01", direction="in")],
                            ),
                            dict(
                                afi="ipv6",
                                acls=[dict(acl_name="acl02", direction="in")],
                            ),
                        ],
                    ),
                ),
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_ntp_global_overridden_idempotent(self):
        set_module_args(
            dict(
                state="overridden",
                config=dict(
                    authenticate=dict(enable=True),
                    authentication_keys=[
                        dict(
                            id=2,
                            algorithm="sha1",
                            encryption=7,
                            key="123456",
                        ),
                        dict(
                            id=23,
                            algorithm="md5",
                            encryption=7,
                            key="123456",
                        ),
                    ],
                    local_interface="Ethernet1",
                    qos_dscp=10,
                    trusted_key=23,
                    servers=[
                        dict(
                            server="25.1.1.1",
                            vrf="vrf01",
                            maxpoll=15,
                            key_id=2,
                        ),
                        dict(
                            server="11.21.1.1",
                            vrf="vrf01",
                            minpoll=13,
                            burst=True,
                            prefer=True,
                        ),
                    ],
                    serve=dict(
                        access_lists=[
                            dict(
                                afi="ip",
                                acls=[dict(acl_name="acl01", direction="in")],
                            ),
                            dict(
                                afi="ipv6",
                                acls=[dict(acl_name="acl02", direction="in")],
                            ),
                        ],
                    ),
                ),
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_ntp_global_merged(self):
        set_module_args(
            dict(
                config=dict(
                    authentication_keys=[
                        dict(
                            id=4,
                            algorithm="sha1",
                            encryption=0,
                            key="123456",
                        ),
                    ],
                    qos_dscp=15,
                    servers=[
                        dict(
                            server="110.21.1.1",
                            version=3,
                            iburst=True,
                            source="vlan500",
                        ),
                        dict(
                            server="110.22.2.2",
                            local_interface="Management1",
                        ),
                    ],
                    serve=dict(
                        access_lists=[
                            dict(
                                afi="ip",
                                acls=[dict(acl_name="acl03", direction="in")],
                            ),
                        ],
                    ),
                ),
            ),
        )
        commands = [
            "ntp serve ip access-group acl03 in",
            "ntp authentication-key 4 sha1 0 123456",
            "ntp server 110.21.1.1 iburst source Vlan500 version 3",
            "ntp server 110.22.2.2 local-interface Management1",
            "ntp qos dscp 15",
        ]
        self.execute_module(changed=True, commands=sorted(commands))

    def test_eos_ntp_global_merged_authenate(self):
        set_module_args(
            dict(
                config=dict(
                    authenticate=dict(
                        enable=False,
                        servers=False,
                    ),
                ),
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_ntp_global_merged_authenate_server_true(self):
        set_module_args(
            dict(
                config=dict(
                    authenticate=dict(
                        enable=False,
                        servers=True,
                    ),
                ),
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_eos_ntp_global_replaced(self):
        set_module_args(
            dict(
                state="replaced",
                config=dict(
                    authentication_keys=[
                        dict(
                            id=4,
                            algorithm="sha1",
                            encryption=0,
                            key="123456",
                        ),
                    ],
                    qos_dscp=15,
                    servers=[
                        dict(server="110.21.1.1", version=3, iburst=True),
                    ],
                    serve=dict(
                        access_lists=[
                            dict(
                                afi="ip",
                                acls=[dict(acl_name="acl03", direction="in")],
                            ),
                        ],
                    ),
                ),
            ),
        )
        commands = [
            "no ntp serve ip access-group acl01 in",
            "no ntp serve ipv6 access-group acl02 in",
            "no ntp authentication-key 2 sha1 7 123456",
            "no ntp authentication-key 23 md5 7 123456",
            "no ntp server vrf vrf01 11.21.1.1 burst minpoll 13 prefer",
            "no ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
            "no ntp authenticate",
            "no ntp local-interface Ethernet1",
            "no ntp trusted-key 23",
            "ntp serve ip access-group acl03 in",
            "ntp authentication-key 4 sha1 0 123456",
            "ntp server 110.21.1.1 iburst version 3",
            "ntp qos dscp 15",
        ]
        self.execute_module(changed=True, commands=sorted(commands))

    def test_eos_ntp_global_overridden(self):
        set_module_args(
            dict(
                state="overridden",
                config=dict(
                    authentication_keys=[
                        dict(
                            id=4,
                            algorithm="sha1",
                            encryption=0,
                            key="123456",
                        ),
                    ],
                    qos_dscp=15,
                    local_interface="Vlan100",
                    servers=[
                        dict(server="110.21.1.1", version=3, iburst=True),
                    ],
                    serve=dict(
                        access_lists=[
                            dict(
                                afi="ip",
                                acls=[dict(acl_name="acl03", direction="in")],
                            ),
                        ],
                    ),
                ),
            ),
        )
        commands = [
            "no ntp serve ip access-group acl01 in",
            "no ntp serve ipv6 access-group acl02 in",
            "no ntp authentication-key 2 sha1 7 123456",
            "no ntp authentication-key 23 md5 7 123456",
            "no ntp server vrf vrf01 11.21.1.1 burst minpoll 13 prefer",
            "no ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
            "no ntp authenticate",
            "no ntp trusted-key 23",
            "ntp serve ip access-group acl03 in",
            "ntp local-interface Vlan100",
            "ntp authentication-key 4 sha1 0 123456",
            "ntp server 110.21.1.1 iburst version 3",
            "ntp qos dscp 15",
        ]
        self.execute_module(changed=True, commands=sorted(commands))

    def test_eos_ntp_global_deleted(self):
        set_module_args(dict(state="deleted"))
        commands = [
            "no ntp serve ip access-group acl01 in",
            "no ntp serve ipv6 access-group acl02 in",
            "no ntp authentication-key 2 sha1 7 123456",
            "no ntp authentication-key 23 md5 7 123456",
            "no ntp server vrf vrf01 11.21.1.1 burst minpoll 13 prefer",
            "no ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
            "no ntp authenticate",
            "no ntp local-interface Ethernet1",
            "no ntp trusted-key 23",
            "no ntp qos dscp 10",
        ]
        self.execute_module(changed=True, commands=sorted(commands))

    def test_eos_ntp_global_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(
            changed=False,
            filename="eos_ntp_global_config.cfg",
        )
        gathered_list = {
            "authenticate": {"enable": True},
            "authentication_keys": [
                {
                    "algorithm": "sha1",
                    "encryption": 7,
                    "id": 2,
                    "key": "123456",
                },
                {
                    "algorithm": "md5",
                    "encryption": 7,
                    "id": 23,
                    "key": "123456",
                },
            ],
            "local_interface": "Ethernet1",
            "qos_dscp": 10,
            "serve": {
                "access_lists": [
                    {
                        "acls": [{"acl_name": "acl01", "direction": "in"}],
                        "afi": "ip",
                    },
                    {
                        "acls": [{"acl_name": "acl02", "direction": "in"}],
                        "afi": "ipv6",
                    },
                ],
            },
            "servers": [
                {
                    "burst": True,
                    "minpoll": 13,
                    "prefer": True,
                    "server": "11.21.1.1",
                    "vrf": "vrf01",
                },
                {
                    "key_id": 2,
                    "maxpoll": 15,
                    "server": "25.1.1.1",
                    "vrf": "vrf01",
                },
            ],
            "trusted_key": "23",
        }
        self.assertEqual(sorted(gathered_list), sorted(result["gathered"]))

    def test_eos_ntp_global_parsed(self):
        commands = [
            "ntp authentication-key 2 sha1 7 123456",
            "ntp authentication-key 23 md5 7 123456",
            "ntp trusted-key 23",
            "ntp authenticate",
            "ntp local-interface Ethernet1",
            "ntp qos dscp 10",
            "ntp server vrf vrf01 11.21.1.1 prefer burst minpoll 13",
            "ntp server vrf vrf01 25.1.1.1 maxpoll 15 key 2",
            "ntp serve ip access-group acl01 in",
            "ntp serve ipv6 access-group acl02 in",
        ]
        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {
            "authenticate": {"enable": True},
            "authentication_keys": [
                {
                    "algorithm": "sha1",
                    "encryption": 7,
                    "id": 2,
                    "key": "123456",
                },
                {
                    "algorithm": "md5",
                    "encryption": 7,
                    "id": 23,
                    "key": "123456",
                },
            ],
            "local_interface": "Ethernet1",
            "qos_dscp": 10,
            "serve": {
                "access_lists": [
                    {
                        "acls": [{"acl_name": "acl01", "direction": "in"}],
                        "afi": "ip",
                    },
                    {
                        "acls": [{"acl_name": "acl02", "direction": "in"}],
                        "afi": "ipv6",
                    },
                ],
            },
            "servers": [
                {
                    "burst": True,
                    "minpoll": 13,
                    "prefer": True,
                    "server": "11.21.1.1",
                    "vrf": "vrf01",
                },
                {
                    "key_id": 2,
                    "maxpoll": 15,
                    "server": "25.1.1.1",
                    "vrf": "vrf01",
                },
            ],
            "trusted_key": "23",
        }
        self.assertEqual(sorted(parsed_list), sorted(result["parsed"]))

    def test_eos_ntp_global_rendered(self):
        set_module_args(
            dict(
                state="rendered",
                config=dict(
                    authenticate=dict(enable=True),
                    authentication_keys=[
                        dict(
                            id=2,
                            algorithm="sha1",
                            encryption=7,
                            key="123456",
                        ),
                        dict(
                            id=23,
                            algorithm="md5",
                            encryption=7,
                            key="123456",
                        ),
                    ],
                    local_interface="Ethernet1",
                    qos_dscp=10,
                    trusted_key=23,
                    servers=[
                        dict(
                            server="25.1.1.1",
                            vrf="vrf01",
                            maxpoll=15,
                            key_id=2,
                        ),
                        dict(
                            server="11.21.1.1",
                            vrf="vrf01",
                            minpoll=13,
                            burst=True,
                            prefer=True,
                        ),
                    ],
                    serve=dict(
                        access_lists=[
                            dict(
                                afi="ip",
                                acls=[dict(acl_name="acl01", direction="in")],
                            ),
                            dict(
                                afi="ipv6",
                                acls=[dict(acl_name="acl02", direction="in")],
                            ),
                        ],
                    ),
                ),
            ),
        )
        commands = [
            "ntp authentication-key 2 sha1 7 123456",
            "ntp authentication-key 23 md5 7 123456",
            "ntp trusted-key 23",
            "ntp authenticate",
            "ntp local-interface Ethernet1",
            "ntp qos dscp 10",
            "ntp server vrf vrf01 11.21.1.1 burst minpoll 13 prefer",
            "ntp server vrf vrf01 25.1.1.1 key 2 maxpoll 15",
            "ntp serve ip access-group acl01 in",
            "ntp serve ipv6 access-group acl02 in",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(commands),
            result["rendered"],
        )
