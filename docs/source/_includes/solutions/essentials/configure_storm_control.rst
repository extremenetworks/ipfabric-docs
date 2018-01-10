.. NOTE: This file has been generated automatically, don't manually edit it

configure_storm_control
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure Storm/BUM control on an interface 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``
   *password*                        Login password to connect to the device

                                     Type: ``string``
   **intf_type**                     Interface type

                                     Choose from:

                                     - ethernet
                                     - tengigabitethernet
                                     - gigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet

                                     **Default**: ethernet
   **intf_name**                     Interface name physical port or port channel number. E.g:0/1 or 7

                                     Type: ``string``
   *broadcast_limit_type*            Broadcast rate limit format

                                     Choose from:

                                     - limit-bps
                                     - limit-percent
   *broadcast_limit_value*           If broadcast_limit_type=limit-bps,Valid Values are <0-100000000000> else <0-100>

                                     Type: ``string``
   *broadcast_limit_action*          Broadcast Action

                                     Choose from:

                                     - shutdown
                                     - monitor

                                     **Default**: shutdown
   *multicast_limit_type*            Multicast rate limit format

                                     Choose from:

                                     - limit-bps
                                     - limit-percent
   *multicast_limit_value*           If multicast_limit_type=limit-bps,Valid Values are <0-100000000000> else <0-100>

                                     Type: ``string``
   *multicast_limit_action*          Multicast Action

                                     Choose from:

                                     - shutdown
                                     - monitor

                                     **Default**: shutdown
   *unknown_unicast_limit_type*      Unknown Unicast rate limit format

                                     Choose from:

                                     - limit-bps
                                     - limit-percent
   *unknown_unicast_limit_value*     If unknown_unicast_limit_type=limit-bps,Valid Values are <0-100000000000> else <0-100>

                                     Type: ``string``
   *unknown_unicast_limit_action*    Unknown Unicast Action

                                     Choose from:

                                     - shutdown
                                     - monitor

                                     **Default**: shutdown
   ================================  ======================================================================

