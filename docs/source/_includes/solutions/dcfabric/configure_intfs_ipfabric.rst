.. NOTE: This file has been generated automatically, don't manually edit it

configure_intfs_ipfabric
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure IP addresses on a device 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``

                                     **Default**: admin
   *password*                        Login password to connect to the device

                                     Type: ``string``

                                     **Default**: password
   **interfaces**                    Interfaces

                                     Type: ``array``
   *bfd_multiplier*                  BFD multiplier

                                     Type: ``string``
   *bfd_rx*                          BFD RX receive timer

                                     Type: ``string``
   *bfd_tx*                          BFD TX transmit timer

                                     Type: ``string``
   *mtu*                             MTU size

                                     Type: ``string``
   *ip_mtu*                          IP MTU size

                                     Type: ``string``
   ================================  ======================================================================

