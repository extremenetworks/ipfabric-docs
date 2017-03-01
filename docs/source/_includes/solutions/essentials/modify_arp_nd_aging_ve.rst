.. NOTE: This file has been generated automatically, don't manually edit it

modify_arp_nd_aging_ve
~~~~~~~~~~~~~~~~~~~~~~

**Description**: configure arp nd aging for ve 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       mgmt_ip of the Device

                                     Type: ``string``
   *username*                        login username

                                     Type: ``string``

                                     **Default**: admin
   *password*                        login password

                                     Type: ``string``

                                     **Default**: password
   *rbridge_id*                      Rbridge id on which arp-aging-timeout has to be configured.

                                     Type: ``array``
   **vlan_id**                       vlan id

                                     Type: ``string``
   **arp_aging_type**                Arp or ND

                                     Choose from:

                                     - arp_aging
                                     - nd_cache_expiry
   *arp_aging_timeout*               Arp Aging Timeout in Minutes <0..240>.

                                     Type: ``integer``

                                     **Default**: 4
   *nd_cache_expire_time*            Cache Expire Timeout in Seconds <30-14400>.

                                     Type: ``integer``

                                     **Default**: 270
   ================================  ======================================================================

