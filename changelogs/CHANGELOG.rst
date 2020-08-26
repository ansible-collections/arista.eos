===================================
Arista Eos Collection Release Notes
===================================

.. contents:: Topics


v1.0.3
======

Bugfixes
--------

- Added error pattern to the terminal plugin to handle change mode error seen in lag interfaces config.

v1.0.2
======

Release Summary
---------------

- rereleasing 1.0.1 with updated changelog.

v1.0.1
======

Minor Changes
-------------

- Add round trip testcases to the 2.9 resource modules.
- Add unit testcases to the eos_l3_interfaces resource modules.
- Add unit testcases to the eos_lag_interfaces resource modules.
- Sorted the list of params of ip address before forming the tuple.
- Updated docs.

Bugfixes
--------

- Fixes mismatch in documentation and code for using eos_lag_interfaces where the code required 'Port-Channel\d.*:' but the docs did not document this. The module now supports both 'Port-Channel\d.*:' and '\d.*:'.
- Make `src`, `backup` and `backup_options` in eos_config work when module alias is used (https://github.com/ansible-collections/arista.eos/pull/85).

v1.0.0
======

New Plugins
-----------

Cliconf
~~~~~~~

- eos - Use eos cliconf to run command on Arista EOS platform

Httpapi
~~~~~~~

- eos - Use eAPI to run command on eos platform

New Modules
-----------

- eos_acl_interfaces - ACL interfaces resource module
- eos_acls - ACLs resource module
- eos_banner - Manage multiline banners on Arista EOS devices
- eos_bgp - Configure global BGP protocol settings on Arista EOS.
- eos_command - Run arbitrary commands on an Arista EOS device
- eos_config - Manage Arista EOS configuration sections
- eos_eapi - Manage and configure Arista EOS eAPI.
- eos_facts - Collect facts from remote devices running Arista EOS
- eos_interface - (deprecated, removed after 2022-06-01) Manage Interface on Arista EOS network devices
- eos_interfaces - Interfaces resource module
- eos_l2_interface - (deprecated, removed after 2022-06-01) Manage L2 interfaces on Arista EOS network devices.
- eos_l2_interfaces - L2 interfaces resource module
- eos_l3_interface - (deprecated, removed after 2022-06-01) Manage L3 interfaces on Arista EOS network devices.
- eos_l3_interfaces - L3 interfaces resource module
- eos_lacp - LACP resource module
- eos_lacp_interfaces - LACP interfaces resource module
- eos_lag_interfaces - LAG interfaces resource module
- eos_linkagg - (deprecated, removed after 2022-06-01) Manage link aggregation groups on Arista EOS network devices
- eos_lldp - Manage LLDP configuration on Arista EOS network devices
- eos_lldp_global - LLDP resource module
- eos_lldp_interfaces - LLDP interfaces resource module
- eos_logging - Manage logging on network devices
- eos_ospfv2 - OSPFv2 resource module
- eos_static_route - (deprecated, removed after 2022-06-01) Manage static IP routes on Arista EOS network devices
- eos_static_routes - Static routes resource module
- eos_system - Manage the system attributes on Arista EOS devices
- eos_user - Manage the collection of local users on EOS devices
- eos_vlan - (deprecated, removed after 2022-06-01) Manage VLANs on Arista EOS network devices
- eos_vlans - VLANs resource module
- eos_vrf - Manage VRFs on Arista EOS network devices
