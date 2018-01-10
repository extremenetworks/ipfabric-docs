.. NOTE: This file has been generated automatically, don't manually edit it

add_mac_rule_acl_bulk
~~~~~~~~~~~~~~~~~~~~~

**Description**: Add an L2 ACL rule to an existing ACL 

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
   **acl_name**                      Name of the access list

                                     Type: ``string``
   **acl_rules**                     A list of ACL sequence rules as acl_rules='[{"source": "HHHH.HHHH.HHHH", "seq_id": 10}, {"source": "HHHH.HHHH.HHHH", "seq_id": 20}]'

                                     Type: ``array``
   ================================  ======================================================================

