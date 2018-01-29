.. NOTE: This file has been generated automatically, don't manually edit it

create_vrf
~~~~~~~~~~

**Description**: This creates a Virtual Routing and Forwarding (VRF) instance on a switch for L3 tenants. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``
   *password*                        The login password to connect to the device.

                                     Type: ``string``
   **vrf_name**                      The VRF name, for example vrf32 or 32.

                                     Type: ``string``
   *rbridge_id*                      The RBridge ID of the switch. This parameter is only applicable for VDX switches.

                                     Type: ``array``
   *afi*                             The IP address type.

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   *rd*                              The Route Distinguisher <ASN:nn or VPN Route Distinguisher>, and is mandatory for MLX

                                     Type: ``string``
   ================================  ======================================================================

