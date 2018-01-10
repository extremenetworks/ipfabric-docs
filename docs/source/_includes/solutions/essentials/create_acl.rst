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
   *password*                        Login password to connect to the device

                                     Type: ``string``
   *address_type*                    ACL address type, ip or ipv6 or mac required-by:- [SLX, NOS, MLX] accepted-by:- [SLX, NOS, MLX]

                                     Choose from:

                                     - ip
                                     - ipv6
                                     - mac

                                     **Default**: ip
   *acl_type*                        ACL type, extended or standard required-by:- [SLX, NOS] accepted-by:- [SLX, NOS, MLX]

                                     Choose from:

                                     - standard
                                     - extended
   **acl_name**                      Unique name for ACL which must begin with a-z, A-Z. accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   ================================  ======================================================================

