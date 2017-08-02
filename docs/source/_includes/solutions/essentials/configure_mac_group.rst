.. NOTE: This file has been generated automatically, don't manually edit it

configure_mac_group
~~~~~~~~~~~~~~~~~~~

**Description**: Configure Mac Group and the mac addresses. 

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
   **mac_group_id**                  Mac Group id. Valid Range [1,500]

                                     Type: ``integer``
   *mac_address*                     Single/list of Mac addresses to be part of the mac group. Mac Address -> HHHH.HHHH.HHHH format

                                     Type: ``array``
   ================================  ======================================================================

