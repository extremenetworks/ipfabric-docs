.. NOTE: This file has been generated automatically, don't manually edit it

create_l2_tenant_evpn
~~~~~~~~~~~~~~~~~~~~~

**Description**: This will create EVPN VXLAN based L2 broadcast domain spanning multiple switches. or a vLAG pair 

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
   *vni*                             The VNI to be added for EVPN Instance (<NUMBER:1-16777215>) example 1,2,4-6. Valid only on VDX devices.

                                     Type: ``string``
   *vlan_id*                         A single or a range of VLAN IDs to be added under the EVPN instance, e.g. 10 or 10-15 or 10,12,13-15. Valid only on SLXOS devices.

                                     Type: ``string``
   *bridge_domain_id*                A single or a range of BD IDs to be added under the EVPN instance, e.g. 10 or 10-15 or 10,12,13-15. Valid only on SLXOS devices.

                                     Type: ``string``
   ================================  ======================================================================

