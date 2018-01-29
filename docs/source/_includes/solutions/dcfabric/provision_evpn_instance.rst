.. NOTE: This file has been generated automatically, don't manually edit it

provision_evpn_instance
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This will provision overlay EVPN Instance on a switch or a vLAG pair, also configure overlay gateway and advertise the overlay gateway through BGP. 

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
   *rbridge_id*                      The RBridge ID of the VDX switch. This parameter is only applicable for VDX switches.

                                     Type: ``string``
   **evi_name**                      The EVI instance name.

                                     Type: ``string``
   **vtep_name**                     The Overlay gateway name.

                                     Type: ``string``
   **vtep_loopback_id**              The VTEP loopback ID <NUMBER:1-255>.

                                     Type: ``integer``
   **mac_move_threshold**            The MAC move threshold <NUMBER:5-500>.

                                     Type: ``integer``

                                     **Default**: 5
   *vni_auto_map*                    This will enable or disable auto-mapping of VLANs/Bridge-Domains to VNIs.

                                     Type: ``boolean``

                                     **Default**: True
   **principal_ip**                  The principal IP address of the target device.

                                     Type: ``string``
   **mct_interfaces**                The list of ports that are members of the port channel, 1/13, 1/14.

                                     Type: ``array``
   **node_id**                       The ID of the node values <1-128>.

                                     Type: ``integer``

                                     **Default**: 1
   *evpn*                            The EVPN enabled fabric.

                                     Type: ``boolean``

                                     **Default**: True
   *is_principal*                    The Principal Node of Cluster.

                                     Type: ``boolean``
   ================================  ======================================================================

