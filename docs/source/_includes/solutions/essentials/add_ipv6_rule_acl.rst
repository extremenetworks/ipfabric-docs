.. NOTE: This file has been generated automatically, don't manually edit it

add_ipv6_rule_acl
~~~~~~~~~~~~~~~~~

**Description**: This adds an L3 IPv6 ACL rule to an existing ACL. 

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
   **acl_name**                      The name of the access control list. accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *seq_id*                          The sequence number of the rule, if not specified, the rule is added at the end of the list. Valid range is 0 to 4294967290.

                                     Type: ``integer``
   *action*                          The action performed by the ACL rule.

                                     Choose from:

                                     - permit
                                     - deny
                                     - hard-drop

                                     **Default**: permit
   *protocol_type*                   The type of IP packets to be filtered based on the protocol. Valid values are 0 through 255 or key words tcp, udp, icmp or ip. MLX supported key words are - ahp, esp, icmp, ipv6, sctp, tcp, udp

                                     Type: ``string``
   **source**                        The source IP address filters { any | S_IPaddress mask | host S_IPaddress } [ source-operator [ S_port-numbers ] ]

                                     Type: ``string``

                                     **Default**: any
   *destination*                     The destination IP address filters { any | S_IPaddress mask | host S_IPaddress } [ source-operator [ S_port-numbers ] ]

                                     Type: ``string``
   *dscp*                            This matches the specified value against the DSCP value of the packet. to filter.  Can be either a numerical value or DSCP name. For SLX - DSCP value between 0 and 63. Format {<dscp>[,<dscp-force>]}. For NOS - DSCP value between 0 and 63. Format {<dscp>}. For MLX - Only numerical value in range of 0-63 is allowed.

                                     Type: ``string``
   *drop_precedence_force*           This matches the drop_precedence value of the packet. Allowed values are 0 through 2. MLX- Allowed range is <0-3>. Supported by MLX, SLX 9850 and 9540 devices.

                                     Type: ``string``
   *urg*                             This enables the urg for the rule. Use "True" or "False" to enable or disable respectively. Supported by SLX and NOS devices.

                                     Type: ``string``
   *ack*                             This enables the ACK for the rule. Use "True" or "False" to enable or disable respectively. Supported by SLX and NOS devices.

                                     Type: ``string``
   *push*                            This enables the push for the rule. Use "True" or "False" to enable or disable respectively. Supported by SLX and NOS devices.

                                     Type: ``string``
   *fin*                             This enables the FIN for the rule. Use "True" or "False" to enable or disable respectively. Supported by SLX and NOS devices.

                                     Type: ``string``
   *rst*                             This enables the RST for the rule. Use "True" or "False" to enable or disable respectively. Supported by SLX and NOS devices.

                                     Type: ``string``
   *sync*                            This enables the SYNC for the rule. Use "True" or "False" to enable or disable respectively. Supported by SLX and NOS devices.

                                     Type: ``string``
   *vlan_id*                         The VLAN interface to which the ACL is bound.

                                     Type: ``integer``
   *count*                           This enables the statistics for the rule. Use "True" or "False" to enable or disable respectively. Supported by SLX and NOS devices.

                                     Type: ``string``
   *log*                             This enables the logging for the rule (Available for permit or deny only). Use "True" or "False" to enable or disable respectively.

                                     Type: ``string``
   *mirror*                          This enables the mirror for the rule. Use "True" or "False" to enable or disable respectively. Supported by MLX, SLX 9850 and 9540 devices.

                                     Type: ``string``
   *copy_sflow*                      This enables the copy-sflow for the rule. Use "True" or "False" to enable or disable respectively. Supported by MLX, SLX 9850 and 9540 devices.

                                     Type: ``string``
   *dscp_marking*                    The dscp-marking number used to mark the DSCP value in the incoming packet with the value you specify in the filter.  Only supported by MLX devices. Allowed values are 0 through 63.

                                     Type: ``string``
   *fragment*                        The policy applied to fragmented packets that contain a non-zero fragment offset. Only supported by MLX devices.

                                     Type: ``boolean``
   *drop_precedence*                 This matches the drop_precedence value of the packet. Only supported by MLX devices. MLX- Allowed range is <0-3>.

                                     Type: ``string``
   *icmp_filter*                     This specify the ICMP type and ICMP code or ICMP message. Format is [ [ icmp-type <vlaue> ] [ icmp-code <value> ] ] | [ icmp-message <value> ] icmp-type and icmp-code values are between 0-255. Only supported by MLX devices. icmp-message value can be one of these beyond-scope, destination-unreachable, dscp, echo-reply, echo-request, flow-label, fragments, header, hop-limit, mld-query, mld-reduction, mld-report, nd-na, nd-ns, next-header, no-admin, no-route, packet-too-big, parameter-option, parameter-problem, port-unreachable, reassembly-timeout, renum-command, renum-result, renum-seq-number, router-advertisement, router-renumbering, router-solicitation, routing, sequence, time-exceeded, unreachable

                                     Type: ``string``
   *tcp_operator*                    This specify a comparison operator for the TCP port. This parameter applies only when you specify tcp as the protocol. Allowed values are ['established', 'syn', 'established syn']. Only supported by MLX devices.

                                     Type: ``string``
   *acl_rules*                       The bulk operation that is supported to create more than one ACL rule in one action execution. The parameters are passed to create multiple rules that will follow the constraints similar to a single rule creation. NOTE- If rules are specified in the acl_rules, the rule specified outside of the array will be ignored and only rules in the acl_array will be processed. NOTE- On MLX platform, maximum 64 rules can be configured using this parameter. User need to execute this action more than once to configure more than 64 rules.

                                     Type: ``array``
   ================================  ======================================================================

