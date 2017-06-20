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
   **vni**                           VNI to be added for EVPN Instance (<NUMBER:1-16777215>) example 1,2,4-6

                                     Type: ``string``
   ================================  ======================================================================

