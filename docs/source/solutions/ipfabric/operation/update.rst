Managing IP Fabrics 
===================

Updating switch credentials and information
-------------------------------------------

A switch is registered to the server using the switch credentials. If the credentials are
changed on the switch, the change must be updated in the |bwc| server
using the ``bwc ipf inventory update --host=<ip_address>`` command.

.. code:: shell

    $ bwc ipf inventory update --host=10.24.39.225  --user=lab123 --passwd=123lab

      Inventory Update
      +--------------+---------+------------+----------+------+------+-------+---------+
      | IP           | Model   | Rbridge-Id | Firmware | Name | Role |   ASN | Fabric  |
      +--------------+---------+------------+----------+------+------+-------+---------+
      | 10.24.39.225 | VDX6740 |        225 | 7.1.0    | sw0  | Leaf | 65000 | default |
      +--------------+---------+------------+----------+------+------+-------+---------+


Generating a topology map
-------------------------

You can display the fabric topology of an IP Fabric.

1. Enter the ``bwc ipf show topology fabric=<fabric_name>`` command.

Refer the :doc:`ipf CLI <../ipf_cli/basic_cli>` page for options available for the
``bwc ipf show topology`` command.

.. code:: shell

    $ bwc ipf show topology fabric=default --format=pdf --render_dir=/tmp

      Topology map generated: /tmp/topology_default_20160811-020715.pdf

.. note::
   "- -format=<option>" and "- -render_dir=<file location>" is optional. By default a PDF
   file and a dot file is generated in *tmp* folder if format flag and render_dir
   flags are not used.

2. Open the topology file that was generated using appropriate software.


Confirming IP Fabric details
----------------------------

To check the details of the registered switches in the |bwc| server against the current
switch configuration, use following commands:


.. code:: shell

    bwc ipf show config bgp fabric=<fabric_name>
    bwc ipf show topology fabric=<fabric_name> [ --format=<format> ] [--render_dir=<file location>]
    bwc ipf inventory list --fabric=<fabric_name> | --host=<switch_ip>
    bwc ipf inventory show vcs links fabric=<fabric_name>
    bwc ipf inventory show lldp fabric=<fabric_name>

.. _ip_fabric_parameters:

IP Fabric configuration parameters
----------------------------------

|ipf| has a default set of configuration parameters defined for an IP Fabric. The values
defined in this default configuration parameter set are fixed and cannot be changed. You
can display the values of the parameters using the ``bwc ipf fabric config show`` CLI
command:

.. code:: shell
    
    $ bwc ipf fabric config show fabric=default

      +----------------------+-----------------+
      | Fabric Name          | default         |
      | bgp_multihop         | 5               |
      | spine_asn_block      | 64512-64999     |
      | leaf_asn_block       | 65000-65534     |
      | max_paths            | 8               |
      | loopback_port_number | 1               |
      | evpn_enabled         | Yes             |
      | allowas_in           | 5               |
      | bfd_multiplier       | 3               |
      | p2p_link_range       | 10.10.10.0/23   |
      | bfd_tx               | 300             |
      | anycast_mac          | aabb.ccdd.eeff  |
      | loopback_ip_range    | 172.32.254.0/24 |
      | bfd_rx               | 300             |
      +----------------------+-----------------+


If you want a different set of configuration parameters or a configuration with
**unnumbered** for the IP address, you must create a new IP Fabric and define the
values for the configuration parameters. The following parameters can be added
with the ``bwc ipf fabric config set fabric=<fabric_name> key=<key_name> value=<valu_name>``
command as explained in next section:

+------------------------+-------------------------------------------------------------------+
| anycast_mac            | A valid MAC address in the format xxxx.xxxx.xxxx or               |
|                        | xx:xx:xx:xx:xx:xx                                                 |
+------------------------+-------------------------------------------------------------------+
| evpn_enabled           | Yes or No                                                         |
+------------------------+-------------------------------------------------------------------+
| bfd_tx                 | An integer from 50 through 30000                                  |
+------------------------+-------------------------------------------------------------------+
| bfd_rx                 | An integer from 50 through 30000                                  |
+------------------------+-------------------------------------------------------------------+
| bfd_multiplier         | An integer from 3 through 50                                      |
+------------------------+-------------------------------------------------------------------+                 
| bgp_multihop           | An integer from 1 through 55                                      |
+------------------------+-------------------------------------------------------------------+               
| max_paths              | An integer from 1 through 32                                      |
+------------------------+-------------------------------------------------------------------+
| p2p_link_range         | **(Required)** a valid IP-network or the word “unnumbered”        |
|                        +-------------------------------------------------------------------+ 
|                        | (case insensitive), based on what kind of BGP peers               |
|                        +-------------------------------------------------------------------+
|                        | connectivity you want, IP numbered or unnumbered. (Refer          |
|                        +-------------------------------------------------------------------+
|                        | overview section for details).                                    |
+------------------------+-------------------------------------------------------------------+
| loopback_ip_range      | **(Required)** A valid IP-network, for example,172.32.254.0/24    |
+------------------------+-------------------------------------------------------------------+                    
| leaf_asn_block         |  **(Required)** A single value or range from 1 through 4294967295 |
+------------------------+-------------------------------------------------------------------+                 
| spine_asn_block        | **(Required)** A single value or range from 1 through 4294967295  |
+------------------------+-------------------------------------------------------------------+                  
| loopback_port_number   | **(Required)** A number from 1 through 255                        |
+------------------------+-------------------------------------------------------------------+                       
| allowas_in             | A number from 1 through 10                                        |
+------------------------+-------------------------------------------------------------------+

The required parameters must be added to the user-defined/custom configuration. The other
parameters are not optional.If you do not add optional parameters, Brocade Workflow Composer
will use the values from the default configuration.

.. note::
    Once the required parameters are added to the user-defined fabric, they cannot be modified or deleted.
    To modify/update the mandatory values create a new fabric and define the parameters for this fabric.

Creating a new IP Fabric with user-defined parameters
-----------------------------------------------------

1. Use the ``bwc ipf fabric add fabric=<fabric_name>`` command to create a new fabric
   configuration. For example, the following command creates a new user-defined IP Fabric
   called **user_fab**.

.. code:: shell

    $ bwc ipf fabric add fabric=user_fab
      Fabric user_fab added successfully

2. Use the ``bwc ipf fabric config set key=<key> value=<value> fabric=<fabric_name>``
   command to add parameters to the *user_fab* fabric created in previous step.

.. code-block:: shell
    :emphasize-lines: 1,4,7,10,13,16,19,22,25
   
    $ bwc ipf fabric config set key=p2p_link_range value=10.10.10.0/23 fabric=user_fab
      Setting p2p_link_range with value 10.10.10.0/23 added to fabric user_fab
    
    $ bwc ipf fabric config set key=spine_asn_block value=64512-64999 fabric=user_fab
      Setting spine_asn_block with value 64512-64999 added to fabric user_fab
   
    $ bwc ipf fabric config set key=leaf_asn_block value=65000-65534 fabric=user_fab
      Setting leaf_asn_block with value 65000-65534 added to fabric user_fab
   
    $ bwc ipf fabric config set key=loopback_ip_range value=172.32.254.0/24 fabric=user_fab
      Setting loopback_ip_range with value 172.32.254.0/24 added to fabric user_fab
   
    $ bwc ipf fabric config set key=loopback_port_number value=1 fabric=user_fab
      Setting loopback_port_number with value 1 added to fabric user_fab
   
    $ bwc ipf fabric config set key=bfd_multiplier value=10 fabric=new_fab
      Setting bfd_multiplier with value 10 added to fabric user_fab
   
    $ bwc ipf fabric config set key=bfd_rx value=888 fabric=user_fab
      Setting bfd_rx  with value 888 added to fabric user_fab
   
    $ bwc ipf fabric config set key=bfd_tx value=888 fabric=user_fab
      Setting bfd_tx with value 888 added to fabric user_fab
   
    $ bwc ipf fabric config set key=allowas_in value=7 fabric=user_fab
      Setting allowas_in with value 7 added to fabric user_fab

3. Check the parameter values before saving the configuration.
4. Use the ``bwc ipf fabric config show fabric=<fabric_name>`` command to display the fabric
   details added in step 2.

.. code:: shell

    $ bwc ipf fabric config show fabric=user_fab

      Fabric Config Show
      +----------------------+-----------------+
      | Field                | Value           |
      +----------------------+-----------------+
      | Fabric Name          | user_fab        |
      | spine_asn_block      | 64512-64999     |
      | leaf_asn_block       | 65000-65534     |
      | loopback_port_number | 1               |
      | allowas_in           | 7               |
      | bfd_multiplier       | 10              |
      | p2p_link_range       | 10.10.10.0/23   |
      | bfd_tx               | 888             |
      | loopback_ip_range    | 172.32.254.0/24 |
      | bfd_rx               | 888             |
      +----------------------+-----------------+

Use :command:`fabric=<fabric name>` parameter to display details for a specific fabric.
