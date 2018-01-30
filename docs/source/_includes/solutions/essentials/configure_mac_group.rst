.. NOTE: This file has been generated automatically, don't manually edit it

configure_mac_group
~~~~~~~~~~~~~~~~~~~

**Description**: This creates a new MAC group on a device and configures the member MAC addresses. 

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
   **mac_group_id**                  The MAC group ID <NUMBER:1,500>.

                                     Type: ``integer``
   *mac_address*                     A single or comma seperated list of MAC addresses to be part of the MAC group. The MAC address is in HHHH.HHHH.HHHH format.

                                     Type: ``array``
   ================================  ======================================================================

