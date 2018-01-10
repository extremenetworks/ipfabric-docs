.. NOTE: This file has been generated automatically, don't manually edit it

validate_vrrpe_state
~~~~~~~~~~~~~~~~~~~~

**Description**: Validate VRRPe state on multiple switches to ensure one VRRPe master is elected and other switches are in backup mode. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``array``
   *username*                        Login user name to connect to the device

                                     Type: ``array``
   *password*                        Login password to connect to the device

                                     Type: ``array``
   **intf_type**                     Interface type, VDX/SLX supports only ve and MLX supports both

                                     Choose from:

                                     - ethernet
                                     - ve

                                     **Default**: ve
   **intf_name**                     name of the interface, for ethernet slot/port, for ve, ve-id like 10,20

                                     Type: ``string``
   **vrrpe_group**                   Virtual extender group ID. <NUMBER:1-255>

                                     Type: ``string``
   ================================  ======================================================================

