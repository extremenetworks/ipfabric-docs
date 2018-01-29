.. NOTE: This file has been generated automatically, don't manually edit it

configure_anycast_gw_mac_evpn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configures anycast gateway address. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP of the Device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   **rbridge_id**                    The RBridge ID of the VDX switch. This parameter is only applicable for VDX switches.

                                     Type: ``string``
   **mac**                           The Anycast gateway MAC in XXXX.YYYY.ZZZZ format.

                                     Type: ``string``
   *type*                            The Anycast MAC configurarion for IPv4 and IPv6.

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   ================================  ======================================================================

