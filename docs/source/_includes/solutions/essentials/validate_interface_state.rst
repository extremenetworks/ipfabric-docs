.. NOTE: This file has been generated automatically, don't manually edit it

validate_interface_state
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Validate L1 and L2 state for port channel or physical interface is UP. 

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

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ethernet

                                     **Default**: tengigabitethernet
   **intf_name**                     Interface names, can be comma separated physical ports, port channel numbers. Examples are 224/0/1, 224/0/2 or 7, 8, 9

                                     Type: ``string``
   **intf_state**                    Interface state (up or down)

                                     Choose from:

                                     - up
                                     - down
   ================================  ======================================================================

