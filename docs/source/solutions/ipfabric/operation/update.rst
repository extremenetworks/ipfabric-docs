Other features to manage IP Fabric 
==================================

Updating switch credentials and information
-------------------------------------------

A switch is registered in the server using the switch credentials. If the credentials are
changed on the switch, the change must be updated in the Brocade Workflow Composer Server
using the ``bwc ipf inventory update --ip=ip-address`` command.

.. code:: shell

    $ bwc ipf inventory update --ip=10.24.39.216

      <OUTPUT GOES HERE>


Generating a topology map
-------------------------

You can display the fabric topology of an IP Fabric.

1. Enter the bwc show topology format command.

.. todo:: 
    Refer to the bwc show on page 37 command for options available for the bwc show topology
    format command.

.. code:: shell

    $ bwc ipf show topology --format=<file format>

.. note::
    --format=<option> is optional. A PDF file is generated if not format flag is not used.

2. Open the topology file that was generated using the appropriate software.


Confirming IP Fabric details
----------------------------

To check the details of the registered switches in the |bwc| server against the current
switch configuration, use the following commands:


.. code:: shell

    bwc ipf show config bgp [ --fabric=fabric_name ]
    bwc ipf show topology [ --fabric=fabric_name ] [ --format=format ]
    bwc ipf inventory list [ --fabric=fabric_name | --ip=ip-address ]
    bwc ipf inventory show vcs-links [ --fabric=fabric_name ]
    bwc ipf inventory show lldp [ --fabric=fabric_name ]

IP Fabric configuration parameters
----------------------------------

|ipf| has a default set of configuration parameters defined for an IP Fabric. The values
defined in this default configuration parameter set are fixed and cannot be changed. You
can display the values of the parameters using the bwc ipf fabric config show CLI command:

.. code:: shell
    
    $ bwc ipf fabric config show

    <OUTPUT GOES HERE>

If you want a different set of configuration parameters or a configuration with
**unnumbered** for the IP address, you must create a new IP Fabric and define the
values for the configuration parameters. The following parameters can be added
with the bwc ipf fabric config show command:

+------------------------+-------------------------------------------------------------------+
| :anycast_mac:          | A valid MAC address in the format xxxx.xxxx.xxxx or               |
|                        | xx:xx:xx:xx:xx:xx                                                 |
+------------------------+-------------------------------------------------------------------+
| :evpn_enabled:         | Yes or No                                                         |
+------------------------+-------------------------------------------------------------------+
| :bfd_tx:               | An integer from 50 through 30000                                  |
+------------------------+-------------------------------------------------------------------+
| :bfd_rx:               | An integer from 50 through 30000                                  |
+------------------------+-------------------------------------------------------------------+
| :bfd_multiplier:       | An integer from 3 through 50                                      |
+------------------------+-------------------------------------------------------------------+                 
| :bgp_multihop:         | An integer from 1 through 55                                      |
+------------------------+-------------------------------------------------------------------+               
| :max_paths:            | An integer from 1 through 32                                      |
+------------------------+-------------------------------------------------------------------+
| :p2p_link_range:       | **(Required)** a valid IP-network or the word “unnumbered”        |
|                        +-------------------------------------------------------------------+ 
|                        | (case insensitive), based on what kind of BGP peers               |
|                        +-------------------------------------------------------------------+
|                        | connectivity you want, IP numbered or unnumbered. (Refer          |
|                        +-------------------------------------------------------------------+
|                        | overview section for details).                                    |
+------------------------+-------------------------------------------------------------------+
| :loopback_ip_range:    | **(Required)** A valid IP-network, for example,172.32.254.0/24    |
+------------------------+-------------------------------------------------------------------+                    
| :leaf_asn_block:       |  **(Required)** A single value or range from 1 through 4294967295 |
+------------------------+-------------------------------------------------------------------+                 
| :spine_asn_block:      | **(Required)** A single value or range from 1 through 4294967295  |
+------------------------+-------------------------------------------------------------------+                  
| :loopback_port_number: | **(Required)** A number from 1 through 255                        |
+------------------------+-------------------------------------------------------------------+                       
| :allowas_in:           | A number from 1 through 10                                        |
+------------------------+-------------------------------------------------------------------+

Note, however, that the required parameters must be added to the new configuration. The other
parameters are not required, but if you do not add them, Brocade Workflow Composer will use
the values from the default configuration.

Once the required parameters are added to the fabric, they cannot be modified or deleted.
Also, if incorrect values are added to the configuration, the configuration cannot be 
modified. You must create a new fabric and define a new configuration.

Creating a new IP Fabric with user-defined IP configurations
------------------------------------------------------------

1. Use the bwc ipf fabric add command to create a new fabric configuration. For example,
   the following command creates a new IP Fabric called **user_fab**.

.. todo::
    UPDATE OUTPUT

.. code:: shell

    $ bwc ipf fabric add --fabric=user_fab
    Successfully added the fabric. Object details:
    Fabric: user_fab

2. Use the bwc ipf fabric config add command to add configuration values.

.. code:: shell
   
    $ bwc ipf fabric config add p2p_link_range 10.10.10.0/23 --fabric=user_fab
    p2p_link_range: 10.10.10.0/23
    $ bwc ipf fabric config add spine_asn_block 64512-64999 --fabric=user_fab
    spine_asn_block: 64512-64999
    $ bwc ipf fabric config add leaf_asn_block 65000-65534 --fabric=user_fab
    leaf_asn_block: 65000-65534
    $ bwc ipf fabric config add loopback_ip_range 172.32.254.0/24 --fabric=user_fab
    loopback_ip_range: 172.32.254.0/24
    $ bwc ipf fabric config add loopback_port_number '1' --fabric=user_fab
    loopback_port_number: '1'
    $ bwc ipf fabric config add bfd_multiplier 10 --fabric=new_fab
    bfd_multiplier: '10'
    $ bwc ipf fabric config add bfd_rx 888 --fabric=user_fab
    'bfd_rx': '888'
    $ bwc ipf fabric config add bfd_tx 888 --fabric=user_fab
    'bfd_tx ': '888'
    $ bwc ipf fabric config add allowas_in 7 --fabric=user_fab
    allowas_in: '7

3. Check the parameter values before saving the configuration.
4. Use the bwc ipf fabric config show command to display the fabric details added in step 2.

.. code:: shell

    $ bwc ipf fabric config show --fabric=user_fab
    fabric_name: user_fab
    fabric_settings:
    'bfd_multiplier': '10'
    'bfd_rx': '888'
    'bfd_tx': '888'
    leaf_asn_block: 65000-65534
    loopback_ip_range: 172.32.254.0/24
    loopback_port_number: '1'
    p2p_link_range: 10.10.10.0/23
    spine_asn_block: 64512-64999
    allowas_in: '7'

Use :command:`--fabric=<fabric name>` parameter to display details for a specific fabric.
