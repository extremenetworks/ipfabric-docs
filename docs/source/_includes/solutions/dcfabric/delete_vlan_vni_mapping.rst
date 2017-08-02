.. NOTE: This file has been generated automatically, don't manually edit it

delete_vlan_vni_mapping
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Delete VLAN to VNI mapping on an overlay gateway, also set the VLAN to VNI mapping mode to Auto or Manual. 

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
   *vlan_id*                         Single or range of VLAN IDs, e.g. 10 or 10-15 or 10,12,13-15.  For 802.1Q VLANs ID must be below 4096, for service or transport VFs in a Virtual Fabrics context, valid range is from 4096 through 8191.

                                     Type: ``string``
   *auto*                            If set to True, delete vlan to vni auto mapping under overlay gateway

                                     Type: ``boolean``
   ================================  ======================================================================

