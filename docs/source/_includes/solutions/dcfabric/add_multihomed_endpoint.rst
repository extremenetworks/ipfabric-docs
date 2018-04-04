.. NOTE: This file has been generated automatically, don't manually edit it

add_multihomed_endpoint
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This workflow creates VLANs, port channel and configures port channel as a Trunk. In Bridge-domain context, workflow will create bridge-domains, logical interfaces and associate the logical interfaces to the bridge-domains. Configures VLAN/Bridge-domain to VNI mapping under the overlay gateway. The workflow also creates the MCT client and its interfaces. For service or transport VFs in a Virtual Fabrics context, workflow will create g-vlans and map c-tags under the switchport. 

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
                                     - tengigabitethernet
                                     - gigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet

                                     **Default**: ethernet
   **ports**                         A single or a list of ports that are members of the port channel. Examples for VDX, SLX are  24/0/1, 24/0/2 or 1/13, 1/14.

                                     Type: ``array``
   *port_speed*                      The configurable port speed.

                                     Choose from:

                                     - 1000
                                     - 10000
                                     - 25000
                                     - 40000
                                     - 100000

                                     **Default**: 10000
   *intf_desc*                       The description for all the ports, space is not allowed, use '_' instead.

                                     Type: ``string``
   *auto_pick_port_channel_id*       If selected, workflow will pick the lowest available port channel on the switch.

                                     Type: ``boolean``
   *trunk_no_default_native*         Configure the switchport mode as trunk-no-default-native.

                                     Type: ``boolean``
   *port_channel_id*                 The Portchannel interface number. VDX <1-6144>, SLX-9850 <1-512>, SLX-9540 <1-64>, SLX-9140/9240 <1-1024>, if auto pick option is selected, no need to specify `port_channel_id`.

                                     Type: ``string``
   *port_channel_desc*               The port channel description without any space.

                                     Type: ``string``
   *mode*                            The port channel type.

                                     Choose from:

                                     - standard
                                     - brocade

                                     **Default**: standard
   *protocol*                        The port channel mode.

                                     Choose from:

                                     - active
                                     - passive
                                     - modeon

                                     **Default**: active
   *mtu*                             The L2 MTU size in bytes <Number:1522-9216>.

                                     Type: ``integer``
   *enabled*                         Select true to enable the port, false to disable the port.

                                     Type: ``boolean``

                                     **Default**: True
   *auto_pick_network_id*            In Bridge-domain context, if selected, workflow will pick the lowest available Single/Range of BRIDGE-DOMAIN IDs available on the switch, valid range is from 1 through 4096. For service or transport VFs in a Virtual Fabrics context, if selected, workflow will pick the lowest available Single/Range of VF IDs available on the switch, valid range is from 4096 through 8191. For Virtual Fabric/Bridge-Domain and ctag classification, use auto_pick_network_id or network_id.

                                     Type: ``boolean``
   *network_id*                      For SLXOS, single or range of Bridge Domain IDs, valid range is 1-4096. For VDX, when using Virtual Fabrics, single or range of VF IDs, valid range is 4096-8191. If `auto_pick_network_id=True`, network_id need not be specified.

                                     Type: ``string``
   *vlan_id*                         A single or range of VLANs to be configured on the interface. For 802.1Q VLANs ID must be below 4096. Valid for vlan_id only use cases. For Virtual Fabric/Bridge-Domain and ctag classification, use auto_pick_network_id or network_id.

                                     Type: ``string``
   *vlan_desc*                       The VLAN description, space is not allowed, use '_' instead. Same VLAN description is configured on all the VLANs when the range is provided.

                                     Type: ``string``
   *c_tag*                           A single or range of VLAN IDs <NUMBER:1-4090>. Valid only if switchport_mode is trunk. This is mandatory parameter in Virtual Fabric/Bridge-Domain context. Not applicable, if `vlan_type=untagged`.

                                     Type: ``string``
   *auto_pick_lif_id*                This auto generates physical/port-channel logical interfaces. Valid only on SLXOS devices.

                                     Type: ``boolean``
   *lif_id*                          A single or comma seperated list of logical interface IDs. Format for the logical interfaces is <physical/port-channel number>.<number>. This can be ignored, if `auto_pick_lif_id=True and auto_pick_port_channel_id=True`. Valid only on SLXOS devices.

                                     Type: ``string``
   *vlan_type*                       In bridge-domain context, the VLAN tag type to be configured under logical interfaces. If vlan_type is untagged, enable `trunk_no_default_native` parameter. Valid only on SLXOS devices.

                                     Choose from:

                                     - untagged
                                     - tagged

                                     **Default**: tagged
   *vni*                             Single or a range of VNI <NUMBER:1-16777215> mappings for VLANs or NETWORK IDs, for example 10 or 10-15 or 10,12,13-15. When using ranges, the number of values in a VLAN ID or c_tag range must correspond to the number of values in a VNI range.

                                     Type: ``string``
   *mct_client_name*                 Cluster Client name for Node Specific configuration, both `mct_client_name` and `mct_client_id` are required for MCT client creation. Valid on SLXOS devices.

                                     Type: ``string``
   *mct_client_id*                   The ID for the Cluster Client. Valid IDs are 1 - 512. Both `mct_client_name` and `mct_client_id` are required for MCT client creation. Valid on SLXOS devices.

                                     Type: ``integer``
   *display_show_results*            This enable or disable execution of show commands on the device to display the output.

                                     Type: ``boolean``
   ================================  ======================================================================

