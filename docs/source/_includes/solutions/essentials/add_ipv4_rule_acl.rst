.. NOTE: This file has been generated automatically, don't manually edit it

add_ipv4_rule_acl
~~~~~~~~~~~~~~~~~

**Description**: Add a Layer 3 IPv4 ACL rule to an already existing ACL. 

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
   **acl_name**                      The name of the access control list accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *seq_id*                          The sequence number of the rule, if not specified, the rule is added at the end of the list. Valid range is 0 to 4294967290 required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``integer``
   *action*                          The action performed by the ACL rule. required-by:- [SLX, NOS, MLX] accepted-by:- [SLX, NOS, MLX]

                                     Choose from:

                                     - permit
                                     - deny
                                     - hard-drop

                                     **Default**: permit
   *protocol_type*                   The type of IP packets to be filtered based on the protocol. Valid values are <0-255> or key words tcp, udp, icmp or ip. This parameter is required for extended ACL. For MLX - Valid values are <0-255> or supported protocol keywords. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   **source**                        The source IP address filters { any | S_IPaddress/mask(0.0.0.255) | S_IPaddress/Prefix | host,S_IPaddress } [ source-operator [ S_port-numbers ] ] required-by:- [All] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``

                                     **Default**: any
   *destination*                     The destination IP address filters { any | S_IPaddress/mask(0.0.0.255) | S_IPaddress/Prefix | host,S_IPaddress } [ source-operator [ S_port-numbers ] ] required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *dscp*                            This matches the specified value against the DSCP value of the packet to filter.  Allowed values are 0 through 63. For SLX - dscp value between 0 and 63. Format {<dscp>[,<dscp-force>]}. For NOS - dscp value between 0 and 63. Format {<dscp>]}. For MLX - this field will be used for dscp-mapping. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *drop_precedence_force*           This matches the drop_precedence value of the packet. Allowed values are 0 through 2. For MLX - Allowed values are 0 through 3. required-by:- [None] accepted-by:- [SLX, MLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``
   *urg*                             This enables the urg for the rule. Use "True" or "False" to enable or disable respectively. required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *ack*                             This enables the ack for the rule. Use "True" or "False" to enable or disable respectively. required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *push*                            This enables the push for the rule. Use "True" or "False" to enable or disable respectively. required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *fin*                             This enables the fin for the rule. Use "True" or "False" to enable or disable respectively. required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *rst*                             This enables the rst for the rule. Use "True" or "False" to enable or disable respectively. required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *sync*                            This enables the sync for the rule. Use "True" or "False" to enable or disable respectively. required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *vlan_id*                         The VLAN interface to which the ACL is bound required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``integer``
   *count*                           This enables the statistics for the rule. Use "True" or "False" to enable or disable respectively. required-by:- [None] accepted-by:- [SLX, NOS]

                                     Type: ``string``
   *log*                             This enables the logging for the rule. Use "True" or "False" to enable or disable respectively. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *mirror*                          This enables the mirror for the rule. Use "True" or "False" to enable or disable respectively. required-by:- [None] accepted-by:- [SLX, MLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``
   *copy_sflow*                      This enables the copy-sflow for the rule. Use "True" or "False" to enable or disable respectively. required-by:- [None] accepted-by:- [SLX, MLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``
   *dscp_marking*                    This is the dscp-marking number that is used to mark the DSCP value in the incoming packet with the value you specify to filter. Allowed values are 0 through 63. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *fragment*                        The fragment keyword used to allow the ACL to filter fragmented packets. Use the non-fragment keyword to filter non-fragmented packets. - fragment - non-fragment required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *precedence*                      This will match packets with given precedence value. Allowed value { <0 to 7> | critical | flash | flash-override | immediate | internet | network | priority | routine  } required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *option*                          This will match match IP option packets. supported values are - any, eol, extended-security, ignore, loose-source-route, no-op, record-route, router-alert, security, streamid, strict-source-route, timestamp Allowed value in decimal <0-255>. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *suppress_rpf_drop*               This will permit packets that fail RPF check. Use true or false to enable or disable respectively. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``boolean``
   *priority*                        This will set priority. Allowed value is <0-7>. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``integer``
   *priority_force*                  This will force packet outgoing priority. Allowed value is <0-7>. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``integer``
   *priority_mapping*                This will map incoming packet priority. Allowed value is <0-7>. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``integer``
   *tos*                             This will match packets with given TOS value. Allowed values are { <0-15> | 'max-reliability' | 'max-throughput' | 'min-delay' | 'normal' } required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *tcp_operator*                    This specify a comparison operator for the TCP port. This parameter applies only when you specify tcp as the protocol. Allowed values are ["established", "syn", "established syn"]. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *icmp_filter*                     This is the ICMP message type to be filtered. required-by:- [None] accepted-by:- [MLX]

                                     Choose from:

                                     - administratively-prohibited
                                     - any-icmp-type
                                     - destination-host-prohibited
                                     - destination-host-unknown
                                     - destination-net-prohibited
                                     - destination-network-unknown
                                     - echo
                                     - echo-reply
                                     - general-parameter-problem
                                     - host-precedence-violation
                                     - host-redirect
                                     - host-tos-redirect
                                     - host-tos-unreachable
                                     - host-unreachable
                                     - information-reply
                                     - information-request
                                     - mask-reply
                                     - mask-request
                                     - net-redirect
                                     - net-tos-redirect
                                     - net-tos-unreachable
                                     - net-unreachable
                                     - packet-too-big
                                     - parameter-problem
                                     - port-unreachable
                                     - precedence-cutoff
                                     - protocol-unreachable
                                     - reassembly-timeout
                                     - redirect
                                     - router-advertisement
                                     - router-solicitation
                                     - source-host-isolated
                                     - source-quench
                                     - source-route-failed
                                     - time-exceeded
                                     - timestamp-reply
                                     - timestamp-request
                                     - ttl-exceeded
                                     - unreachable
   *drop_precedence*                 This matches the drop_precedence value of the packet. Allowed values are 0 through 2. For MLX - Allowed values are 0 through 3. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *acl_rules*                       This bulk operation is supported to create more than one ACL rule in one action execution. The parameters are passed to create multiple rules that will follow the constraints similar to a single rule creation. NOTE- if rules are specified in acl_rules, the rule specified outside of the array will be ignored and only the rules in the acl_array will be processed NOTE- On MLX platform, maximum 64 rules can be configured using this parameter. User need to execute this action more than once to configure more than 64 rules.

                                     Type: ``array``
   ================================  ======================================================================

