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
   *password*                        login password

                                     Type: ``string``
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
   **acl_name**                      access list name (max 63)

                                     Type: ``string``
   *rbridge_id*                      RBridge ID of the VDX switch under which VE will be configured, only needed for VDX device.

                                     Type: ``string``
   **intf_type**                     Interface type gigabitethernet or tengigabitethernet, etc

                                     Choose from:

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ve
                                     - loopback
                                     - ethernet

                                     **Default**: tengigabitethernet
   **intf_name**                     interface name as array (182/0/97)

                                     Type: ``array``
   **acl_direction**                 Direction of ACL binding on the specified interface

                                     Choose from:

                                     - in
                                     - out

                                     **Default**: in
   *traffic_type*                    Traffic type for the ACL being applied

                                     Choose from:

                                     - switched
                                     - routed
   *seq_id*                          Sequence number of the rule, if not specified, the rule is added at the end of the list. Valid range is 0 to 4294967290

                                     Type: ``integer``
   *action*                          Action performed by ACL rule

                                     Choose from:

                                     - permit
                                     - deny
                                     - hard-drop

                                     **Default**: permit
   *protocol_type*                   Protocol Number Custom value between 0 and 255, tcp, udp, icmp or ip

                                     Type: ``string``
   **source**                        The source MAC in HHHH.HHHH.HHHH format or source IPv4 or IPv6 address, including tcp and udp port numbers. { any | S_IPaddress mask | host S_IPaddress } [ source-operator [ S_port-numbers ] ]

                                     Type: ``string``

                                     **Default**: any
   *srchost*                         The source MAC in HHHH.HHHH.HHHH format. The value is required only when the source is 'host'.

                                     Type: ``string``
   *src_mac_addr_mask*               the src_mac_addr_mask - the mask for source MAC in HHHH.HHHH.HHHH format.

                                     Type: ``string``
   *destination*                     The destination MAC in HHHH.HHHH.HHHH format or destination IPv4 or IPv6 address, including tcp and udp port numbers. { any | D_IPaddress mask | host D_IPaddress } [ destination-operator [ D_port-numbers ] ]

                                     Type: ``string``
   *dsthost*                         Destination MAC in HHHH.HHHH.HHHH format. The value is required only when the dst is 'host'

                                     Type: ``string``
   *dst_mac_addr_mask*               the dst_mac_addr_mask - the mask for destination MAC in HHHH.HHHH.HHHH format.

                                     Type: ``string``
   *dscp*                            DSCP value to match against. Can be either a numerical value or DSCP name

                                     Type: ``string``
   *drop_precedence_force*           Matches the specified value against the drop_precedence value of the packet to filter.  Allowed values are 0 through 2.

                                     Type: ``string``
   *urg*                             Enables urg for the rule

                                     Type: ``string``
   *ack*                             Enables ack for the rule

                                     Type: ``string``
   *push*                            Enables push for the rule

                                     Type: ``string``
   *fin*                             Enables fin for the rule

                                     Type: ``string``
   *rst*                             Enables rst for the rule

                                     Type: ``string``
   *sync*                            Enables sync for the rule

                                     Type: ``string``
   *vlan_id*                         VLAN interface to which the ACL is bound

                                     Type: ``integer``
   *vlan_tag_format*                 Action to apply on the traffic, either to drop (deny), allow (permit) or force drop (hard-drop)

                                     Choose from:

                                     - untagged
                                     - single-tagged
                                     - double-tagged
   *vlan*                            VLAN IDs - 'any' or 1-4096, Mask 0xHHH. Format{(<VlanID> [<Mask>]) | (<OuterVlan> [<Mask>] <InnerVlan> [<Mask>])}.

                                     Type: ``string``
   *ethertype*                       the ethertype - 'arp', 'fcoe', 'ipv4' or custom value between 1536 and 65535.

                                     Type: ``string``
   *arp_guard*                       Enables arp-guard for the rule

                                     Type: ``string``
   *pcp*                             PCP value between 0 and 7. Format {<pcp>[,<pcp-force>]}.

                                     Type: ``string``
   *count*                           Enables statistics for the rule

                                     Type: ``string``
   *log*                             Enables logging for the rule (Available for permit or deny only)

                                     Type: ``string``
   *mirror*                          Enables mirror for the rule

                                     Type: ``string``
   *copy_sflow*                      Enables copy-sflow for the rule

                                     Type: ``string``
   *acl_exists*                      Indicates is the acl already exists.

                                     Type: ``boolean``
   *acl_rules*                       A list of ACL sequence rules as acl_rules='[{"source": "<src-address-mask>", "seq_id": 10}, {"source": "<src-address-mask>", "seq_id": 20}]'

                                     Type: ``array``
   ================================  ======================================================================

