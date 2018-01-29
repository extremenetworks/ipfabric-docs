.. NOTE: This file has been generated automatically, don't manually edit it

attach_service_policy_to_interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: The attach Input/Output Policy Map. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   *rbridge_id*                      The RBridge ID of the VDX switch under which VE will be configured, only needed for VDX device.

                                     Type: ``string``
   **intf_type**                     The interface type.

                                     Choose from:

                                     - ethernet
                                     - port_channel
                                     - tengigabitethernet
                                     - gigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet

                                     **Default**: tengigabitethernet
   **intf_name**                     The interface name of the physical port or port channel number. E.g 0/1 or 7.

                                     Type: ``string``
   **policy_map_name**               A Single Policy Map Class Name for configuring In/Out Policy. List of Class Names to configure In & Out Policy. (Max Size -64). For Example. 'Policy_map_in' or 'Policy_map_out' or 'Policy_map_in, Policy_map_out'

                                     Type: ``array``
   *policy_type*                     The In/Out Policy Map  (Max Size -64).

                                     Choose from:

                                     - In
                                     - Out
                                     - Both

                                     **Default**: In
   ================================  ======================================================================

