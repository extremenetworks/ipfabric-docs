.. NOTE: This file has been generated automatically, don't manually edit it

apply_acl
~~~~~~~~~

**Description**: Apply an ACL to a physical port, port channel, VE or management interface. 

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
   **intf_type**                     Interface type, can be a physical port, port channel, VE or management interface

                                     Choose from:

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ve
                                     - loopback
                                     - ethernet

                                     **Default**: tengigabitethernet
   **intf_name**                     Interface names, can be comma separated physical ports, port channel numbers or VEs. Examples are 224/0/1, 224/0/2 or 4, 5, 6 or 80, 81.

                                     Type: ``array``
   *rbridge_id*                      RBridge ID of the VDX switch under which VE will be configured, only needed for VDX device.

                                     Type: ``string``
   **acl_name**                      Name of the access list

                                     Type: ``string``
   **acl_direction**                 Direction of ACL binding on the specified interface

                                     Choose from:

                                     - in
                                     - out

                                     **Default**: in
   *traffic_type*                    Traffic type for the ACL being applied

                                     Choose from:

                                     - switched
                                     - routed
   ================================  ======================================================================

