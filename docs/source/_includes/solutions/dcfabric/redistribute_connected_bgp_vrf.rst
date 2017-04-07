.. NOTE: This file has been generated automatically, don't manually edit it

redistribute_connected_bgp_vrf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Redistribute BGP connected routes under VRF address-family 

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
   *rbridge_id*                      Single or list of RBridge IDs separated by comma, for example, 1 or 1,2, 4.  This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **ipv4_unicast**                  Configure IPv4 unicast address family

                                     Type: ``boolean``
   **ipv6_unicast**                  Configure IPv6 unicast address family

                                     Type: ``boolean``
   *ipv4_vrf_name*                   IPv4 VRF name

                                     Type: ``string``
   *ipv6_vrf_name*                   IPv6 VRF name

                                     Type: ``string``
   ================================  ======================================================================

