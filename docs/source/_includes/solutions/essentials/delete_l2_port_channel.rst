.. NOTE: This file has been generated automatically, don't manually edit it

delete_l2_port_channel
~~~~~~~~~~~~~~~~~~~~~~

**Description**: This deletes the port channel interface and deletes the port chanel configuration from all the member ports. 

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
   **port_channel_id**               Port channel interface number.For VDX range is <NUMBER:1-6144>. For MLX range is <1-256>, CER/CES range is <1-64>, Avalanche range is <1-64>, Fusion range is <1-512> Cedar/Freedom range is <1-1024>

                                     Type: ``integer``
   ================================  ======================================================================

