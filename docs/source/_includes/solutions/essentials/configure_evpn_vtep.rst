.. NOTE: This file has been generated automatically, don't manually edit it

configure_evpn_vtep
~~~~~~~~~~~~~~~~~~~

**Description**: Configure EVPN VTEP on a leaf/vLAG pair 

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
   **loopback_id**                   Loopback id (<NUMBER:1-255>)

                                     Type: ``integer``
   *rbridge_id*                      Single/List of rbridge ID's(example rbridge_id=1 or rbridge_id=1,2,3)

                                     Type: ``array``
   **name**                          Overlay Gateway Name

                                     Type: ``string``
   ================================  ======================================================================

