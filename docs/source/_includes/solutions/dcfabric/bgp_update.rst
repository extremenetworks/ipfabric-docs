.. NOTE: This file has been generated automatically, don't manually edit it

bgp_update
~~~~~~~~~~

**Description**: Update the details of all the switches in the fabric or a specified single switch 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   *host*                            Management IP address of the switch

                                     Type: ``string``
   *user*                            Login user name to connect to the device

                                     Type: ``string``
   *passwd*                          Login password to connect to the device

                                     Type: ``string``
   *neighbor_address*                BGP Neighbor address

                                     Type: ``string``
   *state*                           Device Provisioning State. Its mainly needed to mark the state during workflow execution.

                                     Choose from:

                                     - Provisioned
                                     - Failed
   ================================  ======================================================================

