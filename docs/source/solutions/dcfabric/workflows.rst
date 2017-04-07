Workflows
=========

This document provides an overview of how to use the DC Fabric Automation Suite workflows
with Brocade VDX and SLX switches. These can be used as independent workflows, or tied
together to form more complex workflows. They can be manually triggered,
or they can be tied to :doc:`sensors </sensors>` using rules.

.. note::
    Content is still being added to this section

.. contents::
   :local:
   :depth: 1

.. _Add_l3_tenant_endpoint:

Add_l3_tenant_endpoint
~~~~~~~~~~~~~~~~~~~~~~

Description
```````````
The Add_l3_tenant_endpoint workflow automates the addition of an endpoint which need Layer
3 termination within the VCS fabric. It automates the provisioning of both the edge ports 
as well as the VRRP-E based redundant gateway. It combines the actions in 
server_provision, :ref:`Configure_edge_ports<Configure_edge_ports>`,  
and :ref:`Configure_vrrpe_gw<Configure_vrrpe_gw>`.

Requirements
````````````

This workflow is designed for operating in VCS Fabric mode.

Parameters
``````````

   mgmt_ip
       Management IP of the switch.

   rbridge_id (optional)
       Single/List of rbridge ID's, e.g. rbridge_id=1 or rbridge_id=1,2,3

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

   ports
       Single interface or list of interfaces separated by comma that needs to be mapped to 
       the port channel e.g 1/2/10, 3/4/15

   vlan_id
       Single vlan_id or range of vlans. At least one vlan_id must be provided. e.g. 10

   port_channel_id
       Portchannel interface number. <NUMBER: 1-6144>

   mode (optional)
       Port channel mode type, e.g. standard or brcd. Default Value is standard

   protocol (optional)
       Port channel protocol type. e.g. active, passive, mode on. Default Value is active
  
   ve_ip
       Single ip if Rbridge id is one or list of ip's for multiple Rbridge-id's separated by
       comma that needs to be configured on ve interface.

   vrid (optional)
       Vrrpe Router ID

   virtual_ip
       Vrrpe Virtual IP

   virtual_mac
       Vrrpe Virtual MAC with 02e0.5200.00XX, 2nd byte from right can be replaced with user
       defined values

Output
``````

   result
       Boolean - True/False, if workflow succeeded

   ve_ip
       IP address assigned to the VE interface

   vrid
       Vrrpe Router ID assigned to the VE interface

   virtual_ip
       Vrrpe Virtual IP assigned to the VE interface

   virtual-mac
       Vrrpe Virtual Mac assigned to the VE interface


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

   "Input is not a valid Interface"
       Returned if interface name is not valid port numbers.

   "Pls specify a valid description"
       Returned if interface description length is less than 1.

   "Length of the description is more than the allowed size"
       Returned if interface description length is more than 63.

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
       Returned if any one of the input is invalid during short path forwarding configuration

.. _Add_l3_tenant_endpoint_evpn:

Add_l3_tenant_endpoint_evpn
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
```````````
The Add_l3_tenant_endpoint_evpn workflow automates the configuration of the edge ports of the
BGP EVPN based IP fabric. The workflow automates creation of port-channel interfaces (LAGs and
vLAGs), configuration of the port-channel interface as access or trunk, creation and association
of VLANs with the port-channel interfaces, validation of the port channel state as well as
creation of layer 3 gateway using Anycast Gateway protocol and modify ARP ND ageing on the
vLAG pair or leaf switch and association of the layer 3 gateways with a VRF. 

Requirements
````````````
This workflow is designed for operating in IP Fabric mode. 

Parameters
``````````
   mgmt_ip
       Management IP of the switch.

   intf_desc (optional)
        Interface description name

   intf_type (optional)
        Interface type gigabitethernet, tengigabitethernet, fortygigabitethernet, hundredgigabitethernet.
        port_channel. Default is tengigabitethernet

   intf_name
       Single interface name/range of interfaces which will be associated with port-channel.

   vlan_id
       Single vlan or range of vlans e.g. 100.

   vrf_name
        VRF Name e.g. vrf101.

   auto_pick_port_channel_id
       Flag Auto picks Port_channel id <1-6144> if user does not want to specify the 
       port-channel id e.g True. Default is False (which does not enable auto picking)

   port_channel_id (optional)
       Portchannel interface number. <NUMBER: 1-6144> if not interested in auto picking.

   switchport_mode (optional)
       Switch port mode e.g. access, trunk

   mode (optional)
       Port channel mode type, e.g. standard or brcd

   protocol (optional)
       Port channel protocol type. e.g. active, passive, mode on

   anycast_address
       Ipv4 address with subnet/prefix length, e.g. 10.1.1.1/24.

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

    Invalid IP “anycast_address”

.. note::
   autopick_port_channel_id flag has to be unset and port-channel id has to be specified
   if the workflow has to be re-run.

.. _Configure_edge_ports:

Configure_edge_ports
~~~~~~~~~~~~~~~~~~~~

Description
```````````
The Configure_edge_ports workflow automates the configuration of the edge ports. 
The workflow automates creation of port-channel interfaces (LAGs and vLAGs), 
configuration of the port-channel interface as access or trunk, creation and
association of VLANs with the port-channel interfaces as well as validation of
the port channel state.

Requirements
````````````
This workflow is designed for operating on edge devices.

Parameters
``````````
   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   vlan_id
       Single vlan_id. At least one vlan_id must be provided. e.g. 10
    
   intf_desc (optional)
        Interface description name
   
   intf_type (optional)
        Interface type gigabitethernet/tengigabitethernet/fortygigabitethernet/hundredgigabitethernet
         Default Value is tengigabitethernet

   ports
       Single interface or list of interfaces separated by comma that needs   to be mapped to the port channel e.g 1/2/10, 3/4/15

   vlan_id
       Single vlan_id or range of vlans. At least one vlan_id must be provided. e.g. 10

   port_channel_id
       Portchannel interface number. <NUMBER: 1-6144>

   
   mode (optional)
       Port channel mode type, e.g. standard or brcd
	   Default Value is standard


   protocol (optional)
       Port channel protocol type. e.g. active, passive, mode on
           Default Value is active
	   
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

   “SWITCHING_NOT_ENABLED | %Error: Interface not configured for switching”
       Returned if given interfaces are already part of a port-channel 
 
.. _Configure_vrrpe_gw:

Configure_vrrpe_gw
~~~~~~~~~~~~~~~~~~

Description
```````````

The Configure_vrrpe_gw workflow automates the creation of a VRRP-E based default gateway
including the VE interfaces.

Requirements
````````````

This workflow is designed for operating in both VCS and IP Fabric mode.

Parameters
``````````

   mgmt_ip
       Management IP of the switch.

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
       Boolean - True/False, if workflow succeeded

   ve_ip
       IP address assigned to the VE interface

   vrid
       Vrrpe Router ID assigned to the VE interface

   virtual_ip
       Vrrpe Virtual IP assigned to the VE interface

   virtual-mac
       Vrrpe Virtual Mac assigned to the VE interface

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

.. _Create_l2_tenant_evpn:

Create_l2_tenant_evpn
~~~~~~~~~~~~~~~~~~~~~

Description
```````````

The Create_l2_tenant_evpn workflow provisions an L2 domain extension in the BGP EVPN based IP fabric,
on the selected leaves or vLAG pairs.The workflow must be provided with the set of vLAG pairs or
leaf switches between which the layer 2 extension is required.

Requirements
````````````

This workflow is designed for operating in IP Fabric mode.

Parameters
``````````

   mgmt_ip
       Management IP of the switch. At least one switch mgmt ip must be provided.

   vni
       The VNI to be used for the Layer 2 extension <NUMBER:1-16777215>, e.g. vni=500
       (EVPN instance must be configured under each rbridge-id)

Output
``````

   result
       Boolean - True/False, if action succeeded

Error Messages
``````````````

   "Input is not a valid VNI value"
       Returned if VNI value is < 1 or > 16777215

   "EVPN instance not configured under rbridge-id"
       Returned if evpn instance is not already configured

   "Invalid Input values for VNI <vni> add for evi <evi> under rbridge <rbridge-id>
       Returned if input is invalid.

   "VLAG PAIR must be <= 2 leaf nodes"
       Returned if VLAG pair is more than two nodes

.. _Create_l3_tenant_evpn:

Create_l3_tenant_evpn
~~~~~~~~~~~~~~~~~~~~~

Description
```````````

The Create_l3_tenant_evpn workflow provisions the BGP EVPN based IP fabric with an L3 tenant
identified by a VRF. This workflow provisions the vlan, VRF for the Layer 3 tenant at the identified
leaf switches or vLAG pairs, enables routing for the VRF across the IP fabric by enabling the
VRF address family in BGP and creating L3VNI interface and also enables redistribution of
connected routes in the VRF to BGP EVPN.

Requirements
````````````

This workflow is designed for operating in IP Fabric mode.

Parameters
``````````

   mgmt_ip
       Management IP of the switch.

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

Output
``````

   result
       Boolean - True/False, if workflow succeeded


Error Messages
``````````````

   "Not a valid VLAN"
       Returned if VLAN provided are invalid, e.g. > 4094

   "vlan 1 is default vlan"
       Returned if VLAN provided is 1.

   "Vlan cannot be created, as it is not a user/fcoe vlan"
       Returned if VLAN provided is part of user/fcoe vlan (4087/4096/1002).

.. _provision_evpn_instance:

provision_evpn_instance
~~~~~~~~~~~~~~~~~~~~~~~

Description
```````````

The provision_evpn_instance workflow provisions the BGP EVPN instance which includes configure evpn 
instance, evpn vtep, conversational arp, conversational mac and mac move thresold.

Requirements
````````````

This workflow is designed for operating in IP Fabric mode.

Parameters
``````````

   mgmt_ip
       Management IP of the switch.

   rbridge_id (optional)
       Single/List of rbridge ID's, e.g. rbridge_id=1 or rbridge_id=1,2,3

   evi_name
       evpn instance name.Must be a text string <Word:1-64>, e.g. evi1.

   vtep_name
       Overlay Gateway Name. Can contain alphabets, digits, hyphen or underscore
       Must be a text string <WORD:1-32>, e.g. vtep1.

   vtep_loopback_id
       Vtep loopback id. Must be an integer <NUMBER:1-255>, e.g. 250 

   mac_move_threshold
        mac move threshold. Must be an integer <NUMBER:5-500>, default 20, e.g 30

Output
``````

   result
       Boolean - True/False, if workflow succeeded


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

   "Mac Move Threshold is Invalid. Not in <5-500> range"
       Returned if given mac move threshold is < 5 and > 500. e.g. 501


.. include:: /_includes/solutions/dcfabric/add_multihomed_endpoint_and_gw_evpn.rst

.. include:: /_includes/solutions/dcfabric/add_multihomed_endpoint_and_gw.rst

.. include:: /_includes/solutions/dcfabric/add_multihomed_endpoint.rst

.. include:: /_includes/solutions/dcfabric/add_singlehomed_endpoint.rst

.. include:: /_includes/solutions/dcfabric/configure_anycast_gateway_evpn.rst

.. include:: /_includes/solutions/dcfabric/configure_anycast_gw_mac_evpn.rst

.. include:: /_includes/solutions/dcfabric/configure_arp_nd_suppression.rst

.. include:: /_includes/solutions/dcfabric/configure_bgp_ipfabric.rst

.. include:: /_includes/solutions/dcfabric/configure_bgp_neighbor.rst

.. include:: /_includes/solutions/dcfabric/configure_bgp_parameters_ipfabric.rst

.. include:: /_includes/solutions/dcfabric/configure_bgp_redistribute_connected.rst

.. include:: /_includes/solutions/dcfabric/configure_conversational_arp_evpn.rst

.. include:: /_includes/solutions/dcfabric/configure_conversational_mac_evpn.rst

.. include:: /_includes/solutions/dcfabric/configure_device_ipfabric.rst

.. include:: /_includes/solutions/dcfabric/configure_evpn_instance.rst

.. include:: /_includes/solutions/dcfabric/configure_evpn_vtep.rst

.. include:: /_includes/solutions/dcfabric/configure_fabric_infra.rst

.. include:: /_includes/solutions/dcfabric/configure_interface_ipfabric.rst

.. include:: /_includes/solutions/dcfabric/configure_intfs_ipfabric.rst

.. include:: /_includes/solutions/dcfabric/configure_vrrpe_gw.rst

.. include:: /_includes/solutions/dcfabric/create_l2_tenant_evpn.rst

.. include:: /_includes/solutions/dcfabric/create_l3_tenant_evpn.rst

.. include:: /_includes/solutions/dcfabric/create_vrf_evpn.rst

.. include:: /_includes/solutions/dcfabric/fabric_add.rst

.. include:: /_includes/solutions/dcfabric/fabric_config_delete.rst

.. include:: /_includes/solutions/dcfabric/fabric_config_set.rst

.. include:: /_includes/solutions/dcfabric/fabric_delete.rst

.. include:: /_includes/solutions/dcfabric/fabric_list.rst

.. include:: /_includes/solutions/dcfabric/get_flow_trace_ip_fabric.rst

.. include:: /_includes/solutions/dcfabric/modify_arp_nd_aging_ve.rst

.. include:: /_includes/solutions/dcfabric/provision_evpn_instance.rst

.. include:: /_includes/solutions/dcfabric/query_topology.rst

.. include:: /_includes/solutions/dcfabric/redistribute_connected_bgp_vrf.rst

.. include:: /_includes/solutions/dcfabric/set_max_path_bgp.rst

.. include:: /_includes/solutions/dcfabric/show_config_bgp.rst

.. include:: /_includes/solutions/dcfabric/show_lldp_links.rst

.. include:: /_includes/solutions/dcfabric/show_vcs_links.rst

.. include:: /_includes/solutions/dcfabric/switch_add.rst

.. include:: /_includes/solutions/dcfabric/switch_delete.rst

.. include:: /_includes/solutions/dcfabric/switch_list.rst

.. include:: /_includes/solutions/dcfabric/switch_update.rst

.. include:: /_includes/solutions/dcfabric/topology_generate.rst
