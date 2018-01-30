.. NOTE: This file has been generated automatically, don't manually edit it

configure_arp_nd_suppression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configure ARP, ND suppression. 

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
   **vlan_id**                       The VLAN ID.

                                     Type: ``string``
   **suppression_type**              The suppression type

                                     Choose from:

                                     - ARP
                                     - ND
                                     - Both

                                     **Default**: ARP
   ================================  ======================================================================

