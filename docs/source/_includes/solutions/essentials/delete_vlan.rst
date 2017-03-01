.. NOTE: This file has been generated automatically, don't manually edit it

delete_vlan
~~~~~~~~~~~

**Description**: Delete one or more VLANs on a switch 

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
   **vlan_id**                       VLAN ID, can be single or range of VLANs. For example 5 or 5-9

                                     Type: ``string``
   ================================  ======================================================================

