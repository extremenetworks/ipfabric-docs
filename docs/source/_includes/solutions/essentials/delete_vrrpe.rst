.. NOTE: This file has been generated automatically, don't manually edit it

delete_vrrpe
~~~~~~~~~~~~

**Description**: This deletes VRRPe group. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``
   *password*                        The login password to connect to the device.

                                     Type: ``string``
   **intf_type**                     The interface type, VDX/SLX supports only ve and MLX supports both ve and ethernet.

                                     Choose from:

                                     - ethernet
                                     - ve
   **intf_name**                     The name of the interface, for ethernet slot/port, for ve, ve-id like 10,20.

                                     Type: ``string``
   *rbridge_id*                      The RBridge IDs of the VDX switches, for example 51 or 51,52. This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **vrrpe_group**                   The virtual extender group ID

                                     Type: ``string``
   *ip_version*                      The IPv4 or IPv6 group.

                                     Type: ``string``

                                     **Default**: IPv4
   ================================  ======================================================================

