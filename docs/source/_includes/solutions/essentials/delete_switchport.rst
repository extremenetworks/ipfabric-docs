.. NOTE: This file has been generated automatically, don't manually edit it

delete_switchport
~~~~~~~~~~~~~~~~~

**Description**: Delete Switchport on an interface. 

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
   **intf_name**                     Interface name, for VDX in 3-tuple format (24/0/1), SLX in 2-tuple format (24/1). Example for interface 235/0/35 or 235/0/35-40 Example for port-channel 10 or 1-10

                                     Type: ``string``
   ================================  ======================================================================

