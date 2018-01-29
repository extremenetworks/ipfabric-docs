.. NOTE: This file has been generated automatically, don't manually edit it

configure_evpn_instance
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configure EVPN instance on a switch or a vLAG pair. 

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
   *rbridge_id*                      The RBridge ID of the VDX switch. This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **evi_name**                      The EVPN instance name., for example 'evpn1 or 32'.

                                     Type: ``string``
   *duplicate_mac_timer*             The duplicate MAC timer, in integer.

                                     Type: ``integer``

                                     **Default**: 10
   *max_count*                       The max count, value in integer.

                                     Type: ``integer``

                                     **Default**: 10
   ================================  ======================================================================

