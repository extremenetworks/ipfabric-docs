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
   **vlan_id**                       Single VLAN or range of VLANs. For example 21 or 21-26

                                     Type: ``string``
   *intf_desc*                       VLAN description.  Same description is used when creating multiple VLANs

                                     Type: ``string``
   ================================  ======================================================================

