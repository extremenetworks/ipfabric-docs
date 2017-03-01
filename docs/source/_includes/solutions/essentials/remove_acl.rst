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
                                     - ethernet

                                     **Default**: tengigabitethernet
   **intf_name**                     Interface names, can be comma separated physical ports, port channel numbers or VEs. Examples are 224/0/1, 224/0/2 or 7, 8, 9

                                     Type: ``array``
   *rbridge_id*                      RBridge ID of the VDX switch.  This parameter is only applicable to VDX switches

                                     Type: ``string``
   **acl_name**                      ACL name

                                     Type: ``string``
   **acl_direction**                 ACL direction

                                     Choose from:

                                     - in
                                     - out

                                     **Default**: in
   *traffic_type*                    Traffic type for the ACL being removed

                                     Choose from:

                                     - switched
                                     - routed
   ================================  ======================================================================

