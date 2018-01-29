.. NOTE: This file has been generated automatically, don't manually edit it

configure_anycast_gateway_evpn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**: This configures anycast gateway address. 

.. table::

   ================================  ======================================================================
   Parameter                         Description
   ================================  ======================================================================
   **mgmt_ip**                       The management IP address of the device.

                                     Type: ``string``
   *username*                        The login user name to connect to the device.

                                     Type: ``string``

                                     **Default**: admin
   *password*                        The login password to connect to the device.

                                     Type: ``string``

                                     **Default**: password
   **vlan_id**                       This is a single or a range of VLAN IDs, e.g. 10 or 10-15 or 10,12,13-15.

                                     Type: ``string``
   **anycast_address**               This is a single or list of IPv4 or IPv6 address with subnet/prefix length separated by comma. e.g. 10.10.9.10/22 or 10.10.9.10/22,11.11.10.9/22.

                                     Type: ``string``
   ================================  ======================================================================

