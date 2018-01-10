.. NOTE: This file has been generated automatically, don't manually edit it

add_ipv6_rule_acl
~~~~~~~~~~~~~~~~~

**Description**: Add an L3 IPv6 ACL rule to an existing ACL 

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
   **acl_name**                      Name of the access list accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *seq_id*                          Sequence number of the rule, if not specified, the rule is added at the end of the list. Valid range is 0 to 4294967290 required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``integer``
   *action*                          Action performed by ACL rule required-by:- [SLX, NOS, MLX] accepted-by:- [SLX, NOS, MLX]

                                     Choose from:

                                     - permit
                                     - deny
                                     - hard-drop

                                     **Default**: permit
   *protocol_type*                   Type of IP packets to be filtered based on protocol. Valid values are 0 through 255 or key words tcp, udp, icmp or ip MLX supported key words are - ahp, esp, icmp, ipv6, sctp, tcp, udp required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   **source**                        Source address filters { any | S_IPaddress mask | host S_IPaddress } [ source-operator [ S_port-numbers ] ] required-by:- [All] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``

                                     **Default**: any
   *destination*                     Destination address filters { any | S_IPaddress mask | host S_IPaddress } [ source-operator [ S_port-numbers ] ] required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *dscp*                            Matches the specified value against the DSCP value of the packet to filter.  Can be either a numerical value or DSCP name For SLX - dscp value between 0 and 63. Format {<dscp>[,<dscp-force>]}. For NOS - dscp value between 0 and 63. Format {<dscp>]}. For MLX - Only numerical value in range of 0-63 is allowed. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *drop_precedence_force*           Matches the drop_precedence value of the packet.  Allowed values are 0 through 2. MLX- Allowed range is <0-3>. required-by:- [None] accepted-by:- [SLX, MLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``
   *urg*                             Enables urg for the rule required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *ack*                             Enables ack for the rule required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *push*                            Enables push for the rule required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *fin*                             Enables fin for the rule required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *rst*                             Enables rst for the rule required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *sync*                            Enables sync for the rule required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *vlan_id*                         VLAN interface to which the ACL is bound required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``integer``
   *count*                           Enables statistics for the rule required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *log*                             Enables logging for the rule (Available for permit or deny only) required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *mirror*                          Enables mirror for the rule required-by:- [None] accepted-by:- [SLX, MLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``
   *copy_sflow*                      Enables copy-sflow for the rule required-by:- [None] accepted-by:- [SLX, MLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``
   *dscp_marking*                    dscp-marking number is used to mark the DSCP value in the incoming packet with the value you specify to filter. Allowed values are 0 through 63. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *fragment*                        The policy applies to fragmented packets that contain a non-zero fragment offset. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``boolean``
   *drop_precedence*                 Matches the drop_precedence value of the packet. MLX- Allowed range is <0-3>. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *icmp_filter*                     Specify ICMP type and ICMP code or ICMP message. Format is [ [ icmp-type <vlaue> ] [ icmp-code <value> ] ] | [ icmp-message <value> ] icmp-type and icmp-code values are between 0-255. icmp-message value can be one of these beyond-scope, destination-unreachable, dscp, echo-reply, echo-request, flow-label, fragments, header, hop-limit, mld-query, mld-reduction, mld-report, nd-na, nd-ns, next-header, no-admin, no-route, packet-too-big, parameter-option, parameter-problem, port-unreachable, reassembly-timeout, renum-command, renum-result, renum-seq-number, router-advertisement, router-renumbering, router-solicitation, routing, sequence, time-exceeded, unreachable required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *tcp_operator*                    Specifies a comparison operator for the TCP port. This parameter applies only when you specify tcp as the protocol.  Allowed values are [established, syn] required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *acl_rules*                       Bulk operation is supported to create more than one ACL rule in one action execution. The parameters passed to create multiple rules will follow the constraints similar of single rule creation. NOTE- if rules are specified in acl_rules the rule specified outside of array will be ignored and only rules in acl_array will be processed

                                     Type: ``array``
   ================================  ======================================================================

