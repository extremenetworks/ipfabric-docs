.. NOTE: This file has been generated automatically, don't manually edit it

register_device_credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This Add/Update the device credentials into st2store for NE pack actions. SNMP credentials are applicable only to NetIron(NI) based devices (MLX, CER, CES). 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   **username**                      The SSH login user name to connect to the device.

                                     Type: ``string``
   **password**                      The SSH login password to connect to the device.

                                     Type: ``string``
   *enable_password*                 The password to enter into config enable mode. This applies to few platforms like MLX, CER, CES if applicable.

                                     Type: ``string``
   *snmp_port*                       The SNMP port on the target device. This is optional for devices where SNMP port is configurable.

                                     Type: ``integer``

                                     **Default**: 161
   *snmp_version*                    The SNMP version used to connect to the device. This is mandatory parameter for NI based devices.

                                     Choose from:

                                     - v2
                                     - v3
                                     - None

                                     **Default**: None
   *snmp_v2c*                        The SNMPv2 community string. This is mandatory in snmp_version value is "v2".

                                     Type: ``string``
   *snmpv3_user*                     The SNMPv3 User. This is mandatory if snmp_version is "v3".

                                     Type: ``string``

                                     **Default**: None
   *snmpv3_auth*                     The SNMPv3 authentication protocol. This is mandatory if snmp_version is "v3".

                                     Choose from:

                                     - md5
                                     - sha
                                     - noauth

                                     **Default**: noauth
   *auth_pass*                       The Authkey pass phrase configured on the SNMP agent. This is mandatory if snmpv3_auth is "md5" or "sha".

                                     Type: ``string``
   *snmpv3_priv*                     The SNMPv3 privacy protocol. This is mandatory if snmp_version is "v3". "aes128" is equivalent to "aes" in NI SNMP configuration.

                                     Choose from:

                                     - aes128
                                     - des
                                     - nopriv

                                     **Default**: nopriv
   *priv_pass*                       The privacy pass phrase configured on the SNMP agent. This is mandatory if snmpv3_priv is "aes128" or "des".

                                     Type: ``string``
   *rest_protocol*                   The protocol used for REST requests. This applies to REST platforms such as SLX, VDX if applicable.

                                     Choose from:

                                     - http
                                     - https

                                     **Default**: http
   ================================  ======================================================================

