.. NOTE: This file has been generated automatically, don't manually edit it

modify_arp_nd_aging_ve
~~~~~~~~~~~~~~~~~~~~~~

**Description**: This will modify ARP and ND aging timers on the VE interface. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   *rbridge_id*                      The RBridge ID of the VDX switch. This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **vlan_id**                       This is a single or a range of VLAN IDs, e.g. 10 or 10-15 or 10,12,13-15.

                                     Type: ``string``
   **arp_aging_type**                The ARP aging type

                                     Choose from:

                                     - arp_aging
                                     - nd_cache_expiry

                                     **Default**: arp_aging
   *arp_aging_timeout*               The ARP aging timeout in minutes <0..240>.

                                     Type: ``integer``

                                     **Default**: 4
   *nd_cache_expire_time*            The ND cache expiration timeout in seconds <30-14400>.

                                     Type: ``integer``

                                     **Default**: 270
   ================================  ======================================================================

