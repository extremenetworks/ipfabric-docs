.. NOTE: This file has been generated automatically, don't manually edit it

modify_arp_nd_aging_ve
~~~~~~~~~~~~~~~~~~~~~~

**Description**: Modify ARP and ND aging timers on VE interface 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``

                                     **Default**: admin
   *password*                        Login password to connect to the device

                                     Type: ``string``

                                     **Default**: password
   *rbridge_id*                      RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **vlan_id**                       VLAN ID

                                     Type: ``string``
   **arp_aging_type**                Aging type

                                     Choose from:

                                     - arp_aging
                                     - nd_cache_expiry

                                     **Default**: arp_aging
   *arp_aging_timeout*               ARP aging timeout in minutes <0..240>.

                                     Type: ``integer``

                                     **Default**: 4
   *nd_cache_expire_time*            ND cache expiration timeout in seconds <30-14400>.

                                     Type: ``integer``

                                     **Default**: 270
   ================================  ======================================================================

