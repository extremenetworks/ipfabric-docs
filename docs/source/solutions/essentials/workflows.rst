Workflows
=========

Introduction
------------

This document provides an overview of how to use the Network Essentials workflows and actions
with Brocade VDX and SLX switches. These actions can be used as independent actions,
or as part of a more complex workflow. :doc:`Actions</actions>` can be manually triggered,
or they can be tied to :doc:`sensors </sensors>` using rules.

Workflows
---------

.. note::

    There may not be any workflows here in Essentials. Might only be Actions, with Workflows in
    DC Fabrics, or IXP


configure_tenant
----------------

Description
~~~~~~~~~~~

.. note::

    This section provides a brief description of what the workflow does. Generally 1-3 lines?

This workflow will configure a new L3 Tenant. This includes VRF, VLAN, IP and VRRP setup.
    

Requirements
~~~~~~~~~~~~

.. note::

    This section notes any requirements, pre-requisites, assumptions, etc. Note that the main intro
    covers supported devices & versions, this section should not any different version requirements,
    or variation between SLX & VDX, or between IP Fabric & VCS Fabric

This workflow is designed for VDX switches operating in either VCS Fabric or IP Fabric mode. It is not
designed for SLX switches. This fabric must already be registered with the |bwc| inventory service.

Parameters
~~~~~~~~~~

.. note::

    This section details the parameters, required vs optional, defaults, etc. It can contain longer
    descriptions than what we can fit in the web UI.

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
~~~~~~

.. note::

    This section details return values

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   result
       Boolean - True/False, if workflow succeeded

   rd
       RD auto-assigned to tenant

Error Messages
~~~~~~~~~~~~~~

.. note::

    This section lists any known error messages

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   "Invalid VLAN ID"
       Returned if VLAN(s) provided are invalid, e.g. > 4094.

   "Unknown Fabric"
       Returned if fabric is not registered. 


-----------------

Actions
-------

.. note::

    This section covers Actions in this Suite.

configure_ntp
-------------

Description
~~~~~~~~~~~

.. note::

    This section provides a brief description of what the workflow does. Generally 1-3 lines?

``configure_ntp`` sets the NTP servers that the device should poll.

Requirements
~~~~~~~~~~~~

.. note::

    This section notes any requirements, pre-requisites, assumptions, etc. Note that the main intro
    covers supported devices & versions, this section should not any different version requirements,
    or variation between SLX & VDX, or between IP Fabric & VCS Fabric

No specific requirements. Unless otherwise specified, datastore credentials will be used.

Parameters
~~~~~~~~~~

.. note::

    This section details the parameters, required vs optional, defaults, etc. It can contain longer
    descriptions than what we can fit in the web UI.

.. code-block:: guess
   :emphasize-lines: 1,5,9

   servers
       Comma-separated list of NTP servers, e.g. 10.1.1.1,10.1.1.2.
       At least one server must be provided.

   switch
       Comma-separated list of switches to apply the configuration to.
       At least one switch IP/hostname must be provided.

    exclusive (optional)
       Boolean value (True/False). Set to True to ensure that device **only** uses the provided
       NTP servers, and removes any existing NTP servers. Default is False - the existing NTP
       NTP configuration will not be changed


Output
~~~~~~

.. note::

    This section details return values

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   result
       Boolean - True/False, if workflow succeeded

Error Messages
~~~~~~~~~~~~~~

.. note::

    This section lists any known error messages

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16

   "Invalid NTP Server"
       Returned if one or more NTP servers are invalid.
