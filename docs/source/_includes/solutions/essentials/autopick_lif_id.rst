.. NOTE: This file has been generated automatically, don't manually edit it

autopick_lif_id
~~~~~~~~~~~~~~~

**Description**: This returns the next lowest available Logical Interface ID on SLX platforms. 

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
   *intf_type*                       The interface type.

                                     Choose from:

                                     - ethernet
                                     - port_channel

                                     **Default**: ethernet
   **intf_name**                     The interface Port number or Port channel number. Examples for SLX are 1/13, 1/14.

                                     Type: ``string``
   *length_of_the_range*             This returns the lowest available Single/Range of Logical Interface values. For example 1/1.1 or 1/1.1,1/1.2 or 1.1 or 1.1,1.2.

                                     Type: ``string``

                                     **Default**: 1
   ================================  ======================================================================

