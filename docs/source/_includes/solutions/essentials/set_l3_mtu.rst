.. NOTE: This file has been generated automatically, don't manually edit it

set_l3_mtu
~~~~~~~~~~

**Description**: This sets the L3 MTU size on physical, port channel or ve interface. 

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
   **intf_type**                     The interface type.

                                     Choose from:

                                     - ethernet
                                     - tengigabitethernet
                                     - gigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ve

                                     **Default**: tengigabitethernet
   **intf_name**                     The interface names which can be comma separated physical ports, or port channel numbers. Examples are 224/0/1, 224/0/2 or 7, 8, 9.

                                     Type: ``array``
   **mtu_size**                      For SLX IPV4/IPV6 MTU size in bytes <Number:1300-9194>. For VDX IPV4 <Number:1300-9100> or IPV6 <Number:1280-9100> MTU size in bytes. For MLX you may enter any number within range of IPv4 <576-9198> , IPv6 <1280-9198>. However, this value must be 18 bytes less than the value of l2 system mtu(global maximum frame size).

                                     Type: ``integer``
   *afi*                             The IP version.

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   ================================  ======================================================================

