.. NOTE: This file has been generated automatically, don't manually edit it

set_l3_system_mtu
~~~~~~~~~~~~~~~~~

**Description**: Set L3 system global MTU. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Virtual IP of the VCS Fabric or management IP of the switch.

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``
   *password*                        Login password to connect to the device

                                     Type: ``string``
   **mtu_size**                      MTU size in bytes <Number:1300-9100> for IPV4, <Number:1280-9100> for IPV6 , for MLX IPv4 <576-9198> , IPv6 <1280-8982>

                                     Type: ``integer``
   *afi*                             IP version

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   ================================  ======================================================================

