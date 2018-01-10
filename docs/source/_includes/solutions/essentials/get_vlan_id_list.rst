.. NOTE: This file has been generated automatically, don't manually edit it

get_vlan_id_list
~~~~~~~~~~~~~~~~

**Description**: Expand the range for given list of Vlans IDs 

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
   **vlan_id_list**                  Single/Range of vlans_ids.Returns the list of VLANS IDs in the range. For example 10 or 1-25 or 1-25,26,28. For example, if vlan_id_list='400,401,420-425' returns 400,401,420,421,422,423,424,425.

                                     Type: ``string``
   ================================  ======================================================================

