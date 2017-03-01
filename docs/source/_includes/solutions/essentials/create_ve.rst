.. NOTE: This file has been generated automatically, don't manually edit it

create_ve
~~~~~~~~~

**Description**: Create a VE, assign IP addresses and VRF on multiple switches. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``

                                     **Default**: admin
   *password*                        Login password to connect to the device

                                     Type: ``string``

                                     **Default**: password
   *rbridge_id*                      Single or list of RBridge IDs separated by comma, for example, 1 or 1,2, 4.  This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **vlan_id**                       Interface VLAN ID. <NUMBER:1-4090/8191>, can be greater than 4090 only if VF is enabled.

                                     Type: ``string``
   *ip_address*                      Single or list of IPv4/IPv6 addresses to be configured on the VE. IPv4/subnet-length or IPv6/prefix-length, for example 10.0.0.10/22, 30.0.0.10/22.

                                     Type: ``array``
   *vrf_name*                        VRF name. For example vrf32 or 32

                                     Type: ``string``
   *ipv6_use_link_local_only*        IPv6 link local

                                     Type: ``boolean``
   ================================  ======================================================================

