.. NOTE: This file has been generated automatically, don't manually edit it

delete_vlan_vni_mapping
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This will delete the VLAN to VNI mapping on an overlay gateway, and will also set the VLAN to VNI mapping mode to Auto or Manual. 

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
   *vlan_id*                         A single or a range of VLAN IDs, e.g. 10 or 10-15 or 10,12,13-15. For 802.1Q VLANs ID must be below 4096, for service or transport VFs in a Virtual Fabrics context, and valid range is from 4096 through 8191.

                                     Type: ``string``
   *auto*                            If set to True, this will delete VLAN to VNI auto mapping under the overlay gateway.

                                     Type: ``boolean``
   ================================  ======================================================================

