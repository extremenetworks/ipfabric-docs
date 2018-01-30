.. NOTE: This file has been generated automatically, don't manually edit it

configure_policy_map_class
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This creates the Policy Map, Class Instance and Police Configurations. 

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
   **policy_map_name**               The Policy Map Class Name (Max Size -64).

                                     Type: ``string``
   *class_name*                      The Policy Map Class Name (Max Size -64).

                                     Type: ``string``

                                     **Default**: default
   *cir*                             The Committed Information Rate. The Valid Range is <0-300000000000> bits Per Second.

                                     Type: ``integer``
   *cbs*                             The Committed Burst Rate. The Valid Range is <1250-37500000000> Bytes.

                                     Type: ``integer``
   *eir*                             The Extended Information Rate. The Valid Range is <0-300000000000> bits Per Second.

                                     Type: ``integer``
   *ebs*                             The Extended Burst Rate. The Valid Range is <1250-37500000000> Bytes.

                                     Type: ``integer``
   ================================  ======================================================================

