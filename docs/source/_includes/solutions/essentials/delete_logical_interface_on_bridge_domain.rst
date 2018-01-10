.. NOTE: This file has been generated automatically, don't manually edit it

delete_logical_interface_on_bridge_domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Delete logical interfaces under a bridge domain. 

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
   **bridge_domain_id**              Bridge-domain IDs. <1-4096> on SLX9140,SLX9850 and <1-3566> on SLX9240.

                                     Type: ``string``
   *bridge_domain_service_type*      bridge domain service type. `p2p` is not supported on SLX9140 and SLX9240 platforms.

                                     Choose from:

                                     - p2mp
                                     - p2p

                                     **Default**: p2mp
   *intf_type*                       Interface type to be deleted from the bridge_domain.

                                     Choose from:

                                     - ethernet
                                     - port_channel
                                     - both

                                     **Default**: ethernet
   *logical_interface_number*        Single/List of logical Interface Number for physical port or port channel separated by comma. E.g:0/1.1,10.1,0/20.1 or 7.1. 1. If intf_type is 'both'  --> all the LIFs {ethernet & port_channel} will be deleted on the BD. 2. If intf_type is 'ethernet' and logical_interface_number is not passed --> all the ethernet LIFs will be deleted on the BD. 3. If intf_type is 'port_channel' and logical_interface_number is not passed --> all the port_channel LIFs will be deleted on the BD. 4. If intf_type is 'port_channel or ethernet' and logical_interface_number is passed --> port_channel/ethernet LIFs passed will be deleted on the BD.

                                     Type: ``string``
   ================================  ======================================================================

