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
   *password*                        Login password to connect to the device

                                     Type: ``string``
   **intf_type**                     Interface type, can be a physical port, port channel, VE or management interface required-by:- [All] accepted-by:- [SLX, NOS, MLX]

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
   **intf_name**                     Interface names, can be comma separated physical ports, port channel numbers or VEs. Examples are 224/0/1, 224/0/2 or 4, 5, 6 or 80, 81. required-by:- [All] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``array``
   *rbridge_id*                      RBridge ID of the VDX switch under which VE will be configured, only needed for VDX device. required-by:- [None] accepted-by:- [NOS]

                                     Type: ``string``
   **acl_name**                      Name of the access list required-by:- [All] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   **acl_direction**                 Direction of ACL binding on the specified interface required-by:- [SLX, NOS, MLX] accepted-by:- [SLX, NOS, MLX]

                                     Choose from:

                                     - in
                                     - out

                                     **Default**: in
   *traffic_type*                    Traffic type for the ACL being applied required-by:- [None] accepted-by:- [SLX, NOS]

                                     Choose from:

                                     - switched
                                     - routed
   ================================  ======================================================================

