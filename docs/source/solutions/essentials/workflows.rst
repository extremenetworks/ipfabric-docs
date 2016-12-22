Workflows
=========

This document provides an overview of how to use the Network Essentials workflows and actions
with Brocade VDX and SLX switches. These actions can be used as independent actions,
or as part of a more complex workflow. :doc:`Actions</actions>` can be manually triggered,
or they can be tied to :doc:`sensors </sensors>` using rules.

.. note::
    Content is still being added to this section

.. contents::
   :local:
   :depth: 2

Workflows
---------

.. contents::
   :local:
   :depth: 1

.. _server_provision:

server_provision
~~~~~~~~~~~~~~~~

Description
```````````

This workflow includes administrative settings on an interface, create VLAN and
configure Switchport Mode as access or trunk and associate access or trunk VLANs
    

Requirements
````````````

This workflow is designed for operating on edge devices.


Parameters
``````````

   mgmt_ip
       Management IP of the switch.

   intf_type
       Interface type gigabitethernet or tengigabitethernet or port_channel,

   intf_name
       Interface name in 3-tuple format (example: 2/0/96) or port-channel number <1-6144>       

   enabled
       Admin setting on the interface. Boolean type. <True/False>       

   vlan_id
       Single or range of vlan_id. At least one vlan_id must be provided. e.g. 4-10
	
   switchport_mode
	   Switchport mode to be configured under the interface access/trunk, e.g. trunk.
	   Default Value is 'access'  

   intf_desc (optional)
       Vlan Description to be configured. Must be a text string, e.g. test_vlan   
	   
Output
``````

   Result
       Boolean - True/False, if workflow succeeded


Error Messages
``````````````

   "Not a valid VLAN"
       Returned if VLAN provided are invalid, e.g. > 4094

   "vlan 1 is default vlan"
       Returned if VLAN provided is 1.

   "Vlan cannot be created, as it is not a user/fcoe vlan"
       Returned if VLAN provided is part of user/fcoe vlan (4087/4096/1002).
	
   "Input is not a valid Interface"
       Returned if interface name is not valid port numbers.

Actions
-------

.. contents::
   :local:
   :depth: 1

.. _autopick_port_channel_id:

autopick_port_channel_id
~~~~~~~~~~~~~~~~~~~~~~~~

Description
```````````

``autopick_port_channel_id`` Provides a port_channel number < 1-6144> which is not 
pre-existing on the setup, if port_channel id is not passed.

Requirements
````````````
No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````
   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.
   
   port_channel_id (optional)
       Portchannel interface number. <NUMBER: 1-6144>

Output
``````
   Result
       Provides port-channel id, if action succeeded

Error Messages
``````````````
   No error messages

.. _configure_anycast_gateway_evpn:

configure_anycast_gateway_evpn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
```````````
``configure_anycast_gateway_evpn`` Configure anycast gateway ip on ve interface

Requirements
````````````
No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````
   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   vlan_id
       Single vlan_id. At least one vlan_id must be provided. e.g. 10

   anycast_address
       Ipv4 address with subnet/prefix length

Output
``````
   Result
       Boolean - True/False, if action succeeded

Error Messages
``````````````
   “Invalid IP anycast_address"
       Returned if ip address format is wrong e.g. 10.0.0.10.1
   “Ve interface not configured for rbridge id”
       Returned if the ve is not created before configuring anycast ip.

.. _configure_conversational_arp_evpn:

configure_conversational_arp_evpn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
```````````

``configure_conversational_arp_evpn`` configure conversational arp on the device.

Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

Output
``````

   result
       Boolean - True/False, if action succeeded

Error Messages
``````````````
    No error messages

.. _configure_conversational_mac_evpn:

configure_conversational_mac_evpn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
```````````

``configure_conversational_mac_evpn`` Configure conversational mac on the device.

Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

Output
``````

   result
       Boolean - True/False, if action succeeded

Error Messages
``````````````
    No error messages

.. _configure_evpn_instance:

configure_evpn_instance
~~~~~~~~~~~~~~~~~~~~~~~

Description
```````````

``configure_evpn_instance`` Configures evpn instance with the given evpn name,
rd-auto, route target both auto ignore-as, duplicate MAC timer,  max count.
 
Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.
   
   rbridge_id (optional)
       Rbridge ids of the devices

   duplicate_mac_timer (optional)
       Value in integer 5-300, default 10

   max_count
       Value in integer in 3-10, default 10
   
   ignore_as (optional) 
        Boolean true or false, default is True

Output
``````

   Result
       Returns true, if action succeeded

Error Messages
``````````````

   "EVPN instance already configured with <reason>"
       Returned if evpn instance or rd-auto or duplicate-mac-timer-value or max-count are already
       configured.

.. _configure_evpn_vtep:

configure_evpn_vtep
~~~~~~~~~~~~~~~~~~~

Description
```````````

``configure_evpn_vtep`` Configure EVPN VTEP on a leaf/vLAG pair.

Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   rbridge_id (optional)
       Single/List of rbridge ID's, e.g. rbridge_id=1 or rbridge_id=1,2,3

   name
       Overlay Gateway Name. Can contain alphabets, digits, hyphen or underscore
       Must be a text string <WORD:1-32>, e.g. vtep1.

   loopback_id
       Vtep loopback id. Must be an integer <NUMBER:1-255>, e.g. 250 


Output
``````

   result
       Boolean - True/False, if action succeeded

Error Messages
``````````````

   "Loopback Id is Invalid. Not in <1-255> range"
       Returned if loopback id provided is > 255 or < 1, e.g. 256

   "Overlay Gateway Name is Invalid. Not in <1-32> range"
       Returned if length of Vtep name provided is > 32 or < 1, e.g 35

   "Input for Overlay Gateway name can contain only alphabets digits, hyphen or underscore"
       Returned if Vtep name contains any special characters.

   "Overlay Gateway name is already configured"
       Returned if vtep name is already configured on the device.


.. _configure_mac_move_detection:

configure_mac_move_detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
```````````

``configure_mac_move_detection`` Configure mac move threshold on a Leaf/vlag pair device.

Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   move_threshold
       Mac move threshold. Must be an integer <NUMBER:5-500>, default 20, e.g 30

Output
``````

   result
       Boolean - True/False, if action succeeded

Error Messages
``````````````

   "Mac Move Threshold is Invalid. Not in <5-500> range"
       Returned if given mac move threshold is < 5 and > 500. e.g. 501

.. _create_port_channel:

create_port_channel
~~~~~~~~~~~~~~~~~~~

Description
```````````

``create_port_channel`` Create a port channel and map it to the interface and enables
 protocol and mode on the interaces.

Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.
   
   intf_type (optional)
        Interface type gigabitethernet/tengigabitethernet/fortygigabitethernet/hundredgigabitethernet
         Default Value is tengigabitethernet

   ports
       Single interface or list of interfaces separated by comma that needs   to be mapped to the port channel e.g 1/2/10, 3/4/15

   port_channel_id
       Portchannel interface number. <NUMBER: 1-6144>
   
   mode (optional)
       Port channel mode type, e.g. standard or brcd
	   Default Value is standard

   protocol (optional)
       Port channel protocol type. e.g. active, passive, mode on
           Default Value is active

   intf_desc (optional)
       Interface specific description. Must be a text string <string, min: 1 chars, max: 63 chars>.


Output
``````

   Result
       Boolean - True/False, if action succeeded

Error Messages
``````````````

   "SWITCHING_NOT_ENABLED | %Error: Interface not configured for switching"
       Returned if given interfaces are already part of a port-channel 


.. _create_switchport_access:

create_switchport_access
~~~~~~~~~~~~~~~~~~~~~~~~

Description
```````````

``create_switchport_access`` Enables Switch mode access on an interface and associates access VLAN.

Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   vlan_id
       Single or range of vlan_id. At least one vlan_id must be provided. e.g. 4-10

   intf_type
       Interface type gigabitethernet or tengigabitethernet or port_channel,

   intf_name
       Interface name in 3-tuple format (example: 2/0/96) or port-channel number <1-6144>

Output
``````

   Result
       Boolean - True/False, if action succeeded

Error Messages
``````````````

   "Not a valid VLAN"
       Returned if VLAN provided are invalid, e.g. > 4094

   "vlan 1 is default vlan"
       Returned if VLAN provided is 1.

   "Input is not a valid Interface"
       Returned if interface name is not valid port numbers.

.. _create_switchport_trunk:

create_switchport_trunk
~~~~~~~~~~~~~~~~~~~~~~~~

Description
```````````

``create_switchport_trunk`` Enables Switch mode trunk on interfaces and associates trunk VLANs.

Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   vlan_id
       Single or range of vlan_id. At least one vlan_id must be provided. e.g. 4-10

   intf_type
       Interface type gigabitethernet or tengigabitethernet or port_channel.

   intf_name
       Interface name in 3-tuple format (example: 2/0/96) or port-channel number <1-6144>

Output
``````

   Result
       Boolean - True/False, if action succeeded

Error Messages
``````````````
   
   "Not a valid VLAN"
       Returned if VLAN provided are invalid, e.g. > 4094

   "vlan 1 is default vlan"
       Returned if VLAN provided is 1.

   "Interface type or name invalid"
       Returned if interface name is not valid port numbers.

.. _create_ve:

create_ve
~~~~~~~~~

Description
```````````

``create_ve`` Create a VE and associate an IP address and vrf if any per rbridge.

Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   rbridge_id
       Single/List of rbridge ID's, e.g. rbridge_id=1 or rbridge_id=1,2,3

   vlan_id
       Single vlan_id. At least one vlan_id must be provided. e.g. 10

   ip_address (optional)
       Single or list of ip/ipv6 addresses to be configured on the Ve. IPv4/subnet-length
       or IPv6/prefix-length. e.g. '10.0.0.10/22, 30.0.0.10/22'

   vrf_name (optional)
       Name of the VRF. Must be a text string <WORD:1-32>, e.g. vrf10 or 10.

   ipv6_use_link_local_only (optional)
       Configure automatically computed link-local address. e.g. ipv6_use_link_local_only


Output
``````

   result
       Boolean - True/False, if action succeeded

Error Messages
``````````````

   "rbridge_id and ip_address lists are not matching"
       Returned if given rbridge_id and ip_address lists are not matching

   "Invalid IP address <ip-address>"
       Returned if ip address format is wrong e.g. 10.0.0.10.1

   "Pass IP address along with netmask.(ip-address/netmask)"
       Returned if IP address input is without netwmask e.g. 10.0.0.1.

   "Invalid Input values while creating to Ve"
       Returned if any one of the input is invalid.

   "Invalid Input values while assigning IP address to Ve"
       Returned if any one of the input is invalid.

   "Invalid Input values while configuring IPV6 link local"
       Returned if input is invalid.

.. _create_vlan:

create_vlan
~~~~~~~~~~~

Description
```````````

``create_vlan`` Creates a single/range of VLAN's on the device.

Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   vlan_id
       Single or range of vlan_id. At least one vlan_id must be provided. e.g. 4-10

   intf_desc (optional)
       Interface specific description. Must be a text string <string, min: 1 chars, max: 63 chars>.

Output
``````

   result
       Boolean - True/False, if action succeeded

Error Messages
``````````````

   "Not a valid VLAN"
       Returned if VLAN provided are invalid, e.g. > 4094

   "vlan 1 is default vlan"
       Returned if VLAN provided is 1.

   "Vlan cannot be created, as it is not a user/fcoe vlan"
       Returned if VLAN provided is part of user/fcoe vlan (4087/4096/1002).

   "Pls specify a valid description"
       Returned if interface description length is less than 1.

   "Length of the description is more than the allowed size"
       Returned if interface description length is more than 63.

.. _create_vrf_evpn:

create_vrf_evpn
~~~~~~~~~~~~~~~

Description
```````````

``create_vrf_evpn`` Create a VRF, RD, RT and L3VNI for the EVPN tenants on the device.

Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   vrf_name
       Name of the VRF. Must be a text string <WORD:1-32>, e.g. vrf10.

   l3vni
       Layer 3 VNI for VXLAN routing. Must be a integer <NUMBER:1-16777215>, e.g. 100.

   route_distinguisher
       BGP router id of the Leafs, e.g. 10.20.31.1,10.20.31.2.

   rt
       RT for the address family, e.g. 101.

   tenant_addressing_type
       Tenant addressing type ipv4/ipv6/both, e.g. both.

   ipv4_route_target_import_evpn
       ipv4 import Target-VPN community 'ASN:nn'. e.g. 101:101

   ipv4_route_target_export_evpn
       ipv4 import Target-VPN community 'ASN:nn'. e.g. 101:101

   ipv6_route_target_import_evpn
       ipv6 import Target-VPN community 'ASN:nn'. e.g. 102:102

   ipv6_route_target_export_evpn
       ipv6 import Target-VPN community 'ASN:nn'. e.g. 103:103

   rbridge_id (optional)
       Single/List of rbridge ID's, e.g. rbridge_id=1 or rbridge_id=1,2,3

Output
``````

   result
       Boolean - True/False, if action succeeded

Error Messages
``````````````

   "Invalid Input types while creating VRF <vrf name> on rbridge_id <rbridge_id>"
       Returned if given vrf name and rbridge_id is invalid

   "Invalid input types while configuring RD <rd> on VRF <vrf name> on rbridge_id <rbridge_id>'
       Returned if given rd, vrf name and rbridge_id is invalid

   "Invalid input types while configuring l3vni <l3vni> on VRF <vrf name> on rbridge_id <rbridge_id>'
       Returned if given l3vni, vrf name and rbridge_id is invalid

   "Invalid input types while configuring target VPN on VRF <vrf name> on rbridge_id <rbridge_id>'
       Returned if given route target, vrf name and rbridge_id is invalid

.. _create_vrrpe:

create_vrrpe
~~~~~~~~~~~~

Description
```````````

``create_vrrpe`` Create VRRPe group and assign virtual IP, virtual mac.

Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   rbridge_id (optional)
       Single/List of rbridge ID's, e.g. rbridge_id=1 or rbridge_id=1,2,3

   vlan_id
       Single or range of vlan_id. At least one vlan_id must be provided. e.g. 4-10

   intf_desc (optional)
       Interface specific description. Must be a text string <string, min: 1 chars, 
       max: 63 chars>.

   ve_ip
       Single ip if Rbridge id is one or list of ip's for multiple Rbridge-id's separated by
       comma that needs to be configured on ve interface.

   vrid (optional)
       Vrrpe Router ID

   virtual_ip
       Vrrpe Virtual IP

   virtual_mac
       Vrrpe Virtual MAC with 02e0.5200.00XX, 2nd byte from right can be replace with user 
       defined values

Output
``````
   result
       Boolean - True/False, if action succeeded

Error Messages
``````````````

   "Invalid Virtual IP Address"
       Returned if input is not a valid IP address

   "Pass VIP address without netmask"
       Returned if IP address input is with netwmask e.g. 10.0.0.1/22.

   "Device is pre-configured with ip version"
       Returned if the device is already configured with the same IP address

   "Invalid Input types while creating VRRPE group"
       Returned if any one of the input is invalid.

   "Invalid input values vrid, rbridge_id, vmac"
       Returned if any one of the input is invalid during VMAC to the extender group association.

   "Invalid input values vrid, rbridge_id, ve_name"
       Returned if any one of the input is invalid during short path forwarding configuration.

.. _execute_cli:

execute_cli
~~~~~~~~~~~

Description
```````````
``execute_cli`` Execute CLI command and return the result.

Requirements
````````````
No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````
   host
       Management IP of the switch. At least one switch mgmt ip must be provided.

   Cli_cmd
       CLI commands to execute on the specified VDX device e.g “show port-channel 101”
   
Output
``````
   Result
       Returns cli cmd output, if action succeeded

Error Messages
``````````````
   "Failed to execute cli on host due to reason"
       Returned for any error

.. _get_switch_details:

get_switch_details
~~~~~~~~~~~~~~~~~~

Description
```````````
``get_switch_details`` Gets the rbridge list and principal rbridge management ip in the vcs.
 
Requirements
````````````
No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````
   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

Output
``````
   Result
       Array with rbridge_id list and switch_ip, if action succeeded

Error Messages
``````````````
       "No error msg”

.. _modify_arp_nd_aging_ve:

modify_arp_nd_aging_ve
~~~~~~~~~~~~~~~~~~~~~~

Description
```````````
``modify_arp_nd_aging_ve`` Configure anycast gateway ip on ve interface

Requirements
````````````
No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````
   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   vlan_id
       Single vlan_id. At least one vlan_id must be provided. e.g. 10

   arp_aging_type
       Arp or ND e.g arp_aging
   
   arp_aging_timeout (optional)
       Arp Aging Timeout in Minutes <0...240> e.g 4

   rbridge_id (optional)
       Rbridge id on which arp-aging-timeout has to be configured

Output
``````
   Result
       Boolean - True/False, if action succeeded

Error Messages
``````````````
   “Configuring IP ARP aging timeout failed"
       Returned if arp aging timout is not within <0...240>
   “Ve interface not configured for rbridge id”
       Returned if the ve is not create before configuring anycast ip.

.. _redistribute_connected_bgp_vrf:

redistribute_connected_bgp_vrf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
```````````

``redistribute_connected_bgp_vrf`` Redistribute BGP Connected Routes under default/non-default vrf
address-family on the device.

Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   rbridge_id (optional)
       Single/List of rbridge ID's, e.g. rbridge_id=1 or rbridge_id=1,2,3

   ipv4_unicast
       Address family unicast ipv4 True/False. e.g. True

   ipv6_unicast
       Address family unicast ipv6 True/False. e.g. False

   ipv4_vrf_name
       Name of the VRF. Must be a text string <WORD:1-32>, e.g. vrf10.
       (Address family ipv4 must be configured under vrf)

   ipv6_vrf_name
       Name of the VRF. Must be a text string <WORD:1-32>, e.g. vrf10.
       (Address family ipv6 must be configured under vrf)

Output
``````

   result
       Boolean - True/False, if action succeeded

Error Messages
``````````````

   "Invalid Input values"
       Returned if any one of the input is invalid.

.. _set_intf_admin_state:

set_intf_admin_state
~~~~~~~~~~~~~~~~~~~~

Description
```````````

``set_intf_admin_state`` enables a single/range of physical interfaces, port-channel,
loopback, ve on a device

Requirements
````````````

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   intf_type
       Interface type gigabitethernet or tengigabitethernet or port_channel,

   intf_name
       Interface name in 3-tuple format (example: 2/0/96) or port-channel number <1-6144>       

   enabled
       Admin setting on the interface. Boolean type. <True/False>       

   rbridge_id (optional)
	   Rbridge id under which ve/loopback is configured. e.g. 1

   intf_desc (optional)
       Vlan Description to be configured. Must be a text string, e.g. test_vlan

Output
``````

   Result
       Boolean - True/False, if action succeeded

Error Messages
``````````````

   "Input is not a valid Interface"
       Returned if interface name is not valid port numbers.

   "Pls specify a valid description"
       Returned if interface description length is less than 1.

   "Length of the description is more than the allowed size"
       Returned if interface description length is more than 63.