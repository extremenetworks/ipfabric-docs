.. NOTE: This file has been generated automatically, don't manually edit it

configure_mac_move_detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: Configure the switch to enable MAC move detection and set the threshold for number of MAC moves in time-window to trigger the detection. 

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
   **move_threshold**                MAC move threshold <NUMBER:5-500>

                                     Type: ``integer``

                                     **Default**: 5
   ================================  ======================================================================

