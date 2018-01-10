.. NOTE: This file has been generated automatically, don't manually edit it

configure_bridge_domain
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Create bridge domain for p2mp/p2p and bind the logical interface. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``
   *password*                        Login password to connect to the device

                                     Type: ``string``
   **bridge_domain_id**              Bridge-domain ID.

                                     Type: ``string``
   *bridge_domain_service_type*      bridge domain service type.

                                     Choose from:

                                     - p2mp
                                     - p2p

                                     **Default**: p2mp
   *vc_id*                           VC Id under the VPLS Instance. Range <1-4294967295>

                                     Type: ``string``
   *statistics*                      Configure Statistics.

                                     Type: ``boolean``

                                     **Default**: True
   *bpdu_drop_enable*                Drop BPDU packets.

                                     Type: ``boolean``

                                     **Default**: True
   *local_switching*                 Configure local switching.

                                     Type: ``boolean``

                                     **Default**: True
   *peer_ip*                         Single or list of IPv4/IPv6 addresses to be configured on the bridge_domain. IPv4, for example 10.0.0.10.

                                     Type: ``array``
   *pw_profile_name*                 Pw-profile name (Max Size - 64).

                                     Type: ``string``

                                     **Default**: default
   *intf_type*                       Logical interface type.Valid Types 'ethernet','port_channel'. For Example. 'ethernet' --> if all the entries in logical_interface_number are of type ethernet 'port_channel' --> if all the entries in logical_interface_number are of type port_channel 'ethernet,port_channel,ethernet,port_channel' --> If the entries in logical_interface_number are of mixed types.

                                     Type: ``string``
   *logical_interface_number*        Physical port or port channel number list.Logical Interace ID. E.g '0/34.11,21.1,0/35.1,22.1'

                                     Type: ``string``
   *vlan_id*                         VLAN ID to map the broadcast domain to a router interface.

                                     Type: ``string``
   ================================  ======================================================================

