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
   **rbridge_id**                    Single Rbridge or list of Rbridge's separated by comma that needs ve/vrrpe creation

                                     Type: ``array``
   **vlan_id**                       VLAN ID

                                     Type: ``string``
   *intf_desc*                       Interface description

                                     Type: ``string``
   *ve_ip*                           Single or list of RBridge IDs separated by comma, for example, 1 or 1,2, 4.  This parameter is only applicable for VDX switches.

                                     Type: ``array``
   *vrid*                            Virtual group ID

                                     Type: ``string``
   **virtual_ip**                    VRRPe virtual IP address without the netmask

                                     Type: ``string``
   **vrf_name**                      VRF name, for example vrf32 or 32

                                     Type: ``string``
   *afi*                             IP address type

                                     Choose from:

                                     - ipv4
                                     - ipv6

                                     **Default**: ipv4
   ================================  ======================================================================

