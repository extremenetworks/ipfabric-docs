.. NOTE: This file has been generated automatically, don't manually edit it

configure_vni_mapping
~~~~~~~~~~~~~~~~~~~~~

**Description**: This configure overlay gateway type and VLAN or Bridge-Domain to VNI mapping 

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
   *vlan_id*                         A single or a range of VLAN IDs, e.g. 10 or 10-15 or 10,12,13-15. For 802.1Q VLANs ID must be below 4096, for service or transport VFs in a Virtual Fabrics context, valid range is from 4096 through 8191.

                                     Type: ``string``
   *vlan_vni*                        A single or a range of VNI <NUMBER:1-16777215> mappings for VLANs, for example 10 or 10-15 or 10,12,13-15. When using ranges, the number of values in a VLAN ID range must correspond to the number of values in a VNI range.

                                     Type: ``string``
   *bridge_domain_id*                A single or range of Bridge-Domain IDs, e.g. 10 or 10-15 or 10,12,13-15. Valid values are from 1 through 4096 on SLX9140,SLX9850,SLX9540 and from 1 through 3566 on SLX9240 .Supported only on SLXOS platforms.

                                     Type: ``string``
   *bridge_domain_vni*               A single or range of VNI <NUMBER:1-16777215> mappings for BDs, for example 10 or 10-15 or 10,12,13-15. When using ranges, the number of values in a Bridge-Domain ID range must correspond to the number of values in a VNI range.

                                     Type: ``string``
   ================================  ======================================================================

