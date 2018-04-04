.. NOTE: This file has been generated automatically, don't manually edit it

delete_vni_mapping
~~~~~~~~~~~~~~~~~~

**Description**: This action will delete the VLAN/Bridge-Domain to VNI and auto mapping under an overlay gateway. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   *auto*                            If set to True, this will delete VLAN to VNI auto mapping under the overlay gateway.

                                     Type: ``boolean``
   *vlan_id*                         A single or a range of VLAN IDs, e.g. 10 or 10-15 or 10,12,13-15. For 802.1Q VLANs ID must be below 4096, for service or transport VFs in a Virtual Fabrics context, and valid range is from 4096 through 8191.

                                     Type: ``string``
   *bridge_domain_id*                A single or range of Bridge-Domain IDs, e.g. 10 or 10-15 or 10,12,13-15. Valid values are from 1 through 4096 on SLX9140,SLX9850,SLX9540 and from 1 through 3566 on SLX9240.

                                     Type: ``string``
   ================================  ======================================================================

