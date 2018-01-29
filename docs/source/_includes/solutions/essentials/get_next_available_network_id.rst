.. NOTE: This file has been generated automatically, don't manually edit it

get_next_available_network_id
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This returns the next lowest available VF ID (4096-8191) on VDX platform and bridge-domain ID on SLX platforms. 

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
   *length_of_the_range*             This returns the lowest available Single/Range of VF values. Max Length = 4095. For example 10 or 1-25 or 1-25,26,28. For example, if length_of_the_range=2, returns 4096,4097. length_of_the_range=1-3, returns 4096,4097,4098.

                                     Type: ``string``

                                     **Default**: 1
   ================================  ======================================================================

