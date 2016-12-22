Using IP Fabric 
===============

These workflows can be used with IP Fabric implementations. This document provides a summary of
what the workflows do - see the :doc:`reference documentation <../workflows>` for specific
details on requirements, parameters, return codes and error messages.

.. contents::
   :local:
   :depth: 1

Configure Edge Ports
--------------------

**Workflow Name: configure_edge_ports**

The configure_edge_ports workflow automates the configuration of the edge ports of the IP fabric.
The workflow automates creation of port-channel interfaces (LAGs and vLAGs), configuration of the
port-channel interface as access or trunk, creation and association of VLANs with the port-channel
interfaces as well as validation of the port channel state.

This workflow must be used to automate the provisioning external layer 2 connections from the IP
fabric. The external connections can be to endpoints in the network like physical hosts or
network services like load balancers and firewalls or can be to other networking devices like
Core devices from the border leaf.

Reference: :ref:`configure_edge_ports<configure_edge_ports>`

Configure VRRPe Gateway
-----------------------

**Workflow Name: configure_vrrpe_gw**

The configure_vrrpe_gw workflow automates the creation of a VRRP-E based default gateway
in an IP fabric vLAG pair including the VE interfaces.

This workflow can be used to create the L3 boundary at the leaf vLAG pair
of the IP Fabric. 

Reference: :ref:`configure_vrrpe_gw<configure_vrrpe_gw>`

Add L3 Tenant Endpoint
----------------------

** Workflow Name: add_l3_tenant_endpoint**

The add_l3_tenant_endpoint workflow automates the addition of an endpoint along with
the provisioning of the Layer 3 gateway at leaf vLAG pair. It automates the provisioning
of both the edge ports as well as the VRRP-E based redundant gateway. It combines the
actions in configure_edge_ports and configure_vrrpe_gw

Reference: :ref:`Add_l3_tenant_endpoint<Add_l3_tenant_endpoint>`

BGP EVPN-Specific Workflows
---------------------------

.. note::
    The workflows below are specific to IP Fabric with BGP-EVPN.

Create L2 Tenant EVPN
~~~~~~~~~~~~~~~~~~~~~

** Workflow Name: Create_l2_tenant_evpn**

The Create_l2_tenant_evpn workflow provisions an L2 domain extension in the BGP
EVPN based IP fabric, on the selected leaves or vLAG pairs. The workflow must be
provided with the set of vLAG pairs or leaf switches between which the Layer 2
extension is required.

After the switch is added to the fabric, this workflow can be used to create a
Layer 2 extension within the BGP EVPN IP fabric. The VNI to be used for the
Layer 2 extension is an input to this workflow. The extension of the VNI across
the set of vLAG pairs or leaf switches is automated by this workflow. No edge port
provisioning is performed in this workflow.

Reference: :ref:`Create_l2_tenant_evpn<Create_l2_tenant_evpn>`

Create L3 Tenant EVPN
~~~~~~~~~~~~~~~~~~~~~

** Workflow Name: Create_l3_tenant_evpn**

The create_l3_tenant_evpn workflow provisions the BGP EVPN based IP fabric with an L3
tenant identified by a VRF. This workflow provisions the VRF for the Layer 3 tenant
at the identified leaf switches or vLAG pairs, enables routing for the VRF across
the IP fabric by enabling the VRF address family in BGP and creating L3VNI interface
and also enables redistribution of connected routes in the VRF to BGP EVPN. The
workflow must be provided with the set of vLAG pairs or leaf switches between which
the layer 3 services for the VRF are required.

After the switch is added to the fabric, this workflow can be used to create a layer 3
VRF routing services within the BGP EVPN IP fabric. No edge port provisioning is performed
in this workflow.

Reference: :ref:`Create_l3_tenant_evpn<Create_l3_tenant_evpn>`

Add L3 Tenant Endpoint EVPN
~~~~~~~~~~~~~~~~~~~~~~~~~~~

** Workflow Name: add_l3_tenant_endpoint_evpn**

The add_l3_tenant_endpoint_evpn workflow automates the configuration of the edge
ports of the BGP EVPN based IP fabric. The workflow automates creation of
port-channel interfaces (LAGs and vLAGs), configuration of the port-channel
interface as access or trunk, creation and association of VLANs with the port-channel
interfaces, validation of the port channel state as well as creation of layer 3
gateway using Anycast Gateway protocol on the vLAG pair or leaf switch and
association of the layer 3 gateways with a VRF.

Once Layer 3 VRF routing services are created in a BGP EVPN based IP fabric using
create_l3_tenant_evpn workflow, the connection of a network endpoint requiring
layer 3 VRF routing services and a default gateway can be configured using this workflow.

Reference: :ref:`add_l3_tenant_endpoint_evpn<add_l3_tenant_endpoint_evpn>`
