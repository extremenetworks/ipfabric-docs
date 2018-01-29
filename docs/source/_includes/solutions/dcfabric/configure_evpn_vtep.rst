.. NOTE: This file has been generated automatically, don't manually edit it

configure_evpn_vtep
~~~~~~~~~~~~~~~~~~~

**Description**: This configure EVPN VTEP on a leaf or vLAG pair. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   **loopback_id**                   The loopback ID, <NUMBER:1-255>.

                                     Type: ``integer``
   *rbridge_id*                      A single or a list of RBridge IDs separated by comma, for example, 1 or 1,2, 4. This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **name**                          The overlay gateway name.

                                     Type: ``string``
   *vni_auto_map*                    This configure VLAN/bridge-domain to vni auto mapping under overlay gateway.

                                     Type: ``boolean``

                                     **Default**: True
   ================================  ======================================================================

