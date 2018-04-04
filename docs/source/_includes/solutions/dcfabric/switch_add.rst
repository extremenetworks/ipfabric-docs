.. NOTE: This file has been generated automatically, don't manually edit it

switch_add
~~~~~~~~~~

**Description**: Register a switch in the inventory and assign to a fabric 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **fabric**                        Name of the fabric

                                     Type: ``string``
   **host**                          Management IP address of the switch

                                     Type: ``string``
   **user**                          Login user name to connect to the switch

                                     Type: ``string``
   **passwd**                        Login password to connect to the device

                                     Type: ``string``
   *protocol*                        The protocol used for REST requests. This applies to REST platforms such as SLX and VDX.

                                     Choose from:

                                     - http
                                     - https

                                     **Default**: http
   ================================  ======================================================================

