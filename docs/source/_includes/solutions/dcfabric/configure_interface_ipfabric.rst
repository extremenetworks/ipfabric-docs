.. NOTE: This file has been generated automatically, don't manually edit it

configure_interface_ipfabric
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure IP addresses on a device 

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
   **interface**                     Interface name

                                     Type: ``string``
   *ip*                              IP address to be assigned

                                     Type: ``string``
   *state*                           State

                                     Choose from:

                                     - present
                                     - absent

                                     **Default**: present
   *enabled*                         Enabled

                                     Type: ``boolean``

                                     **Default**: True
   *rbridge_id*                      RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``string``
   *donor*                           Donor

                                     Type: ``string``
   *bfd_multiplier*                  BFD Multiplier

                                     Type: ``string``
   *bfd_rx*                          BFD receive

                                     Type: ``string``
   *bfd_tx*                          BFD transmit

                                     Type: ``string``
   *mtu*                             MTU size

                                     Type: ``string``
   *ip_mtu*                          IP MTU size

                                     Type: ``string``
   ================================  ======================================================================

