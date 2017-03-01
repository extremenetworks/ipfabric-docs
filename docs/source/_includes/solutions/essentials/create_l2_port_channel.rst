.. NOTE: This file has been generated automatically, don't manually edit it

create_l2_port_channel
~~~~~~~~~~~~~~~~~~~~~~

**Description**: Create a port channel and map it to the interface and enable channel-group mode 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   *username*                        login username

                                     Type: ``string``

                                     **Default**: admin
   *password*                        login password

                                     Type: ``string``

                                     **Default**: password
   **intf_type**                     Interface type ethernet/gigabitethernet/tengigabitethernet/fortygigabitethernet/hundredgigabitethernet

                                     Choose from:

                                     - tengigabitethernet
                                     - gigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - ethernet

                                     **Default**: tengigabitethernet
   **ports**                         Single or list of ports that are members of the port channel. Examples for VDX, SLX are  24/0/1, 24/0/2 or 1/13, 1/14

                                     Type: ``array``
   **port_channel_id**               Port channel interface number.<NUMBER:1-6144>

                                     Type: ``string``
   *mode*                            Port channel type

                                     Choose from:

                                     - standard
                                     - brocade

                                     **Default**: standard
   *protocol*                        port channel mode type

                                     Choose from:

                                     - active
                                     - passive
                                     - modeon

                                     **Default**: active
   *intf_desc*                       Port channel Interface description name

                                     Type: ``string``
   ================================  ======================================================================

