.. NOTE: This file has been generated automatically, don't manually edit it

configure_vlan_vni_mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure overlay gateway type and VLAN to VNI mapping 

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
   **vlan_id**                       Single or range of VLAN IDs, e.g. 10 or 10-15 or 10,12,13-15.  For 802.1Q VLANs ID must be below 4096, for service or transport VFs in a Virtual Fabrics context, valid range is from 4096 through 8191.

                                     Type: ``string``
   **vni**                           Single or range of VNI <NUMBER:1-16777215> mappings for VLANs, for example 10 or 10-15 or 10,12,13-15. When using ranges, the number of values in a VLAN ID range must correspond to the number of values in a VNI range.

                                     Type: ``string``
   ================================  ======================================================================

