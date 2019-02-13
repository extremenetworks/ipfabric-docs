Overview
========

Automation Suites are collections of workflows, actions, sensors and services that target
specific networking use-cases, e.g. Data Center Fabric architectures, or Internet Exchanges.
They deliver turnkey workflows for provisioning, validation, troubleshooting and remediation
workflows.

These are installed on top of |ewc|. Users can install one or more suites. Suites may have
dependencies - e.g. the Network Essentials suite is foundational for other suites.

Users may modify these workflows to customise them to their needs.

Network Essentials
~~~~~~~~~~~~~~~~~~

Network Essentials is a foundational set of workflows for operating Extreme network devices. It
includes actions such as edge port provisioning, ACL management etc. These are basic building
blocks that are used by other suites. Customers can also use these blocks to create their own
customised workflows.

Starting with v1.2 supports Extreme SLX, VDX and MLXe device families. See more details :doc:`here<essentials/overview>`.

DC Fabric
~~~~~~~~~~

The DC Fabric Automation Suite is an add-on package for |ewc| that provides services and pre-built
automations for managing Data Center Fabrics - both VCS Fabric and IP Fabric architectures. It
includes workflows such as:

* Manage Fabric Templates
* Build IP Fabric Infrastructure
* Manage EVPN Tenants and Edge Ports
* IP Fabric Validation and Troubleshooting
* Manage VCS Fabric Tenants and Edge Ports

Starting with v1.2, DC Fabric automation supports all VDX device models, and SLX 9240/9140 switches. 

See more details :doc:`here<dcfabric/overview>`.

.. rubric:: What's Next?

* :doc:`Install EWC<../install/ewc>` if you haven't already!
* Choose which suites you need, and install them. Follow these instructions:

  + :doc:`Network Essentials<essentials/install>`
  + :doc:`DC Fabric<dcfabric/install>`
