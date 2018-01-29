.. NOTE: This file has been generated automatically, don't manually edit it

delete_ipv6_rule_acl
~~~~~~~~~~~~~~~~~~~~

**Description**: This deletes the IPv6 ACL rule from an existing IPv6 ACL. 

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
   **acl_name**                      The name of the ACL (standard or extended) to delete the rule from required-by:- [All] accepted-by:- [SLX, NOS, MLX].

                                     Type: ``string``
   **seq_id**                        The sequence numbers of rules to be deleted. { seq id | all | comman and hyphen separated seq ids } Example:- { 10 | all | 1,2,3-10,20,35-  } Note:- "-" separated values will look for seq_ids in range including the values and 35- is equal to starting from 35 delete all configured sequence ids, including 35. required-by:- [None] accepted-by:- [SLX, NOS, MLX]

                                     Type: ``string``
   ================================  ======================================================================

