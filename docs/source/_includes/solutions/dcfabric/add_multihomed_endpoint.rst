.. NOTE: This file has been generated automatically, don't manually edit it

add_multihomed_endpoint
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Create VLAN, port channel and configure port channel as Access or Trunk, validate port channel state. 

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
   **vlan_id**                       Single or range of VLANs

                                     Type: ``string``
   *vlan_desc*                       VLAN description, space is not allowed, use '_' instead.  Same VLAN description is configured on all the VLANs when the range is provided.

                                     Type: ``string``
   **intf_type**                     Interface type

                                     Choose from:

                                     - ethernet
                                     - tengigabitethernet
                                     - gigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet

                                     **Default**: tengigabitethernet
   **ports**                         Single or list of ports that are members of the port channel. Examples for VDX, SLX are  24/0/1, 24/0/2 or 1/13, 1/14

                                     Type: ``array``
   *intf_desc*                       Description for all the ports, space is not allowed, use '_' instead.

                                     Type: ``string``
   *auto_pick_port_channel_id*       If selected, workflow will pick the lowest available port channel on the switch.

                                     Type: ``boolean``
   *port_channel_id*                 Portchannel interface number <NUMBER:1-6144>

                                     Type: ``string``
   *port_channel_desc*               Port channel description without any space.

                                     Type: ``string``
   *mode*                            Port channel type

                                     Choose from:

                                     - standard
                                     - brocade

                                     **Default**: standard
   *protocol*                        Port channel mode

                                     Choose from:

                                     - active
                                     - passive
                                     - modeon

                                     **Default**: active
   *mtu*                             L2 MTU size in bytes <Number:1522-9216>

                                     Type: ``integer``
   *enabled*                         Select true to enable the port, false to disable the port

                                     Type: ``boolean``

                                     **Default**: True
   ================================  ======================================================================

