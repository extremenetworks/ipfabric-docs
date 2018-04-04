.. NOTE: This file has been generated automatically, don't manually edit it

add_or_remove_l2_acl_rule
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This adds or removes an ACL rule to or from an L2 ACL. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   *delete*                          This indicates an add or delete operation. If TRUE, this indicates a remove operation.

                                     Type: ``boolean``
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   **acl_name**                      The name of the access control list.

                                     Type: ``string``
   *seq_id*                          The sequence numbers of rules to be deleted { seq id | all | comman and hyphen separated seq ids } Example:- { 10 | all | 1,2,3-10,20,35-  } Note:- 1. Range operation is only supported for delete operation. 2. "-" separated values will look for seq_ids inthe range including the values and 35- is equal to starting from 35 delete all configured sequence ids, including 35.

                                     Type: ``string``
   *action*                          The action to apply on the traffic, either to drop (deny), allow (permit) or force drop (hard-drop).

                                     Choose from:

                                     - deny
                                     - permit
                                     - hard-drop

                                     **Default**: deny
   *source*                          The source filter, which can be 'any' or 'host', or the actual MAC in HHHH.HHHH.HHHH format MLX - Source filter, can be 'any' or the actual MAC in HHHH.HHHH.HHHH format.

                                     Type: ``string``

                                     **Default**: any
   *srchost*                         The source MAC in HHHH.HHHH.HHHH format. The value is required only when the source is 'host'.  Only supported by SLX and NOS devices.

                                     Type: ``string``
   *src_mac_addr_mask*               The mask for the source MAC in HHHH.HHHH.HHHH format.

                                     Type: ``string``
   *dst*                             The destination filter, this can be 'any' or 'host', or the actual MAC of the destination in HHHH.HHHH.HHHH format. MLX - Destination filter, can be 'any' or the actual MAC in HHHH.HHHH.HHHH format.

                                     Type: ``string``

                                     **Default**: any
   *dsthost*                         The destination MAC in HHHH.HHHH.HHHH format. The value is required only when the dst is 'host'.

                                     Type: ``string``
   *dst_mac_addr_mask*               The mask for the destination MAC in HHHH.HHHH.HHHH format.

                                     Type: ``string``
   *vlan_tag_format*                 The action to apply on the traffic, either to drop (deny), allow (permit) or force drop (hard-drop). Only supported by SLX 9850 and 9540 devices.

                                     Choose from:

                                     - untagged
                                     - single-tagged
                                     - double-tagged
   *vlan*                            The VLAN IDs - 'any' or 1-4096, Mask 0xHHH. Format{(<VlanID> [<Mask>]) | (<OuterVlan> [<Mask>] <InnerVlan> [<Mask>])}.

                                     Type: ``string``
   *ethertype*                       The EtherType, this can be 'arp', 'fcoe', 'ipv4' or custom value between 1536 and 65535. For MLX EtherType, can be 'arp', 'fcoe', 'ipv4-l5', 'ipv6' or custom value between integers 1536 and 65535.

                                     Type: ``string``
   *arp_guard*                       This enables the arp-guard for the rule.  Only supported by MLXe and SLX 9850, 9540 devices.

                                     Type: ``string``

                                     **Default**: False
   *pcp*                             The PCP value between 0 and 7. Format {<pcp>[,<pcp-force>]}. Only supported by SLX 9850 and 9540 devices.

                                     Type: ``string``
   *drop_precedence_force*           This matches the specified value against the drop_precedence value of the packet to filter. Allowed values are 0 through 2. For MLX Platform supported range is 0 through 3. Only supported by MLX, SLX 9850 and 9540 devices.

                                     Type: ``string``
   *count*                           This enables the packet count.

                                     Type: ``string``

                                     **Default**: False
   *log*                             This enables logging.

                                     Type: ``string``

                                     **Default**: False
   *mirror*                          This enables the mirror for the rule. Only supported by MLXe and SLX 9850, 9540 devices.

                                     Type: ``string``

                                     **Default**: False
   *copy_sflow*                      This enables the copy-sflow for the rule. Only supported by SLX 9850, 9540 devices.

                                     Type: ``string``

                                     **Default**: False
   *drop_precedence*                 This matches the specified value against the drop_precedence value of the packet to filter. Allowed values are 0 through 2. For MLX Platform supported range is 0 through 3. Only supported by MLXe and SLX 9850, 9540 devices.

                                     Type: ``string``
   *priority*                        This matches the specified value against the priority value of the packet to filter. Allowed values are 0 through 7. Only supported by MLX devices.

                                     Type: ``integer``
   *priority_force*                  This matches the specified value against the priority_force value of the packet to filter. Allowed values are 0 through 7. Only supported by MLX devices.

                                     Type: ``integer``
   *priority_mapping*                This matches the specified value against the priority_mapping value of the packet to filter. Allowed values are 0 through 7. Only supported by MLX devices.

                                     Type: ``integer``
   *acl_rules*                       This bulk operation is supported to create more than one ACL rule in one action execution. The parameters are passed to create multiple rules that will follow the constraints similar to a single rule creation. NOTE- if rules are specified in acl_rules, the rule specified outside of the array will be ignored and only the rules in the acl_array will be processed. NOTE- On MLX platform, maximum 64 rules can be configured using this parameter. User need to execute this action more than once to configure more than 64 rules.

                                     Type: ``array``
   ================================  ======================================================================

