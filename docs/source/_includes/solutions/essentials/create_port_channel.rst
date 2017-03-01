.. NOTE: This file has been generated automatically, don't manually edit it

create_port_channel
~~~~~~~~~~~~~~~~~~~

**Description**: Create a port channel and map it to the interface and enable channel-group mode 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management Virtual Ip address of the VDX device

                                     Type: ``string``
   *username*                        login username

                                     Type: ``string``

                                     **Default**: admin
   *password*                        login password

                                     Type: ``string``

                                     **Default**: password
   **intf_type**                     Interface type gigabitethernet/tengigabitethernet/fortygigabitethernet/hundredgigabitethernet

                                     Choose from:

                                     - tengigabitethernet
                                     - gigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - ethernet

                                     **Default**: tengigabitethernet
   **ports**                         Single interface or list of interfaces separated by comma that needs to be mapped to the port channel

                                     Type: ``array``
   **port_channel_id**               Portchannel interface number.<NUMBER:1-6144>

                                     Type: ``string``
   *mode*                            port channel type

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
   *intf_desc*                       Interface description name

                                     Type: ``string``
   ================================  ======================================================================

