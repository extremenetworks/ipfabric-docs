Using VCS Fabric 
================

These workflows can be used with VCS Fabric implementations. This document provides a summary of
what the workflows do - see the :doc:`reference documentation <../workflows>` for specific
details on requirements, parameters, return codes and error messages.

.. contents::
   :local:
   :depth: 1

Configure Edge Ports
--------------------

**Workflow Name: Configure_edge_ports**

The Configure_edge_ports workflow automates the configuration of the edge ports of the VCS fabric.
The workflow automates creation of port-channel interfaces (LAGs and vLAGs), configuration of the
port-channel interface as access or trunk, creation and association of VLANs with the port-channel
interfaces as well as validation of the port channel state.

This workflow must be used to automate the provisioning external layer 2 connections from the
VCS fabric. The external connections can be to endpoints in the network like physical hosts
or network services like load balancers and firewalls or can be to other networking devices
like Core devices.

Reference: :ref:`Configure_edge_ports<Configure_edge_ports>`

Configure VRRPe Gateway
-----------------------

**Workflow Name: Configure_vrrpe_gw**

The Configure_vrrpe_gw workflow automates the creation of a VRRP-E based default gateway
in a VCS fabric including the VE interfaces.

This workflow can be used for use cases where L3 boundary is present in the VCS fabric.
This could be at the spine in a VRRP-E based redundant gateway for the VLANs 
present in the fabric, the provisioning for which is automated through this workflow. 
It could also be used where the Layer 3 boundary is at the border leaves.

Reference: :ref:`Configure_vrrpe_gw<Configure_vrrpe_gw>`

Add L3 Tenant Endpoint
----------------------

** Workflow Name: Add_l3_tenant_endpoint**

The Add_l3_tenant_endpoint workflow automates the addition of an endpoint which needs
Layer 3 termination within the VCS fabric. It automates the provisioning of both the
edge ports as well as the VRRP-E based redundant gateway. It combines the actions in
Configure_edge_ports and Configure_vrrpe_gw.

Reference: :ref:`Add_l3_tenant_endpoint<Add_l3_tenant_endpoint>`
