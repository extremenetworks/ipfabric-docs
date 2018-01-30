.. NOTE: This file has been generated automatically, don't manually edit it

configure_bgp_ipfabric
~~~~~~~~~~~~~~~~~~~~~~

**Description**: This will configure BGP. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   **rbridge_id**                    The RBridge ID of the VDX switch. This parameter is only applicable for VDX switches.

                                     Type: ``string``
   *role*                            The switch role.

                                     Type: ``string``
   *afi*                             The IP address family.

                                     Type: ``string``
   *allowas_in*                      This allows AS in.

                                     Type: ``string``
   *bfd_multiplier*                  The BFD multiplier.

                                     Type: ``string``
   *bfd_rx*                          The BFD receive.

                                     Type: ``string``
   *bfd_tx*                          The BFD transmit.

                                     Type: ``string``
   *evpn*                            This enable EVPN.

                                     Type: ``boolean``

                                     **Default**: True
   *local_asn*                       The local ASN.

                                     Type: ``string``
   *loopback_port_number*            The loopback port number.

                                     Type: ``string``
   *max_paths*                       The maximum paths.

                                     Type: ``string``
   *multihop*                        The multihop.

                                     Type: ``string``
   **neighbors**                     The neighbors.

                                     Type: ``array``
   *p2p_link_range*                  The P2P link range.

                                     Type: ``string``
   *recursion*                       The recursion.

                                     Type: ``boolean``

                                     **Default**: True
   *source*                          The source.

                                     Type: ``string``
   *update_source*                   The update source.

                                     Type: ``string``
   *vrf*                             The VRF name.

                                     Type: ``string``
   *leaf_peer_group*                 The peer group name for all leaf nodes.

                                     Type: ``string``
   *spine_peer_group*                The peer group name for all spine nodes.

                                     Type: ``string``
   *network*                         The BGP network to be advertised.

                                     Type: ``string``
   *single_spine_as*                 The AS number to be assigned to all spines.

                                     Type: ``string``
   ================================  ======================================================================

