.. NOTE: This file has been generated automatically, don't manually edit it

configure_arp_nd_suppression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configure ARP, ND suppression on a vlan or bridge domain. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       THe management IP address of the target device.

                                     Type: ``string``
   *user*                            The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *passwd*                          The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   *vlan_id*                         The VLAN ID.

                                     Type: ``string``
   *bridge_domain_id*                The Bridge-domain ID. Valid values are <1-4096> on SLX9140,SLX9850,SLX9540 and <1-3566> on SLX9240. Valid only on SLXOS devices.

                                     Type: ``string``
   **suppression_type**              The suppression type

                                     Choose from:

                                     - ARP
                                     - ND
                                     - Both

                                     **Default**: ARP
   ================================  ======================================================================

