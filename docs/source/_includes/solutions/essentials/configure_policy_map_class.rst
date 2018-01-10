.. NOTE: This file has been generated automatically, don't manually edit it

configure_policy_map_class
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Create Policy Map, Class Instance and Police Configurations. 

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
   **policy_map_name**               Policy Map Class Name (Max Size -64)

                                     Type: ``string``
   *class_name*                      Policy Map Class Name (Max Size -64)

                                     Type: ``string``

                                     **Default**: default
   *cir*                             Committed Information Rate.Valid Range <0-300000000000> bits Per Second

                                     Type: ``integer``
   *cbs*                             Committed Burst Rate.Valid Range <1250-37500000000> Bytes

                                     Type: ``integer``
   *eir*                             Extended Information Rate.Valid Range <0-300000000000> bits Per Second

                                     Type: ``integer``
   *ebs*                             Extended Burst Rate.Valid Range <1250-37500000000> Bytes

                                     Type: ``integer``
   ================================  ======================================================================

