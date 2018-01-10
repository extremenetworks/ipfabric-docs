.. NOTE: This file has been generated automatically, don't manually edit it

firmware_download
~~~~~~~~~~~~~~~~~

**Description**: Download Firmware and Check the status 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   **host_ip**                       IP address of the firmware download server

                                     Type: ``string``
   *proto_username*                  Username to use for firmwaredownload protocol

                                     Type: ``string``
   *proto_password*                  Password to use for firmwaredownload protocol

                                     Type: ``string``
   **firmware_path**                 Full firmware path.

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``
   *password*                        Login password to connect to the device

                                     Type: ``string``
   *protocol_type*                   Protocol to use for firmwaredownload

                                     Choose from:

                                     - scp
                                     - sftp
                                     - ftp

                                     **Default**: scp
   *disruptive_download*             Should the download be ISSU upgrade or disruptive download

                                     Type: ``boolean``
   *timeout*                         Action timeout .

                                     Type: ``integer``

                                     **Default**: 1800
   ================================  ======================================================================

