.. NOTE: This file has been generated automatically, don't manually edit it

drop_provision
~~~~~~~~~~~~~~

**Description**: This workflow accomplishes the task of stopping traffic on a specified interface by first creating and then applying a deny ACL with specific network attributes on that interface. 

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
   **intf_type**                     Interface type gigabitethernet or tengigabitethernet, etc

                                     Choose from:

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - ethernet

                                     **Default**: tengigabitethernet
   **intf_name**                     interface name as array (182/0/97)

                                     Type: ``array``
   *protocol_type*                   Protocol Number Custom value between 0 and 255, tcp, udp, icmp or ip

                                     Type: ``string``
   **source**                        The source MAC in HHHH.HHHH.HHHH format or source IPv4 or IPv6 address, including tcp and udp port numbers. { any | S_IPaddress mask | host S_IPaddress } [ source-operator [ S_port-numbers ] ]

                                     Type: ``string``

                                     **Default**: any
   *src_mac_addr_mask*               the src_mac_addr_mask - the mask for source MAC in HHHH.HHHH.HHHH format.

                                     Type: ``string``
   *destination*                     The destination MAC in HHHH.HHHH.HHHH format or destination IPv4 or IPv6 address, including tcp and udp port numbers. { any | D_IPaddress mask | host D_IPaddress } [ destination-operator [ D_port-numbers ] ]

                                     Type: ``string``
   *dst_mac_addr_mask*               the dst_mac_addr_mask - the mask for destination MAC in HHHH.HHHH.HHHH format.

                                     Type: ``string``
   *dscp*                            DSCP value to match against. Can be either a numerical value or DSCP name

                                     Type: ``string``
   *vlan_id*                         VLAN interface to which the ACL is bound

                                     Type: ``integer``
   *ethertype*                       the ethertype - 'arp', 'fcoe', 'ipv4' or custom value between 1536 and 65535.

                                     Type: ``string``

                                     **Default**: arp
   **address_type**                  the address type IPv4 IPv6 or MAC used to create the acl.

                                     Choose from:

                                     - ip
                                     - ipv6
                                     - mac
   **intf**                          interface name as string (182/0/97)

                                     Type: ``string``
   *acl_exists*                      Indicates is the acl already exists.

                                     Type: ``boolean``
   *seq_id*                          Sequence number of the rule, if not specified, the rule is added at the end of the list. Valid range is 0 to 4294967290

                                     Type: ``integer``
   ================================  ======================================================================

