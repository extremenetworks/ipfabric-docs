.. NOTE: This file has been generated automatically, don't manually edit it

remove_switchport_trunk_allowed_vlan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Remove switch port trunk allowed vlan from an interface. 

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
   **intf_type**                     Interface type

                                     Choose from:

                                     - ethernet
                                     - tengigabitethernet
                                     - gigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel

                                     **Default**: tengigabitethernet
   **intf_name**                     Interface name, for VDX in 3-tuple format (24/0/1), SLX in 2-tuple format (24/1) or Port-channel number <1-6144>.

                                     Type: ``string``
   **vlan_id**                       Single or range of VLANs to be configured on the interface. NOS - Valid values <1-4090/8191 when VFAB disabled/enabled> SLX - Valid values <1-4090> For example, 5 or 4-7 or 4,6,9-11 or all. Range not supported for VFAB vlans.

                                     Type: ``string``
   *c_tag*                           Ctag Vlan ID.Valid values <1-4090>. Valid only on NOS devices

                                     Type: ``string``
   ================================  ======================================================================

