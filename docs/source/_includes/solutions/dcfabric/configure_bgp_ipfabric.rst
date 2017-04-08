.. NOTE: This file has been generated automatically, don't manually edit it

configure_bgp_ipfabric
~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure BGP 

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
   **rbridge_id**                    RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``string``
   *afi*                             IP address family

                                     Type: ``string``
   *allowas_in*                      Allow AS in

                                     Type: ``string``
   *bfd_multiplier*                  BFD multiplier

                                     Type: ``string``
   *bfd_rx*                          BFD receive

                                     Type: ``string``
   *bfd_tx*                          BFD transmit

                                     Type: ``string``
   *evpn*                            Enable EVPN

                                     Type: ``boolean``

                                     **Default**: True
   *local_asn*                       Local ASN

                                     Type: ``string``
   *loopback_port_number*            Loopback port number

                                     Type: ``string``
   *max_paths*                       Maximum paths

                                     Type: ``string``
   *multihop*                        Multihop

                                     Type: ``string``
   **neighbors**                     Neighbors

                                     Type: ``array``
   *p2p_link_range*                  P2P link range

                                     Type: ``string``
   *recursion*                       Recursion

                                     Type: ``boolean``

                                     **Default**: True
   *retain_rt_all*                   Retain RT all

                                     Type: ``boolean``
   *source*                          Source

                                     Type: ``string``
   *update_source*                   Update source

                                     Type: ``string``
   *vrf*                             VRF name

                                     Type: ``string``
   ================================  ======================================================================

