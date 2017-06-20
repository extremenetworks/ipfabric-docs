.. NOTE: This file has been generated automatically, don't manually edit it

validate_interface_state
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Validate L1 and L2 state for port channel, physical, ve, loopback interface is UP. 

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
                                     - ethernet
                                     - ve
                                     - loopback

                                     **Default**: tengigabitethernet
   **intf_name**                     Interface name physical port, port channel number, ve, loopback. Examples are 224/0/1 or 7

                                     Type: ``string``
   **intf_state**                    Interface state (up or down)

                                     Choose from:

                                     - up
                                     - down
   *rbridge_id*                      Single or list of RBridge IDs separated by comma, for example, 1 or 1,2, 4.  This parameter is only applicable for VDX switches.

                                     Type: ``array``
   ================================  ======================================================================

