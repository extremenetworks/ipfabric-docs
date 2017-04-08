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
   *intf_desc*                       Interface description

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
   **port_channel_id**               Portchannel interface number <NUMBER:1-6144>

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
   ================================  ======================================================================

