.. NOTE: This file has been generated automatically, don't manually edit it

configure_logical_interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Create logical interface under the physical/port-channel interface and untag/tag vlan. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``
   *password*                        Login password to connect to the device

                                     Type: ``string``
   *intf_type*                       Interface type

                                     Choose from:

                                     - ethernet
                                     - port_channel

                                     **Default**: ethernet
   **intf_name**                     Interface Port number or Port channel number. Examples for SLX are 1/13, 1/14

                                     Type: ``string``
   **logical_interface_number**      Interface name physical port or port channel number. E.g:0/1.1 or 7.1

                                     Type: ``string``
   *vlan_type*                       vlan tag type

                                     Choose from:

                                     - untagged
                                     - tagged
                                     - double_tagged
   *vlan_id*                         Single/List of VLANIDs. Vlan id range <1-4090>

                                     Type: ``string``
   *inner_vlan_id*                   Configure Single/List of Inner VLAN for the logical interface.vlan id range <1-4090>

                                     Type: ``string``
   ================================  ======================================================================

