.. NOTE: This file has been generated automatically, don't manually edit it

configure_device_ipfabric
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure switch 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``

                                     **Default**: admin
   *password*                        Login password to connect to the device

                                     Type: ``string``

                                     **Default**: password
   *afi*                             IP address family

                                     Type: ``string``
   *allowas_in*                      Allow AS in

                                     Type: ``string``
   *anycast_mac*                     Anycast MAC address

                                     Type: ``string``
   *bfd_multiplier*                  BFD multiplier

                                     Type: ``string``
   *bfd_rx*                          BFD receive

                                     Type: ``string``
   *bfd_tx*                          BFD transmit

                                     Type: ``string``
   *mtu*                             MTU size

                                     Type: ``string``
   *ip_mtu*                          IP MTU size

                                     Type: ``string``
   *bgp_local_asn*                   BGP local ASN

                                     Type: ``string``
   *bgp_multihop*                    Multihop

                                     Type: ``string``
   **bgp_neighbors**                 BGP neighbors

                                     Type: ``array``
   *bgp_vrf*                         BGP VRF name

                                     Type: ``string``
   *chassis*                         Chassis

                                     Type: ``boolean``
   *evpn*                            Enable EVPN

                                     Type: ``boolean``

                                     **Default**: True
   **interfaces**                    Interface list

                                     Type: ``array``
   *loopback_port_number*            Loopback port number

                                     Type: ``string``
   *max_paths*                       Maximum paths

                                     Type: ``string``
   *p2p_link_range*                  P2P link range

                                     Type: ``string``
   **rbridge_id**                    RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``string``
   *recursion*                       Enable recursion

                                     Type: ``boolean``

                                     **Default**: True
   *role*                            Switch role

                                     Type: ``string``
   *source*                          Source

                                     Type: ``string``
   *update_source*                   Update Source

                                     Type: ``string``
   *fabric*                          Fabric name

                                     Type: ``string``
   *vtep_loopback_port_number*       VTEP loopback port number

                                     Type: ``string``
   *mac_move_threshold*              MAC move threshold

                                     Type: ``integer``
   *leaf_peer_group*                 Peer group name for all the leaf nodes

                                     Type: ``string``
   *spine_peer_group*                Peer group name for all the spines

                                     Type: ``string``
   *network*                         network to be advertised

                                     Type: ``string``
   *single_spine_as*                 AS number to be assigned to all spines

                                     Type: ``string``
   **device**                        IP address of the target device.

                                     Type: ``string``
   ================================  ======================================================================

