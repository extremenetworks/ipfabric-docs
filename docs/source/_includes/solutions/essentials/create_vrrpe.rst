.. NOTE: This file has been generated automatically, don't manually edit it

create_vrrpe
~~~~~~~~~~~~

**Description**: Create a VRRPe session on multiple switches by creating VRRPe group and assigning virtual IP 

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
   *rbridge_id*                      RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``string``
   **ve_name**                       Interface VE name

                                     Type: ``string``
   **vrid**                          Virtual group ID

                                     Type: ``string``
   **virtual_ip**                    VRRPe virtual IP address without the netmask

                                     Type: ``string``
   ================================  ======================================================================

