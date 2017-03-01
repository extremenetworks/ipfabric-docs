.. NOTE: This file has been generated automatically, don't manually edit it

delete_ve
~~~~~~~~~

**Description**: Delete a VE on multiple switches 

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
   *rbridge_id*                      RBridge IDs of the VDX switches, for example 51 or 51,52. This parameter is only applicable for VDX switches.

                                     Type: ``array``
   **vlan_id**                       VLAN ID. Allowed range for SLX <NUMBER:1-4090>, for VDX <NUMBER:1-4090/8191> greater than 4090 only if VF is enabled

                                     Type: ``string``
   ================================  ======================================================================

