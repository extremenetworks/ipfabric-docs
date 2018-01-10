.. NOTE: This file has been generated automatically, don't manually edit it

configure_bgp_parameters_ipfabric
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure BGP. This action is not intended to be run directly by the end users. Used by configure_fabric_infra to configure IP Fabric infrastructure. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          Management IP address of the target device

                                     Type: ``string``
   *user*                            Login user name to connect to the device

                                     Type: ``string``
   *passwd*                          Login password to connect to the device

                                     Type: ``string``
   **local_asn**                     Local ASN

                                     Type: ``string``
   **rbridge_id**                    RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``string``
   **role**                          Switch role

                                     Type: ``string``
   *vrf*                             VRF name in <1-32> characters.

                                     Type: ``string``

                                     **Default**: default
   *afi*                             IP Address familty type

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   *bfd_tx*                          BFD TX timer

                                     Type: ``string``
   *bfd_rx*                          BFD RX timer

                                     Type: ``string``
   *bfd_multiplier*                  BFD Multiplier

                                     Type: ``string``
   *max_paths*                       Maximum paths for BGP address families

                                     Type: ``string``
   *recursion*                       Configure next hop recursion

                                     Type: ``boolean``
   *evpn*                            Enable EVPN

                                     Type: ``boolean``
   *loopback_port_number*            Loopback port number

                                     Type: ``string``
   *update_source*                   Update source

                                     Type: ``string``
   *leaf_peer_group*                 Peer group name for all leaf nodes

                                     Type: ``string``
   *spine_peer_group*                Peer group name for all spine nodes

                                     Type: ``string``
   *peer_ebgp_multihop*              Enable BGP multihop peering

                                     Type: ``string``
   *single_spine_as*                 Flag to indicate that all spines have the same AS number assigned

                                     Type: ``string``
   ================================  ======================================================================

