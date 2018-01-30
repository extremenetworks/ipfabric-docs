.. NOTE: This file has been generated automatically, don't manually edit it

create_mct_client
~~~~~~~~~~~~~~~~~

**Description**: This will create MCT client, associate client interfaces and deploy. 

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
   **client_name**                   The name for the Cluster Client. The name can contain maximum 64 characters.

                                     Type: ``string``
   **client_id**                     The ID for the Cluster Client. Valid IDs are 1 - 512.

                                     Type: ``integer``
   **intf_type**                     The Client Interface type.

                                     Choose from:

                                     - port_channel
                                     - ethernet

                                     **Default**: ethernet
   **intf_name**                     The interface name physical port, port channel number. Examples are 224/0/1. or 7

                                     Type: ``string``
   ================================  ======================================================================

