.. NOTE: This file has been generated automatically, don't manually edit it

set_l3_mtu
~~~~~~~~~~

**Description**: Set L3 MTU size on physical or port channel interface 

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
   **intf_type**                     Interface type

                                     Choose from:

                                     - ethernet
                                     - tengigabitethernet
                                     - gigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ve

                                     **Default**: tengigabitethernet
   **intf_name**                     Interface names, can be comma separated physical ports, port channel numbers. Examples are 224/0/1, 224/0/2 or 7, 8, 9

                                     Type: ``array``
   **mtu_size**                      For SLX IPV4/IPV6 MTU size in bytes <Number:1300-9194>. For VDX IPV4 <Number:1300-9100> or IPV6 <Number:1280-9100> MTU size in bytes.

                                     Type: ``integer``
   *afi*                             IP version

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   ================================  ======================================================================

