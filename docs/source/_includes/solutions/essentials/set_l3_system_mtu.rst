.. NOTE: This file has been generated automatically, don't manually edit it

set_l3_system_mtu
~~~~~~~~~~~~~~~~~

**Description**: Set L3 system MTU on the VCS fabric or vLag pair. Only supported on VDX devices. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Virtual IP of the VCS Fabric or management IP of the switch.

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``

                                     **Default**: admin
   *password*                        Login password to connect to the device

                                     Type: ``string``

                                     **Default**: password
   **mtu_size**                      MTU size in bytes <Number:1300-9100> for IPV4, <Number:1280-9100> for IPV6

                                     Type: ``integer``
   *afi*                             IP version

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   ================================  ======================================================================

