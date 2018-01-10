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
   *protocol_type*                   Type of IP packets to be filtered based on protocol. Valid values are <0-255> or key words tcp, udp, icmp or ip For MLX - Valid values are <0-255> or supported protocol keywords. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   **source**                        Source address filters { any | S_IPaddress/mask(0.0.0.255) | host,S_IPaddress } [ source-operator [ S_port-numbers ] ] required-by:- [All] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``

                                     **Default**: any
   *destination*                     Destination address filters { any | S_IPaddress/mask(0.0.0.255) | host,S_IPaddress } [ source-operator [ S_port-numbers ] ] required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *dscp*                            Matches the specified value against the DSCP value of the packet to filter.  Allowed values are 0 through 63. For SLX - dscp value between 0 and 63. Format {<dscp>[,<dscp-force>]}. For NOS - dscp value between 0 and 63. Format {<dscp>]}. For MLX - this field will be used for dscp-mapping. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *drop_precedence_force*           Matches the drop_precedence value of the packet. Allowed values are 0 through 2. For MLX - Allowed values are 0 through 3. required-by:- [None] accepted-by:- [SLX, MLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

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
   *log*                             Enables logging for the rule. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   *mirror*                          Enables mirror for the rule required-by:- [None] accepted-by:- [SLX, MLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``
   *copy_sflow*                      Enables copy-sflow for the rule required-by:- [None] accepted-by:- [SLX, MLX] (NOTE:- SLX16r and SLXs devices doesn't support this parameter)

                                     Type: ``string``
   *dscp_marking*                    dscp-marking number is used to mark the DSCP value in the incoming packet with the value you specify to filter. Allowed values are 0 through 63. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *fragment*                        Use fragment keyword to allow the ACL to filter fragmented packets. Use the non-fragment keyword to filter non-fragmented packets. - fragment - non-fragment required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *precedence*                      Match packets with given precedence value. Allowed value { <0 to 7> | critical | flash | flash-override | immediate | internet | network | priority | routine  } required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *option*                          Match match IP option packets. supported values are - any, eol, extended-security, ignore, loose-source-route, no-op, record-route, router-alert, security, streamid, strict-source-route, timestamp Allowed value in decimal <0-255>. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *suppress_rpf_drop*               Permit packets that fail RPF check required-by:- [None] accepted-by:- [MLX]

                                     Type: ``boolean``
   *priority*                        set priority. Allowed value is <0-7>. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``integer``
   *priority_force*                  force packet outgoing priority. Allowed value is <0-7>. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``integer``
   *priority_mapping*                map incoming packet priority. Allowed value is <0-7>. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``integer``
   *tos*                             Match packets with given TOS value. Allowed value in decimal <0-15>. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``integer``
   *established*                     This policy applies only to TCP packets that have the ACK or RST bits set on. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``boolean``
   *icmp_filter*                     ICMP message type to be filtered. required-by:- [None] accepted-by:- [MLX]

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
   *drop_precedence*                 Matches the drop_precedence value of the packet. Allowed values are 0 through 2. For MLX - Allowed values are 0 through 3. required-by:- [None] accepted-by:- [MLX]

                                     Type: ``string``
   *acl_rules*                       Bulk operation is supported to create more than one ACL rule in one action execution. The parameters passed to create multiple rules will follow the constraints similar of single rule creation. NOTE- if rules are specified in acl_rules the rule specified outside of array will be ignored and only rules in acl_array will be processed

                                     Type: ``array``
   ================================  ======================================================================

