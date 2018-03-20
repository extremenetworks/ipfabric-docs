.. NOTE: This file has been generated automatically, don't manually edit it

create_l3_tenant_evpn
~~~~~~~~~~~~~~~~~~~~~

**Description**: This create VRF, create L3VNI on VE interface and assign VRF forwarding, redistribute connected routes in the BGP VRF address families. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   **vrf_name**                      The VRF name, 1-32 characters.

                                     Type: ``string``
   **l3vni**                         L3VNI for the VRF. VDX <1-8191> and SLX <1-4096>.

                                     Type: ``integer``
   *vlan_id*                         A single VLAN ID. VDX <1-8191> and SLXOS <1-4090>. If vlan_id is passed for VDX devices , `vlan_id` & `l3vni` args must of be same value. If vlan_id is not passed for VDX devices , `l3vni` will be assumed as `vlan_id`. This is mandatory args for SLXOS devices. In Bridge-domain context for SLXOS, use network_id.

                                     Type: ``string``
   *network_id*                      Bridge-domain ID. Valid only on SLXOS devices. Valid range is from 1 through 4096 on SLX-9140/SLX-9850/SLX-9540 and 1 through 3566 on SLX-9240.

                                     Type: ``integer``
   **route_distinguisher**           The BGP router ID of the leafs, for example, 10.20.31.1, 10.20.31.2.

                                     Type: ``array``
   **route_target**                  The Route Target for the address family, for example, 101.

                                     Type: ``integer``
   **tenant_addressing_type**        The Tenant IP addressing type.

                                     Choose from:

                                     - ipv4
                                     - ipv6
                                     - both

                                     **Default**: ipv4
   **maximum_paths**                 Forward packets over multiple paths.

                                     Type: ``integer``

                                     **Default**: 8
   ================================  ======================================================================

