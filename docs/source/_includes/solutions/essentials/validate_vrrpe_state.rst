.. NOTE: This file has been generated automatically, don't manually edit it

validate_vrrpe_state
~~~~~~~~~~~~~~~~~~~~

**Description**: This validates VRRPe state on multiple switches to ensure one VRRPe master. is elected and other switches are in backup mode. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``array``
   *username*                        The login user name to connect to the device.

                                     Type: ``array``
   *password*                        The login password to connect to the device.

                                     Type: ``array``
   **intf_type**                     The interface type, VDX/SLX supports only ve and MLX supports both ve and ethernet.

                                     Choose from:

                                     - ethernet
                                     - ve

                                     **Default**: ve
   **intf_name**                     The name of the interface, for ethernet slot/port, for ve, ve-id like 10,20.

                                     Type: ``string``
   **vrrpe_group**                   The virtual extender group ID. <NUMBER:1-255>

                                     Type: ``string``
   ================================  ======================================================================

