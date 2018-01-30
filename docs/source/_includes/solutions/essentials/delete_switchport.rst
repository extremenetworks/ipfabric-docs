.. NOTE: This file has been generated automatically, don't manually edit it

delete_switchport
~~~~~~~~~~~~~~~~~

**Description**: This deletes the Switchport on an interface. 

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
                                     - port_channel

                                     **Default**: tengigabitethernet
   **intf_name**                     The interface name, can be port or port channel. For example to specify ports, 24/0/1 (VDX) or 24/1 (SLX). For port channel, 10 or 1-10

                                     Type: ``string``
   ================================  ======================================================================

