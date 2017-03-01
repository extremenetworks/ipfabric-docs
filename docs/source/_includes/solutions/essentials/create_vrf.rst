.. NOTE: This file has been generated automatically, don't manually edit it

create_vrf
~~~~~~~~~~

**Description**: Create Virtual Routing and Forwarding (VRF) instance on the switch for L3 tenants. 

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
   **vrf_name**                      VRF name, for example vrf32 or 32

                                     Type: ``string``
   *rbridge_id*                      RBridge ID of the switch. This parameter is only applicable for VDX switches.

                                     Type: ``string``
   *afi*                             IP address type

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   ================================  ======================================================================

