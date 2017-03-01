.. NOTE: This file has been generated automatically, don't manually edit it

set_l2_system_mtu
~~~~~~~~~~~~~~~~~

**Description**: Set L2 system MTU on the VCS fabric or vLag pairs.  Only supported on VDX devices. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Virtual IP of VCS Fabric or management IP of the switch.

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``

                                     **Default**: admin
   *password*                        Login password to connect to the device

                                     Type: ``string``

                                     **Default**: password
   **mtu_size**                      MTU size in bytes <Number:1522-9216>

                                     Type: ``integer``
   ================================  ======================================================================

