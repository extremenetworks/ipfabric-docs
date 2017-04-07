Workflows
=========

DC Fabric Automation Suite includes turnkey automations required to provision, validate and troubleshoot data center networks spanning Day 0 and Day n activities.  Designed to work with multiple data center architectures such as IP Fabric, IP Fabric with EVPN overlay, VCS Fabric as well as multiple device families such as VDX, SLX.  

This is a reference documentation organized around key usecases as outlined below.  These can be used as independent workflows, or tied together to form more complex workflows. They can be manually triggered, or they can be tied to :doc:`sensors </sensors>` using rules.

.. note::
    Content is still being added to this section

.. contents::
   :local:
   :depth: 2

Manage Fabric Templates
-----------------------

.. include:: /_includes/solutions/dcfabric/fabric_add.rst

.. include:: /_includes/solutions/dcfabric/fabric_delete.rst

.. include:: /_includes/solutions/dcfabric/fabric_list.rst

.. include:: /_includes/solutions/dcfabric/fabric_config_set.rst

.. include:: /_includes/solutions/dcfabric/fabric_config_delete.rst


Build IP Fabric Infrastructure
------------------------------

.. include:: /_includes/solutions/dcfabric/switch_add.rst

.. include:: /_includes/solutions/dcfabric/switch_delete.rst

.. include:: /_includes/solutions/dcfabric/switch_list.rst

.. include:: /_includes/solutions/dcfabric/switch_update.rst

.. include:: /_includes/solutions/dcfabric/topology_generate.rst

.. include:: /_includes/solutions/dcfabric/configure_fabric_infra.rst

Manage EVPN Tenants and Edge Ports
----------------------------------

.. include:: /_includes/solutions/dcfabric/create_l2_tenant_evpn.rst

Details
```````

The create_l2_tenant_evpn workflow provisions an L2 domain extension in the BGP EVPN based IP fabric,
on the selected leaves or vLAG pairs.The workflow must be provided with the set of vLAG pairs or
leaf switches between which the layer 2 extension is required.

Requirements
````````````

This workflow is designed for use in IP Fabric EVPN networks only.

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

.. include:: /_includes/solutions/dcfabric/create_l3_tenant_evpn.rst

Details
```````

The Create_l3_tenant_evpn workflow provisions the BGP EVPN based IP fabric with an L3 tenant
identified by a VRF. This workflow provisions the vlan, VRF for the Layer 3 tenant at the identified
leaf switches or vLAG pairs, enables routing for the VRF across the IP fabric by enabling the
VRF address family in BGP and creating L3VNI interface and also enables redistribution of
connected routes in the VRF to BGP EVPN.

Requirements
````````````

This workflow is designed for operating in IP Fabric mode.

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

.. include:: /_includes/solutions/dcfabric/add_multihomed_endpoint.rst

.. include:: /_includes/solutions/dcfabric/add_multihomed_endpoint_and_gw_evpn.rst

Details
```````
The add_multihomed_endpoint_and_gw_evpn workflow automates the configuration of the edge ports of the
BGP EVPN based IP fabric. The workflow automates creation of port-channel interfaces (LAGs and
vLAGs), configuration of the port-channel interface as access or trunk, creation and association
of VLANs with the port-channel interfaces, validation of the port channel state as well as
creation of layer 3 gateway using Anycast Gateway protocol and modify ARP ND ageing on the
vLAG pair or leaf switch and association of the layer 3 gateways with a VRF. 

Requirements
````````````
This workflow is designed for use in IP Fabric with EVPN networks. 

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


IP Fabric Validation and Troubleshooting
----------------------------------------

.. include:: /_includes/solutions/dcfabric/get_flow_trace_ip_fabric.rst

.. include:: /_includes/solutions/dcfabric/query_topology.rst

.. include:: /_includes/solutions/dcfabric/show_config_bgp.rst

.. include:: /_includes/solutions/dcfabric/show_lldp_links.rst

.. include:: /_includes/solutions/dcfabric/show_vcs_links.rst


Manage VCS Fabric Tenants and Edge Ports
----------------------------------------

.. include:: /_includes/solutions/dcfabric/add_multihomed_endpoint.rst

Details
```````
The add_multihomed_endpoint workflow automates the configuration of the edge ports. 
The workflow automates creation of port-channel interfaces (LAGs and vLAGs), 
configuration of the port-channel interface as access or trunk, creation and
association of VLANs with the port-channel interfaces as well as validation of
the port channel state.

Requirements
````````````
This workflow is designed for operating on edge devices of IP Fabric, EVPN or VCS networks.

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
 
.. include:: /_includes/solutions/dcfabric/add_multihomed_endpoint_and_gw.rst

Details
```````
The add_multihomed_endpoint_and_gw workflow automates the addition of an endpoint which needs Layer
3 termination within the fabric. It automates the provisioning of both the edge ports 
as well as the VRRP-E based redundant gateway.

Requirements
````````````
This workflow is designed for use in IP Fabric (no EVPN) and VCS Fabric networks.

Output
``````

   result
       Boolean - True/False, if workflow succeeded

   ve_ip
       IP address assigned to the VE interface

   vrid
       Vrrpe Router ID assigned to the VE interface

.. include:: /_includes/solutions/dcfabric/add_singlehomed_endpoint.rst

.. include:: /_includes/solutions/dcfabric/configure_vrrpe_gw.rst

Requirements
````````````

This workflow is designed for use in IP Fabric, EVPN and VCS networks.

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

Misc
----
.. include:: /_includes/solutions/dcfabric/configure_anycast_gateway_evpn.rst

.. include:: /_includes/solutions/dcfabric/configure_anycast_gw_mac_evpn.rst

.. include:: /_includes/solutions/dcfabric/configure_conversational_arp_evpn.rst

.. include:: /_includes/solutions/dcfabric/configure_conversational_mac_evpn.rst

.. include:: /_includes/solutions/dcfabric/create_vrf_evpn.rst

.. include:: /_includes/solutions/dcfabric/configure_arp_nd_suppression.rst

.. include:: /_includes/solutions/dcfabric/configure_bgp_redistribute_connected.rst

.. include:: /_includes/solutions/dcfabric/configure_device_ipfabric.rst

.. include:: /_includes/solutions/dcfabric/configure_evpn_instance.rst

.. include:: /_includes/solutions/dcfabric/configure_evpn_vtep.rst

.. include:: /_includes/solutions/dcfabric/configure_interface_ipfabric.rst

.. include:: /_includes/solutions/dcfabric/configure_intfs_ipfabric.rst

.. include:: /_includes/solutions/dcfabric/modify_arp_nd_aging_ve.rst

.. include:: /_includes/solutions/dcfabric/provision_evpn_instance.rst

.. include:: /_includes/solutions/dcfabric/redistribute_connected_bgp_vrf.rst

.. include:: /_includes/solutions/dcfabric/set_max_path_bgp.rst
