.. NOTE: This file has been generated automatically, don't manually edit it

persist_configuration
~~~~~~~~~~~~~~~~~~~~~

**Description**: This action saves the running/default configurations to startup configurations on the SLX devices. Perform `write memory` operation on MLX devices. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       A single or list management IP address of the target devices.

                                     Type: ``array``
   *username*                        A single or list of login user names to connect to the devices.

                                     Type: ``array``
   *password*                        A single or list of the login passwords to connect to the devices.

                                     Type: ``array``
   *source_name*                     Save the running/default configurations to startup configurations. Applicable to SLX9840, SLX9850, SLX9140, SLX9240.

                                     Choose from:

                                     - running-config
                                     - default-config

                                     **Default**: running-config
   ================================  ======================================================================

