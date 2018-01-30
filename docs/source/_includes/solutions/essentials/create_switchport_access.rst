.. NOTE: This file has been generated automatically, don't manually edit it

create_switchport_access
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configures a port channel or a physical interface as an access interface, or adds a untagged port to a VLAN for NI. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``
   *password*                        The login password to connect to the device.

                                     Type: ``string``
   **intf_type**                     The interface type.

                                     Choose from:

                                     - ethernet
                                     - tengigabitethernet
                                     - gigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel

                                     **Default**: tengigabitethernet
   **intf_name**                     The interface name, for VDX in 3-tuple format (24/0/1), SLX/NI in 2-tuple format (24/1) or Port-channel number <1-6144>, for NI <1-256>.

                                     Type: ``string``
   **vlan_id**                       The VLAN ID to be configured on the interface. For 802.1Q VLANs, ID must be below 4096, for service or transport VFs valid range is from 4096 through 8191, for NI, vlan range <1-4090>.

                                     Type: ``string``
   *mac_group_id*                    The ID of a previously created MAC group to be used in MAC-based VLAN classification at the access port. This is applicable only when Virtual Fabric is enabled.  This is a fabric-wide ID with valid values of 1 through 500. it is no-op for NI.

                                     Type: ``array``
   ================================  ======================================================================

