.. NOTE: This file has been generated automatically, don't manually edit it

configure_logical_interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This creates the logical interface under the physical/port-channel interface and untag/tag vlan. 

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
   *intf_type*                       The interface type.

                                     Choose from:

                                     - ethernet
                                     - port_channel

                                     **Default**: ethernet
   **intf_name**                     The interface Port number or Port channel number. Examples for SLX are 1/13, 1/14.

                                     Type: ``string``
   **logical_interface_number**      The interface name of the physical port or port channel number. E.g:0/1.1 or 7.1. Format for the logical interfaces is <physical/port-channel number>.<number>.

                                     Type: ``string``
   *vlan_type*                       The VLAN tag type.

                                     Choose from:

                                     - untagged
                                     - tagged
                                     - double_tagged
   *vlan_id*                         A single or a list of VLANIDs. VLAN ID range is 1-4090. If `vlan_type` is `tagged`, `vlan_id` needs to be specified. If `vlan_type` is `double_tagged`, `vlan_id` needs to be specified and is interpreted as outer_vlan_id.. If `vlan_type` is `untagged`, `vlan_id` needs to be specified. Valid only on SLX9850,SLX9540.

                                     Type: ``string``
   *inner_vlan_id*                   This configures a single VLAN or a list of Inner VLANs for the logical interface. Valid vlan id range <1-4090>. Valid only if `vlan_type` is `double_tagged`.

                                     Type: ``string``
   ================================  ======================================================================

