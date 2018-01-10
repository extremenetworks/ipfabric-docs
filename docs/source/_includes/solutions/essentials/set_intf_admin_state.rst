.. NOTE: This file has been generated automatically, don't manually edit it

set_intf_admin_state
~~~~~~~~~~~~~~~~~~~~

**Description**: Enable or disable a single physical port, port-channel, loopback or VE interface on a device.  Optionally set the interface description, For MLX port-channel admin state changes means it changes member port's admin state 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``
   *password*                        Login password to connect to the device

                                     Type: ``string``
   **intf_type**                     Interface type

                                     Choose from:

                                     - ethernet
                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ve
                                     - loopback

                                     **Default**: tengigabitethernet
   **intf_name**                     Interface names, port channel numbers or VEs. Examples are 224/0/1, 224/0/2, 0/1 or 7, 8, 9

                                     Type: ``string``
   *enabled*                         Admin setting of the interface(s)

                                     Type: ``boolean``

                                     **Default**: True
   *intf_desc*                       Interface description without any space

                                     Type: ``string``
   *rbridge_id*                      RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``string``
   ================================  ======================================================================

