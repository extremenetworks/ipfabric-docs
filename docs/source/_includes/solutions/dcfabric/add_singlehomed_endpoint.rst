.. NOTE: This file has been generated automatically, don't manually edit it

add_singlehomed_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Create VLAN, configure interface as Access or Trunk, and validate interface state. 

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
                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ve
                                     - loopback

                                     **Default**: tengigabitethernet
   **intf_name**                     Single port. Examples for VDX, SLX are  24/0/1 or 1/13.

                                     Type: ``string``
   *intf_desc*                       Port description, space is not allowed, use '_' instead.

                                     Type: ``string``
   *enabled*                         Select true to enable the port, false to disable the port

                                     Type: ``boolean``

                                     **Default**: True
   **switchport_mode**               Switch port mode

                                     Choose from:

                                     - access
                                     - trunk

                                     **Default**: access
   **vlan_id**                       Single or range of VLANs to be configured on the interface, e.g. 5 or 4-7 or 4,6,9-11 or all. For 802.1Q VLANs ID must be below 4096, for service or transport VFs in a Virtual Fabrics context, valid range is from 4096 through 8191.

                                     Type: ``string``
   *vlan_desc*                       VLAN description, space is not allowed, use '_' instead.  Same VLAN description is configured on all the VLANs when the range is provided.

                                     Type: ``string``
   *c_tag*                           Single or range of VLAN IDs <NUMBER:1-4090>. Valid only on NOS devices & if switchport_mode is trunk.

                                     Type: ``string``
   *mac_group_id*                    MAC group ID <NUMBER:1,500>. Only applicable if switchport_mode is access.

                                     Type: ``array``
   ================================  ======================================================================

