.. NOTE: This file has been generated automatically, don't manually edit it

redistribute_connected_bgp_vrf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: configure redistribute connected under default/non-default vrf address-family 

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
   **ipv4_unicast**                  Configure Address family unicast ipv4

                                     Type: ``boolean``
   **ipv6_unicast**                  Configure Address family unicast ipv4

                                     Type: ``boolean``
   *ipv4_vrf_name*                   ipv4 vrf name

                                     Type: ``string``
   *ipv6_vrf_name*                   ipv6 vrf name

                                     Type: ``string``
   ================================  ======================================================================

