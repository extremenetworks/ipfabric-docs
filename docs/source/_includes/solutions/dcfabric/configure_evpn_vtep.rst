.. NOTE: This file has been generated automatically, don't manually edit it

configure_evpn_vtep
~~~~~~~~~~~~~~~~~~~

**Description**: Configure EVPN VTEP on a leaf or vLAG pair 

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
   **loopback_id**                   Loopback ID, <NUMBER:1-255>

                                     Type: ``integer``
   *rbridge_id*                      Single or list of RBridge IDs separated by comma, for example, 1 or 1,2, 4.  This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **name**                          Overlay gateway name

                                     Type: ``string``
   *vni_auto_map*                    Configure vlan/bridge-domain to vni auto mapping under overlay gateway

                                     Type: ``boolean``

                                     **Default**: True
   ================================  ======================================================================

