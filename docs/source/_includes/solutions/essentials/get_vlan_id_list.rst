.. NOTE: This file has been generated automatically, don't manually edit it

get_vlan_id_list
~~~~~~~~~~~~~~~~

**Description**: This expands the range for a given list of VLAN IDs or VE IDs 

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
   *vlan_id_list*                    A single or a range of vlans_ids. Returns the list of VLANS IDs in the range. For example 10 or 1-25 or 1-25,26,28. For example, if vlan_id_list='400,401,420-425' returns 400,401,420,421,422,423,424,425.

                                     Type: ``string``
   *ve_id_list*                      A single or a range of ve_ids. Returns the list of VE IDs in the range. For example 10 or 1-25 or 1-25,26,28. For example, if ve_id_list='400,401,420-425' returns 400,401,420,421,422,423,424,425.

                                     Type: ``string``
   ================================  ======================================================================

