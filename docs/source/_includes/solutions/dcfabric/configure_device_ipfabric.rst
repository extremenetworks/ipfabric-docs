.. NOTE: This file has been generated automatically, don't manually edit it

configure_device_ipfabric
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configures the switch. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          The anagement IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   *afi*                             The IP address family.

                                     Type: ``string``
   *allowas_in*                      Allows AS in.

                                     Type: ``string``
   *anycast_mac*                     The Anycast MAC address.

                                     Type: ``string``
   *ipv6_anycast_mac*                The IPV6 Anycast MAC address.

                                     Type: ``string``
   *bfd_multiplier*                  The BFD multiplier.

                                     Type: ``string``
   *bfd_rx*                          The BFD receive.

                                     Type: ``string``
   *bfd_tx*                          The BFD transmit.

                                     Type: ``string``
   *mtu*                             The MTU size.

                                     Type: ``string``
   *ip_mtu*                          The IP MTU size.

                                     Type: ``string``
   *ipv6_mtu*                        The IP MTU size.

                                     Type: ``string``
   *bgp_local_asn*                   The BGP local ASN.

                                     Type: ``string``
   *bgp_multihop*                    The Multihop.

                                     Type: ``string``
   **bgp_neighbors**                 The BGP neighbors.

                                     Type: ``array``
   *bgp_vrf*                         The BGP VRF name.

                                     Type: ``string``
   *chassis*                         The chassis.

                                     Type: ``boolean``
   *evpn*                            This enable EVPN.

                                     Type: ``boolean``

                                     **Default**: True
   **interfaces**                    The interface list.

                                     Type: ``array``
   *loopback_port_number*            The loopback port number.

                                     Type: ``string``
   *max_paths*                       The maximum paths.

                                     Type: ``string``
   *p2p_link_range*                  The P2P link range.

                                     Type: ``string``
   **rbridge_id**                    The RBridge ID of the VDX switch. This parameter is only applicable. for VDX switches.

                                     Type: ``string``
   *recursion*                       This enables recursion.

                                     Type: ``boolean``

                                     **Default**: True
   *role*                            The switch role.

                                     Type: ``string``
   *source*                          The source.

                                     Type: ``string``
   *update_source*                   This updates the source.

                                     Type: ``string``
   *fabric*                          The fabric name.

                                     Type: ``string``
   *vtep_loopback_port_number*       The VTEP loopback port number.

                                     Type: ``string``
   *mac_move_threshold*              The MAC move threshold.

                                     Type: ``integer``
   *vni_auto_map*                    This cnfigures VLAN/bridge-domain to VNI auto mapping under overlay gateway.

                                     Type: ``boolean``
   *leaf_peer_group*                 The peer group name for all the leaf nodes.

                                     Type: ``string``
   *spine_peer_group*                The peer group name for all the spines.

                                     Type: ``string``
   *network*                         The network to be advertised.

                                     Type: ``string``
   *single_spine_as*                 The AS number to be assigned to all spines.

                                     Type: ``string``
   **device**                        The IP address of the target device.

                                     Type: ``string``
   *enable_vf*                       This enable or disable VCS virtual-fabric on a VCS fabric.

                                     Type: ``boolean``
   **principal_ip**                  The principal IP address of the target device.

                                     Type: ``string``
   *control_vlan*                    This controls VLAN for MCT cluster

                                     Type: ``string``
   *switch_model*                    The model of the device.

                                     Type: ``string``
   *mct_interfaces*                  The list of ports that are members of the port channel. 1/13, 1/14.

                                     Type: ``array``
   *cluster_peer_ip*                 The cluster peer IP address in a.b.c.d format.

                                     Type: ``string``
   *node_id*                         The ID of the node, values <1-128>.

                                     Type: ``integer``

                                     **Default**: 1
   *is_principal*                    The principal Node of Cluster.

                                     Type: ``boolean``
   ================================  ======================================================================

