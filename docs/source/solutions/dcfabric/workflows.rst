Workflows
=========

This document provides an overview of how to use the DC Fabric Automation Suite workflows
with Brocade VDX and SLX switches. These can be used as independent workflows, or tied
together to form more complex workflows. They can be manually triggered,
or they can be tied to :doc:`sensors </sensors>` using rules.

.. contents::
   :local:
   :depth: 1

.. note::
    Content is still being added to this section

.. _configure_edge_ports:

configure_edge_ports
~~~~~~~~~~~~~~~~~~~~

Description
```````````

This workflow automates the configuration of the edge ports of the VCS fabric.
The workflow automates creation of port-channel interfaces (LAGs and vLAGs), configuration of the
port-channel interface as access or trunk, creation and association of VLANs with the port-channel
interfaces as well as validation of the port channel state.

.. _configure_interface_vlan:

configure_interface_vlan
~~~~~~~~~~~~~~~~~~~~~~~~

This workflow can be used to configure or modify edge Layer 2 interfaces of the VCS fabric.
However, unlike configure_edge_ports, this workflow does not create the corresponding VLANs
or perform any validation.
 
.. _configure_vrrpe_gw:

configure_vrrpe_gw
~~~~~~~~~~~~~~~~~~

The configure_vrrpe_gw workflow automates the creation of a VRRP-E based default gateway
in a VCS fabric including the VE interfaces.

.. _add_l3_tenant_endpoint:

add_l3_tenant_endpoint
~~~~~~~~~~~~~~~~~~~~~~

The add_l3_tenant_endpoint workflow automates the addition of an endpoint which needs
Layer 3 termination within the VCS fabric. It automates the provisioning of both the
edge ports as well as the VRRP-E based redundant gateway. It combines the actions in
:ref: `configure_edge_ports` and :ref: `configure_vrrpe_gw`.

.. _create_l2_tenant_evpn:

create_l2_tenant_evpn
~~~~~~~~~~~~~~~~~~~~~

Description
```````````

The create_l2_tenant_evpn workflow provisions an L2 domain extension in the BGP EVPN based IP fabric,
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


.. _add_l2_tenant_endpoint_evpn:

add_l2_tenant_endpoint_evpn
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The add_l2_tenant_endpoint_evpn is an alias for configure_edge_ports and hence performs
the same automation actions. Once Layer 2 extension is created in a BGP EVPN based IP
fabric using create_l2_tenant_evpn workflow, the connection of a network endpoint requiring
layer 2 extension, to the vLAG pairs can be configured using this workflow.

.. _create_l3_tenant_evpn:

create_l3_tenant_evpn
~~~~~~~~~~~~~~~~~~~~~

Description
```````````

The create_l3_tenant_evpn workflow provisions the BGP EVPN based IP fabric with an L3 tenant
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

.. _add_l3_tenant_endpoint_evpn:

add_l3_tenant_endpoint_evpn
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The add_l3_tenant_endpoint_evpn workflow automates the configuration of the edge
ports of the BGP EVPN based IP fabric. The workflow automates creation of
port-channel interfaces (LAGs and vLAGs), configuration of the port-channel
interface as access or trunk, creation and association of VLANs with the port-channel
interfaces, validation of the port channel state as well as creation of layer 3
gateway using Anycast Gateway protocol on the vLAG pair or leaf switch and
association of the layer 3 gateways with a VRF.