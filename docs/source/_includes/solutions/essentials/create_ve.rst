.. NOTE: This file has been generated automatically, don't manually edit it

create_ve
~~~~~~~~~

**Description**: This creates a VE and assign IP addresses, VRF on one or more switches. 

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
   *rbridge_id*                      A single or list of RBridge IDs separated by comma, for example, 1 or 1,2, 4. This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **vlan_id**                       The VLAN ID. The allowed range for SLX <NUMBER:1-4090>, for VDX <NUMBER:1-4090/8191> greater than 4090 only if VF is enabled, and for MLX, the range is <NUMBER:1-4090>.

                                     Type: ``string``
   *ve_id*                           The VE interface ID. For NOS range is 1-4090, MLX range is 1-255, SLX range is 1-4096. For MLX, this is a mandatory field.

                                     Type: ``string``
   *ip_address*                      A single or list of IPv4/IPv6 addresses to be configured on the VE. IPv4/subnet-length or IPv6/prefix-length, for example 10.0.0.10/22, 30.0.0.10/22. List of IP addresses is valid only in VDX Cluster Nodes.

                                     Type: ``array``
   *vrf_name*                        VRF name. For example vrf32 or 32

                                     Type: ``string``
   *ipv6_use_link_local_only*        IPv6 link local

                                     Type: ``boolean``
   *skip_vlan_config*                Skip Vlan to VE mapping for SLXOS platforms.

                                     Type: ``boolean``
   ================================  ======================================================================

