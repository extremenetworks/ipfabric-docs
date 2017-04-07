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
   *intf_desc*                       Interface description

                                     Type: ``string``
   *enabled*                         Admin setting on the interface.

                                     Type: ``boolean``

                                     **Default**: True
   *auto_pick_port_channel_id*       If selected, workflow will pick the lowest available port channel on the switch.

                                     Type: ``boolean``
   *port_channel_id*                 Portchannel interface number <NUMBER:1-6144>, if auto pick option is selected and switchport_mode is access no need to specify the VLAN ID.

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
   **vlan_id**                       Single VLAN ID

                                     Type: ``string``
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
   ================================  ======================================================================

