.. NOTE: This file has been generated automatically, don't manually edit it

configure_mac_move_detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configures the switch to enable MAC move detection and set the threshold for the number of MAC moves in time-window to trigger the detection. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the target device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``
   *password*                        THe login password to connect to the device.

                                     Type: ``string``
   **move_threshold**                The MAC move threshold <NUMBER:5-500>.

                                     Type: ``integer``

                                     **Default**: 5
   ================================  ======================================================================

