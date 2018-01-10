.. NOTE: This file has been generated automatically, don't manually edit it

execute_cli
~~~~~~~~~~~

**Description**: Execute CLI command and return the result. Device type should be appropriate to get reliable output. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Ip address of the device

                                     Type: ``string``
   *username*                        login username

                                     Type: ``string``
   *password*                        login password

                                     Type: ``string``
   **cli_cmd**                       CLI commands to execute on the device

                                     Type: ``array``
   *config_operation*                Flag to indicate whether commands are for configuration or show

                                     Type: ``boolean``
   **device_type**                   Connecting device type

                                     Choose from:

                                     - nos
                                     - slx
                                     - ni

                                     **Default**: nos
   *enable_passwd*                   privilege exec mode password. Applicable only to MLX device.

                                     Type: ``string``
   ================================  ======================================================================

