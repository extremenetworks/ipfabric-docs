.. NOTE: This file has been generated automatically, don't manually edit it

create_vrrpe
~~~~~~~~~~~~

**Description**: This creates a VRRPe session on multiple switches by creating VRRPe group and assigning virtual IP. 

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
   **intf_type**                     The interface type. VDX/SLX supports only ve and MLX supports both ve and ethernet.

                                     Choose from:

                                     - ethernet
                                     - ve
   **intf_name**                     The name of the interface.

                                     Type: ``string``
   *rbridge_id*                      The RBridge ID of the VDX switch. This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **vrid**                          Virtual group ID

                                     Type: ``string``
   **virtual_ip**                    The VRRPe virtual IP address without the netmask.

                                     Type: ``string``
   ================================  ======================================================================

