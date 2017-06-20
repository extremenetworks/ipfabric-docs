.. NOTE: This file has been generated automatically, don't manually edit it

configure_bgp_neighbor
~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure BGP neighbors on the switch. This action is not intended to be run directly by the end users. Used by configure_fabric_infra to configure IP Fabric infrastructure. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          Device to configure

                                     Type: ``string``
   *user*                            Login user name to connect to the device

                                     Type: ``string``
   *passwd*                          Login password to connect to the device

                                     Type: ``string``
   **peer_asn**                      Peer ASN

                                     Type: ``string``
   **peer_ip**                       Peer IP address

                                     Type: ``string``
   **rbridge_id**                    RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``string``
   **role**                          Switch role

                                     Type: ``string``
   *vrf*                             VRF name <1-32> characters

                                     Type: ``string``

                                     **Default**: default
   *multihop*                        Enable BGP multihop peering

                                     Type: ``string``
   *allowas_in*                      Allow AS in

                                     Type: ``string``
   *evpn*                            Enable EVPN

                                     Type: ``boolean``
   *update_source*                   Update source

                                     Type: ``string``
   *leaf_peer_group*                 Peer group for all leaf nodes

                                     Type: ``string``
   *spine_peer_group*                Peer group for all spine nodes

                                     Type: ``string``
   *network*                         network to be advertised

                                     Type: ``string``
   *single_spine_as*                 Flag to indicate that all spines have the same AS number assigned

                                     Type: ``string``
   ================================  ======================================================================

