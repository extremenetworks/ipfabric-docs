.. NOTE: This file has been generated automatically, don't manually edit it

configure_bgp_neighbor
~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configure BGP neighbors on the switch. This action is not intended to be run directly by the end users. Used by configure_fabric_infra to configure IP Fabric infrastructure. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          The device to configure.

                                     Type: ``string``
   *user*                            The login user name to connect to the device.

                                     Type: ``string``
   *passwd*                          The login password to connect to the device.

                                     Type: ``string``
   **peer_asn**                      The peer ASN.

                                     Type: ``string``
   **peer_ip**                       The peer IP address.

                                     Type: ``string``
   **rbridge_id**                    The RBridge ID of the VDX switch. This parameter is only applicable. for VDX switches.

                                     Type: ``string``
   **role**                          The switch role.

                                     Type: ``string``
   *vrf*                             The VRF name <1-32> characters.

                                     Type: ``string``

                                     **Default**: default
   *multihop*                        This enable BGP multihop peering.

                                     Type: ``string``
   *allowas_in*                      This allow AS in.

                                     Type: ``string``
   *evpn*                            This enable EVPN.

                                     Type: ``boolean``
   *update_source*                   The update source.

                                     Type: ``string``
   *leaf_peer_group*                 The peer group for all leaf nodes.

                                     Type: ``string``
   *spine_peer_group*                The peer group for all spine nodes.

                                     Type: ``string``
   *network*                         The network to be advertised.

                                     Type: ``string``
   *single_spine_as*                 The flag to indicate that all spines have the same AS number assigned.

                                     Type: ``string``
   *encapsulation_type*              The encapsulation type for BGP neighbor. e.g. nsh, vxlan.

                                     Type: ``string``

                                     **Default**: vxlan
   ================================  ======================================================================

