.. NOTE: This file has been generated automatically, don't manually edit it

set_max_path_bgp
~~~~~~~~~~~~~~~~

**Description**: configure max-paths bgp under vrf address-family 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Device to get the NOS version

                                     Type: ``string``
   *username*                        login username

                                     Type: ``string``

                                     **Default**: admin
   *password*                        login password

                                     Type: ``string``

                                     **Default**: password
   *rbridge_id*                      Single/List of rbridge ID's(example rbridge_id=1 or rbridge_id=1,2,3)

                                     Type: ``array``
   **ipv4_unicast**                  Address family unicast ipv4

                                     Type: ``boolean``
   **ipv6_unicast**                  Address family unicast ipv6

                                     Type: ``boolean``
   *ipv4_vrf_name*                   ipv4 vrf name

                                     Type: ``string``
   *ipv6_vrf_name*                   ipv6 vrf name

                                     Type: ``string``
   **maximum_paths**                 Forward packets over multiple paths

                                     Type: ``integer``

                                     **Default**: 8
   ================================  ======================================================================

