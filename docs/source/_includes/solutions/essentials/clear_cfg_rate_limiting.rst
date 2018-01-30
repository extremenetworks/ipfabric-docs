.. NOTE: This file has been generated automatically, don't manually edit it

clear_cfg_rate_limiting
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This workflow accomplishes the task of removing the rate config on a specified interface by unconfiguring the service policy on that interface. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The device IP address.

                                     Type: ``string``
   *username*                        The login username.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password.

                                     Type: ``string``

                                     **Default**: password
   **intf_type**                     The interface type - gigabitethernet or tengigabitethernet, etc.

                                     Choose from:

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - ethernet

                                     **Default**: tengigabitethernet
   **intf_name**                     The interface name as an array (182/0/97).

                                     Type: ``array``
   **policy_map_name**               The service policy configured on the interface.

                                     Type: ``array``
   **policy_type**                   This is In, Out or Both.

                                     Type: ``string``
   *rbridge_id*                      The RBridge ID of the VDX switch under which VE will be configured, only needed for VDX device.

                                     Type: ``string``
   ================================  ======================================================================

