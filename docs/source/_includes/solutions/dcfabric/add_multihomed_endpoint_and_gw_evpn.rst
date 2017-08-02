.. NOTE: This file has been generated automatically, don't manually edit it

add_multihomed_endpoint_and_gw_evpn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Add an endpoint (Server, FW, LB, VM) to an existing L3 tenant in an EVPN IP fabric and also configures IP Anycast Gateway. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``

                                     **Default**: admin
   *password*                        Login password to connect to the device

                                     Type: ``string``

                                     **Default**: password
   **intf_type**                     Interface type

                                     Choose from:

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel

                                     **Default**: tengigabitethernet
   **intf_name**                     List of ports that are members of the port channel. Examples for VDX, SLX are 24/0/1, 24/0/2 or 1/13, 1/14.

                                     Type: ``array``
   *intf_desc*                       Description for all the ports, space is not allowed, use '_' instead.

                                     Type: ``string``
   *enabled*                         Select true to enable the port, false to disable the port

                                     Type: ``boolean``

                                     **Default**: True
   *auto_pick_port_channel_id*       If selected, workflow will pick the lowest available port channel on the switch.

                                     Type: ``boolean``
   *port_channel_id*                 Portchannel interface number <NUMBER:1-6144>, if auto pick option is selected and switchport_mode is access no need to specify the VLAN ID.

                                     Type: ``string``
   *port_channel_desc*               Port channel description without any space

                                     Type: ``string``
   *mode*                            Port channel type.

                                     Choose from:

                                     - standard
                                     - brocade

                                     **Default**: standard
   *protocol*                        port channel mode

                                     Choose from:

                                     - active
                                     - passive
                                     - modeon

                                     **Default**: active
   **switchport_mode**               Switch port mode

                                     Choose from:

                                     - access
                                     - trunk

                                     **Default**: access
   **vlan_id**                       Single VLAN ID.  For 802.1Q VLANs ID must be below 4096, for service or transport VFs in a Virtual Fabrics context, valid range is from 4096 through 8191.

                                     Type: ``string``
   *vlan_desc*                       VLAN description, space is not allowed, use '_' instead.

                                     Type: ``string``
   *c_tag*                           Single VLAN ID <NUMBER:1-4090>. Valid only on NOS devices & if switchport_mode is trunk.

                                     Type: ``string``
   *vni*                             Specify the VNI mapping for the VLAN. <NUMBER:1-16777215>.

                                     Type: ``string``
   *mac_group_id*                    MAC group ID <NUMBER:1,500>. Only applicable if switchport_mode is access.

                                     Type: ``array``
   **vrf_name**                      VRF name

                                     Type: ``string``
   **anycast_address**               IPv4 or IPv6 address with subnet/prefix length.

                                     Type: ``string``
   **arp_aging_type**                Aging type

                                     Choose from:

                                     - arp_aging
                                     - nd_cache_expiry

                                     **Default**: arp_aging
   *arp_aging_timeout*               ARP aging timeout in minutes <0..240>.

                                     Type: ``integer``

                                     **Default**: 4
   *nd_cache_expire_time*            Cache expiry timeout in seconds <30-14400>.

                                     Type: ``integer``

                                     **Default**: 270
   *mtu*                             L2 MTU size in bytes <Number:1522-9216>

                                     Type: ``integer``
   *display_show_results*            Enable or disable execution of show commands on the device to display the output.

                                     Type: ``boolean``
   ================================  ======================================================================

