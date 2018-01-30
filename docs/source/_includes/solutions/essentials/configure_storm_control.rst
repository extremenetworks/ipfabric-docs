.. NOTE: This file has been generated automatically, don't manually edit it

configure_storm_control
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configures Storm/BUM control on an interface. 

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
   **intf_type**                     The interface type.

                                     Choose from:

                                     - ethernet
                                     - tengigabitethernet
                                     - gigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet

                                     **Default**: ethernet
   **intf_name**                     The interface name of the physical port or port channel number. E.g:0/1 or 7.

                                     Type: ``string``
   *broadcast_limit_type*            Broadcast rate limit format

                                     Choose from:

                                     - limit-bps
                                     - limit-percent
   *broadcast_limit_value*           If broadcast_limit_type=limit-bps, the Valid Values are <0-100000000000>. else <0-100>

                                     Type: ``string``
   *broadcast_limit_action*          The Broadcast Action

                                     Choose from:

                                     - shutdown
                                     - monitor

                                     **Default**: shutdown
   *multicast_limit_type*            The Multicast rate limit format

                                     Choose from:

                                     - limit-bps
                                     - limit-percent
   *multicast_limit_value*           If multicast_limit_type=limit-bps, the Valid Values are <0-100000000000>. else <0-100>

                                     Type: ``string``
   *multicast_limit_action*          The Multicast Action

                                     Choose from:

                                     - shutdown
                                     - monitor

                                     **Default**: shutdown
   *unknown_unicast_limit_type*      The Unknown Unicast rate limit format.

                                     Choose from:

                                     - limit-bps
                                     - limit-percent
   *unknown_unicast_limit_value*     If unknown_unicast_limit_type=limit-bps, the Valid Values are <0-100000000000> else <0-100>

                                     Type: ``string``
   *unknown_unicast_limit_action*    The Unknown Unicast Action

                                     Choose from:

                                     - shutdown
                                     - monitor

                                     **Default**: shutdown
   ================================  ======================================================================

