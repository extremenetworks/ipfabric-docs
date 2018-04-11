Network Essentials Actions
==========================

This is a reference documentation for Network Essentials Automation Suite actions and workflows to automate SLX, VDX and
NetIron(NI) devices. These actions can be used as independent actions, or as part of a more complex
workflow. :doc:`Actions</actions>` can be manually triggered, or they can be tied to
:doc:`sensors </sensors>` using rules.

.. contents::
   :local:
   :depth: 1

Most of the actions below can be used to automate SLX, VDX and NI platforms, however, if an action is only valid for a particular platform, 
it will be documented in the action details, otherwise, the action is supported for all platforms.  

Pre-requisites for Automation
-----------------------------
For automation actions to work properly, following requirements must be met:

* Device firmware is supported by the automation suite
* SSH enabled on the device
* Ports 22 (SSH) and 443 (HTTPS) or 80 (HTTP) not blocked between automation & the device 
* Devices must be configured with appropriate credentials prior to registering in NE
* SSH user credentials must have Admin privileges on the device
* For NI devices, SNMP server must be enabled and SNMPv2 or SNMPv3 credentials must have read/write access to all OIDs/MIBs

Pre-requisites for HTTPS
~~~~~~~~~~~~~~~~~~~~~~~~
The following set up must be done on the devices and automation server in order for REST APIs to use HTTPS:

1. Enable HTTPS on SLX and/or VDX devices.

* SLX-R Security Guide: https://documentation.extremenetworks.com/slxos/SW/17rx/17.2.01/slxr-17.2.01-securityguide.pdf
* SLX-S Security Guide: https://documentation.extremenetworks.com/slxos/SW/17sx/53-1005318-01_SecuritySlxOS_17s.1.02_CG_Sep2017.pdf
* VDX Security Guide: https://documentation.extremenetworks.com/networkos/SW/73x/nos-730-securityguide.pdf

  - Ensure SLX and/or VDX device clocks are synchronized with the Certificate Authority's clock (date/time). 
  - Use the mgmt_ip address of the device when enrolling the common name for the Certificate Signing Request.


  .. code-block:: bash

    device# crypto ca enroll t1 country US state CA locality SJ organization Extreme orgunit SFI common <mgmt_ip of device> protocol SCP host 10.70.12.102 user fvt directory /users/home/crypto
    Password: ********** 

2. Copy trusted certificate authority's certificate to /etc/pyswitchlib/cacert.pem location on automation server.  If multiple certificate authorities are used, then concatenate the certificates to the same location on automation server.

Device Registration
-------------------
Starting with Network Essentials (NE) Automation Suite v1.2, the device credentials registration feature enables users to register a device and its associated credentials once, eliminating the need to provide device credentials for each action invocation. One time device registration is required for all device types, however, based on device type and user options, users may need to provide a different set of device credentials.

NE Automation Suite actions use primarily REST and SSH protocols to interact with SLX and VDX devices. The username and
password are sufficient for these protocols.  For NetIron(NI), in addition to SSH, actions use SNMP protocols that require the following additional credentials:

* Username and password for SSH
* SNMP version, and the relevant SNMP credentials - Community string for SNMPv2, Username, auth-priv
  protocols and the corresponding passphrases for SNMP v3.
* Enable password for NetIron devices where privileged exec mode is password protected.


For SLX and NOS devices SNMP credentials are not applicable and can be ignored.

.. include:: /_includes/solutions/essentials/register_device_credentials.rst

Prior to using NE actions, all devices must be registered with appropriate credentials, see examples below:

NE Automation Suite includes new actions to register device credentials to register a device.

- Registering SNMPv2 credentials and enable password for NetIron device:

  .. code-block:: bash

    st2 run network_essentials.register_device_credentials mgmt_ip=10.24.85.107 username=admin password=admin snmp_version=v2 snmp_v2c=public enable_password=password

- Registering SNMPv3 credentials and enable password for NetIron device:

  .. code-block:: bash

    st2 run network_essentials.register_device_credentials mgmt_ip=10.24.85.107 username=admin password=password snmp_version=v3 snmpv3_user=v3user4 snmpv3_auth=md5 snmpv3_priv=aes auth_pass="md5 user" priv_pass="test aes user"

- Registering for SLX or NOS device:

  .. code-block:: bash

    st2 run network_essentials.register_device_credentials mgmt_ip=10.24.85.107 username=admin password=admin

- If HTTPS is enabled on SLX or NOS device:

  .. code-block:: bash

    st2 run network_essentials.register_device_credentials mgmt_ip=10.24.81.125 username=admin password=password rest_protocol=https

Update Device registration: The ``register_device_credentials`` action can also be used to
overwrite existing device credentials. Since this action overwrites all the existing credentials,
the user must provide all the parameters and not just the changed credentials. For example:

  .. code-block:: bash

    st2 run network_essentials.register_device_credentials username=admin password=password snmp_version=v2 snmp_v2c=public

If you later need to update ``enable_password``, you also need to provide the existing ``snmp_version`` and
``snmp_v2c`` values:. 

  .. code-block:: bash

    st2 run network_essentials.register_device_credentials username=admin password=password snmp_version=v2 snmp_v2c=public enable_password=password

.. include:: /_includes/solutions/essentials/get_registered_device_credential_list.rst

Display registered devices: ``get_registered_device_credential_list`` lists all registered
devices and provides the corresponding SNMP version configured:

.. include:: /_includes/solutions/essentials/delete_device_credentials.rst

Deleting device registration: Device details will be maintained until explicitly deleted. 
Both default and device-specific credentials can be removed: 

  .. code-block:: bash

    st2 run network_essentials.delete_device_credentials mgmt_ip=1.1.1.1

Device credential lookup: SSH credentials can still come as parameters from actions (which is maintained for backward compatibility).  Other credentials are expected to be registered per device.  The NE Automation Suite actions fetch device credentials using the following sequence:

For SSH credentials:

- Check if username and password parameter comes from action (or)
- Lookup st2 store for device specific username and password

For SNMP credentials:

- Check if version is v2 or v3 then lookup credentials in the st2 store for device specific SNMP credentials

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

Bridge Domains(BD) are only supported on the SLX family of devices.

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

Virtual Fabrics are only supported on the VDX family of devices.

The Virtual Fabrics (VF) feature in NOS enables Layer 2 multi-tenancy solutions provides
support for overlapping VLANs, VLAN scaling, and transparent VLAN services, by providing both
traditional VLAN service and a transport service. The VF feature is deployed in data
centers that require logical switch partitioning with a large number of customer VLAN domains that
must be isolated from each other in the data plane. On hardware platforms that supports the VF
feature, such as VDX 8770 series and VDX 6740 series, the VLAN ID range is extended from the
standard 802.1Q limit of 4095, to 8191.  

Network Essentials Automation Suite v1.2 release includes new workflows and enhancements to the existing workflows
to automate VF provisioning.  

A VF operates like a regular 802.1Q VLAN, while allowing the number of networks to scale beyond the
standard 4K (4096) limit. Users can use enable_vf action to enable VF on a switch. After enabling
VF, users can use existing workflows to manage VFs, for example, to create or delete a VF, use
create_vlan or delete_vlan actions.  

.. include:: /_includes/solutions/essentials/enable_vf.rst

.. include:: /_includes/solutions/essentials/get_next_available_network_id.rst

.. include:: /_includes/solutions/essentials/configure_mac_group.rst

.. include:: /_includes/solutions/essentials/delete_mac_group.rst

ACL Management
---------------

With the addition of the NI platform support in NE Automation Suite v1.2, ACL Management actions support SLX, VDX and NI platforms. ACL actions provide abstraction covering common features across all these platforms. However, ACL actions also support platform specific features as optoinal attributes. Platform specific attributes are documented as part of the field description. If the field description does not specify any platform restrictions, those fields are applicable to all platforms.

.. include:: /_includes/solutions/essentials/create_acl.rst

.. include:: /_includes/solutions/essentials/delete_acl.rst

.. include:: /_includes/solutions/essentials/add_ipv4_rule_acl.rst

.. include:: /_includes/solutions/essentials/add_ipv6_rule_acl.rst

.. include:: /_includes/solutions/essentials/add_or_remove_l2_acl_rule.rst

.. include:: /_includes/solutions/essentials/delete_ipv4_rule_acl.rst

.. include:: /_includes/solutions/essentials/delete_ipv6_rule_acl.rst

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
This section includes the known issues in Network Essentials Automation Suite 1.0.0 release. Common issues are listed in the beginning of the section and the issues specific to a particular network device platform are organized under the corresponding platform sub-section.


SLX:
~~~~
400 - Time taken for IPV6 ACL is higher due to bulking not supported on IPv6 SLX

NI:
~~~~
333 - add_or_remove_l2_acl_rule : In negative scenarios the error string is missing last few characters
323 - create_ve action does not configure IPv4/v6 addresses for dual stack scenarios
