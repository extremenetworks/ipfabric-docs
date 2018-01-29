.. NOTE: This file has been generated automatically, don't manually edit it

validate_interface_vlan
~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This validates the port channel or physical interface belonging to the specified VLAN. 

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
   **vlan_id**                       A single VLAN or range of VLANs, for example 2 or 3-9.

                                     Type: ``string``
   **intf_type**                     The interface type.

                                     Choose from:

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ethernet
   **intf_name**                     Interface name, for VDX in 3-tuple format (24/0/1), SLX/NI in 2-tuple format (24/1) or Port-channel number <1-6144>, for NI <1-256>.

                                     Type: ``string``
   *intf_mode*                       The interface mode.

                                     Choose from:

                                     - trunk
                                     - access

                                     **Default**: access
   ================================  ======================================================================

