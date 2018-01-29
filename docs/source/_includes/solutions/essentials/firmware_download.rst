.. NOTE: This file has been generated automatically, don't manually edit it

firmware_download
~~~~~~~~~~~~~~~~~

**Description**: This downloads Firmware and checks the status. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   **host_ip**                       The IP address of the firmware download server.

                                     Type: ``string``
   *proto_username*                  The username to use for firmwaredownload protocol.

                                     Type: ``string``
   *proto_password*                  The password to use for firmwaredownload protocol.

                                     Type: ``string``
   **firmware_path**                 The full firmware path.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``
   *password*                        The login password to connect to the device.

                                     Type: ``string``
   *protocol_type*                   The protocol to use for firmwaredownload.

                                     Choose from:

                                     - scp
                                     - sftp
                                     - ftp

                                     **Default**: scp
   *disruptive_download*             Specifies if download is an ISSU upgrade or a disruptive download.

                                     Type: ``boolean``
   *timeout*                         The action timeout.

                                     Type: ``integer``

                                     **Default**: 1800
   ================================  ======================================================================

