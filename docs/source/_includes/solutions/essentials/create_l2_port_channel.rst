.. NOTE: This file has been generated automatically, don't manually edit it

create_l2_port_channel
~~~~~~~~~~~~~~~~~~~~~~

**Description**: This create an L2 port channel (LAG or vLAG) in Static or LACP mode. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``
   *password*                        The login password to connect to the device.

                                     Type: ``string``
   **intf_type**                     The interface type - ethernet/gigabitethernet/tengigabitethernet/fortygigabitethernet/hundredgigabitethernet.

                                     Choose from:

                                     - tengigabitethernet
                                     - gigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - ethernet

                                     **Default**: tengigabitethernet
   **ports**                         A single or a list of ports that are members of the port channel. Examples for VDX, SLX are  24/0/1, 24/0/2 or 1/13, 1/14.

                                     Type: ``array``
   *port_speed*                      The configurable port speed that is supported on SLX and VDX.

                                     Choose from:

                                     - 1000
                                     - 10000
                                     - 25000
                                     - 40000
                                     - 100000
   **port_channel_id**               Port channel interface number.For VDX range is <NUMBER:1-6144>. For MLX range is <1-256>, CER/CES range is <1-64>, Avalanche range is <1-64>, Fusion range is <1-512> Cedar/Freedom range is <1-1024>

                                     Type: ``string``
   *mode*                            The port channel type. SLX and MLX supports standard type only.

                                     Choose from:

                                     - standard
                                     - brocade

                                     **Default**: standard
   *protocol*                        The port channel mode. For MLX, use active for dynamic and modeon for static.

                                     Choose from:

                                     - active
                                     - passive
                                     - modeon

                                     **Default**: active
   *port_channel_desc*               The port channel interface description. For MLX, this is mandatory. field.

                                     Type: ``string``
   ================================  ======================================================================

