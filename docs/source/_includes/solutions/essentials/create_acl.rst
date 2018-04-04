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
   *address_type*                    The ACL address type, IP or IPv6 or MAC.

                                     Choose from:

                                     - ip
                                     - ipv6
                                     - mac

                                     **Default**: ip
   *acl_type*                        The ACL type, extended or standard. This is required for SLX and NOS. The acl_type is required by MLX for IP/IPv6 ACL.

                                     Choose from:

                                     - standard
                                     - extended
   **acl_name**                      The unique name for the ACL which must begin with a-z, A-Z. Keywords "all" and "test" can not be used as acl_name.

                                     Type: ``string``
   ================================  ======================================================================

