.. NOTE: This file has been generated automatically, don't manually edit it

set_intf_admin_state
~~~~~~~~~~~~~~~~~~~~

**Description**: This enable or disable physical port, port-channel, loopback or VE interfaces on a device.  Optionally, sets the interface description. For MLX, port-channel admin state changes means it changes member port's admin state. 

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
                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ve
                                     - loopback

                                     **Default**: tengigabitethernet
   **intf_name**                     The interface names, port channel numbers or VEs. For example to specify ports, for VDX 24/0/1 or 24/0/1-2  , for SLX/NI  24/1 or 24/1-2 . For port channel or l3 interface , 10 or 1-10

                                     Type: ``string``
   *enabled*                         The admin setting of the interface(s).

                                     Type: ``boolean``

                                     **Default**: True
   *intf_desc*                       The interface description without any space.

                                     Type: ``string``
   *rbridge_id*                      The RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``string``
   ================================  ======================================================================

