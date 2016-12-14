Overview
========

.. include:: __tech_preview.rst

Automation Suites are collections of workflows, actions, sensors and services that target
specific networking use-cases, e.g. Data Center Fabric architectures, or Internet Exchanges.
They deliver turnkey workflows for provisioning, validation, troubleshooting and remediation
workflows.

These are installed on top of |bwc|. Users can install one or more suites. Suites may have
dependencies - e.g. the Network Essentials suite is foundational for other suites.

These suites are fully supported by Brocade. Users may modify these workflows to customise them
to their needs.

Network Essentials
~~~~~~~~~~~~~~~~~~

Network Essentials is a foundational set of workflows for operating Brocade network devices. It
includes actions such as port provisioning, SNMP, NTP & AAA configuration. These are basic building
blocks that are used by other suites. Customers can also use these blocks to create their own
customised workflows.

It currently supports Brocade VDX and SLX devices. See more details :doc:`here<essentials/overview>`.

DC Fabrics
~~~~~~~~~~

The DC Fabrics Automation Suite is an add-on package for |bwc| that provides services and pre-built automations for managing
Brocade Data Center Fabrics - both VCS Fabric and IP Fabric architectures. It includes workflows such as:

* Provision and validate Brocade IP Fabrics and BGP-EVPN
* Perform Layer-2 path traces across VCS Fabrics
* Find and provision edge ports

It works with all current Brocade VDX switches, and SLX-9850 switches when used as a super-spine.
See more details :doc:`here<dcfabric/overview>`.

Internet Exchange
~~~~~~~~~~~~~~~~~

The Internet Exchange suite provides workflows that target common use-cases seen by Internet Exchanges.
Workflows include customer port provisioning, move systems to quarantine, MAC ACL updates, and route
server validation.

It works with Brocade SLX-9850 and 9540 switches, and will in future work with Brocade MLXe devices.
Technical Preview versions of this automation suite will begin shipping soon.

.. rubric:: What's Next?

* :doc:`Install BWC<../install/bwc>` if you haven't already!
* Choose which suites you need, and install them. Follow these instructions:

  + :doc:`Network Essentials<essentials/install>`
  + :doc:`DC Fabrics<dcfabric/install>`
