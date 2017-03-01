.. NOTE: This file has been generated automatically, don't manually edit it

delete_ipv4_rule_acl
~~~~~~~~~~~~~~~~~~~~

**Description**: Delete IPv4 ACL rule from an existing IPv4 ACL 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``

                                     **Default**: admin
   *password*                        Login password to connect to the device

                                     Type: ``string``

                                     **Default**: password
   **acl_name**                      Name of the ACL (standard or extended) to delete the rule from

                                     Type: ``string``
   **seq_id**                        Sequence number of the rule to be deleted

                                     Type: ``integer``
   ================================  ======================================================================

