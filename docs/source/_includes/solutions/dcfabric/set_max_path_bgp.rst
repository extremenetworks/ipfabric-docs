.. NOTE: This file has been generated automatically, don't manually edit it

set_max_path_bgp
~~~~~~~~~~~~~~~~

**Description**: Configure maximum paths for BGP under VRF address-family 

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
   *rbridge_id*                      Single or list of ports that are members of the port channel. Examples for VDX, SLX are  24/0/1, 24/0/2 or 1/13, 1/14

                                     Type: ``array``
   **ipv4_unicast**                  Enable IPv4 unicast address family

                                     Type: ``boolean``
   **ipv6_unicast**                  Enable IPv6 unicast address family

                                     Type: ``boolean``
   *ipv4_vrf_name*                   IPv4 VRF name

                                     Type: ``string``
   *ipv6_vrf_name*                   IPv6 VRF name

                                     Type: ``string``
   **maximum_paths**                 Forward packets over multiple paths

                                     Type: ``integer``

                                     **Default**: 8
   ================================  ======================================================================

