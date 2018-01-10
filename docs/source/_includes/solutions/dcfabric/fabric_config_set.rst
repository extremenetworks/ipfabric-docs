.. NOTE: This file has been generated automatically, don't manually edit it

fabric_config_set
~~~~~~~~~~~~~~~~~

**Description**: Add or Update the specified fabric parameter from the fabric template in the inventory 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **fabric**                        Name of the fabric

                                     Type: ``string``
   *key*                             Name of the fabric key to be added or updated

                                     Choose from:

                                     - p2p_link_range
                                     - spine_asn_block
                                     - spine_peer_group
                                     - leaf_asn_block
                                     - leaf_peer_group
                                     - loopback_ip_range
                                     - loopback_port_number
                                     - evpn_enabled
                                     - vtep_loopback_port_number
                                     - anycast_mac
                                     - bfd_tx
                                     - bfd_rx
                                     - bfd_multiplier
                                     - bgp_multihop
                                     - max_paths
                                     - allowas_in
                                     - mtu
                                     - ip_mtu
                                     - vni_auto_map
                                     - enable_vf
                                     - control_VLAN
                                     - mct_link_ip_range
   *other_key*                       Other fabric keys to be added or updated, which are not available through key enum

                                     Type: ``string``
   **value**                         Value of the parameter to be added or updated

                                     Type: ``string``
   ================================  ======================================================================

