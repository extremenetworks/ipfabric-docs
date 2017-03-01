.. NOTE: This file has been generated automatically, don't manually edit it

add_or_remove_l2_acl_rule
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Add or remove an ACL rule to or from an L2 ACL 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   *delete*                          Indicates add or delete operation. TRUE indicates a remove operation.

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
   *seq_id*                          Sequence number of the rule.  For add operation, if not specified, the rule is added at the end of the list.

                                     Type: ``integer``
   *action*                          Action to apply on the traffic, either to drop (deny), allow (permit) or force drop (hard-drop)

                                     Choose from:

                                     - deny
                                     - permit
                                     - hard-drop

                                     **Default**: deny
   *source*                          Source filter, can be 'any' or 'host', or the actual MAC in HHHH.HHHH.HHHH format.

                                     Type: ``string``

                                     **Default**: any
   *srchost*                         The source MAC in HHHH.HHHH.HHHH format. The value is required only when the source is 'host'.

                                     Type: ``string``
   *src_mac_addr_mask*               Mask for the source MAC in HHHH.HHHH.HHHH format.

                                     Type: ``string``
   *dst*                             Destination filter, can be 'any' or 'host', or the actual MAC of the destination in HHHH.HHHH.HHHH format.

                                     Type: ``string``

                                     **Default**: any
   *dsthost*                         Destination MAC in HHHH.HHHH.HHHH format. The value is required only when the dst is 'host'

                                     Type: ``string``
   *dst_mac_addr_mask*               Mask for the destination MAC in HHHH.HHHH.HHHH format.

                                     Type: ``string``
   *ethertype*                       EtherType, can be 'arp', 'fcoe', 'ipv4' or custom value between 1536 and 65535.

                                     Type: ``string``

                                     **Default**: arp
   *vlan*                            VLAN ID - custom value between 1 and 4096.

                                     Type: ``integer``
   *count*                           Enables the packet count

                                     Type: ``string``

                                     **Default**: False
   *log*                             Enables the logging

                                     Type: ``string``

                                     **Default**: False
   ================================  ======================================================================

