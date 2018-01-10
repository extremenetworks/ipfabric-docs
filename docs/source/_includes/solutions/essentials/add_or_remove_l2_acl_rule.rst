.. NOTE: This file has been generated automatically, don't manually edit it

add_or_remove_l2_acl_rule
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Add or remove an ACL rule to or from an L2 ACL 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   *delete*                          Indicates add or delete operation. TRUE indicates a remove operation. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``boolean``
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
   *seq_id*                          Sequence number of the rule.  For add operation, if not specified, the rule is added at the end of the list. For delete operation seq_id is required-by parameter for MLX, SLX, VDX. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``integer``
   *action*                          Action to apply on the traffic, either to drop (deny), allow (permit) or force drop (hard-drop) required-by:- [SLX, NOS, MLX] accepted-by:- [SLX, NOS, MLX]

                                     Choose from:

                                     - deny
                                     - permit
                                     - hard-drop

                                     **Default**: deny
   *source*                          Source filter, can be 'any' or 'host', or the actual MAC in HHHH.HHHH.HHHH format MLX - Source filter, can be 'any' or the actual MAC in HHHH.HHHH.HHHH format. required-by:- [SLX, NOS, MLX] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``

                                     **Default**: any
   *srchost*                         The source MAC in HHHH.HHHH.HHHH format. The value is required only when the source is 'host'. required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *src_mac_addr_mask*               Mask for the source MAC in HHHH.HHHH.HHHH format. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *dst*                             Destination filter, can be 'any' or 'host', or the actual MAC of the destination in HHHH.HHHH.HHHH format. MLX - Destination filter, can be 'any' or the actual MAC in HHHH.HHHH.HHHH format. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``

                                     **Default**: any
   *dsthost*                         Destination MAC in HHHH.HHHH.HHHH format. The value is required only when the dst is 'host' required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *dst_mac_addr_mask*               Mask for the destination MAC in HHHH.HHHH.HHHH format. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *vlan_tag_format*                 Action to apply on the traffic, either to drop (deny), allow (permit) or force drop (hard-drop) required-by:- [None] accepted-by:- [SLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Choose from:

                                     - untagged
                                     - single-tagged
                                     - double-tagged
   *vlan*                            VLAN IDs - 'any' or 1-4096, Mask 0xHHH. Format{(<VlanID> [<Mask>]) | (<OuterVlan> [<Mask>] <InnerVlan> [<Mask>])}. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *ethertype*                       EtherType, can be 'arp', 'fcoe', 'ipv4' or custom value between 1536 and 65535. For MLX EtherType, can be 'arp', 'fcoe', 'ipv4-l5', 'ipv6' or custom value between 1536 and 65535. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *arp_guard*                       Enables arp-guard for the rule required-by:- [None] accepted-by:- [SLX, MLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``

                                     **Default**: False
   *pcp*                             PCP value between 0 and 7. Format {<pcp>[,<pcp-force>]}. required-by:- [None] accepted-by:- [SLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``
   *drop_precedence_force*           Matches the specified value against the drop_precedence value of the packet to filter.  Allowed values are 0 through 2. For MLX Platform supported range is 0 through 3. required-by:- [None] accepted-by:- [SLX, MLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``
   *count*                           Enables the packet count required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``

                                     **Default**: False
   *log*                             Enables the logging required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``

                                     **Default**: False
   *mirror*                          Enables mirror for the rule required-by:- [None] accepted-by:- [SLX, MLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``

                                     **Default**: False
   *copy_sflow*                      Enables copy-sflow for the rule required-by:- [None] accepted-by:- [SLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``

                                     **Default**: False
   *drop_precedence*                 Matches the specified value against the drop_precedence value of the packet to filter.  Allowed values are 0 through 2. For MLX Platform supported range is 0 through 3. required-by:- [None] accepted-by:- [SLX, MLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``
   *priority*                        Matches the specified value against the priority value of the packet to filter.  Allowed values are 0 through 7. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``integer``
   *priority_force*                  Matches the specified value against the priority_force value of the packet to filter.  Allowed values are 0 through 7. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``integer``
   *priority_mapping*                Matches the specified value against the priority_mapping value of the packet to filter.  Allowed values are 0 through 7. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``integer``
   ================================  ======================================================================

