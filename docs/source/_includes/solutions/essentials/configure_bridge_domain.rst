.. NOTE: This file has been generated automatically, don't manually edit it

configure_bridge_domain
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This will create the bridge domain for p2mp/p2p and bind the logical interface. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``
   *password*                        THe login password to connect to the device.

                                     Type: ``string``
   **bridge_domain_id**              The Bridge-domain ID. Valid values are <1-4096> on SLX9140,SLX9850,SLX9540 and <1-3566> on SLX9240.

                                     Type: ``string``
   *bridge_domain_service_type*      The bridge domain service type. `p2p` is valid only on SLX9850,SLX9540.

                                     Choose from:

                                     - p2mp
                                     - p2p

                                     **Default**: p2mp
   *vc_id*                           The VC Id under the VPLS Instance. Range <1-4294967295>. Valid only on SLX9850,SLX9540.

                                     Type: ``string``
   *statistics*                      Configure Statistics.

                                     Type: ``boolean``

                                     **Default**: True
   *bpdu_drop_enable*                Drop BPDU packets. Valid only on SLX9850,SLX9540.

                                     Type: ``boolean``
   *local_switching*                 Configured local switching. Valid only on SLX9850,SLX9540.

                                     Type: ``boolean``
   *peer_ip*                         A single or a list of IPv4/IPv6 addresses to be configured on the bridge_domain. IPv4, for example 10.0.0.10. Valid only on SLX9850,SLX9540.

                                     Type: ``array``
   *pw_profile_name*                 The pw-profile name (Max Size - 64). Valid only on SLX9850,SLX9540.

                                     Type: ``string``

                                     **Default**: default
   *intf_type*                       The logical interface type. Valid Types are 'ethernet','port_channel'. For Example. 'ethernet' --> if all the entries in logical_interface_number are of type ethernet 'port_channel' --> if all the entries in logical_interface_number are of type port_channel 'ethernet,port_channel,ethernet,port_channel' --> If the entries in logical_interface_number are of mixed types.

                                     Type: ``string``
   *logical_interface_number*        The physical port or port channel number list. Format for the logical interfaces is <physical/port-channel number>.<number>. For E.g '0/34.11,21.1,0/35.1,22.1'

                                     Type: ``string``
   *vlan_id*                         The VLAN ID to map the broadcast domain to a router interface. Valid range <1-4096>

                                     Type: ``string``
   ================================  ======================================================================

