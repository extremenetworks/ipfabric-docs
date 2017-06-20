.. NOTE: This file has been generated automatically, don't manually edit it

create_acl
~~~~~~~~~~

**Description**: Create an Access Control List 

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
   *address_type*                    ACL address type, ip or ipv6 or mac

                                     Choose from:

                                     - ip
                                     - ipv6
                                     - mac

                                     **Default**: ip
   **acl_type**                      ACL type, extended or standard

                                     Choose from:

                                     - standard
                                     - extended
   **acl_name**                      Unique name for ACL, can be up to 63 characters long, and must begin with a-z, A-Z or 0-9. You can also use underscore (_) or hyphen (-) in an ACL name, but not as the first character.

                                     Type: ``string``
   ================================  ======================================================================

