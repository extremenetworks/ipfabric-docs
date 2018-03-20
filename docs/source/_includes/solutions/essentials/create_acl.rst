.. NOTE: This file has been generated automatically, don't manually edit it

create_acl
~~~~~~~~~~

**Description**: This creates an Access Control List. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``
   *password*                        The login password to connect to the device.

                                     Type: ``string``
   *address_type*                    The ACL address type, ip or ipv6 or mac. required-by:- [SLX, NOS, MLX] accepted-by:- [SLX, NOS, MLX]

                                     Choose from:

                                     - ip
                                     - ipv6
                                     - mac

                                     **Default**: ip
   *acl_type*                        The ACL type, extended or standard. acl_type is required by MLX for ip/ipv6 acl. required-by:- [SLX, NOS] accepted-by:- [SLX, NOS, MLX]

                                     Choose from:

                                     - standard
                                     - extended
   **acl_name**                      The unique name for the ACL which must begin with a-z, A-Z. Keywords "all" and "test" can not be used as acl_name. accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   ================================  ======================================================================

