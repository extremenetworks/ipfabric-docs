.. NOTE: This file has been generated automatically, don't manually edit it

create_mct_client
~~~~~~~~~~~~~~~~~

**Description**: Create MCT client, associate client interfaces and deploy 

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
   **client_name**                   Name for the Cluster Client. Name can contain maximum 64 Characters.

                                     Type: ``string``
   **client_id**                     ID for the Cluster Client. Valid IDs are 1 - 512.

                                     Type: ``integer``
   **intf_type**                     Client Interface type

                                     Choose from:

                                     - port_channel
                                     - ethernet

                                     **Default**: ethernet
   **intf_name**                     Interface name physical port, port channel number. Examples are 224/0/1 or 7

                                     Type: ``string``
   ================================  ======================================================================

