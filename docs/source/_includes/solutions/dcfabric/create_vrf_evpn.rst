.. NOTE: This file has been generated automatically, don't manually edit it

create_vrf_evpn
~~~~~~~~~~~~~~~

**Description**: This will create VRF for L3 tenants. It will assign l3vni, route_distinguisher and IPv4/IPv6 route target. 

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
   **vrf_name**                      The VRF name. For example vrf32 or 32.

                                     Type: ``string``
   *l3vni*                           THe VNI for the VRF. Valid Values for VDX. '<NUMBER:1-16777215>', Valid Values for SLX. '<NUMBER:1-4096>'.

                                     Type: ``integer``
   *route_distinguisher*             The VPN route Distinguisher. '<ASN:nn or IP-address:nn>'.

                                     Type: ``array``
   *ipv4_route_target_import_evpn*   The IPv4 import target VPN community. 'ASN:nn'.

                                     Type: ``string``
   *ipv4_route_target_export_evpn*   The IPv4 export target VPN community. 'ASN:nn'.

                                     Type: ``string``
   *ipv6_route_target_import_evpn*   The IPv6 import target VPN community. 'ASN:nn'.

                                     Type: ``string``
   *ipv6_route_target_export_evpn*   The IPv6 import target VPN community. 'ASN:nn'.

                                     Type: ``string``
   *rbridge_id*                      A single or a list of RBridge IDs separated by comma, for example, 1 or 1,2, 4. This parameter is only applicable for VDX switches.

                                     Type: ``array``
   ================================  ======================================================================

