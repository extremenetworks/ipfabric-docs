.. NOTE: This file has been generated automatically, don't manually edit it

remove_acl
~~~~~~~~~~

**Description**: Remove an ACL from physical port, port channel, VE or mgmt interface. 

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
   **intf_type**                     Interface type required-by:- [All] accepted-by:- [SLX, NOS, MLX]

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
   **intf_name**                     Interface names, can be comma separated physical ports, port channel numbers or VEs. Examples are 224/0/1, 224/0/2 or 7, 8, 9 required-by:- [All] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``array``
   *rbridge_id*                      RBridge ID of the VDX switch under which VE will be configured, only needed for VDX device. required-by:- [None] accepted-by:- [NOS]

                                     Type: ``string``
   **acl_name**                      ACL name required-by:- [All] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   **acl_direction**                 ACL direction required-by:- [All] accepted-by:- [SLX, NOS, MLX]

                                     Choose from:

                                     - in
                                     - out

                                     **Default**: in
   *traffic_type*                    Traffic type for the ACL being removed required-by:- [None] accepted-by:- [None]

                                     Choose from:

                                     - switched
                                     - routed
   ================================  ======================================================================

