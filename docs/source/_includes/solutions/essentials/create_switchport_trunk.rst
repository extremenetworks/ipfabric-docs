.. NOTE: This file has been generated automatically, don't manually edit it

create_switchport_trunk
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure port channel or a physical interface as a Trunk interface. 

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
   **vlan_id**                       For 802.1Q VLANs, single or range of VLANs, for example, 5 or 4-7 or 4,6,9-11 or all; ID must be below 4096.  For service or transport VFs, single ID, range can be from 4096 through 8191.

                                     Type: ``string``
   *c_tag*                           Specifies an incoming C-TAG or range of C-TAGs for service or transport VLANs in a Virtual Fabrics context.  For service VF only single ID is allowed, for Transport VFs a range of IDs, for example, 100-200, or 10,20,100-200.

                                     Type: ``string``
   ================================  ======================================================================

