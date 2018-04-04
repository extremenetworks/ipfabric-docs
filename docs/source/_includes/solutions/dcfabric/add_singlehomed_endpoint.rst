.. NOTE: This file has been generated automatically, don't manually edit it

add_singlehomed_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This workflow creates VLAN, configures interface as Access or Trunk, and validates the interface state.In Bridge-domain context, workflow will create bridge-domains, logical interfaces and associate the logical interfaces to the bridge-domains. Configures VLAN/Bridge-domain to VNI mapping under the overlay gateway. 

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
   **intf_type**                     The interface type.

                                     Choose from:

                                     - ethernet
                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ve
                                     - loopback

                                     **Default**: ethernet
   **intf_name**                     A single port. Examples for VDX, SLX are  24/0/1 or 1/13.

                                     Type: ``string``
   *intf_desc*                       The port description, where space is not allowed, use '_' instead.

                                     Type: ``string``
   *enabled*                         This selects true to enable the port, false to disable the port.

                                     Type: ``boolean``

                                     **Default**: True
   **switchport_mode**               The switch port mode.

                                     Choose from:

                                     - access
                                     - trunk
                                     - trunk_no_default_native

                                     **Default**: access
   *auto_pick_network_id*            In Bridge-domain context, if selected, workflow will pick the lowest available Single/Range of BRIDGE-DOMAIN IDs available on the switch, valid range is from 1 through 4096. For service or transport VFs in a Virtual Fabrics context, if selected, workflow will pick the lowest available Single/Range of VF IDs available on the switch, valid range is from 4096 through 8191. For Virtual Fabric/Bridge-Domain and ctag classification, use auto_pick_network_id or network_id.

                                     Type: ``boolean``
   *network_id*                      For SLXOS, single or range of Bridge Domain IDs, valid range is 1-4096. For VDX, when using Virtual Fabrics, single or range of VF IDs, valid range is 4096-8191. If `auto_pick_network_id=True`, network_id need not be specified.

                                     Type: ``string``
   *vlan_id*                         A single or range of VLANs to be configured on the interface. For 802.1Q VLANs ID must be below 4096. Valid for vlan_id only use cases. For Virtual Fabric/Bridge-Domain and ctag classification, use auto_pick_network_id or network_id.

                                     Type: ``string``
   *vlan_desc*                       The VLAN description, where space is not allowed, use '_' instead.  Same VLAN description is configured on all the VLANs when the range is provided.

                                     Type: ``string``
   *c_tag*                           A single or range of VLAN IDs <NUMBER:1-4090>. Valid only if switchport_mode is trunk. This is mandatory parameter in Virtual Fabric/Bridge-Domain context. Not applicable, if `vlan_type=untagged`.

                                     Type: ``string``
   *mac_group_id*                    The MAC group ID <NUMBER:1,500>. Only applicable if switchport_mode is access and on VDX platforms.

                                     Type: ``array``
   *auto_pick_lif_id*                The auto generates physical port lifs or port channel lifs. Valid only on SLXOS devices.

                                     Type: ``boolean``
   *lif_id*                          A single or comma seperated list of logical interface IDs. Format for  the logical interfaces is <physical/port-channel number>.<number>. This can be ignored, if `auto_pick_lif_id=True and auto_pick_port_channel_id=True`. Valid only on SLXOS devices.

                                     Type: ``string``
   *vlan_type*                       In bridge-domain context, the VLAN tag type to be configured under logical interfaces. If vlan_type is untagged, enable `trunk_no_default_native` parameter. Valid on SLXOS devices.

                                     Choose from:

                                     - untagged
                                     - tagged

                                     **Default**: tagged
   *vni*                             Single or range of VNI <NUMBER:1-16777215> mappings for VLANs or NETWORK IDs, for example 10 or 10-15 or 10,12,13-15. When using ranges, the number of values in a VLAN ID or c_tag range must correspond to the number of values in a VNI range.

                                     Type: ``string``
   ================================  ======================================================================

