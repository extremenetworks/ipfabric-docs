.. NOTE: This file has been generated automatically, don't manually edit it

cfg_rate_limiting
~~~~~~~~~~~~~~~~~

**Description**: This workflow accomplishes the task of limiting the cir on a specified interface by applying a service policy on that interface. This is accomplished by first adding an ip extended ACL to the class map, adding the class map to a policy. The policy is applied to the interface. If the input parameter acl_exists is false, then the ACL is first created and then all else proceeds as before. 

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
   **acl_name**                      The access control list name (max 63)

                                     Type: ``string``
   **intf_type**                     The interface type, gigabitethernet or tengigabitethernet, etc

                                     Choose from:

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - ethernet

                                     **Default**: tengigabitethernet
   **intf_name**                     The nterface name as an array (182/0/97)

                                     Type: ``array``
   **class_map_name**                The class map name that will be a part of the service policy.

                                     Type: ``string``
   *class_map_name_exists*           This indicates the class map name that already exists.

                                     Type: ``boolean``

                                     **Default**: True
   **policy_map_name**               The class map name that will be a part of the service policy.

                                     Type: ``array``
   *policy_map_name_exists*          Indicates the policy map name already exists.

                                     Type: ``boolean``

                                     **Default**: True
   **cir**                           The maximum cir that can be allowed through the interface.

                                     Type: ``integer``
   **policy_type**                   In, Out or Both.

                                     Type: ``string``
   **protocol_type**                 The Protocol Number Custom value between 0 and 255, tcp, udp, icmp or ip

                                     Type: ``string``
   **source**                        The source MAC in HHHH.HHHH.HHHH format or source IPv4 or IPv6 address, including tcp and udp port numbers. { any | S_IPaddress mask | host S_IPaddress } [ source-operator [ S_port-numbers ] ]

                                     Type: ``string``

                                     **Default**: any
   *acl_exists*                      This indicates that the acl already exists.

                                     Type: ``boolean``
   *match_type*                      This indicates the class match type.

                                     Type: ``string``

                                     **Default**: True
   *rbridge_id*                      The RBridge ID of the VDX switch under which VE will be configured, only needed for VDX device.

                                     Type: ``string``
   *address_type*                    The Address type - ip or ipv6

                                     Choose from:

                                     - ip
                                     - ipv6
   *destination*                     The destination IP address filters { any | S_IPaddress/mask(0.0.0.255) | host,S_IPaddress } [ source-operator [ S_port-numbers ] ]

                                     Type: ``string``
   *seq_id*                          The sequence number of the rule, if not specified, the rule is added at the end of the list. Valid range is 0 to 4294967290

                                     Type: ``integer``
   *dst_mac_addr_mask*               The dst_mac_addr_mask - the mask for the destination MAC in HHHH.HHHH.HHHH format.

                                     Type: ``string``
   *src_mac_addr_mask*               The source IP address filters { any | S_IPaddress/mask(0.0.0.255) | host,S_IPaddress } [ source-operator [ S_port-numbers ] ]

                                     Type: ``string``
   *dscp*                            The DSCP value to match against. This can be either a numerical value or DSCP name

                                     Type: ``string``
   *vlan_id*                         The VLAN interface to which the ACL is bound

                                     Type: ``integer``
   *ethertype*                       The ethertype - 'arp', 'fcoe', 'ipv4' or a custom value between 1536 and 65535.

                                     Type: ``string``

                                     **Default**: arp
   ================================  ======================================================================

