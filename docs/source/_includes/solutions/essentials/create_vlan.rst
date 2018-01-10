.. NOTE: This file has been generated automatically, don't manually edit it

create_vlan
~~~~~~~~~~~

**Description**: Create a single or range of VLANs on a switch 

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
   **vlan_id**                       Single VLAN ID or range of VLAN IDs. For example 21 or 21-26 or 10,13-14,89-91

                                     Type: ``string``
   *vlan_desc*                       VLAN description. Same description is used when creating multiple VLANs

                                     Type: ``string``
   ================================  ======================================================================

