.. NOTE: This file has been generated automatically, don't manually edit it

set_intf_admin_state
~~~~~~~~~~~~~~~~~~~~

**Description**: Enable or disable a single physical port, port-channel, loopback or VE interface on a device.  Optionally set the interface description. 

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

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ve
                                     - loopback

                                     **Default**: tengigabitethernet
   **intf_name**                     Interface names, can be comma separated physical ports, port channel numbers or VEs. Examples are 224/0/1, 224/0/2 or 7, 8, 9

                                     Type: ``string``
   *enabled*                         Admin setting of the interface(s)

                                     Type: ``boolean``

                                     **Default**: True
   *intf_desc*                       Interface description

                                     Type: ``string``
   *rbridge_id*                      RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``string``
   ================================  ======================================================================

