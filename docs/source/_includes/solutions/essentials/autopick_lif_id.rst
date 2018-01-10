.. NOTE: This file has been generated automatically, don't manually edit it

autopick_lif_id
~~~~~~~~~~~~~~~

**Description**: Returns the next lowest available Logical Interface ID on SLX platforms. 

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
   *length_of_the_range*             Returns the lowest available Single/Range of Logical Interface values. For example 1/1.1 or 1/1.1,1/1.2 or 1.1 or 1.1,1.2.

                                     Type: ``string``

                                     **Default**: 1
   ================================  ======================================================================

