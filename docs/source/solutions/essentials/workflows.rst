Workflows
=========

This document provides an overview of how to use the Network Essentials workflows and actions
with Brocade VDX and SLX switches. These actions can be used as independent actions,
or as part of a more complex workflow. :doc:`Actions</actions>` can be manually triggered,
or they can be tied to :doc:`sensors </sensors>` using rules.

.. note::
    Content is still being added to this section

Actions
-------

.. contents::
   :local:
   :depth: 1
 
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