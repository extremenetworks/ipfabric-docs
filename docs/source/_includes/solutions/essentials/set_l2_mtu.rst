.. NOTE: This file has been generated automatically, don't manually edit it

set_l2_mtu
~~~~~~~~~~

**Description**: This sets the L2 MTU size on physical or port channel interfaces. 

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

                                     **Default**: tengigabitethernet
   **intf_name**                     The interface names that can be comma separated physical ports, port channel numbers. Examples are 224/0/1, 224/0/2 or 7, 8, 9

                                     Type: ``array``
   **mtu_size**                      For SLX MTU size in bytes <Number:1548-9216>. For VDX <Number:1522-9216>.

                                     Type: ``integer``
   ================================  ======================================================================

