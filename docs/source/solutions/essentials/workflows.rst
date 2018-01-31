Network Essentials Actions
==========================

This is a reference documentation for Network Essentials Actions and Workflows to automate VDX and
SLX switches. These actions can be used as independent actions, or as part of a more complex
workflow. :doc:`Actions</actions>` can be manually triggered, or they can be tied to
:doc:`sensors </sensors>` using rules.

.. contents::
   :local:
   :depth: 1

Most of the actions below can be used to automate SLX or VDX switches, however there are some
actions that are only valid for VDX switches as outlined below. If an action is only valid for VDX
it will be documented in the action details, otherwise the action is supported for both VDX and SLX.  

Device Registration
-------------------
Starting with Network Essentials (NE) v1.2, device credentials registration feature enables users to register device and associated credentials one time and thereby eliminating the need for providing device credentials in every action invocation.  This is supported for SLX, VDX and MLXe device families.  However based on device type, and user options, users need to provide different set of device credentials.

NE actions use primarily REST and SSH protocols to interact with SLX and VDX devices, username and password are sufficient for these protocols.

However, for MLXe, NE action use primarily SSH and SNMP protocols, requiring following additional credentials:
Username and password for SSH
- Users must provide the choice of SNMP version, SNMP v2 and SNMP v3 have different set of credentials.  Community string in case of SNMPV2 and username, auth-priv protocols and the corresponding pass phrases for SNMP v3.
- CLI perspective NetIron devices have privilege exec mode which is password protected

This release, use of Network Essentials has the following changes:
- One time device registration is required for all devices including SLX, NOS and NetIron based devices. 
- Devices must be configured with appropriate credentials prior to registering in NE 

NE includes new actions to register device credentials to register a device.

Factory Default Credentials - if registration is not performed, NE actions use the following factory default credentials to authenticate with a device:

  .. code-block:: bash

    SSH username: ‘admin’
    SSH password: ‘password’
    SNMP version:  ‘v2’
    SNMPv2_community: ‘public’

For SLX and NOS devices SNMP credentials are not applicable and it can be ignored.

.. include:: /_includes/solutions/essentials/register_device_credentials.rst

Default Credentials - In many environments, customers use common device credentials for most of the devices, users can register these common credentials as default credentials and don't have to register each device separately.  Example below outlines the registration for a mix of platforms:

  .. code-block:: bash

    st2 run network_essentials.register_device_credentials username=admin password=password snmp_version=v2 snmp_v2c=public enable_password=password

    or

    st2 run network_essentials.register_device_credentials mgmt_ip=USER.DEFAULT username=admin password=password snmp_version=v2 snmp_v2c=public enable_password=password

Device Specific Credentials - In environments, some or most of the devices may have unique credentials. If a device credentials are not the same as default credentials, device credentials must be explicitly registered, for example:

- Device specific registration with SNMPv2 credential and enable password for NetIron:

  .. code-block:: bash

    st2 run network_essentials.register_device_credentials mgmt_ip=10.24.85.107 username=admin password=admin snmp_version=v2 snmp_v2c=public enable_password=password

- Device specific registration with SNMPv3 credential and enable password for NetIron:

  .. code-block:: bash

    st2 run network_essentials.register_device_credentials mgmt_ip=10.24.85.107 username=admin password=password snmp_version=v3 snmpv3_user=v3user4 snmpv3_auth=md5 snmpv3_priv=aes auth_pass="md5 user" priv_pass="test aes user"

- Device specific registration for SLX and NOS:

  .. code-block:: bash

    st2 run network_essentials.register_device_credentials mgmt_ip=10.24.86.96  username=admin password=admin

Update Device registration - register_device_credentials action can also be used to overwrite existing device credentials. Since this action overwrites all the existing credentials, user must provide all the parameters not just the changed credentials.  For example:

  .. code-block:: bash

    st2 run network_essentials.register_device_credentials username=admin password=password snmp_version=v2 snmp_v2c=public

Now if user wants to update “enable_password” then user needs to give the existing snmp_version and snmp_v2c. 

  .. code-block:: bash

    st2 run network_essentials.register_device_credentials username=admin password=password snmp_version=v2 snmp_v2c=public enable_password=password

.. include:: /_includes/solutions/essentials/get_registered_device_credential_list.rst

Display registered device - “get_registered_device_credential_list” action lists all the registered devices and provides the corresponding SNMP version configured.

.. include:: /_includes/solutions/essentials/delete_device_credentials.rst

Deleting device registration
Device once registered will be part of st2 store until user deletes it.  Both default as well as device specific registrations can be deleted from registered device list: 

  .. code-block:: bash

    st2 run network_essentials.delete_device_credentials mgmt_ip=USER.DEFAULT (or)
    st2 run network_essentials.delete_device_credentials mgmt_ip=1.1.1.1

Device credential lookup - SSH credentials can still come as parameters from actions (which is maintained for backward compatibility).  Other credentials are expected to be registered per device or group default.  NE actions fetch device credentials using the following sequence:

For SSH credentials:
- Check if username and password parameter comes from action (or)
- Lookup st2 store for device specific username and password (or)
- Lookup st2 store for group default username and password (or)
- Code default value (admin/password)

For SNMP credentials:
- Check if version is v2 or v3 accordingly lookup the credentials in the following order:
- Lookup st2 store for device specific SNMP credentials (or)
- Lookup st2 store for group default SNMP credentials (or)
- Code default value [SNMPV2 community string “public”]

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

.. include:: /_includes/solutions/essentials/delete_switchport.rst

.. include:: /_includes/solutions/essentials/delete_ve.rst

.. include:: /_includes/solutions/essentials/delete_vlan.rst

.. include:: /_includes/solutions/essentials/remove_switchport_trunk_allowed_vlan.rst

.. include:: /_includes/solutions/essentials/remove_switchport_access_vlan.rst

.. include:: /_includes/solutions/essentials/delete_vrf.rst

.. include:: /_includes/solutions/essentials/delete_vrrpe.rst

.. include:: /_includes/solutions/essentials/set_intf_admin_state.rst

.. include:: /_includes/solutions/essentials/set_l2_mtu.rst

.. include:: /_includes/solutions/essentials/set_l3_mtu.rst

.. include:: /_includes/solutions/essentials/set_l2_system_mtu.rst

.. include:: /_includes/solutions/essentials/set_l3_system_mtu.rst

.. include:: /_includes/solutions/essentials/configure_mac_move_detection.rst

Bridge Domains
--------------

Bridge Domains(BD) is only supported on SLX family of devices.

.. include:: /_includes/solutions/essentials/configure_bridge_domain.rst

.. include:: /_includes/solutions/essentials/get_next_available_network_id.rst

.. include:: /_includes/solutions/essentials/delete_bridge_domain.rst

.. include:: /_includes/solutions/essentials/configure_logical_interface.rst

.. include:: /_includes/solutions/essentials/autopick_lif_id.rst

.. include:: /_includes/solutions/essentials/delete_logical_interface_on_bridge_domain.rst

.. include:: /_includes/solutions/essentials/delete_logical_interface_on_interface.rst

.. include:: /_includes/solutions/essentials/delete_service_policy_to_interface.rst


Virtual Fabrics
---------------

Virtual Fabrics are only supported on VDX family of devices.

The Virtual Fabrics (VF) feature in NOS enables Layer 2 multi-tenancy solutions that provide
support for overlapping VLANs, VLAN scaling, and transparent VLAN services by providing both
traditional VLAN service and a transport service. The Virtual Fabrics feature is deployed in data
centers that require logical switch partitioning with a large number of customer VLAN domains that
must be isolated from each other in the data plane. On the hardware platforms that support this
feature, such as VDX 8770 series and VDX 6740 series, the VLAN ID range is extended from the
standard 802.1Q limit of 4095, to 8191.  

Network Essentials v1.2 release includes new workflows and enhancements to the existing workflows
to automate VF provisioning.  

A VF operates like a regular 802.1Q VLAN, but allows the number of networks to scale beyond the
standard 4K (4096) limit. Users can use enable_vf action to enable VF on a switch. After enabling
VF, users can use existing workflows to manage VFs, for example, to create or delete a VF, use
create_vlan or delete_vlan actions.  

.. include:: /_includes/solutions/essentials/enable_vf.rst

.. include:: /_includes/solutions/essentials/get_next_available_network_id.rst

.. include:: /_includes/solutions/essentials/configure_mac_group.rst

.. include:: /_includes/solutions/essentials/delete_mac_group.rst

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

**Sample Output:**

.. code-block:: json

  [
    {
      "interface-name": null,
      "is-resolved": "true",
      "age": "02:02:12",
      "interface-type": "unknown",
      "ip-address": "80.0.110.11",
      "entry-type": "dynamic",
      "mac-address": "0000.07ab.839a"
    }
  ]

.. include:: /_includes/solutions/essentials/find_mac.rst

**Sample Output:**

.. code-block:: json

  [
    {
      "vlanid": "5308",
      "mac-state": "active",
      "mac-address": "22:00:00:11:11:19",
      "mac-type": "dynamic",
      "forwarding-interface": {
      "interface-type": "tengigabitethernet",
      "interface-name": "21/0/1"
      }
    },
    {
      "vlanid": "2",
      "mac-state": "active",
      "mac-address": "00:d0:b0:11:01:01",
      "mac-type": "dynamic",
      "forwarding-interface": {
      "interface-type": "tengigabitethernet",
      "interface-name": "21/0/1"
      }
    }
  ]

.. include:: /_includes/solutions/essentials/ping_vrf_targets.rst

.. include:: /_includes/solutions/essentials/validate_L2_port_channel_state.rst

**Sample Output:**

.. code-block:: json
 
  {
    "member-ports": [
      "tengigabitethernet 37/0/12",
      "tengigabitethernet 37/0/13",
      "tengigabitethernet 37/0/14",
      "tengigabitethernet 38/0/11",
      "tengigabitethernet 38/0/12",
      "tengigabitethernet 38/0/13"
    ],
    "state": "in_sync"
  }

  {
    "member-ports": [
      "tengigabitethernet 37/0/11",
      "tengigabitethernet 38/0/14"
    ],
    "state": "out_of_sync"
  }

.. include:: /_includes/solutions/essentials/validate_interface_state.rst

**Sample Output:**

.. code-block:: json

  {
    "state": "down",
    "intf": true
  }
  {
    "state": "up",
    "intf": true
  }
  {
    "state": false,
    "intf": true
  }

.. include:: /_includes/solutions/essentials/validate_interface_vlan.rst

.. code-block:: json

  {
    "vlan": true
  }
  {
    "vlan": false
  }


.. include:: /_includes/solutions/essentials/validate_vrrpe_state.rst


Utility Actions
---------------

.. include:: /_includes/solutions/essentials/execute_cli.rst

.. include:: /_includes/solutions/essentials/get_os_version.rst

.. include:: /_includes/solutions/essentials/get_switch_details.rst


VCS Specific Actions
--------------------

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
