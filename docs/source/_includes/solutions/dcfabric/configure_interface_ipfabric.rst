.. NOTE: This file has been generated automatically, don't manually edit it

configure_interface_ipfabric
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configure IP addresses on a device. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          The management IP address of the target device.

                                     Type: ``string``
   *user*                            The login user name to connect to the device.

                                     Type: ``string``
   *passwd*                          THe login password to connect to the device.

                                     Type: ``string``
   **interface**                     The interface name.

                                     Type: ``string``
   *ip*                              The IP address to be assigned.

                                     Type: ``string``
   *state*                           The State.

                                     Choose from:

                                     - present
                                     - absent

                                     **Default**: present
   *enabled*                         Enabled.

                                     Type: ``boolean``

                                     **Default**: True
   *rbridge_id*                      The RBridge ID of the VDX switch.  This parameter is only applicable. for VDX switches.

                                     Type: ``string``
   *donor*                           Donor

                                     Type: ``string``
   *bfd_multiplier*                  The BFD Multiplier.

                                     Type: ``string``
   *bfd_rx*                          The BFD receive.

                                     Type: ``string``
   *bfd_tx*                          The BFD transmit.

                                     Type: ``string``
   *mtu*                             The MTU size.

                                     Type: ``string``
   *ip_mtu*                          The IP MTU size.

                                     Type: ``string``
   ================================  ======================================================================

