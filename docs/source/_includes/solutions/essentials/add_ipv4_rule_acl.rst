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
   **acl_name**                      The name of the access control list

                                     Type: ``string``
   *seq_id*                          The sequence number of the rule, if not specified, the rule is added at the end of the list. Valid range is 0 to 4294967290

                                     Type: ``integer``
   *action*                          The action performed by the ACL rule.

                                     Choose from:

                                     - permit
                                     - deny
                                     - hard-drop

                                     **Default**: permit
   *protocol_type*                   The type of IP packets to be filtered based on the protocol. Valid values are <0-255> or key words tcp, udp, icmp or ip. This parameter is required for extended ACL. For MLX - Valid values are <0-255> or supported protocol keywords.

                                     Type: ``string``
   **source**                        The source IP address filters { any | S_IPaddress/mask(0.0.0.255) | S_IPaddress/Prefix | host,S_IPaddress } [ source-operator [ S_port-numbers ] ]

                                     Type: ``string``

                                     **Default**: any
   *destination*                     The destination IP address filters { any | S_IPaddress/mask(0.0.0.255) | S_IPaddress/Prefix | host,S_IPaddress } [ source-operator [ S_port-numbers ] ]

                                     Type: ``string``
   *dscp*                            This matches the specified value against the DSCP value of the packet to filter.  Allowed values are 0 through 63. For SLX - DSCP value between 0 and 63. Format {<dscp>[,<dscp-force>]}. For NOS - DSCP value between 0 and 63. Format {<dscp>}. For MLX - this field will be used for dscp-mapping.

                                     Type: ``string``
   *drop_precedence_force*           This matches the drop_precedence value of the packet. Allowed values are 0 through 2. For MLX - Allowed values are 0 through 3.  Only supported by MLX, SLX 9850 and 9540 devices.

                                     Type: ``string``
   *urg*                             This enables the urg for the rule. Use "True" or "False" to enable or disable respectively.  Only supported by SLX and NOS devices.

                                     Type: ``string``
   *ack*                             This enables the ack for the rule. Use "True" or "False" to enable or disable respectively.  Only supported by SLX and NOS devices.

                                     Type: ``string``
   *push*                            This enables the push for the rule. Use "True" or "False" to enable or disable respectively.  Only supported by SLX and NOS devices.

                                     Type: ``string``
   *fin*                             This enables the fin for the rule. Use "True" or "False" to enable or disable respectively.  Only supported by SLX and NOS devices.

                                     Type: ``string``
   *rst*                             This enables the rst for the rule. Use "True" or "False" to enable or disable respectively.  Only supported by SLX and NOS devices.

                                     Type: ``string``
   *sync*                            This enables the sync for the rule. Use "True" or "False" to enable or disable respectively.  Only supported by SLX and NOS devices.

                                     Type: ``string``
   *vlan_id*                         The VLAN interface to which the ACL is bound.

                                     Type: ``integer``
   *count*                           This enables the statistics for the rule. Use "True" or "False" to enable or disable respectively. Only supported by SLX and NOS devices.

                                     Type: ``string``
   *log*                             This enables the logging for the rule. Use "True" or "False" to enable or disable respectively.

                                     Type: ``string``
   *mirror*                          This enables the mirror for the rule. Use "True" or "False" to enable or disable respectively. Only supported by MLX, SLX 9850 and 9540 devices.

                                     Type: ``string``
   *copy_sflow*                      This enables the copy-sflow for the rule. Use "True" or "False" to enable or disable respectively. Only supported by MLX, SLX 9850 and 9540 devices.

                                     Type: ``string``
   *dscp_marking*                    This is the dscp-marking number that is used to mark the DSCP value in the incoming packet with the value you specify to filter. Allowed values are 0 through 63. Only supprted by MLX devices.

                                     Type: ``string``
   *fragment*                        The fragment keyword used to allow the ACL to filter fragmented packets. Only supprted by MLX devices. Use the non-fragment keyword to filter non-fragmented packets. - fragment - non-fragment

                                     Type: ``string``
   *precedence*                      This will match packets with given precedence value. Only supprted by MLX devices. Allowed value { <0 to 7> | critical | flash | flash-override | immediate | internet | network | priority | routine  }

                                     Type: ``string``
   *option*                          This will match IP option packets. Only supprted by MLX devices. supported values are - any, eol, extended-security, ignore, loose-source-route, no-op, record-route, router-alert, security, streamid, strict-source-route, timestamp Allowed value in decimal <0-255>.

                                     Type: ``string``
   *suppress_rpf_drop*               This will permit packets that fail RPF check. Use true or false to enable or disable respectively. Only supported by MLX devices.

                                     Type: ``boolean``
   *priority*                        This will set priority. Allowed value is <0-7>. Only supprted by MLX devices.

                                     Type: ``integer``
   *priority_force*                  This will force packet outgoing priority. Allowed value is <0-7>. Only supported by MLX devices.

                                     Type: ``integer``
   *priority_mapping*                This will map incoming packet priority. Allowed value is <0-7>. Only supported by MLX devices.

                                     Type: ``integer``
   *tos*                             This will match packets with given TOS value. Only supprted by MLX devices. Allowed values are { <0-15> | 'max-reliability' | 'max-throughput' | 'min-delay' | 'normal' }

                                     Type: ``string``
   *tcp_operator*                    This specify a comparison operator for the TCP port. This parameter applies only when you specify tcp as the protocol. Allowed values are ["established", "syn", "established syn"]. Only supprted by MLX devices.

                                     Type: ``string``
   *icmp_filter*                     This is the ICMP message type to be filtered. Only supprted by MLX devices.

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
   *drop_precedence*                 This matches the drop_precedence value of the packet. Allowed values are 0 through 2. Only supported by MLX devices - Allowed values are 0 through 3.

                                     Type: ``string``
   *acl_rules*                       This bulk operation is supported to create more than one ACL rule in one action execution. The parameters are passed to create multiple rules that will follow the constraints similar to a single rule creation. NOTE- If rules are specified in acl_rules, the rule specified outside of the array will be ignored and only the rules in the acl_array will be processed. NOTE- On MLX platform, maximum 64 rules can be configured using this parameter. User need to execute this action more than once to configure more than 64 rules.

                                     Type: ``array``
   ================================  ======================================================================

