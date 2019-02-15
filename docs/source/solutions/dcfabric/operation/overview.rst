Operation Overview
==================

Introduction
------------

This document provides an overview of how to use the DC Fabric Automation Suite to automate provisioning and 
maintenance of an IP or VCS Fabric. The DC Fabric Automation Suite can automatically configure
interfaces, BGP peerings and related settings. This ensures consistent configuration
across the fabric, with minimal effort.

.. note::
    This document covers the operation of the |bwc| DC Fabric Automation Suite. For more information
    about IP Fabrics in general, see the `Network OS IP Fabric
    Configuration Guide <https://documentation.extremenetworks.com/networkos/SW/73x/nos-730-ipfabrics.pdf>`_
    and the `IP Fabric Validated Design <https://www.extremenetworks.com/resources/extreme-validated-design/extreme-ip-fabric-architecture/>`_ 

The DC Fabric Automation Suite supports easy integration with Zero-Touch Provisioning (ZTP). It can also be used 
without ZTP, but initial switch setup and registration will be a manual process.

The default configuration has a set of predefined parameters used to create the fabric, such 
as ASN range, IP address ranges, etc. To see these parameters, and change them, refer to the
:ref:`IP Fabric parameters<ip_fabric_parameters>` documentation.

.. figure:: ../../../_static/images/solutions/dcfabric/bwc_components.jpg
    :align: center

    **Components of Extreme Workflow Composer**

.. note::
    The VCS ID for spine and leaves should be different in both the ZTP-enabled configuration and
    non-ZTP enabled configuration. If the VCS IDs are the same, the switches will automatically form an
    Ethernet fabric. For example, the VCS ID for spines can be 1 and for leaves it can be 2.

How to use DC Fabric Workflows
------------------------------

This section provides steps to setup an IP Fabric, and create L2 and L3 tenants on the fabric.
It includes examples to achieve key use cases with the sequence of workflow CLI as examples. 
IP Addresses used here are for example purposes only.

Setting up IP Fabric with EVPN
``````````````````````````````

1. First step to setup IP Fabric is to decide on the key fabric parameters. 
   Once the fabric parameters are decided, you can create a new fabric template with your parameters. 
   To create a new fabric, refer to :ref:`ip_fabric_parameters`. This example uses the default fabric
   so no action is necessary.

2. Next is to register the switches to the fabric created in the previous step.
   This example uses the default fabric. First switch added must be a spine, and the roles
   for the rest of the switches are automatically discovered by the DC Fabric Automation Suite. 
   
   Using ``bwc`` CLI you can register the switches as below:

   .. code-block:: bash

     bwc dcf inventory register fabric=default user=admin passwd=password host=10.70.60.47
     bwc dcf inventory register fabric=default user=admin passwd=password host=10.70.62.112
     bwc dcf inventory register fabric=default user=admin passwd=password host=10.70.61.37
     bwc dcf inventory register fabric=default user=admin passwd=password host=10.70.61.38
     bwc dcf inventory register fabric=default user=admin passwd=password host=10.70.61.21
   
   In this example: 
   10.70.60.47 and 10.70.62.112 are two spine switches.  
   10.70.61.37 & 10.70.61.38 are leafs in a vLAG pair  
   10.70.61.21 is a single ToR leaf (no vLAG)

3. After registering the switches, run the ``dcfabric.configure_fabric_infra`` workflow to configure IP
   Fabric underlay and EVPN instance on the switches:
   
   .. code-block:: bash

     st2 run dcfabric.configure_fabric_infra

4. To verify, review the action logs on the workflow or use the following commands directly on the switch:

   .. code-block:: guess
   
     show ip bgp summary rb all
     show bgp evpn summary rbridge-id all
     show bfd neighbors rbridge-id all
     show running-config rbridge-id evpn-instance
     show overlay-gateway 

IP Fabric EVPN - L2 Tenant endpoint provisioning on MCT lag or vLAG pair
````````````````````````````````````````````````````````````````````````

Here are the steps to configure L2 tenant on a dual ToR pair:

1. Use ``dcfabric.add_multihomed_endpoint`` to configure edge ports facing end points such as a server.
   This workflow automates creation of port-channel interfaces, configuration of the port-channel
   interface as access or trunk, creation and association of VLANs with the port-channel interfaces
   and MCT client configuration as well as validation of the port channel state.

   The workflow needs to be run on both ToRs part of MCT cluster as below:

   Example MCT LAG with Bridge Domain usecase (SLX):

   .. code-block:: bash

      st2 run dcfabric.add_multihomed_endpoint mgmt_ip=10.20.60.121 intf_type=ethernet ports=0/22,0/24 port_channel_id=2 network_id=4001-4010 c_tag=201-210 auto_pick_lif_id=True vlan_type=tagged mct_client_name=demo_123 vni=201-210 enabled=True mct_client_id=512 intf_desc=standalone mode=standard protocol=modeon mtu=9100

      st2 run dcfabric.add_multihomed_endpoint mgmt_ip=10.20.60.122 intf_type=ethernet ports=0/22,0/24 port_channel_id=2 network_id=4001-4010 c_tag=201-210 auto_pick_lif_id=True vlan_type=tagged mct_client_name=demo_123 vni=201-210 enabled=True mct_client_id=512 intf_desc=standalone mode=standard protocol=modeon mtu=9100

   Example MCT LAG with VLAN usecase (SLX):
   
   .. code-block:: bash

      st2 run dcfabric.add_multihomed_endpoint mgmt_ip=10.20.60.121 intf_type=ethernet ports=0/22,0/24 port_channel_id=2 network_id=4001-4010 c_tag=201-210 auto_pick_lif_id=True vlan_type=tagged mct_client_name=demo_123 vni=201-210 enabled=True mct_client_id=512 intf_desc=standalone mode=standard protocol=modeon mtu=9100

      st2 run dcfabric.add_multihomed_endpoint mgmt_ip=10.20.60.122 intf_type=ethernet ports=0/22,0/24 port_channel_id=2 network_id=4001-4010 c_tag=201-210 auto_pick_lif_id=True vlan_type=tagged mct_client_name=demo_123 vni=201-210 enabled=True mct_client_id=512 intf_desc=standalone mode=standard protocol=modeon mtu=9100

   The workflow runs the following show commands on the switch and logs the results. You can review
   this in the action results. Or you can directly run the following commands on the switch to verify:
   
   .. code-block:: guess

     show port-channel 400 
     show running-config interface ethernet 0/22
     show running-config interface ethernet 0/24
    
   Example vLAG (VDX):

   .. code-block:: bash

     st2 run dcfabric.add_multihomed_endpoint mgmt_ip=10.70.61.37 vlan_id=201 intf_desc="customer-a" intf_type=tengigabitethernet ports=37/0/11,38/0/11 port_channel_id=400 mode=standard protocol=active 

   The workflow runs the following show commands on the switch and logs the results. You can review
   this in the action results. Or you can directly run the following commands on the switch to verify:
   
   .. code-block:: guess

     show port-channel 400 
     show running-config interface TenGigabitEthernet 37/0/11
     show running-config interface TenGigabitEthernet 38/0/11

2. Next, use the ``create_l2_tenant_evpn`` workflow to provision an L2 domain extension, on the MCT or vLAG pairs. 

   Example MCT (SLX):

   The workflow must be run on both the switches part of MCT cluster. This example, provides the management IP of the swtich to attach the VNI created in the previous setp to EVPN instance:
   
   .. code-block:: bash

    st2 run dcfabric.create_l2_tenant_evpn mgmt_ip=10.20.60.121 bridge_domain_id=4001-4010
    st2 run dcfabric.create_l2_tenant_evpn mgmt_ip=10.20.60.122 bridge_domain_id=4001-4010

    or

    st2 run dcfabric.create_l2_tenant_evpn mgmt_ip=10.20.60.121 vlan_id=10-20 
    st2 run dcfabric.create_l2_tenant_evpn mgmt_ip=10.20.60.122 vlan_id=10-20 

   Example vLAG (VDX):

   The workflow must be provided with the management IP of the vLAG pair or the leaf switch. In this example, provide the management IP of the vLAG pair in order to attach the VNI created in the previous step to EVPN instance:
   
   .. code-block:: bash

     st2 run dcfabric.create_l2_tenant_evpn mgmt_ip=10.70.61.37 vni=201
   
   To verify, review the action logs on the workflow or use the following commands directly on the switch:
   
   .. code-block:: bash

     show running-config rbridge-id evpn-instance

IP Fabric EVPN - L2 Tenant provisioning on a single ToR
```````````````````````````````````````````````````````

Here are the steps to configure an L2 tenant on a single ToR (non vLAG):

1. Use ``network_essentials.add_singlehomed_endpoint`` to configure edge ports facing end points such as a
   server. This workflow automates configuration of the interface as access or trunk, and the creation and
   association of VLANs with the interface.
   
   Example (SLX):

   .. code-block:: bash

     st2 run dcfabric.add_multihomed_endpoint mgmt_ip=10.20.60.123 intf_type=ethernet ports=0/10,0/11 auto_pick_port_channel_id=True vlan_id=10-20 vni=110-120
    
     st2 run dcfabric.create_l2_tenant_evpn mgmt_ip=10.20.60.123 vlan_id=10-20 

   Example (VDX):

   .. code-block:: bash

      st2 run network_essentials.add_singlehomed_endpoint mgmt_ip=10.70.61.21 vlan_id=201 intf_desc="customer-a" intf_type=tengigabitethernet intf_name=21/0/1 switchport_mode=trunk 

   To verify, review the action logs on the workflow or use the following commands directly on the switch:
   
   .. code-block:: bash

     show running-config interface TenGigabitEthernet 21/0/1

2. Next, use the ``create_l2_tenant_evpn`` workflow to provision an L2 domain extension in the BGP
   EVPN based IP fabric, on the selected leaves or vLAG pairs. The workflow must be provided with the
   management IP of the vLAG pair or leaf switch between which the layer 2 extension is required.
   In this example, provide the management IP of the single ToR in order to attach the VNI created in the
   previous setp to EVPN instance:
   
   .. code-block:: bash

     st2 run dcfabric.create_l2_tenant_evpn mgmt_ip=10.70.61.21 vni=201
   
   To verify, review the action logs on the workflow or use the following commands directly on the switch:
   
   .. code-block:: guess

     show running-config rbridge-id evpn-instance
     show vlan 201
     show tunnel brief

IP Fabric EVPN - L3 Tenant provisioning on vLAG pair (VDX)
``````````````````````````````````````````````````````````

Here are the steps to configure an L3 tenant on a vLAG pair:

1. Use ``dcfabric.create_l3_tenant_evpn`` workflow to provision an L3 tenant identified by a VRF.
   This workflow provisions the VRF for the Layer 3 tenant at the identified leaf switches or vLAG
   pairs, enables routing for the VRF across the IP fabric by enabling the VRF address family in BGP
   and creating L3VNI interface. This workflow also enables redistribution of connected routes in the VRF to BGP
   EVPN. The workflow must be provided with the virtual management IP of a vLAG pair or the management IP
   of a leaf switch on which the layer 3 services for the VRF are required.
   
   .. code-block:: bash

    st2 run dcfabric.create_l3_tenant_evpn mgmt_ip=10.70.61.37 vrf_name=vrf2 l3vni=500 route_distinguisher=172.32.254.5,172.32.254.6 tenant_addressing_type=both rt=101
   
   To verify, review the action logs on the workflow or use the following commands directly on the switch:
   
   .. code-block:: guess

     show running-config rbridge-id vrf vrf2 
     show running-config rbridge-id interface ve 500 
     show running-config rbridge-id router bgp address-family ipv4 unicast vrf vrf2 

2. Use ``dcfabric.add_multihomed_endpoint_and_gw_evpn`` workflow to automate the configuration of the edge
   ports of the IP Fabric with EVPN. This workflow automates creation of port-channel interfaces (LAGs
   and vLAGs), configuration of the port-channel interface as access or trunk, creation and
   association of VLANs with the port-channel interfaces, validation of the port channel state as
   well as creation of layer 3 gateway using Anycast Gateway protocol on the vLAG pair and association
   of the layer 3 gateways with a VRF.
   
   .. code-block:: bash

     st2 run dcfabric.add_multihomed_endpoint_and_gw_evpn mgmt_ip=10.70.61.37 intf_desc="customer-a" intf_name=37/0/11,38/0/11 vlan_id=201 switchport_mode=trunk arp_aging_type=arp_aging anycast_address=10.70.20.20/24 vrf_name=vrf2 auto_pick_port_channel_id=true
   
   To verify, review the action logs on the workflow or use the following commands directly on the switch:
   
   .. code-block:: guess

     show port-channel <use the number, autopicked by the workflow>
     show running-config interface TenGigabitEthernet 37/0/11
     show running-config interface TenGigabitEthernet 38/0/11
     show running-config rbridge-id interface ve 201

IP Fabric EVPN - L3 Tenant provisioning on a single ToR (non vLAG)
``````````````````````````````````````````````````````````````````

Here are the steps to configure L3 tenant on a vLAG pair:

1. User ``dcfabric.create_l3_tenant_evpn`` workflow to provision an L3 tenant identified by a VRF.
   This workflow provisions the VRF for the Layer 3 tenant at the identified leaf switches or
   vLAG pairs, enables routing for the VRF across the IP fabric by enabling the VRF address
   family in BGP and creating L3VNI interface. This workflow also enables redistribution of connected
   routes in the VRF to BGP EVPN. The workflow must be provided with the virtual management IP
   the leaf switch on which the layer 3 services for the VRF are required.

   .. code-block:: bash

     st2 run dcfabric.create_l3_tenant_evpn mgmt_ip=10.70.61.21 vrf_name=vrf2 l3vni=500 route_distinguisher=172.32.254.8 tenant_addressing_type=both rt=101

2. Use ``dcfabric.add_multihomed_endpoint_and_gw_evpn`` workflow to automate the configuration of the
   edge ports of IP Fabric with EVPN. This workflow automates creation of port-channel interfaces
   (LAGs and vLAGs), configuration of the port-channel interface as access or trunk, creation and
   association of VLANs with the port-channel interfaces, validation of the port channel state as
   well as creation of layer 3 gateway using Anycast Gateway protocol on the leaf switch and
   association of the layer 3 gateways with a VRF.
   
   .. code-block:: bash

     st2 run dcfabric.add_multihomed_endpoint_and_gw_evpn mgmt_ip=10.70.61.21 intf_desc="customer-a" intf_name=21/0/1 vlan_id=201 switchport_mode=trunk arp_aging_type=arp_aging anycast_address=10.70.70.20/24 vrf_name=vrf2 
   
   To verify, review the action logs on the workflow or use the following commands directly on the switch:
   
   .. code-block:: guess

     show vlan 500


.. rubric:: What's Next?

* Running IP Fabric? Read the :doc:`using_ipfabric` docs.
* VCS Fabric? Check out the :doc:`using_vcsfabric` workflows.
* Deeper reference? Check the :doc:`../workflows`, :doc:`CLI <../dcf_cli/basic_cli>`, or :doc:`ZTP <../ztp_reference>` references.
