.. NOTE: This file has been generated automatically, don't manually edit it

validate_interface_state
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This validates L1 and L2 state for port channel, physical, ve, loopback interface. is UP. 

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

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ethernet
                                     - ve
                                     - loopback

                                     **Default**: tengigabitethernet
   **intf_name**                     The interface name physical port, port channel number, ve, loopback. Examples are 224/0/1 or 7

                                     Type: ``string``
   **intf_state**                    The interface state (up or down).

                                     Choose from:

                                     - up
                                     - down
   *rbridge_id*                      A single or a list of RBridge IDs separated by comma, for example, 1 or 1,2, 4.  This parameter is only applicable for VDX switches.

                                     Type: ``array``
   ================================  ======================================================================

