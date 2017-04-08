.. NOTE: This file has been generated automatically, don't manually edit it

configure_evpn_instance
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure EVPN instance on a switch or a vLAG pair 

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
   *rbridge_id*                      RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **evi_name**                      EVPN instance name., for example 'evpn1 or 32'

                                     Type: ``string``
   *duplicate_mac_timer*             Duplicate MAC timer, in integer

                                     Type: ``integer``

                                     **Default**: 10
   *max_count*                       Max count, value in integer

                                     Type: ``integer``

                                     **Default**: 10
   ================================  ======================================================================

