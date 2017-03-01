Network Essentials Actions
==========================

This is a reference documentation for Network Essentials Actions and Workflows to automate Brocade VDX and SLX switches. These actions can be used as independent actions, or as part of a more complex workflow. :doc:`Actions</actions>` can be manually triggered, or they can be tied to :doc:`sensors </sensors>` using rules.

.. contents::
   :local:
   :depth: 1

Most of the actions below can be used to automate Brocade SLX or VDX switches, however there are few actions that are only valid for  VDX switches as outlined below. If an action is only valid for VDX it will be documented in the action details, otherwise the action is supported for both VDX and SLX.  

Edge Ports Configuration
------------------------

.. include:: /_includes/solutions/essentials/create_l2_port_channel.rst

.. include:: /_includes/solutions/essentials/autopick_port_channel_id.rst

.. include:: /_includes/solutions/essentials/create_vlan.rst

.. include:: /_includes/solutions/essentials/create_switchport_access.rst

.. include:: /_includes/solutions/essentials/create_switchport_trunk.rst

.. include:: /_includes/solutions/essentials/create_ve.rst

.. include:: /_includes/solutions/essentials/create_vrf.rst

.. include:: /_includes/solutions/essentials/create_vrrpe.rst

.. include:: /_includes/solutions/essentials/delete_l2_port_channel.rst

.. include:: /_includes/solutions/essentials/delete_ve.rst

.. include:: /_includes/solutions/essentials/delete_vlan.rst

.. include:: /_includes/solutions/essentials/delete_vrf.rst

.. include:: /_includes/solutions/essentials/delete_vrrpe.rst

.. include:: /_includes/solutions/essentials/set_intf_admin_state.rst

.. include:: /_includes/solutions/essentials/set_l2_mtu.rst

.. include:: /_includes/solutions/essentials/set_l3_mtu.rst

.. include:: /_includes/solutions/essentials/configure_mac_move_detection.rst

ACL Management
---------------

.. include:: /_includes/solutions/essentials/create_acl.rst

.. include:: /_includes/solutions/essentials/delete_acl.rst

.. include:: /_includes/solutions/essentials/add_ipv4_rule_acl.rst

.. include:: /_includes/solutions/essentials/add_ipv6_rule_acl.rst

.. include:: /_includes/solutions/essentials/add_or_remove_l2_acl_rule.rst

.. include:: /_includes/solutions/essentials/delete_ipv4_rule_acl.rst

.. include:: /_includes/solutions/essentials/apply_acl.rst

.. include:: /_includes/solutions/essentials/remove_acl.rst

Validation and Troubleshooting
------------------------------

.. include:: /_includes/solutions/essentials/find_host_ip.rst

.. include:: /_includes/solutions/essentials/find_mac.rst

.. include:: /_includes/solutions/essentials/ping_vrf_targets.rst

.. include:: /_includes/solutions/essentials/validate_L2_port_channel_state.rst

.. include:: /_includes/solutions/essentials/validate_interface_state.rst

.. include:: /_includes/solutions/essentials/validate_interface_vlan.rst

.. include:: /_includes/solutions/essentials/validate_vrrpe_state.rst


Utility Actions
---------------

.. include:: /_includes/solutions/essentials/execute_cli.rst

.. include:: /_includes/solutions/essentials/get_os_version.rst

.. include:: /_includes/solutions/essentials/get_switch_details.rst


VCS Specific Actions
--------------------

.. include:: /_includes/solutions/essentials/set_l2_system_mtu.rst

.. include:: /_includes/solutions/essentials/set_l3_system_mtu.rst

.. include:: /_includes/solutions/essentials/configure_mgmt_virtual_ip.rst

.. include:: /_includes/solutions/essentials/find_my_host_vcs.rst

Known Issues
------------
This section includes the known issues in Network Essentials 1.0.0 release.  Common issues are listed in the beginning of the section and the issues specific to a particular network device platform are organized under the corresponding platform sub-section.

1. ID:277 remove_acl fails with an unknown error on port_channel interfaces
2. ID:312 set_l3_mtu returns success when setting the MTU size back to default value but the switch is not configured with the default MTU size.
3. ID:300 set_l2_mtu returns success when setting the MTU size back to default value but the switch is not configured with the default MTU size.

SLX:
~~~~
4. ID:314 set_l3_mtu not supported on VE interface.
5. ID:309 validate_interface_state not supported on VE interface.
6. ID:308 create_ve times out on SLX.
7. ID:311 ping_vrf_targets is not supported on SLX.

VDX:
~~~~
8. ID:303 validate_interface_vlan doesn’t validate GVLANs i.e. VLANs with ID over 4K.
