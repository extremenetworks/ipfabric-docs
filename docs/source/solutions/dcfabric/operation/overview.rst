Operation Overview
==================

Introduction
------------

This document provides an overview of how to use the DC Fabric suite to automate provisioning and 
maintenance of a Brocade IP or VCS Fabric. The DC Fabric suite can automatically configure
interfaces, BGP peerings and related settings. This ensures consistent configuration
across the fabric, with minimal effort.

.. note::
    This document covers the operation of the |bwc| DC Fabric suite. For more information
    about Brocade IP Fabrics in general, see the `Brocade Network OS IP Fabric
    Configuration Guide <http://www.brocade.com/content/html/en/configuration-guide/nos-701-ipfabrics/index.html>`_
    and the `Brocade IP Fabric Validated Design <http://www.brocade.com/content/html/en/brocade-validated-design/brocade-ip-fabric-bvd/GUID-35138986-3BBA-4BD0-94B4-AFABB2E01D77-homepage.html>`_ 

The DC Fabric suite supports easy integration with Zero-Touch Provisioning (ZTP). It can also be used 
without ZTP, but initial switch setup and registration will be a manual process.

The default configuration has a set of predefined parameters used to create the fabric, such 
as ASN range, IP address ranges, etc. To see these parameters, and change them, refer to the
:ref:`IP Fabric parameters<ip_fabric_parameters>` documentation.

.. figure:: ../../../_static/images/solutions/dcfabric/bwc_components.jpg
    :align: center

    **Components of Brocade Flow Composer**

.. note::
    The VCS ID for spine and leaves should be different in both the ZTP-enabled configuration and
    non-ZTP enabled configuration. If the VCS IDs are same, the switches will automatically form an
    Ethernet fabric. For example, the VCS ID for spines can be 1 and for leaves can be 2.

How to use DC Fabric Worfklows
------------------------------

DC Fabric suite can automatically provision a Brocade VDX switch and create an IP Fabric on the switch
if the switch has ZTP enabled and if no management IP address has been assigned to the switch.

.. rubric:: What's Next?

* Running IP Fabric? Read the :doc:`using_ipfabric` docs.
* VCS Fabric? Check out the :doc:`using_vcsfabric` workflows.
* Deeper reference? Check the :doc:`../workflows`, :doc:`CLI <../dcf_cli/basic_cli>`, or :doc:`ZTP <../ztp_reference>` references.
