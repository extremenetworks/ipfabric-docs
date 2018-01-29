.. NOTE: This file has been generated automatically, don't manually edit it

add_ipv4_rule_acl_bulk
~~~~~~~~~~~~~~~~~~~~~~

**Description**: Add an L3 IPv4 ACL rule to an existing ACL. 

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
   **acl_name**                      The name of the access control list.

                                     Type: ``string``
   **acl_rules**                     A list of ACL sequence rules as acl_rules='[{"source": "x.x.x.x/m.m.m.m", "seq_id": 10}, {"source": "y.y.y.y/m.m.m.m", "seq_id": 20}]'

                                     Type: ``array``
   ================================  ======================================================================

