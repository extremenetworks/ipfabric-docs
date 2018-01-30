.. NOTE: This file has been generated automatically, don't manually edit it

configure_class_map
~~~~~~~~~~~~~~~~~~~

**Description**: This creates the Class Map and sets the match criteris. 

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
   **class_name**                    The Policy Map Class Name (Max Size -64).

                                     Type: ``string``
   *match_type*                      The interface type

                                     Choose from:

                                     - access-group
                                     - bridge-domain
                                     - vlan
   *match_value*                     If match_type=access-group, pass name of MAC/IP Access group, match_type=bridge-domain, pass single Bridge-Domain id, match_type=vlan pass single Vlan Id.

                                     Type: ``string``
   ================================  ======================================================================

