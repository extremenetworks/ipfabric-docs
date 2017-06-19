.. NOTE: This file has been generated automatically, don't manually edit it

get-flow-trace-ip-fabric
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Traces the data path through the IP Fabric network and checks the integrity of the route-programming on the devices along the data path.  Can be used to trace the path of the packet flow in IP fabric topology as well as in identifying the point of failure when a flow is dropped and not reaching the destination. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **host**                          Management IP address of the target device

                                     Type: ``string``
   *username*                        username to ssh into host

                                     Type: ``string``

                                     **Default**: admin
   *password*                        password for login into switch

                                     Type: ``string``

                                     **Default**: password
   **fabric**                        Fabric name

                                     Type: ``string``
   **mac_da**                        Destination MAC address of the flow (myDA in l3fwd) in xxxx.xxxx.xxxx format

                                     Type: ``string``
   **mac_sa**                        Source MAC address of the flow in xxxx.xxxx.xxxx (0010.9400.0008) format

                                     Type: ``string``
   **dip**                           Destination IP of the flow in A.B.C.D/E format

                                     Type: ``string``
   **sip**                           Source IP of the flow in A.B.C.D/E format

                                     Type: ``string``
   **vlan**                          VLAN ID

                                     Type: ``string``
   *interface*                       Ingress interface name in slot/port

                                     Type: ``string``
   *verbose*                         Enables the verbose mode for the script to log more details

                                     Type: ``boolean``
   ================================  ======================================================================

