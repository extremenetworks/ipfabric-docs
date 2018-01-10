.. NOTE: This file has been generated automatically, don't manually edit it

configure_vrrpe_gw
~~~~~~~~~~~~~~~~~~

**Description**: Create VLAN, VE interface on specified GWs and configure VRRPe on VE interfaces. 

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
   *rbridge_id*                      Single Rbridge or list of Rbridge's separated by comma that needs ve/vrrpe creation

                                     Type: ``array``
   **vlan_id**                       VLAN ID

                                     Type: ``string``
   *vlan_desc*                       Vlan description without any space

                                     Type: ``string``
   *ve_ip*                           Single or list of IPv4/IPv6 addresses to be configured on the VE. IPv4/subnet-length or IPv6/prefix-length, for example 10.0.0.10/22, 30.0.0.10/22.

                                     Type: ``array``
   *vrid*                            Virtual group ID

                                     Type: ``string``
   **virtual_ip**                    VRRPe virtual IP address without the netmask

                                     Type: ``string``
   *vrf_name*                        VRF name, for example vrf32 or 32

                                     Type: ``string``
   *afi*                             IP address type

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   **intf_type**                     Interface type, VDX/SLX supports only ve and MLX supports both

                                     Choose from:

                                     - ethernet
                                     - ve

                                     **Default**: ve
   **intf_name**                     name of the interface, for ethernet slot/port, for ve, ve-id like 10,20

                                     Type: ``string``
   *display_show_results*            Enable/Disable output display of show commands executed on the devices.

                                     Type: ``boolean``
   ================================  ======================================================================

