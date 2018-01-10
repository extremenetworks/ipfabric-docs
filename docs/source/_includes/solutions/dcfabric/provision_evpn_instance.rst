.. NOTE: This file has been generated automatically, don't manually edit it

provision_evpn_instance
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Provision overlay EVPN Instance on a switch or a vLAG pair, also configure overlay gateway and advertise the overlay gateway through BGP. 

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
   *rbridge_id*                      RBridge ID of the VDX switch.  This parameter is only applicable for VDX switches.

                                     Type: ``string``
   **evi_name**                      EVI instance name

                                     Type: ``string``
   **vtep_name**                     Overlay gateway name

                                     Type: ``string``
   **vtep_loopback_id**              VTEP loopback ID <NUMBER:1-255>

                                     Type: ``integer``
   **mac_move_threshold**            MAC move threshold <NUMBER:5-500>

                                     Type: ``integer``

                                     **Default**: 5
   *vni_auto_map*                    Enable or disable auto-mapping of VLANs/Bridge-Domains to VNIs.

                                     Type: ``boolean``

                                     **Default**: True
   **principal_ip**                  Principal IP address of the target device

                                     Type: ``string``
   **mct_interfaces**                List of ports that are members of the port channel. 1/13, 1/14.

                                     Type: ``array``
   **node_id**                       ID of the node values <1-128>.

                                     Type: ``integer``

                                     **Default**: 1
   *evpn*                            EVPN enabled fabric.

                                     Type: ``boolean``

                                     **Default**: True
   *is_principal*                    Principal Node of Cluster.

                                     Type: ``boolean``
   ================================  ======================================================================

