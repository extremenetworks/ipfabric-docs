.. NOTE: This file has been generated automatically, don't manually edit it

get-flow-trace-ip-fabric
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This traces the data path through the IP Fabric network and checks the integrity of the route-programming on the devices along the data path. This can be used to trace the path of the packet flow in IP fabric topology as well as in identifying the point of failure when a flow is dropped and is not reaching the destination. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          The management IP address of the target device.

                                     Type: ``string``
   *username*                        The username to SSH into the host.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The password for login into switch.

                                     Type: ``string``

                                     **Default**: password
   **fabric**                        The Fabric name.

                                     Type: ``string``
   **mac_da**                        The destination MAC address of the flow (myDA in l3fwd) in xxxx.xxxx.xxxx format.

                                     Type: ``string``
   **mac_sa**                        The source MAC address of the flow in xxxx.xxxx.xxxx (0010.9400.0008) format.

                                     Type: ``string``
   **dip**                           The destination IP of the flow in A.B.C.D/E format.

                                     Type: ``string``
   **sip**                           The source IP of the flow in A.B.C.D/E format.

                                     Type: ``string``
   **vlan**                          The VLAN ID.

                                     Type: ``string``
   *interface*                       The ingress interface name in slot/port.

                                     Type: ``string``
   *verbose*                         This enables the verbose mode for the script to log more details.

                                     Type: ``boolean``
   ================================  ======================================================================

