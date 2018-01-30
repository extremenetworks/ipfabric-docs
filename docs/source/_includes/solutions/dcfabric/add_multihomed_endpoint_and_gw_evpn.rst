.. NOTE: This file has been generated automatically, don't manually edit it

add_multihomed_endpoint_and_gw_evpn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This add an endpoint (Server, FW, LB, VM) to an existing L3 tenant in an EVPN IP fabric and also configures IP Anycast Gateway. 

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

                                     **Default**: tengigabitethernet
   *port_speed*                      The configurable port speed. Valid if switchport is `trunk` or `trunk_no_default_active`.

                                     Choose from:

                                     - 1000
                                     - 10000
                                     - 25000
                                     - 40000
                                     - 100000

                                     **Default**: 10000
   **intf_name**                     The list of ports that are members of the port channel. Examples for VDX, SLX are 24/0/1, 24/0/2 or 1/13, 1/14.

                                     Type: ``array``
   *intf_desc*                       The description for all the ports, space is not allowed, use '_' instead.

                                     Type: ``string``
   *enabled*                         This selects true to enable the port, false to disable the port.

                                     Type: ``boolean``

                                     **Default**: True
   *auto_pick_port_channel_id*       If selected, workflow will pick the lowest available port channel. on the switch.

                                     Type: ``boolean``
   *port_channel_id*                 The Portchannel interface number. VDX <1-6144>, SLX-9850 <1-512>, SLX-9540 <1-64>, SLX-9140/9240 <1-1024>, if auto pick option is selected and switchport_mode is access no need to specify the VLAN ID.

                                     Type: ``string``
   *port_channel_desc*               The port channel description without any space.

                                     Type: ``string``
   *mode*                            The port channel type.

                                     Choose from:

                                     - standard
                                     - brocade

                                     **Default**: standard
   *protocol*                        The port channel mode

                                     Choose from:

                                     - active
                                     - passive
                                     - modeon

                                     **Default**: active
   **switchport_mode**               The switch port mode

                                     Choose from:

                                     - access
                                     - trunk
                                     - trunk_no_default_native

                                     **Default**: access
   *auto_pick_network_id*            For service or transport VFs in a Virtual Fabrics context, if selected, workflow will pick the lowest available Single/Range of VF IDs available on the switch, valid range is from 4096 through 8191. In Bridge-domain context, if selected, workflow will pick the lowest available Single/Range of BRIDGE-DOMAIN IDs available on the switch, valid range is from 1 through 4096. For Virtual Fabric/Bridge-Domain and ctag classification , use auto_pick_network_id or network_id.

                                     Type: ``boolean``
   *network_id*                      This is a single or range of VLANs to be configured on the interface. For service or transport VFs in a Virtual Fabrics context, valid range is from 4096 through 8191. Single or range of Bridge-domain ID in SLXOS platforms, valid range is from 1 through 4096. If `auto_pick_network_id=True`, network_id need not be specified.

                                     Type: ``string``
   *vlan_id*                         This is a single or a range of VLANs to be configured on the interface. For 802.1Q VLANs ID must be below 4096. Valid for vlan_id only use cases. For Virtual Fabric/Bridge-Domain and ctag classification, use auto_pick_network_id or network_id.

                                     Type: ``string``
   *vlan_desc*                       The VLAN description, space is not allowed, use '_' instead.

                                     Type: ``string``
   *vlan_type*                       In bridge-domain context, the VLAN tag type to be configured under logical interfaces. If vlan_type is untagged, enable `trunk_no_default_native` args.

                                     Choose from:

                                     - untagged
                                     - tagged

                                     **Default**: tagged
   *c_tag*                           A single or a range of VLAN IDs <NUMBER:1-4090>. Valid only if switchport_mode is trunk.

                                     Type: ``string``
   *auto_pick_lif_id*                This auto generates physical port lifs or port channel lifs.

                                     Type: ``boolean``
   *lif_id*                          A single or comma seperated list of logical interface ids. Format for the logical interfaces is <physical/port-channel number>.<number>. If `auto_pick_lif_id=True and auto_pick_port_channel_id=True`, `lif_id` need not be specified.

                                     Type: ``string``
   *vni*                             This specifies the VNI mapping for the VLAN. <NUMBER:1-16777215>.

                                     Type: ``string``
   *mac_group_id*                    The MAC group ID <NUMBER:1,500>. Only applicable if switchport_mode is access and on VDX platforms.

                                     Type: ``array``
   **vrf_name**                      VRF name

                                     Type: ``string``
   **anycast_address**               This is a single or list of IPv4 or IPv6 address with subnet/prefix length separated by comma. e.g. 10.10.9.10/22 or 10.10.9.10/22,11.11.10.9/22.

                                     Type: ``string``
   **arp_aging_type**                The aging type.

                                     Choose from:

                                     - arp_aging
                                     - nd_cache_expiry

                                     **Default**: arp_aging
   *arp_aging_timeout*               The ARP aging timeout in minutes <0..240>.

                                     Type: ``integer``

                                     **Default**: 4
   *nd_cache_expire_time*            Cache expiry timeout in seconds <30-14400>.

                                     Type: ``integer``

                                     **Default**: 270
   *mtu*                             L2 MTU size in bytes <Number:1522-9216>

                                     Type: ``integer``
   *mct_client_name*                 This specify the Cluster Client name for Node Specific configuration. Both `mct_client_name` and `mct_client_id` are mandatory args for mct client creation.

                                     Type: ``string``
   *mct_client_id*                   The ID for the Cluster Client. Valid IDs are 1 - 512. Both `mct_client_name` and `mct_client_id` are mandatory args for mct client creation.

                                     Type: ``integer``
   *display_show_results*            This enable or disable execution of show commands on the device to display the output.

                                     Type: ``boolean``
   **suppression_type**              The suppression type.

                                     Choose from:

                                     - ARP
                                     - ND
                                     - Both

                                     **Default**: ARP
   ================================  ======================================================================

