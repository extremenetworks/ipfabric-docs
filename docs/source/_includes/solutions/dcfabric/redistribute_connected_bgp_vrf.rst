.. NOTE: This file has been generated automatically, don't manually edit it

redistribute_connected_bgp_vrf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This will redistribute BGP connected routes under VRF address-family. 

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
   *rbridge_id*                      A single or list of RBridge IDs separated by comma, for example, 1 or 1,2, 4. This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **ipv4_unicast**                  This will configure IPv4 unicast address family.

                                     Type: ``boolean``
   **ipv6_unicast**                  This will configure IPv6 unicast address family.

                                     Type: ``boolean``
   *ipv4_vrf_name*                   The IPv4 VRF name.

                                     Type: ``string``
   *ipv6_vrf_name*                   The IPv6 VRF name.

                                     Type: ``string``
   ================================  ======================================================================

