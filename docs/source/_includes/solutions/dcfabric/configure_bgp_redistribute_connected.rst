.. NOTE: This file has been generated automatically, don't manually edit it

configure_bgp_redistribute_connected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure BGP route redistribution 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          Management IP address of the target device

                                     Type: ``string``
   *user*                            Login user name to connect to the device

                                     Type: ``string``
   *passwd*                          Login password to connect to the device

                                     Type: ``string``
   **rbridge_id**                    RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``string``
   *vrf*                             VRF name <1-32> characters.

                                     Type: ``string``

                                     **Default**: default
   **source**                        Source type

                                     Choose from:

                                     - connected

                                     **Default**: connected
   *afi*                             IP address type

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   ================================  ======================================================================

