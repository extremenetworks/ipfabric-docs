.. NOTE: This file has been generated automatically, don't manually edit it

add_multihomed_endpoint_and_gw
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Add an endpoint (VM, server, LB, FW) to a VCS or an IP fabric (non EVPN) for an existing tenant. Create interface/port-channel configurations based on the user input on devices. Enable VRRPE configurations 

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
   *rbridge_id*                      Single or comma separated RBridge ID(s) to create VE, VRRPe.  Applicable only for VDX switches.

                                     Type: ``array``
   **intf_type**                     Interface type

                                     Choose from:

                                     - ethernet
                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - VE
                                     - loopback

                                     **Default**: tengigabitethernet
   **intf_name**                     Single or list of ports that are members of the port channel. Examples for VDX, SLX are  24/0/1, 24/0/2 or 24/1, 24/2

                                     Type: ``array``
   *intf_desc*                       Description for all the ports, space is not allowed, use '_' instead.

                                     Type: ``string``
   *enabled*                         Enable or disable admin setting on the interface

                                     Type: ``boolean``

                                     **Default**: True
   **switchport_mode**               Switch port mode

                                     Choose from:

                                     - access
                                     - trunk
                                     - trunk_no_default_native

                                     **Default**: access
   *auto_pick_port_channel_id*       If selected, workflow will pick the lowest available port channel on the switch.

                                     Type: ``boolean``
   *port_channel_id*                 Port channel interface number.<NUMBER:1-6144>

                                     Type: ``string``
   *port_channel_desc*               Port channel description without any space

                                     Type: ``string``
   *mode*                            Portchannel type

                                     Choose from:

                                     - standard
                                     - brocade

                                     **Default**: standard
   *protocol*                        Portchannel mode type

                                     Choose from:

                                     - active
                                     - passive
                                     - modeon

                                     **Default**: active
   *auto_pick_network_id*            For service or transport VFs in a Virtual Fabrics context, if selected, workflow will pick the lowest available Single/Range of VF IDs available on the switch, valid range is from 4096 through 8191. For Virtual Fabric/Bridge-Domain and ctag classification , use auto_pick_network_id or network_id. Valid only on VDX platform.

                                     Type: ``boolean``
   *network_id*                      If auto_pick_network_id=False, Single or range of VLANs to be configured on the interface.For service or transport VFs in a Virtual Fabrics context, valid range is from 4096 through 8191. Valid only on VDX platform.

                                     Type: ``string``
   *vlan_id*                         Single or range of VLANs to be configured on the interface. For 802.1Q VLANs ID must be below 4096. Valid for vlan_id only use cases. For Virtual Fabric and ctag classification , use auto_pick_network_id or network_id.

                                     Type: ``string``
   *vlan_desc*                       VLAN description, space is not allowed, use '_' instead.

                                     Type: ``string``
   *c_tag*                           Single VLAN ID <NUMBER:1-4090>. Valid only on NOS devices & if switchport_mode is trunk.

                                     Type: ``string``
   *mac_group_id*                    MAC group ID <NUMBER:1,500>. Only applicable if switchport_mode is access.

                                     Type: ``array``
   *ve_ip*                           Single or list of IPv4/IPv6 addresses to be configured on the VE. IPv4/subnet-length or IPv6/prefix-length, for example 10.0.0.10/22, 30.0.0.10/22.

                                     Type: ``array``
   *vrid*                            Virtual group ID

                                     Type: ``string``
   *virtual_ip*                      VRRPe virtual IP address without the netmask

                                     Type: ``string``
   *vrf_name*                        VRF name. For example vrf32 or 32.

                                     Type: ``string``
   *afi*                             IP address type

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   *mtu*                             L2 MTU size in bytes <Number:1522-9216>

                                     Type: ``integer``
   *display_show_results*            Enable or disable execution of show commands on the device to display the output.

                                     Type: ``boolean``
   ================================  ======================================================================

