.. NOTE: This file has been generated automatically, don't manually edit it

enable_vf
~~~~~~~~~

**Description**: Enable or disable VCS virtual-fabric on a VCS fabric, when enabled, expands the VLAN ID address space beyond the 802.1Q limit in the fabric, allowing VLANs with IDs greater than 4095, up through 8191. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``
   *password*                        Login password to connect to the device

                                     Type: ``string``
   *virtual_fabric_enable*           Set True to enable or False to disable virtual-fabric on VCS.

                                     Type: ``boolean``

                                     **Default**: True
   ================================  ======================================================================

