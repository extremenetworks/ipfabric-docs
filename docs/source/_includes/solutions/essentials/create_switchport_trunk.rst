.. NOTE: This file has been generated automatically, don't manually edit it

create_switchport_trunk
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configures the port channel or a physical interface as a Trunk or Trunk-no-default-native or add a tagged port to a vlan or list of vlans interface. 

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
   **intf_type**                     Interface type

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
   *trunk_no_default_native*         This configures the interface mode as trunk-no-default-native or trunk. The default interface mode is configured as `trunk`, and it is no-op for NI.

                                     Type: ``boolean``
   *vlan_id*                         For 802.1Q VLANs, single or range of VLANs, for example, 5 or 4-7 or 4,6,9-11 or all; the ID must be below 4096. For service or transport VFs, single ID, range can be from 4096 through 8191. For NI, the VLAN range is <1-4090> and is a mandatory argument.

                                     Type: ``string``
   *c_tag*                           This specifies an incoming C-TAG or range of C-TAGs for service or transport VLANs in a Virtual Fabrics context. For service VF, only single ID is allowed, for transport VFs, a range of IDs, for example, 100-200, or 10,20,100-200, it is no-op for NI.

                                     Type: ``string``
   ================================  ======================================================================

