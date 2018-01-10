.. NOTE: This file has been generated automatically, don't manually edit it

provision_mct_cluster
~~~~~~~~~~~~~~~~~~~~~

**Description**: Provision MCT cluster and peers. 

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
   *control_vlan*                    Single control VLAN to be configured for MCT links.

                                     Type: ``string``

                                     **Default**: 4090
   *port_channel_id*                 Portchannel interface number <NUMBER:1-6144>

                                     Type: ``string``

                                     **Default**: 1024
   *mct_interfaces*                  List of ports that are members of the port channel. 1/13, 1/14.

                                     Type: ``array``
   **interfaces**                    Interfaces

                                     Type: ``array``
   *cluster_name*                    Name of the Cluster.

                                     Type: ``string``
   *cluster_peer_ip*                 Cluster peer IP address in a.b.c.d format.

                                     Type: ``string``
   *node_id*                         ID of the node values <1-128>.

                                     Type: ``integer``

                                     **Default**: 1
   ================================  ======================================================================

