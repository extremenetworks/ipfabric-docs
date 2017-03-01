.. NOTE: This file has been generated automatically, don't manually edit it

validate_L2_port_channel_state
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Validate the port channel state by verifying the sync state of all member ports is 1. 

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
   **port_channel_id**               Portchannel interface number. <NUMBER:1-6144>

                                     Type: ``string``
   ================================  ======================================================================

