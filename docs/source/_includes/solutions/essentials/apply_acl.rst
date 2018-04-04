.. NOTE: This file has been generated automatically, don't manually edit it

apply_acl
~~~~~~~~~

**Description**: This apply an ACL to a physical port, port channel, VE or management interface. 

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
   **intf_type**                     The interface type, can be a physical port, port channel, VE or management interface.

                                     Choose from:

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ve
                                     - loopback
                                     - ethernet
                                     - management
                                     - vlan

                                     **Default**: tengigabitethernet
   **intf_name**                     The interface names, can be comma separated physical ports, port channel numbers or VEs. Examples are 224/0/1, 224/0/2 or 4, 5, 6 or 80, 81.

                                     Type: ``array``
   *rbridge_id*                      The RBridge ID of the VDX switch under which the VE will be configured, only needed for VDX device. Applicable to NOS devices only.

                                     Type: ``string``
   **acl_name**                      The name of the access control list.

                                     Type: ``string``
   **acl_direction**                 The direction of ACL binding on the specified interface.

                                     Choose from:

                                     - in
                                     - out

                                     **Default**: in
   *traffic_type*                    The traffic type for the ACL being applied. Applicable to SLX and NOS devices.

                                     Choose from:

                                     - switched
                                     - routed
   ================================  ======================================================================

