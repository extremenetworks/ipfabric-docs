.. NOTE: This file has been generated automatically, don't manually edit it

configure_mac_group
~~~~~~~~~~~~~~~~~~~

**Description**: Create a new Mac group on a device and configure member mac addresses. 

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
   **mac_group_id**                  MAC group ID <NUMBER:1,500>

                                     Type: ``integer``
   *mac_address*                     Single or comma seperated list of MAC addresses to be part of the MAC group. MAC address in HHHH.HHHH.HHHH format.

                                     Type: ``array``
   ================================  ======================================================================

