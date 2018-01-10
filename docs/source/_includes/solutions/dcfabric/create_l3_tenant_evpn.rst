.. NOTE: This file has been generated automatically, don't manually edit it

create_l3_tenant_evpn
~~~~~~~~~~~~~~~~~~~~~

**Description**: Create VRF, create L3VNI on VE interface and assign VRF forwarding, redistribute connected routes in the BGP VRF address families. 

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
   **vrf_name**                      VRF name, 1-32 characters

                                     Type: ``string``
   *vlan_id*                         Single VLAN ID. VDX <1-8191> and SLXOS <1-4090>. In Bridge-domain context for SLXOS, use network_id

                                     Type: ``string``
   *l3vni*                           L3VNI for the VRF. VDX <1-8191> and SLX <1-4096>

                                     Type: ``integer``
   *network_id*                      In Bridge-domain context for SLXOS, if selected, workflow will associate L3VNI as BRIDGE-DOMAIN ID valid range is from 1 through 4096.

                                     Type: ``integer``
   **route_distinguisher**           BGP router ID of the leafs, for example, 10.20.31.1, 10.20.31.2

                                     Type: ``array``
   **route_target**                  Route Target for the address family, for example, 101

                                     Type: ``integer``
   **tenant_addressing_type**        Tenant IP addressing type

                                     Choose from:

                                     - ipv4
                                     - ipv6
                                     - both

                                     **Default**: ipv4
   **maximum_paths**                 Forward packets over multiple paths

                                     Type: ``integer``

                                     **Default**: 8
   ================================  ======================================================================

