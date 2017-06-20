.. NOTE: This file has been generated automatically, don't manually edit it

add_ipv4_rule_acl
~~~~~~~~~~~~~~~~~

**Description**: Add an L3 IPv4 ACL rule to an existing ACL 

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
   **acl_name**                      Name of the access list

                                     Type: ``string``
   *seq_id*                          Sequence number of the rule, if not specified, the rule is added at the end of the list. Valid range is 0 to 4294967290

                                     Type: ``integer``
   *action*                          Action performed by ACL rule

                                     Choose from:

                                     - permit
                                     - deny
                                     - hard-drop

                                     **Default**: permit
   *protocol_type*                   Type of IP packets to be filtered based on protocol. Valid values are <0-255> or key words tcp, udp, icmp or ip

                                     Type: ``string``
   **source**                        Source address filters { any | S_IPaddress/mask(0.0.0.255) | host,S_IPaddress } [ source-operator [ S_port-numbers ] ]

                                     Type: ``string``

                                     **Default**: any
   *destination*                     Destination address filters { any | S_IPaddress/mask(0.0.0.255) | host,S_IPaddress } [ source-operator [ S_port-numbers ] ]

                                     Type: ``string``
   *dscp*                            Matches the specified value against the DSCP value of the packet to filter.  Allowed values are 0 through 63.

                                     Type: ``string``
   *vlan_id*                         VLAN interface to which the ACL is bound

                                     Type: ``integer``
   *count*                           Enables statistics for the rule

                                     Type: ``string``

                                     **Default**: False
   *log*                             Enables logging for the rule (Available for permit or deny only)

                                     Type: ``string``

                                     **Default**: False
   ================================  ======================================================================

