.. NOTE: This file has been generated automatically, don't manually edit it

set_l3_system_mtu
~~~~~~~~~~~~~~~~~

**Description**: This sets the L3 system global MTU. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The virtual IP of the VCS Fabric or management IP of the switch.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``
   *password*                        The login password to connect to the device.

                                     Type: ``string``
   **mtu_size**                      The MTU size in bytes For NOS <Number:1300-9100> for IPV4, <Number:1280-9100> for IPV6. For SLX <Number:1300-9194> for IPV4/IPv6 For MLX you may enter any number within range of IPv4 <576-9198> , IPv6 <1280-9198>. However, this value must be 18 bytes less than the value of l2 system mtu(global maximum frame size).

                                     Type: ``integer``
   *afi*                             The IP version.

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   ================================  ======================================================================

