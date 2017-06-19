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

                                     **Default**: ['admin']
   *password*                        Login password to connect to the device

                                     Type: ``array``

                                     **Default**: ['password']
   **vlan_id**                       VLAN ID. <NUMBER:1-4090/8191>, can be greater than 4090 only if VF is enabled.

                                     Type: ``string``
   **vrrpe_group**                   Virtual extender group ID. <NUMBER:1-255>

                                     Type: ``string``
   ================================  ======================================================================

