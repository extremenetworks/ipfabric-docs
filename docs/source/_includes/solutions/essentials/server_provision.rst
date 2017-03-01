.. NOTE: This file has been generated automatically, don't manually edit it

server_provision
~~~~~~~~~~~~~~~~

**Description**: Configure vlan,enable the switch port mode and configure the port speed on switch 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Host to configure

                                     Type: ``string``
   *username*                        User name to ssh into host

                                     Type: ``string``

                                     **Default**: admin
   *password*                        Password to ssh into host

                                     Type: ``string``

                                     **Default**: password
   **vlan_id**                       single vlan or range of vlans

                                     Type: ``string``
   **intf_type**                     Interface type gigabitethernet or tengigabitethernet or port_channel

                                     Choose from:

                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ve
                                     - loopback

                                     **Default**: tengigabitethernet
   **intf_name**                     Single interface name/range of interface name physical interface/port-channel

                                     Type: ``string``
   *enabled*                         Set to true to enable port, false to disable port

                                     Type: ``boolean``

                                     **Default**: True
   **switchport_mode**               Specify the switch port mode

                                     Choose from:

                                     - access
                                     - trunk

                                     **Default**: access
   *intf_desc*                       Interface description name

                                     Type: ``string``
   ================================  ======================================================================

