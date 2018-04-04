.. NOTE: This file has been generated automatically, don't manually edit it

delete_ve
~~~~~~~~~

**Description**: This action deletes a VE along with router interface mappings under a VLAN. 

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
   *rbridge_id*                      The RBridge IDs of the VDX switches, for example 51 or 51,52. This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **vlan_id**                       The VLAN ID. Valid values for SLX <NUMBER:1-4090>, for VDX <NUMBER:1-4090/8191> greater than 4090 only if VF is enabled, for MLX, the range is <NUMBER:1-4090>.

                                     Type: ``string``
   *ve_id*                           The VE interface ID. For NOS range is 1-4090, MLX range is 1-255, SLX range is 1-4096. This is mandatory args for MLX devices. If not passed for SLX and VDX devices, `ve_id` will be assumed as `vlan_id`.

                                     Type: ``string``
   ================================  ======================================================================

