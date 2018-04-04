.. NOTE: This file has been generated automatically, don't manually edit it

ping_vrf_targets
~~~~~~~~~~~~~~~~

**Description**: The PING target IPs from the switch using the specified VRF, uses the default VRF if VRF is not provided. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``
   *password*                        The login password to connect to the device.

                                     Type: ``string``
   **targets**                       One or more comma separated target IP addresses.

                                     Type: ``array``
   *vrf*                             The VRF name.

                                     Type: ``string``

                                     **Default**: default-vrf
   *timeout_value*                   The timeout parameter for the PING command. This specifies the time (in seconds for SLX/NOS and in msec for NI) to wait for a response. For SLX/NOS range is 1 to 60 (default value is 1). For NI minimun range is 50 msecs.

                                     Type: ``integer``
   *count*                           The count parameter for the PING command. This specifies the number of transmissions (PINGs).

                                     Type: ``integer``

                                     **Default**: 4
   *size*                            The datagram size. For SLX and NOS the range is 36 to 9100 (default value is 56). For NI the range is 0 to 31954 (default value is 16)

                                     Type: ``integer``
   ================================  ======================================================================

