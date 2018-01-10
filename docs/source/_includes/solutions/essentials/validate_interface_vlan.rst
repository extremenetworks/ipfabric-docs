.. NOTE: This file has been generated automatically, don't manually edit it

validate_interface_vlan
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Validate port channel or physical interface belongs to the specified VLAN 

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
   **vlan_id**                       Single VLAN or range of VLANs, for example 2 or 3-9

                                     Type: ``string``
   **intf_type**                     Interface type

                                     Choose from:

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ethernet
   **intf_name**                     Interface names, can be comma separated physical ports, port channel numbers. Examples are 224/0/1, 224/0/2 or 7, 8, 9

                                     Type: ``string``
   *intf_mode*                       Interface mode

                                     Choose from:

                                     - trunk
                                     - access

                                     **Default**: access
   ================================  ======================================================================

