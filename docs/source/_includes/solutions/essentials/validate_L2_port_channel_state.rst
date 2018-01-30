.. NOTE: This file has been generated automatically, don't manually edit it

validate_L2_port_channel_state
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This validates the port channel state by verifying the sync state of all member. ports is 1. 

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
   **port_channel_id**               The Port channel interface number. <NUMBER:1-6144>. For MLX range is <1-256>.

                                     Type: ``integer``
   ================================  ======================================================================

