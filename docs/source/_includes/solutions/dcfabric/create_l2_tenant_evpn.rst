.. NOTE: This file has been generated automatically, don't manually edit it

create_l2_tenant_evpn
~~~~~~~~~~~~~~~~~~~~~

**Description**: Create EVPN VXLAN based L2 broadcast domain spanning multiple switches or a vLAG pair 

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
   *vni*                             VNI to be added for EVPN Instance (<NUMBER:1-16777215>) example 1,2,4-6. Valid only on VDX devices.

                                     Type: ``string``
   *vlan_id*                         Single or range of VLAN IDs to be added under the EVPN instance, e.g. 10 or 10-15 or 10,12,13-15. Valid only on SLXOS devices.

                                     Type: ``string``
   *bridge_domain_id*                Single or range of BD IDs to be added under the EVPN instance, e.g. 10 or 10-15 or 10,12,13-15. Valid only on SLXOS devices.

                                     Type: ``string``
   ================================  ======================================================================

