.. NOTE: This file has been generated automatically, don't manually edit it

configure_intfs_ipfabric
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This will configure IP addresses on a device. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   **interfaces**                    The interfaces.

                                     Type: ``array``
   *bfd_multiplier*                  The BFD multiplier.

                                     Type: ``string``
   *bfd_rx*                          The BFD RX receive timer.

                                     Type: ``string``
   *bfd_tx*                          The BFD TX transmit timer.

                                     Type: ``string``
   *mtu*                             The MTU size.

                                     Type: ``string``
   *ip_mtu*                          The IP MTU size.

                                     Type: ``string``
   ================================  ======================================================================

