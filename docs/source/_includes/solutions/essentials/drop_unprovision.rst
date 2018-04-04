.. NOTE: This file has been generated automatically, don't manually edit it

drop_unprovision
~~~~~~~~~~~~~~~~

**Description**: This workflow accomplishes the task of allowing traffic back on a specified interface by first deleting the deny ACL currently on that interface. It may also delete the acl, if it is empty. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       device ip address

                                     Type: ``string``
   *username*                        login username

                                     Type: ``string``

                                     **Default**: admin
   *password*                        login password

                                     Type: ``string``

                                     **Default**: password
   **acl_name**                      access list name (max 63)

                                     Type: ``string``
   **intf_type**                     The interface type gigabitethernet or tengigabitethernet, etc.

                                     Choose from:

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - ethernet

                                     **Default**: tengigabitethernet
   **intf_name**                     The interface name as an array (182/0/97).

                                     Type: ``array``
   **address_type**                  the address type IPv4 IPv6 or MAC used to create the acl.

                                     Choose from:

                                     - ip
                                     - ipv6
                                     - mac
   *delete_acl*                      This ndicates whether the ACL should be deleted.

                                     Type: ``boolean``
   *seq_id*                          Sequence number of the rule, if not specified, the rule is added at the end of the list. Valid range is 0 to 4294967290

                                     Type: ``string``
   ================================  ======================================================================

