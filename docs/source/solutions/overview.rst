Overview
========

Automation Suites are collections of workflows, actions, sensors and services that target
specific networking use-cases, e.g. Data Center Fabric architectures, or Internet Exchanges.
They deliver turnkey workflows for provisioning, validation, troubleshooting and remediation
workflows.

These are installed on top of |bwc|. Users can install one or more suites. Suites may have
dependencies - e.g. the Network Essentials suite is foundational for other suites.

Users may modify these workflows to customise them to their needs.

Network Essentials
~~~~~~~~~~~~~~~~~~

Network Essentials is a foundational set of workflows for operating Extreme network devices. It
includes actions such as port provisioning, SNMP, NTP & AAA configuration. These are basic building
blocks that are used by other suites. Customers can also use these blocks to create their own
customised workflows.

It currently supports Extreme VDX and SLX devices. See more details :doc:`here<essentials/overview>`.

DC Fabric
~~~~~~~~~~

The DC Fabric Automation Suite is an add-on package for |bwc| that provides services and pre-built
automations for managing Data Center Fabrics - both VCS Fabric and IP Fabric architectures. It
includes workflows such as:

* Provision and validate IP Fabrics and BGP-EVPN
* Perform Layer-2 path traces across VCS Fabrics
* Find and provision edge ports

It works with all current VDX switches, and SLX-9850 switches when used as a super-spine. It is currently
available as a Technology Preview.

See more details :doc:`here<dcfabric/overview>`.

Internet Exchange
~~~~~~~~~~~~~~~~~

The Internet Exchange suite provides workflows that target common use-cases seen by Internet Exchanges.
Workflows include customer port provisioning, move systems to quarantine, MAC ACL updates, and route
server validation.

It will work with SLX-9850 and 9540 switches. Future updates will include MLXe support.
Technology Preview versions of this automation suite will begin shipping soon.

.. rubric:: What's Next?

* :doc:`Install EWC<../install/bwc>` if you haven't already!
* Choose which suites you need, and install them. Follow these instructions:

  + :doc:`Network Essentials<essentials/install>`
  + :doc:`DC Fabric<dcfabric/install>`
