.. NOTE: This file has been generated automatically, don't manually edit it

delete_logical_interface_on_interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Delete logical interface under the physical/port-channel interface. 

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
   *intf_type*                       Interface type

                                     Choose from:

                                     - ethernet
                                     - port_channel

                                     **Default**: ethernet
   **intf_name**                     Interface Port number or Port channel number. Examples for SLX are 1/13, 1/14

                                     Type: ``string``
   **logical_interface_number**      Single/List of Interface name physical port or port channel number separated by comma. E.g:0/1.1,0/1.2 or 7.1. If 'all', delete all the LIFs under the interface.

                                     Type: ``string``
   ================================  ======================================================================

