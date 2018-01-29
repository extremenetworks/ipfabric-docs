.. NOTE: This file has been generated automatically, don't manually edit it

configure_bgp_redistribute_connected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configure BGP route redistribution. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          The management IP address of the target device.

                                     Type: ``string``
   *user*                            The login user name to connect to the device.

                                     Type: ``string``
   *passwd*                          The login password to connect to the device.

                                     Type: ``string``
   **rbridge_id**                    The RBridge ID of the VDX switch. This parameter is only applicable. for VDX switches.

                                     Type: ``string``
   *vrf*                             The VRF name <1-32> characters.

                                     Type: ``string``

                                     **Default**: default
   **source**                        The source type.

                                     Choose from:

                                     - connected

                                     **Default**: connected
   *afi*                             The IP address type.

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   ================================  ======================================================================

