|ipf|
==========================

.. warning::

    All Automation Suites are currently in "Technology Preview" phase. We are releasing them
    to gain additional feedback, but do not recommend running them in production. We encourage
    people to try them out in non-production scenarios. They have had basic testing, but are
    not fully supported by Brocade TAC.

Brocade IP Fabrics
------------------

An IP Fabric is a collection of discrete Layer 3 elements (such as switches and routers)
arranged in a leaf-spine network. These elements exchange Layer 3 reachability information (by
means of BGP and/or OSPF) to provide a flexible and scalable framework. An IP Fabric can use
Layer 3/Layer 2 information (such as MAC, IP routes distributed by BGP—including eBGP and iBGP
as well as OSPF) to exchange Layer 3 routing information.

.. figure:: ../../_static/images/solutions/dcfabric/3_clos_topology.jpg
      :align: center

      **3-Stage Folded Clos Topology**

For more information about Brocade IP Fabrics, see the `Brocade Network OS IP Fabric Configuration
Guide <http://www.brocade.com/content/html/en/configuration-guide/nos-701-ipfabrics/index.html>`_

|ipf| Overview
-----------------------------------

The |ipf| is an add-on package for |bwc| that provides services and pre-built automations for managing
Brocade IP Fabrics. It can provision and validate Brocade IP Fabrics and BGP-EVPN with minimal effort.
It can easily be customized as required.

|ipf| helps users monitor and configure an IP Fabric. It can be used to:

* Assign roles to the switches in the IP Fabric: *Spine* or *Leaf*, based on discovered connections.
* Check current configurations on the switches, such as IP address, RBridge ID, links, LLDP, ASN, etc.
* Specify configurations to be applied during IP Fabric provisioning, such as P2P IP range, ASN block,
  loopback port IP range, BFD, EVPN configuration, etc.
* Display IP Fabric topology details in various formats such as PDF, JPEG, and PNG.
* Integrate with ZTP to automatically configure switches when they are added to the existing fabric.
* Provision two-member leaf VCS clusters to support server dual-homing.

This automation suite currently supports the External Border Gateway Protocol (eBGP) workflow to provision
an IP Fabric on VDX switches. This can be fully automated, or triggered manually via CLI or API.

The eBGP-based workflow supports both IP numbered & unnumbered configurations.

* IP-based(IP numbered): Each interface on every link between the switches is assigned an IP address
  and eBGP peerings use these IP addresses. This is the default.
* Unnumbered: A loopback interface is created and assigned an IP address. These loopback IP addresses
  are used for BGP peering

Supported Devices
~~~~~~~~~~~~~~~~~

The |ipf| supports the following devices:

* Brocade VDX 6740 running Network OS 7.0.1a and later
* Brocade VDX 6940 running Network OS 7.0.1a and later
* Brocade VDX 8770 running Network OS 7.0.1a and later
* Brocade SLX 9850 running SLX-OS 16r.1.01 and later

What's Next?
-------------------------------
* Install and run |bwc| and |ipf| - follow the :doc:`install` guide.
