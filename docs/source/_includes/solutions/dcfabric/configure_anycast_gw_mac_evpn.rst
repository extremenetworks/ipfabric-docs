.. NOTE: This file has been generated automatically, don't manually edit it

configure_anycast_gw_mac_evpn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure anycast gateway address 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP of the Device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``

                                     **Default**: admin
   *password*                        Login password to connect to the device

                                     Type: ``string``

                                     **Default**: password
   **rbridge_id**                    RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``string``
   **mac**                           Anycast gateway MAC in XXXX.YYYY.ZZZZ format

                                     Type: ``string``
   *type*                            Anycast MAC configurarion for IPv4 and IPv6

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   ================================  ======================================================================

