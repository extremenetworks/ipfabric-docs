.. NOTE: This file has been generated automatically, don't manually edit it

configure_evpn_instance
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure EVPN instance . 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Ip address of the device

                                     Type: ``string``
   *username*                        login username

                                     Type: ``string``

                                     **Default**: admin
   *password*                        login password

                                     Type: ``string``

                                     **Default**: password
   *rbridge_id*                      Rbridge id of the device

                                     Type: ``array``
   **evi_name**                      vrf name. For example 'evpn1 or 32'

                                     Type: ``string``
   *duplicate_mac_timer*             Value in integer,default 10

                                     Type: ``integer``

                                     **Default**: 10
   *max_count*                       Value in integer,default 10

                                     Type: ``integer``

                                     **Default**: 10
   *ignore_as*                       Value in integer,default 10

                                     Type: ``boolean``

                                     **Default**: True
   ================================  ======================================================================

