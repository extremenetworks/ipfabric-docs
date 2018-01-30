.. NOTE: This file has been generated automatically, don't manually edit it

configure_cluster
~~~~~~~~~~~~~~~~~

**Description**: This configure cluster. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   *cluster_name*                    The name of the cluster (MAX 64 Characters).

                                     Type: ``string``
   *cluster_id*                      The cluster id (1-65535).

                                     Type: ``integer``
   *peer_ip*                         The cluster peer ip address in A.B.C.D format.

                                     Type: ``string``
   *peer_interface_type*             The cluster peer interface type.

                                     Choose from:

                                     - Ethernet
                                     - Port-channel
   *peer_interface_id*               The cluster peer interface id.

                                     Type: ``string``
   *deploy*                          This configure cluster deploy.

                                     Type: ``boolean``

                                     **Default**: True
   *df_hold_time*                    The time in seconds to wait before electing a DF.

                                     Type: ``integer``
   *client_isolation_mode*           This configure cluster client isolation mode.

                                     Choose from:

                                     - loose
                                     - strict
   *node_id*                         The ID of the node values <1-128>.

                                     Type: ``integer``

                                     **Default**: 1
   *control_vlan*                    The MCT Control VLAN.

                                     Type: ``integer``

                                     **Default**: 4090
   ================================  ======================================================================

