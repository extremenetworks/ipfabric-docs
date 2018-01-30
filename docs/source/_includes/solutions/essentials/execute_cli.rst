.. NOTE: This file has been generated automatically, don't manually edit it

execute_cli
~~~~~~~~~~~

**Description**: Executes CLI command and returns the result. The device type should be appropriate to get reliable output. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The IP address of the device.

                                     Type: ``string``
   *username*                        The login username.

                                     Type: ``string``
   *password*                        The login password.

                                     Type: ``string``
   **cli_cmd**                       The CLI commands to execute on the device.

                                     Type: ``array``
   *config_operation*                The flag to indicate whether commands are for configuration or for show.

                                     Type: ``boolean``
   **device_type**                   Specifies the connecting device type.

                                     Choose from:

                                     - nos
                                     - slx
                                     - ni

                                     **Default**: nos
   *enable_passwd*                   The privilege exec mode password. Applicable only to MLX device.

                                     Type: ``string``
   ================================  ======================================================================

