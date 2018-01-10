.. NOTE: This file has been generated automatically, don't manually edit it

ping_vrf_targets
~~~~~~~~~~~~~~~~

**Description**: Ping target IPs from the switch using the specified VRF, uses the default VRF if VRF is not provided 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``
   *password*                        Login password to connect to the device

                                     Type: ``string``
   **targets**                       One or more comma separated target IP addresses

                                     Type: ``array``
   *vrf*                             VRF name

                                     Type: ``string``

                                     **Default**: default-vrf
   *timeout_value*                   Timeout parameter for the ping command. Specifies the time (in seconds) to wait for a response. Default value 1 sec for SLX/VDX and 50 sec for MLX.

                                     Type: ``integer``
   *count*                           Count parameter for the ping command. Specifies the number of transmissions (pings).

                                     Type: ``integer``

                                     **Default**: 4
   *size*                            Datagram size

                                     Type: ``integer``

                                     **Default**: 56
   ================================  ======================================================================

