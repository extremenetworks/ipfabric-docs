IP Fabric Solution
==================


About
-----

IP Fabric Solution is an open and programmable turnkey automation solution that
enables organizations to perform the following tasks:

*  Easily provision and validate the Data Center Infrastructure
*  Customize automation to optimize IT operations

It is a pre-packaged |st2|-based automation platform that supports **IP Fabric (IPF)** and
various other solutions.



#
MORE INFO HERE
#


IPF solution can provision and validate Brocade IP Fabrics and BGP-EVPN with minimal effort,
while support for open interfaces and commonly-used infrastructure programming tools enables
simple and straightforward customization when needed.

Through the IPF Cli, network engineers are able to perform the following tasks:

* Specify IP Fabric configuration parameters for automated provisioning
* Show device and IP Fabric state or configuration
* Manage IP Fabric device inventory
* Add, delete, or show specific IP Fabric topology information

This solution currently supports External Border Gateway Protocol (eBGP) workflow
to provision an IP Fabric. This can be handled in two ways:

* Using the Zero-Touch Provisioning (ZTP) process provided by Brocade VDX switches.
* Using a manual process with command line interface (CLI) commands or the
  REpresentational State Transfer (REST) application programming interface (API).

An eBGP-based workflow can be implemented in one of two ways:

* IP-based: Each interface on every link between the switches is assigned an IP address
  and eBGP is enabled on the switches using these physical interface IP addresses
* Unnumbered IP: A loopback port is created and assigned an IP address. These loopback
  IP addresses are then used to create BGP neighbors

IP Fabric Solution helps users monitor and configure an IP Fabric. IP Fabric Solution runs as a
daemon and provides CLI commands for functions such as the following:

* Assigning roles to the switches in the IP Fabric; "spine" or "leaf," based on discovery and connection
* Checking current configurations on the switches, such as IP address, RBridge ID, links, LLDP, ASN, and so on
* Specifying configurations that users want to be applied during IP Fabric provisioning, such as P2P IP range, leaf and ASN
  block, loopback port IP range, and so on
* Displaying IP Fabric topology details in various formats such as PDF, JPEG, and PNG
* Automatically configuring switches when they are added to the existing fabric
* Provisioning a two-member VCS cluster to support dual-homing to servers

ZTP is an automation solution designed to reduce errors and save time when IT needs to bring new
networking infrastructure online.

Currently VDX switches have ZTP enabled on them by default, which eases the configuration and
deployment of new switches when they boot. However, ZTP by itself is not sufficient to configure
switches to participate in an IP Fabric. IP Fabric Solution helps
users transition from a TRILL-based cluster to an IP Fabric deployment.
IP Fabric Solution also provides a CLI client that enables IP Fabric automation. With IP Fabric
Solution, you can specify configurations that you want for an IP Fabric, including:

* Spine Autonomous System Number (ASN) ranges
* Leaf ASN ranges
* Peer-to-Peer links
* Loopback port number
* BGP multi-hop setting
* BFD settings
* Basic extended virtual private network (EVPN) settings
* Loopback port IP range

IP Fabric Solution automatically configures switches when they are added to an IP Fabric, checks
the current configuration on the switches (IP Fabric Switches only), and displays IP Fabric
topology in a selected format (such as a PDF, JPEG, or PNG).

.. figure:: /_static/images/ipfabric_topology.jpg
    :align: center

    **IP fabric topology**

-----------------


Brocade IP Fabrics overview
---------------------------

Leaf-spine deployments are common in data center environments. Referred to generically as IP Clos
networks, they constitute the fundamental building blocks of an IP Fabric.

An IP Fabric is a collection of discrete Layer 3 elements (such as switches and routers)
arranged in a leaf-spine network. These elements exchange Layer 3 reachability information (by
means of BGP and/or OSPF) to provide a flexible and scalable framework. An IP Fabric can use 
Layer 3/Layer 2 information (such as MAC, IP routes distributed by BGP—including eBGP and iBGP
as well as OSPF) to exchange Layer 3 routing information.

For more detailed information, refer to the Brocade's Network OS IP Fabric Configuration Guide.

Data center networks deploy top-of-rack (ToR) and middle-of-rack (MoR) switches that function as
the leaf switches, which are attached to spine switches. The leaf switches are not connected to
each other physically, and spine switches connect only to leaf switches or an upstream core device.
For optional redundancy, servers or blades can be multihomed (dual-homed) to ToR switches in a
two-node VCS Fabric in logical chassis cluster mode by means of vLAG connections to the switches.

With IP Fabrics, where virtual machines (VMs) and physical servers sit behind leaf switches, it
is possible to have nodes in the same Layer 3 subnet spread across one or more leaf switches.
To provide connectivity among such nodes, the Layer 3 subnet is extended from one leaf switch
to the next leaf switch by means of virtual extensible local area networks (VXLANs). VXLAN
tunnels provide Layer 2 extension between VXLAN Tunnel Endpoints (VTEPs) over the Layer 3 
underlay network. VXLAN standards do not mandate a control-plane learning mechanism for Layer 2
reachability information. The most common technique implemented by networking vendors adopts
data-plane learning of Layer 2 reachability information on the data path. However, this is not
the most efficient way to learn MAC reachability information, because all the broadcast, unknown
unicast, and multicast (BUM) traffic is flooded on the data plane. To overcome scaling issues, a
standards-based control-plane learning mechanism (RFC 7432, BGP-EVPN) with VXLAN data 
encapsulation is implemented in Network OS 7.0.0 on Brocade VDX switches. This enables control-plane
learning of Layer 2 reachability information (MAC) and hosts (MAC-IP). This is achieved by binding
such information with the Border Gateway Protocol (BGP) control plane protocol, through the
introduction of an additional address family called Layer 2 Ethernet Virtual Private Network (EVPN)
as part of standards implementation. 

The following topology illustrates a 3-stage folded Clos topology with leafs and spines, with
connectivity to the DC core through border leaf nodes. These nodes provide external connectivity
to the data center fabric and also provide connectivity to network services such as firewalls
and load balancers.

.. figure:: /_static/images/3_clos_topology.jpg
      :align: center

      **3-Stage Folded Clos Topology**


What's Next?
-------------------------------
* Install and run Brocade Workflow Composer and IP Fabric solution - follow :doc:`install/index`
