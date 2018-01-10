.. NOTE: This file has been generated automatically, don't manually edit it

clear_cfg_rate_limiting
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This workflow accomplishes the task of removing rate config on a specified interface by unconfiguring the service policy on that interface. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       device ip address

                                     Type: ``string``
   *username*                        login username

                                     Type: ``string``

                                     **Default**: admin
   *password*                        login password

                                     Type: ``string``

                                     **Default**: password
   **intf_type**                     Interface type gigabitethernet or tengigabitethernet, etc

                                     Choose from:

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - ethernet

                                     **Default**: tengigabitethernet
   **intf_name**                     interface name as array (182/0/97)

                                     Type: ``array``
   **policy_map_name**               the service policy configured on the interface.

                                     Type: ``array``
   **policy_type**                   In, Out or Both.

                                     Type: ``string``
   *rbridge_id*                      RBridge ID of the VDX switch under which VE will be configured, only needed for VDX device.

                                     Type: ``string``
   ================================  ======================================================================

