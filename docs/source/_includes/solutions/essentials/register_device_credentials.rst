.. NOTE: This file has been generated automatically, don't manually edit it

register_device_credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Add/Update the device credentials into st2store for NE pack actions. SNMP credentials are applicable only to NetIron(NI) based devices (MLX, CER, CES) and 'USER.DEFAULT'. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device or "USER.DEFAULT" "USER.DEFAULT" is specified to give a common set of credentials across multiple devices.

                                     Type: ``string``

                                     **Default**: USER.DEFAULT
   **username**                      SSH login user name to connect to the device.

                                     Type: ``string``
   **password**                      SSH login password to connect to the device.

                                     Type: ``string``
   *enable_password*                 password to enter into config enable mode. This applies to few platforms like MLX, CER, CES and special case like USER.DEFAULT if applicable.

                                     Type: ``string``
   *snmp_port*                       SNMP port on target device. This is optional for devices where SNMP port can be configurable.

                                     Type: ``integer``

                                     **Default**: 161
   *snmp_version*                    SNMP version used to connect to device. This is mandatory parameter for NI based devices and USER.DEFAULT.

                                     Choose from:

                                     - v2
                                     - v3
                                     - None

                                     **Default**: None
   *snmp_v2c*                        SNMPv2 community string. This is mandatory in snmp_version value is "v2".

                                     Type: ``string``
   *snmpv3_user*                     SNMPv3 User. This is mandatory if snmp_version is "v3".

                                     Type: ``string``

                                     **Default**: None
   *snmpv3_auth*                     SNMPv3 authentication protocol. This is mandatory if snmp_version is "v3".

                                     Choose from:

                                     - md5
                                     - sha
                                     - noauth

                                     **Default**: noauth
   *auth_pass*                       Authkey pass phrase configured on snmp agent. This is mandatory if snmpv3_auth is "md5" or "sha".

                                     Type: ``string``
   *snmpv3_priv*                     SNMPv3 privacy protocol. This is mandatory if snmp_version is "v3". "aes128" is equivalent to "aes" in NI snmp configuration.

                                     Choose from:

                                     - aes128
                                     - des
                                     - nopriv

                                     **Default**: nopriv
   *priv_pass*                       privacy pass phrase configured on snmp agent. This is mandatory if snmpv3_priv is "aes128" or "des".

                                     Type: ``string``
   ================================  ======================================================================

