.. NOTE: This file has been generated automatically, don't manually edit it

create_switchport_access
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure a port channel or a physical interface as an access interface. 

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
   **intf_type**                     Interface type

                                     Choose from:

                                     - ethernet
                                     - tengigabitethernet
                                     - gigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel

                                     **Default**: tengigabitethernet
   **intf_name**                     Interface name, for VDX in 3-tuple format (24/0/1), SLX in 2-tuple format (24/1) or Port-channel number <1-6144>.

                                     Type: ``string``
   **vlan_id**                       VLAN ID to be configured on the interface. For 802.1Q VLANs, ID must be below 4096, for service or transport VFs valid range is from 4096 through 8191.

                                     Type: ``string``
   *mac_group_id*                    ID of previously created MAC group to be used in MAC-based VLAN classification at the access port.  Applicable only when Virtual Fabric is enabled.  This is a fabric-wide ID, valid values are 1 through 500.

                                     Type: ``array``
   ================================  ======================================================================

