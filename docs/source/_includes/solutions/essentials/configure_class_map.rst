.. NOTE: This file has been generated automatically, don't manually edit it

configure_class_map
~~~~~~~~~~~~~~~~~~~

**Description**: Create Class Map and set the match criteris. 

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
   **class_name**                    Policy Map Class Name (Max Size -64)

                                     Type: ``string``
   *match_type*                      Interface type

                                     Choose from:

                                     - access-group
                                     - bridge-domain
                                     - vlan
   *match_value*                     If match_type=access-group, pass name of MAC/IP Access group, match_type=bridge-domain, pass single Bridge-Domain id, match_type=vlan pass single Vlan Id.

                                     Type: ``string``
   ================================  ======================================================================

