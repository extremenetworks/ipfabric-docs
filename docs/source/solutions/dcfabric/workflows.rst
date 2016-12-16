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
    This is all placeholder text in this section right now

.. _configure_edge_ports:

configure_edge_ports
~~~~~~~~~~~~~~~~~~~~

Description
```````````

This workflow automates the configuration of the edge ports of the VCS fabric.
The workflow automates creation of port-channel interfaces (LAGs and vLAGs), configuration of the
port-channel interface as access or trunk, creation and association of VLANs with the port-channel
interfaces as well as validation of the port channel state.

Requirements
````````````

This workflow is designed for VDX switches operating in either VCS Fabric or IP Fabric mode. It is not
designed for SLX switches. This fabric must already be registered with the |bwc| inventory service.

Parameters
``````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   customer_name
       Customer name. This will be used in VRF & VLAN description. Must be text string, 0-255 characters.

   fabric
       Name of the fabric. This must already be registered with the inventory service.

   vlan_range
       VLAN range to be used for customer. Should be provided as range, e.g. 50-60,70.

   gateway_ip
       VRRPe gateway IP to use for customer.

Output
``````


.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   result
       Boolean - True/False, if workflow succeeded

   rd
       RD auto-assigned to tenant

Error Messages
``````````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   "Invalid VLAN ID"
       Returned if VLAN(s) provided are invalid, e.g. > 4094.

   "Unknown Fabric"
       Returned if fabric is not registered. 

.. _configure_interface_vlan:

configure_interface_vlan
~~~~~~~~~~~~~~~~~~~~~~~~

This workflow can be used to configure or modify edge Layer 2 interfaces of the VCS fabric.
However, unlike configure_edge_ports, this workflow does not create the corresponding VLANs
or perform any validation.

Requirements
````````````

This workflow is designed for VDX switches operating in either VCS Fabric or IP Fabric mode. It is not
designed for SLX switches. This fabric must already be registered with the |bwc| inventory service.

Parameters
``````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   customer_name
       Customer name. This will be used in VRF & VLAN description. Must be text string, 0-255 characters.

   fabric
       Name of the fabric. This must already be registered with the inventory service.

   vlan_range
       VLAN range to be used for customer. Should be provided as range, e.g. 50-60,70.

   gateway_ip
       VRRPe gateway IP to use for customer.

Output
``````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   result
       Boolean - True/False, if workflow succeeded

   rd
       RD auto-assigned to tenant

Error Messages
``````````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   "Invalid VLAN ID"
       Returned if VLAN(s) provided are invalid, e.g. > 4094.

   "Unknown Fabric"
       Returned if fabric is not registered. 


.. _configure_vrrpe_gw:

configure_vrrpe_gw
~~~~~~~~~~~~~~~~~~

The configure_vrrpe_gw workflow automates the creation of a VRRP-E based default gateway
in a VCS fabric including the VE interfaces.

Requirements
````````````

This workflow is designed for VDX switches operating in either VCS Fabric or IP Fabric mode. It is not
designed for SLX switches. This fabric must already be registered with the |bwc| inventory service.

Parameters
``````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   customer_name
       Customer name. This will be used in VRF & VLAN description. Must be text string, 0-255 characters.

   fabric
       Name of the fabric. This must already be registered with the inventory service.

   vlan_range
       VLAN range to be used for customer. Should be provided as range, e.g. 50-60,70.

   gateway_ip
       VRRPe gateway IP to use for customer.

Output
``````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   result
       Boolean - True/False, if workflow succeeded

   rd
       RD auto-assigned to tenant

Error Messages
``````````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   "Invalid VLAN ID"
       Returned if VLAN(s) provided are invalid, e.g. > 4094.

   "Unknown Fabric"
       Returned if fabric is not registered. 


.. _add_l3_tenant_endpoint:

add_l3_tenant_endpoint
~~~~~~~~~~~~~~~~~~~~~~

The add_l3_tenant_endpoint workflow automates the addition of an endpoint which needs
Layer 3 termination within the VCS fabric. It automates the provisioning of both the
edge ports as well as the VRRP-E based redundant gateway. It combines the actions in
:ref: `configure_edge_ports` and :ref: `configure_vrrpe_gw`.

Requirements
````````````

This workflow is designed for VDX switches operating in either VCS Fabric or IP Fabric mode. It is not
designed for SLX switches. This fabric must already be registered with the |bwc| inventory service.

Parameters
``````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   customer_name
       Customer name. This will be used in VRF & VLAN description. Must be text string, 0-255 characters.

   fabric
       Name of the fabric. This must already be registered with the inventory service.

   vlan_range
       VLAN range to be used for customer. Should be provided as range, e.g. 50-60,70.

   gateway_ip
       VRRPe gateway IP to use for customer.

Output
``````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   result
       Boolean - True/False, if workflow succeeded

   rd
       RD auto-assigned to tenant

Error Messages
``````````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   "Invalid VLAN ID"
       Returned if VLAN(s) provided are invalid, e.g. > 4094.

   "Unknown Fabric"
       Returned if fabric is not registered. 

.. _create_l2_tenant_evpn:

create_l2_tenant_evpn
~~~~~~~~~~~~~~~~~~~~~

The create_l2_tenant_evpn workflow provisions an L2 domain extension in the BGP
EVPN based IP fabric, on the selected leaves or vLAG pairs. The workflow must be
provided with the set of vLAG pairs or leaf switches between which the Layer 2
extension is required.

Requirements
````````````

This workflow is designed for VDX switches operating in either VCS Fabric or IP Fabric mode. It is not
designed for SLX switches. This fabric must already be registered with the |bwc| inventory service.

Parameters
``````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   customer_name
       Customer name. This will be used in VRF & VLAN description. Must be text string, 0-255 characters.

   fabric
       Name of the fabric. This must already be registered with the inventory service.

   vlan_range
       VLAN range to be used for customer. Should be provided as range, e.g. 50-60,70.

   gateway_ip
       VRRPe gateway IP to use for customer.

Output
``````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   result
       Boolean - True/False, if workflow succeeded

   rd
       RD auto-assigned to tenant

Error Messages
``````````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   "Invalid VLAN ID"
       Returned if VLAN(s) provided are invalid, e.g. > 4094.

   "Unknown Fabric"
       Returned if fabric is not registered.

.. _add_l2_tenant_endpoint_evpn:

add_l2_tenant_endpoint_evpn
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The add_l2_tenant_endpoint_evpn is an alias for configure_edge_ports and hence performs
the same automation actions. Once Layer 2 extension is created in a BGP EVPN based IP
fabric using create_l2_tenant_evpn workflow, the connection of a network endpoint requiring
layer 2 extension, to the vLAG pairs can be configured using this workflow.

Requirements
````````````

This workflow is designed for VDX switches operating in either VCS Fabric or IP Fabric mode. It is not
designed for SLX switches. This fabric must already be registered with the |bwc| inventory service.

Parameters
``````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   customer_name
       Customer name. This will be used in VRF & VLAN description. Must be text string, 0-255 characters.

   fabric
       Name of the fabric. This must already be registered with the inventory service.

   vlan_range
       VLAN range to be used for customer. Should be provided as range, e.g. 50-60,70.

   gateway_ip
       VRRPe gateway IP to use for customer.

Output
``````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   result
       Boolean - True/False, if workflow succeeded

   rd
       RD auto-assigned to tenant

Error Messages
``````````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   "Invalid VLAN ID"
       Returned if VLAN(s) provided are invalid, e.g. > 4094.

   "Unknown Fabric"
       Returned if fabric is not registered.

.. _create_l3_tenant_evpn:

create_l3_tenant_evpn
~~~~~~~~~~~~~~~~~~~~~

The create_l3_tenant_evpn workflow provisions the BGP EVPN based IP fabric with an L3
tenant identified by a VRF. This workflow provisions the VRF for the Layer 3 tenant
at the identified leaf switches or vLAG pairs, enables routing for the VRF across
the IP fabric by enabling the VRF address family in BGP and creating L3VNI interface
and also enables redistribution of connected routes in the VRF to BGP EVPN. The
workflow must be provided with the set of vLAG pairs or leaf switches between which
the layer 3 services for the VRF are required.

Requirements
````````````

This workflow is designed for VDX switches operating in either VCS Fabric or IP Fabric mode. It is not
designed for SLX switches. This fabric must already be registered with the |bwc| inventory service.

Parameters
``````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   customer_name
       Customer name. This will be used in VRF & VLAN description. Must be text string, 0-255 characters.

   fabric
       Name of the fabric. This must already be registered with the inventory service.

   vlan_range
       VLAN range to be used for customer. Should be provided as range, e.g. 50-60,70.

   gateway_ip
       VRRPe gateway IP to use for customer.

Output
``````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   result
       Boolean - True/False, if workflow succeeded

   rd
       RD auto-assigned to tenant

Error Messages
``````````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   "Invalid VLAN ID"
       Returned if VLAN(s) provided are invalid, e.g. > 4094.

   "Unknown Fabric"
       Returned if fabric is not registered.

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

Requirements
````````````

This workflow is designed for VDX switches operating in either VCS Fabric or IP Fabric mode. It is not
designed for SLX switches. This fabric must already be registered with the |bwc| inventory service.

Parameters
``````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   customer_name
       Customer name. This will be used in VRF & VLAN description. Must be text string, 0-255 characters.

   fabric
       Name of the fabric. This must already be registered with the inventory service.

   vlan_range
       VLAN range to be used for customer. Should be provided as range, e.g. 50-60,70.

   gateway_ip
       VRRPe gateway IP to use for customer.

Output
``````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   result
       Boolean - True/False, if workflow succeeded

   rd
       RD auto-assigned to tenant

Error Messages
``````````````

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   "Invalid VLAN ID"
       Returned if VLAN(s) provided are invalid, e.g. > 4094.

   "Unknown Fabric"
       Returned if fabric is not registered.