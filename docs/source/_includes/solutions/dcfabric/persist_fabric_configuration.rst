.. NOTE: This file has been generated automatically, don't manually edit it

persist_fabric_configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This action saves the running/default configurations to startup configurations on the SLX devices. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   *fabric*                          The name of the IP fabric.

                                     Type: ``string``

                                     **Default**: default
   *username*                        The login user name to connect to the device.

                                     Type: ``string``
   *password*                        The login password to connect to the device.

                                     Type: ``string``
   *source_name*                     Save the running/default configurations to startup configurations. Applicable to SLX9840, SLX9850, SLX9140, SLX9240.

                                     Choose from:

                                     - running-config
                                     - default-config

                                     **Default**: running-config
   ================================  ======================================================================

