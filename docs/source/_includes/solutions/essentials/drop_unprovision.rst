.. NOTE: This file has been generated automatically, don't manually edit it

drop_unprovision
~~~~~~~~~~~~~~~~

**Description**: This workflow accomplishes the task of allowing traffic back on a specified interface by first deleting the deny ACL currently on that interface. If may also delete the acl, if it is empty. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       device ip address

                                     Type: ``string``
   *username*                        login username

                                     Type: ``string``
   *password*                        login password

                                     Type: ``string``
   **acl_name**                      access list name (max 63)

                                     Type: ``string``
   *seq_ids*                         A list of ACL rules sequence ids separated by comma, Examples 30 or 20,30,50

                                     Type: ``array``
   *rbridge_id*                      RBridge ID of the VDX switch under which VE will be configured, only needed for VDX device.

                                     Type: ``string``
   *intf_type*                       Interface type gigabitethernet or tengigabitethernet, etc

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
   *intf_name*                       interface name as array (182/0/97)

                                     Type: ``array``
   *acl_direction*                   Direction of ACL binding on the specified interface

                                     Choose from:

                                     - in
                                     - out

                                     **Default**: in
   *traffic_type*                    Traffic type for the ACL being applied

                                     Choose from:

                                     - switched
                                     - routed
   *delete_acl*                      Indicates whether the acl should be deleted.

                                     Type: ``boolean``
   ================================  ======================================================================

