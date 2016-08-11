IP Fabric Solution CLI
======================

.. note::
  All command line examples in this section begins with $ (dollar sign), which represents
  a shell command prompt. Do not enter another dollar sign. All commands should be entered
  at the shell prompt.

|bwc| |ipf| CLI is an easy to use CLI for |ipf|.

.. todo::
   Add more details on the basic and advance CLI

------------

------------
bwc ipf help
------------

Displays information (help) about all or a specified command.

Syntax
~~~~~~

.. code-block:: shell

  bwc help [ --help ] [ command [ args... ] ]

Parameters
~~~~~~~~~~

.. code-block:: shell
    :emphasize-lines: 1,3

    command
        Specifies the name of the command.
    args
        Specifies any additional arguments.

Usage Guidelines
~~~~~~~~~~~~~~~~

Refer to :command:`bwc <command> --help` for more information on a specific command.

Examples
~~~~~~~~

Use the bwc --help command to display Brocade Workflow Composer commands and their functions.

.. code-block:: shell

    $ bwc --help
    <ADD OUTPUT>

------------

------------
bwc ipf show
------------


Shows the state of BGP peers and other configurations that have been configured on the
switches.

Syntax
~~~~~~

.. code-block:: shell

    bwc ipf show [ --help ]
    bwc ipf show config bgp [ --fabric=<fabric_name> ]
    bwc ipf show topology [ --fabric=<fabric_name> ] [--format=<format> ]
    bwc ipf show version

Parameters
~~~~~~~~~~

.. code-block:: shell
   :emphasize-lines: 1,4,7,10,13,16,20
    
   --help
       Displays help.

   config bgp
       Displays the BGP configuration.

       --fabric=<fabric_name>            
           Specifies the fabric name.

   topology
       Specifies the fabric name and format of the topology display.

       --fabric=<fabric_name>
           Specifies the fabric name.

       --format=<format>
           Specifies the output type of the file to show the topology (PDF, JPEG, or PNG).
           The default is PDF.

   version
       Displays the version of Brocade Workflow Composer Server.

Examples
~~~~~~~~

.. code-block:: shell

    $ bwc ipf show config bgp
    <ADD OUTPUT>

Use the bwc ipf show topology command to generate an IP Fabric topology map in a PDF format.

.. code-block:: shell

    $ bwc ipf show topology --fabric=default --format=pdf

Open the topology file that was generated using the appropriate software.

Use the bwc ipf show version command to display the current version of Brocade Workflow Composer.

.. code-block:: shell

    $ bwc ipf show version
    <ADD OUTPUT>

-----------------

-----------------
bwc ipf inventory
-----------------
Registers, shows, deletes, or updates a list of switches.

Syntax
~~~~~~
.. code:: shell

    bwc ipf inventory register --ip=<ip_address> --fabric=<fabric_name>
    bwc ipf inventory delete --ip=<ip_address>
    bwc ipf inventory update [ --fabric=<fabric_name> | --ip=<ip_address> ]
    bwc ipf inventory list [ --fabric=<fabric_name> | --ip=<ip_address> ]
    bwc ipf inventory show vcs-links [ --fabric=<fabric_name> ]
    bwc ipf inventory show lldp [ --fabric=<fabric_name> ]

Parameters
~~~~~~~~~~
.. code-block:: shell
    :emphasize-lines: 1,4,7,10,13,16,19,22

    register
        Registers an IP address or fabric by name.
    
    delete
        Deletes a specific IP address.
    
    update
        Updates a specific fabric or a switch in the fabric.
    
    list
        Lists information by fabric name or IP address.
    
    show vcs-links
        Lists VCS links by fabric name.
    
    show lldp
        Displays the contents of an LLDP status.
    
    ip
        Specifies an IP address.
    
    fabric
        Specifies a fabric name.

Examples
~~~~~~~~

Use the ``bwc ipf inventory register`` command to register a switch to the default fabric.

.. code:: shell

    $ bwc ipf inventory register --ip=10.24.39.223 --fabric=default
    <ADD OUTPUT>

Use the ``bwc ipf inventory delete`` command to delete a switch from the server.

.. code:: shell

    $ bwc ipf inventory delete --ip=10.24.39.223
    <ADD OUTPUT>

Use the ``bwc ipf inventory update`` command to update a switch on the server (provides a way
to change the username and password).

.. code:: shell

    $ bwc ipf inventory update --ip=10.24.39.223
    <ADD OUTPUT>

Use the ``bwc ipf inventory list`` command to list all switches registered in the server.

.. code:: shell

    $ bwc ipf inventory list
    <ADD OUTPUT>

Use the ``bwc ipf inventory update --fabric=default`` command to update all switches in the
*"default"* fabric.

.. code:: shell

    $ bwc ipf inventory update --fabric=default
    <ADD OUTPUT>

Use the ``bwc ipf inventory show vcs-links`` command to show VCS link status for a two-node VCS
cluster.

.. code:: shell

    $ bwc ipf inventory show vcs-links
    <ADD OUTPUT>

Use the ``bwc ipf inventory show lldp`` command to show the LLDP neighbor.

.. code:: shell

    $ bwc ipf inventory show lldp
    <ADD OUTPUT>

--------------------

--------------------
bwc ipf workflow bgp
--------------------

Executes a BGP workflow on a selected fabric.

Syntax
~~~~~~

.. code:: shell

    bwc ipf workflow bgp [ --fabric=<fabric_name> ]

Parameters
~~~~~~~~~~

.. code-block:: shell
    :emphasize-lines: 1

    --fabric=<fabric_name>
        Specifies the fabric name.

Usage Guidelines
~~~~~~~~~~~~~~~~

The spine has an additional parameter: retain route-target all under address-family l2vpn
evpn.

Examples
~~~~~~~~

Use the ``bwc ipf workflow bgp`` command to implement a workflow on a specific fabric.

.. code-block:: shell

    $ bwc ipf workflow bgp
    <ADD OUTPUT>

--------------

--------------
bwc ipf fabric
--------------

Adds or deletes fabrics and user-created fabric parameters, and shows fabric and fabric configurations.

Syntax
~~~~~~

.. code-block:: shell

    bwc ipf fabric add --fabric=<fabric_name>
    bwc ipf fabric delete --fabric=<fabric_name>
    bwc ipf fabric config show [ --fabric=<fabric_name> ]
    bwc ipf fabric config add key value [ --fabric=<fabric_name> ]
    bwc ipf fabric config delete key [ --fabric=<fabric_name> ]

Parameters
~~~~~~~~~~

.. code-block:: shell
   :emphasize-lines: 1,4,7

   fabric=<fabric_name>
       Specifies the fabric name.

   value
        Specifies the key value.

   key
        Specifies the key.

Usage Guidelines
~~~~~~~~~~~~~~~~
The following key parameters and their values can be added with the ``bwc ipf fabric config
add`` command.

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

Examples
~~~~~~~~

Use the ``bwc ipf fabric add`` command to add a fabric named *"test"*.

.. code-block:: shell

    $ bwc ipf fabric add --fabric=test
    <ADD OUTPUT>

Use the ``bwc ipf fabric delete`` command to delete a fabric named *"test"*.

.. code-block:: shell

    $ bwc ipf fabric delete --fabric=test
    <ADD OUTPUT>


Use the ``bwc ipf fabric config show`` command to show the configuration of the default
fabric (because no name is specified.)

.. code-block:: shell

    $ bwc ipf fabric config show
    <ADD OUTPUT>

Use the ``bwc ipf fabric add --fabric=test`` command to add a fabric configuration to a fabric name 
*"test"*.

.. code-block:: shell

    $ bwc ipf fabric add --fabric=test
    <ADD OUTPUT>
    $ bwc ipf fabric config show --fabric=test
    <ADD OUTPUT>

Use the ``bwc ipf fabric config delete`` command to delete a parameter from a specific fabric
configuration.

.. code-block:: shell

    $ bwc ipf fabric config delete bfd_multiplier --fabric=test
    <ADD OUTPUT>
