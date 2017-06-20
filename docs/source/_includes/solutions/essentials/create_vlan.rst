.. NOTE: This file has been generated automatically, don't manually edit it

create_vlan
~~~~~~~~~~~

**Description**: Create a VLANs and provide VLAN descriptions 

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
   **vlan_id**                       Single VLAN/range of VLANS/batch wise values. For example 21 or 21-26 or 10,13-14,89-91

                                     Type: ``string``
   *vlan_desc*                       VLAN description without any space. Same description is used when creating multiple VLANs

                                     Type: ``string``
   ================================  ======================================================================

