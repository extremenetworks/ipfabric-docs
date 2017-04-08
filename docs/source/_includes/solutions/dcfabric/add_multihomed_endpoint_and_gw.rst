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
   *intf_desc*                       Interface description

                                     Type: ``string``
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
   *enabled*                         Enable or disable admin setting on the interface

                                     Type: ``boolean``

                                     **Default**: True
   **vlan_id**                       Single or range of VLAN(s)

                                     Type: ``string``
   **switchport_mode**               Switch port mode

                                     Choose from:

                                     - access
                                     - trunk

                                     **Default**: access
   *port_channel_id*                 Port channel interface number.<NUMBER:1-6144>

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
   ================================  ======================================================================

