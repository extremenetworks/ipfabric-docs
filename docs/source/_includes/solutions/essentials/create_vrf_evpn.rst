.. NOTE: This file has been generated automatically, don't manually edit it

create_vrf_evpn
~~~~~~~~~~~~~~~

**Description**: Create VRF for L3 tenants.Assign l3vni,route_distinguisher and ipv4/ipv6 route target. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Ip address of the device

                                     Type: ``string``
   *username*                        login username

                                     Type: ``string``

                                     **Default**: admin
   *password*                        login password

                                     Type: ``string``

                                     **Default**: password
   **vrf_name**                      vrf name.Example:- 'vrf32 or 32'

                                     Type: ``string``
   **l3vni**                         vni for the VRF. '<NUMBER:1-16777215>'

                                     Type: ``integer``
   *route_distinguisher*             VPN Route Distinguisher. '<ASN:nn or IP-address:nn>'

                                     Type: ``array``
   *ipv4_route_target_import_evpn*   ipv4 import Target VPN community. 'ASN:nn'

                                     Type: ``string``
   *ipv4_route_target_export_evpn*   ipv4 export Target VPN community. 'ASN:nn'

                                     Type: ``string``
   *ipv6_route_target_import_evpn*   ipv6 import Target VPN community. 'ASN:nn'

                                     Type: ``string``
   *ipv6_route_target_export_evpn*   ipv6 import Target VPN community. 'ASN:nn'

                                     Type: ``string``
   *rbridge_id*                      Single/List of rbridge ID's(example rbridge_id=1 or rbridge_id=1,2,3)

                                     Type: ``array``
   ================================  ======================================================================

