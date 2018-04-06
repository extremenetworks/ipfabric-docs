Network Essentials
==================

Overview
--------

Network Essentials Automation Suite includes key foundational actions and workflows to automate Extreme Networks
devices. This release includes automation building blocks for common networking tasks such as Edge
Ports configuration and validation, and Access Control List management. These basic building blocks are
used by other Automation Suites. Customers can also use the Network Essentials Automation Suite Actions in creating their own custom
workflows for their specific automation needs.

Included Actions
----------------

High level summary of the Actions included in this release:

  * Edge Ports Configuration
  
    - Configuration and deletion of VLAN, Port Channel, VE, VRRPe, VRF on a switch
    
    - Configuration of Access or Trunk VLANs on interfaces
 
    - Setting MTU size at an interface level or system level
    
    - Applying or removing an ACL on the interfaces

  * ACL Management
  
    - Creation and deletion of L2 or L3 ACLs 
    
    - Adding or removing IPv4 or IPv6 rules to an ACL

  * Validation and Troubleshooting
 
    - Validation of VLAN, Port Channel, VE, VRRPe, VRF on a switch
    
    - Ping and validate connectivity from a switch to target IPs using the specified VRF

    - Find to which switch, and interface a physical or virtual host is connected to using the IP or MAC address of the host

For more information about each action, read the :doc:`workflows` guide.

Supported Devices
-----------------

The Network Essentials Automation Suite supports VDX, SLX and MLXe device families. However, this Tech Preview release has been explicitly tested with the following device & OS combinations only:

* SLX SLX 9140, 9240 with SLX OS 17s.1.02 
* SLX 9540, 9850 with SLX OS 17r.1.01ad, 17r.2.01  
* VDX NOS 7.1.0a, 7.2.0a 
* NetIron NI 5.8.0f, 6.0.0d


.. rubric:: What's Next?

* Install and run |bwc| and Network Essentials - follow the :doc:`install` guide.
* Learn more about the available actions - read the :doc:`workflows` guide.
