.. NOTE: This file has been generated automatically, don't manually edit it

configure_fabric_infra
~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configures IP fabric infrastructure. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   *fabric*                          The name of the IP fabric template.

                                     Type: ``string``

                                     **Default**: default
   *username*                        The login user name to connect to the device.

                                     Type: ``string``
   *password*                        The login password to connect to the device.

                                     Type: ``string``
   *batch_size*                      The number of switches to configure concurrently.

                                     Type: ``integer``

                                     **Default**: 10
   **state**                         The filter to fetch all or just unprovisioned devices.

                                     Choose from:

                                     - Unprovisioned
                                     - All

                                     **Default**: Unprovisioned
   ================================  ======================================================================

