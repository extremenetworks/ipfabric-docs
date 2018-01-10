.. NOTE: This file has been generated automatically, don't manually edit it

add_singlehomed_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Create VLAN, configure interface as Access or Trunk, and validate interface state. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``

                                     **Default**: admin
   *password*                        Login password to connect to the device

                                     Type: ``string``

                                     **Default**: password
   **intf_type**                     Interface type

                                     Choose from:

                                     - ethernet
                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ve
                                     - loopback

                                     **Default**: tengigabitethernet
   **intf_name**                     Single port. Examples for VDX, SLX are  24/0/1 or 1/13.

                                     Type: ``string``
   *intf_desc*                       Port description, space is not allowed, use '_' instead.

                                     Type: ``string``
   *enabled*                         Select true to enable the port, false to disable the port

                                     Type: ``boolean``

                                     **Default**: True
   **switchport_mode**               Switch port mode

                                     Choose from:

                                     - access
                                     - trunk
                                     - trunk_no_default_native

                                     **Default**: access
   *auto_pick_network_id*            For service or transport VFs in a Virtual Fabrics context, if selected, workflow will pick the lowest available Single/Range of VF IDs available on the switch, valid range is from 4096 through 8191. In Bridge-domain context, if selected, workflow will pick the lowest available Single/Range of BRIDGE-DOMAIN IDs available on the switch, valid range is from 1 through 4096. For Virtual Fabric/Bridge-Domain and ctag classification , use auto_pick_network_id or network_id.

                                     Type: ``boolean``
   *network_id*                      If auto_pick_network_id=False, Single or range of VLANs to be configured on the interface.For service or transport VFs in a Virtual Fabrics context, valid range is from 4096 through 8191. Single or range of Bridge-domain ID in SLXOS platforms, valid range is from 1 through 4096.

                                     Type: ``string``
   *vlan_id*                         Single or range of VLANs to be configured on the interface. For 802.1Q VLANs ID must be below 4096. Valid for vlan_id only use cases. For Virtual Fabric/Bridge-Domain and ctag classification , use auto_pick_network_id or network_id.

                                     Type: ``string``
   *vlan_desc*                       VLAN description, space is not allowed, use '_' instead.  Same VLAN description is configured on all the VLANs when the range is provided.

                                     Type: ``string``
   *c_tag*                           Single or range of VLAN IDs <NUMBER:1-4090>. Valid only if switchport_mode is trunk.

                                     Type: ``string``
   *mac_group_id*                    MAC group ID <NUMBER:1,500>. Only applicable if switchport_mode is access and on VDX platforms.

                                     Type: ``array``
   *auto_pick_lif_id*                Auto generate physical port lifs or port channel lifs.

                                     Type: ``boolean``
   *vlan_type*                       vlan tag type to be configured under logical interface.

                                     Choose from:

                                     - untagged
                                     - tagged

                                     **Default**: tagged
   *vni*                             Specify single or range of VNI <NUMBER:1-16777215> mappings for VLANs/BDs, for example 10 or 10-15 or 10,12,13-15. When using ranges, the number of values in a VLAN/BD ID range must correspond to the number of values in a VNI range.

                                     Type: ``string``
   ================================  ======================================================================

