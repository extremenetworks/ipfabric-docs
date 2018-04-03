.. NOTE: This file has been generated automatically, don't manually edit it

provision_mct_cluster
~~~~~~~~~~~~~~~~~~~~~

**Description**: This will provision MCT cluster and peers. 

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
   *control_vlan*                    A single control VLAN to be configured for MCT links.

                                     Type: ``string``

                                     **Default**: 4090
   *port_channel_id*                 The port channel interface number <NUMBER:1-6144>.

                                     Type: ``string``

                                     **Default**: 1024
   *mct_interfaces*                  The list of ports that are members of the port channel. 1/13, 1/14.

                                     Type: ``array``
   **interfaces**                    The interfaces to use

                                     Type: ``array``
   *cluster_name*                    The name of the Cluster.

                                     Type: ``string``
   *cluster_peer_ip*                 The Cluster peer IP address in a.b.c.d format.

                                     Type: ``string``
   *node_id*                         The ID of the node values <1-128>.

                                     Type: ``integer``

                                     **Default**: 1
   ================================  ======================================================================

