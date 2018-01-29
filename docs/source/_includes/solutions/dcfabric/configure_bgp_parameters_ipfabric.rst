.. NOTE: This file has been generated automatically, don't manually edit it

configure_bgp_parameters_ipfabric
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configure BGP. This action is not intended to be run directly by the end users. Used configure_fabric_infra to configure IP Fabric infrastructure. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          The management IP address of the target device.

                                     Type: ``string``
   *user*                            The login user name to connect to the device.

                                     Type: ``string``
   *passwd*                          The login password to connect to the device.

                                     Type: ``string``
   **local_asn**                     The local ASN.

                                     Type: ``string``
   **rbridge_id**                    The RBridge ID of the VDX switch. This parameter is only applicable for VDX switches.

                                     Type: ``string``
   **role**                          The switch role.

                                     Type: ``string``
   *vrf*                             The VRF name in <1-32> characters.

                                     Type: ``string``

                                     **Default**: default
   *afi*                             The IP Address familty type.

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   *bfd_tx*                          The BFD TX timer.

                                     Type: ``string``
   *bfd_rx*                          The BFD RX timer.

                                     Type: ``string``
   *bfd_multiplier*                  The BFD Multiplier.

                                     Type: ``string``
   *max_paths*                       The maximum paths for BGP address families.

                                     Type: ``string``
   *recursion*                       This configure next hop recursion.

                                     Type: ``boolean``
   *evpn*                            This enable EVPN

                                     Type: ``boolean``
   *loopback_port_number*            The loopback port number

                                     Type: ``string``
   *update_source*                   This epdate source.

                                     Type: ``string``
   *leaf_peer_group*                 THe peer group name for all leaf nodes.

                                     Type: ``string``
   *spine_peer_group*                The peer group name for all spine nodes.

                                     Type: ``string``
   *peer_ebgp_multihop*              This enable BGP multihop peering

                                     Type: ``string``
   *single_spine_as*                 The flag to indicate that all spines have the same AS number assigned.

                                     Type: ``string``
   ================================  ======================================================================

