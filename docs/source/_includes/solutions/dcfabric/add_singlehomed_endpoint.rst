.. NOTE: This file has been generated automatically, don't manually edit it

add_singlehomed_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Create VLAN, configure interface as Access or Trunk, and validate interface state. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       Management IP address of the target device

                                     Type: ``string``
   *username*                        Login user name to connect to the device

                                     Type: ``string``

                                     **Default**: admin
   *password*                        Login password to connect to the device

                                     Type: ``string``

                                     **Default**: password
   **vlan_id**                       Single or range of VLANs

                                     Type: ``string``
   **intf_type**                     Interface type

                                     Choose from:

                                     - ethernet
                                     - gigabitethernet
                                     - tengigabitethernet
                                     - fortygigabitethernet
                                     - hundredgigabitethernet
                                     - port_channel
                                     - ve
                                     - loopback

                                     **Default**: tengigabitethernet
   **intf_name**                     Single or list of ports that are members of the port channel. Examples for VDX, SLX are  24/0/1, 24/0/2 or 1/13, 1/14

                                     Type: ``string``
   *enabled*                         Select true to enable the port, false to disable the port

                                     Type: ``boolean``

                                     **Default**: True
   **switchport_mode**               Switch port mode

                                     Choose from:

                                     - access
                                     - trunk

                                     **Default**: access
   *intf_desc*                       Interface description

                                     Type: ``string``
   ================================  ======================================================================

