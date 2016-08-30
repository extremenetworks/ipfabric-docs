|ipf|
==========================


Brocade Workflow Composer Overview
----------------------------------

|bwc| is a network automation platform that automates the entire network life
cycle and integrates with cross-domain workflows to improve business agility. Based on the
StackStorm Open Source Project, Workflow Composer provides DevOps-inspired network automation
using open source technologies to integrate with cross-domain systems for end-to-end workflow automation.

|bwc| enables organizations to:

* Automate the entire network lifecycle including: provisioning, validation, troubleshooting and remediation
* Eliminate cross-function workflow delays through event-driven cross-domain automation
* Embrace automation at your own pace with turnkey workflows and nearly 2000 pre-built points of integration;
  extend and customize to meet unique requirements with an architecture that is open at all layers
* Access broad community of like-minded peers to share ideas, collaborate, and support
* Leverage well-known tools and methods to ensure streamlined cross-domain integration

Brocade IP Fabrics
------------------

An IP Fabric is a collection of discrete Layer 3 elements (such as switches and routers)
arranged in a leaf-spine network. These elements exchange Layer 3 reachability information (by
means of BGP and/or OSPF) to provide a flexible and scalable framework. An IP Fabric can use
Layer 3/Layer 2 information (such as MAC, IP routes distributed by BGP—including eBGP and iBGP
as well as OSPF) to exchange Layer 3 routing information.

.. figure:: ../../_static/images/solutions/ipfabric/3_clos_topology.jpg
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

What's Next?
-------------------------------
* Install and run |bwc| and |ipf| - follow the :doc:`install` guide.
