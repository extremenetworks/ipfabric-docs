.. NOTE: This file has been generated automatically, don't manually edit it

set_l2_mtu
~~~~~~~~~~

**Description**: Set L2 MTU size on physical or port channel interfaces 

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

                                     **Default**: tengigabitethernet
   **intf_name**                     Interface names, can be comma separated physical ports, port channel numbers. Examples are 224/0/1, 224/0/2 or 7, 8, 9

                                     Type: ``array``
   **mtu_size**                      MTU size in bytes <Number:1522-9216>

                                     Type: ``integer``
   ================================  ======================================================================

