.. NOTE: This file has been generated automatically, don't manually edit it

create_vrf_evpn
~~~~~~~~~~~~~~~

**Description**: Create VRF for L3 tenants.Assign l3vni,route_distinguisher and ipv4/ipv6 route target. 

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
   **vrf_name**                      VRF name. For example vrf32 or 32

                                     Type: ``string``
   **l3vni**                         VNI for the VRF. '<NUMBER:1-16777215>'. Supported only for VDX

                                     Type: ``integer``
   *route_distinguisher*             VPN route Distinguisher. '<ASN:nn or IP-address:nn>'

                                     Type: ``array``
   *ipv4_route_target_import_evpn*   IPv4 import target VPN community. 'ASN:nn'. Supported only for VDX

                                     Type: ``string``
   *ipv4_route_target_export_evpn*   IPv4 export target VPN community. 'ASN:nn'. Supported only for VDX

                                     Type: ``string``
   *ipv6_route_target_import_evpn*   IPv6 import target VPN community. 'ASN:nn'. Supported only for VDX

                                     Type: ``string``
   *ipv6_route_target_export_evpn*   IPv6 import target VPN community. 'ASN:nn'. Supported only for VDX

                                     Type: ``string``
   *rbridge_id*                      Single or list of RBridge IDs separated by comma, for example, 1 or 1,2, 4.  This parameter is only applicable for VDX switches.

                                     Type: ``array``
   ================================  ======================================================================

