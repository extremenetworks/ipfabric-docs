.. NOTE: This file has been generated automatically, don't manually edit it

configure_cluster
~~~~~~~~~~~~~~~~~

**Description**: Configure cluster 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP of the Device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``

                                     **Default**: admin
   *password*                        Login password to connect to the device

                                     Type: ``string``

                                     **Default**: password
   *cluster_name*                    name of the cluster(MAX 64 Characters)

                                     Type: ``string``
   *cluster_id*                      cluster id (1-65535)

                                     Type: ``integer``
   *peer_ip*                         cluster peer ip address in A.B.C.D format

                                     Type: ``string``
   *peer_interface_type*             cluster peer interface type

                                     Choose from:

                                     - Ethernet
                                     - Port-channel
   *peer_interface_id*               cluster peer interface id

                                     Type: ``string``
   *deploy*                          Configure cluster deploy

                                     Type: ``boolean``

                                     **Default**: True
   *df_hold_time*                    Time in seconds to wait before electing a DF

                                     Type: ``integer``
   *client_isolation_mode*           Configure cluster client isolation mode

                                     Choose from:

                                     - loose
                                     - strict
   *node_id*                         ID of the node values <1-128>.

                                     Type: ``integer``

                                     **Default**: 1
   *control_vlan*                    MCT Control Vlan.

                                     Type: ``integer``

                                     **Default**: 4090
   ================================  ======================================================================

