.. NOTE: This file has been generated automatically, don't manually edit it

delete_logical_interface_on_interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This deletes the logical interface under the physical/port-channel interface. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   *intf_type*                       The interface type.

                                     Choose from:

                                     - ethernet
                                     - port_channel

                                     **Default**: ethernet
   **intf_name**                     The interface Port number or Port channel number. Examples for SLX are 1/13, 1/14.

                                     Type: ``string``
   **logical_interface_number**      A single or list of Interface name, physical port or port channel number separated by comma. E.g:0/1.1,0/1.2 or 7.1. If 'all', it will delete all the LIFs under the interface.

                                     Type: ``string``
   ================================  ======================================================================

