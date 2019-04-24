DC Fabric CLI
=============

.. note::
  All command line examples in this section begins with ``$`` (dollar sign), which represents
  a shell command prompt. Do not enter another dollar sign. All commands should be entered
  at the shell prompt.

|ewc|'s DC Fabric CLI provides a simple way to interrogate and configure your IP Fabric.

------------

--------
bwc help
--------

Displays information (help) about all or a specified command.

Syntax
~~~~~~

.. code-block:: shell

   $ bwc help
     usage: bwc [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]
            [--config-file CONFIG_FILE] [--print-config] [--skip-config]

     Extreme Workflow composer CLI
     
     optional arguments:
       --version             show program's version number and exit
       -v, --verbose         Increase verbosity of output. Can be repeated.
       -q, --quiet           Suppress output except warnings and errors.
       --log-file LOG_FILE   Specify a file to log output. Disabled by default.
       -h, --help            Show help message and exit.
       --debug               Show tracebacks on errors.
       --config-file CONFIG_FILE
                             Path to the CLI config file
       --print-config        Parse the config file and print the values
       --skip-config         Don't parse and use the CLI config file
     
     Commands:
       complete       print bash completion command
       help           print detailed help for another command
       dcf fabric add  Add a new Fabric
       dcf fabric config set  Set or update Fabric properties
       dcf fabric config delete  Delete Fabric property
       dcf fabric config show  Display Fabric configuration for the specified Fabric
       dcf fabric delete  Delete an existing Fabric
       dcf fabric list  List all the Fabrics
       dcf inventory delete  Delete device
       dcf inventory list  List a specific device details or all the devices in the specified Fabric
       dcf inventory register  Add devices to a Fabric
       dcf inventory show lldp  List LLDP details for the specified switch or fabric
       dcf inventory show vcs links  List VCS link details for the specified switch or fabric
       dcf inventory update  Update inventory details for the specified device or entire Fabric
       dcf show config bgp  Display Fabric configuration for the specified Fabric
       dcf show topology  Generates Topology for the specified Fabric
       dcf workflow bgp  Execute the IP Fabric Workflow and display the details

Usage Guidelines
~~~~~~~~~~~~~~~~

Refer to :command:`bwc dcf inventory/fabric <command> --help` for more information on a specific command.

Examples
~~~~~~~~

Use the ``bwc --help`` command to display Extreme Workflow Composer commands and their functions.


.. code-block:: guess
   :emphasize-lines: 1,10

   $ bwc dcf fabric list -h
     usage: bwc dcf fabric list [-h] [--fabric <fabric>]
     
     List all the Fabrics
     
     optional arguments:
       -h, --help         show this help message and exit
       --fabric <fabric>  Fabric for which the configuration will be displayed

   $ bwc dcf inventory register -h
     usage: bwc dcf inventory register [-h] [-f {csv,json,table,value,yaml}]
                                       [-c COLUMN] [--max-width <integer>]
                                       [--noindent]
                                       [--quote {all,minimal,none,nonnumeric}]
                                       host fabric user passwd
     
     Add devices to a Fabric
     
     positional arguments:
       host                  IP of the device to be deleted
       fabric                Fabric to which the device will be added
       user                  Username to connect to the device
       passwd                Password to connect to the device
     
     optional arguments:
       -h, --help            show this help message and exit
     
     output formatters:
       output formatter options
     
       -f {csv,json,table,value,yaml}, --format {csv,json,table,value,yaml}
                             the output format, defaults to table
       -c COLUMN, --column COLUMN
                             specify the column(s) to include, can be repeated
     
     table formatter:
       --max-width <integer>
                             Maximum display width, <1 to disable. You can also use
                             the CLIFF_MAX_TERM_WIDTH environment variable, but the
                             parameter takes precedence.
     
     json formatter:
       --noindent            whether to disable indenting the JSON
     
     CSV Formatter:
       --quote {all,minimal,none,nonnumeric}
                             when to include quotes, defaults to nonnumeric

------------

----------------------
bwc dcf show <command>
----------------------


Shows the state of BGP peers and other elements that have been configured on the
switches.

Syntax
~~~~~~

.. code-block:: shell

    bwc dcf show config bgp --fabric=<fabric_name> | --host=<ip_address>
    bwc dcf show topology <fabric_name>  [--format=<format>] [--render_dir=<dir_path>]

Parameters
~~~~~~~~~~

.. code-block:: guess
   :emphasize-lines: 1,4,7,10,13,16
    
   config bgp
       Displays the BGP configuration.

       fabric=<fabric_name>            
           Specifies the fabric name.

   topology
       Specifies the fabric name and format of the topology display.

       fabric=<fabric_name>
           Specifies the fabric name.

       --format=<format>
           Specifies the output type of the file to show the topology (PDF, JPEG, or PNG).
           The default is PDF.

       --render_dir=<dir_path>
           Specifies the path where the topology file will be saved.
           The default is /tmp.


Examples
~~~~~~~~

.. code-block:: shell

    $ bwc dcf show config bgp

      Show BGP Configuration
  
      Switch 10.24.39.225 (Leaf):
      rbridge-id 225
        router bgp
          local-as 65000
          bfd interval 300 min-rx 300 multiplier 3
          neighbor 10.10.10.1 remote-as 64512 state ESTAB up_time 2d20h40m creation_time 2016-08-11
          05:11:45
          neighbor 10.10.10.1 ebgp-multihop 5
          neighbor 10.10.10.3 remote-as 64513 state ESTAB up_time 17h5m24s creation_time 2016-08-11
          05:11:45
          neighbor 10.10.10.3 ebgp-multihop 5
          address-family ipv4 unicast
           redistribute connected
           neighbor 10.10.10.1 allowas-in 5
           neighbor 10.10.10.3 allowas-in 5
           maximum-paths 8
           graceful-restart
           next-hop-recursion
          address-family l2vpn evpn
           neighbor 10.10.10.1 activate
           neighbor 10.10.10.1 allowas-in 5
           neighbor 10.10.10.1 next-hop-unchanged
           neighbor 10.10.10.3 activate
           neighbor 10.10.10.3 allowas-in 5
           neighbor 10.10.10.3 next-hop-unchanged
  
      Switch 10.24.39.224 (Spine):
      rbridge-id 224
        router bgp
          local-as 64512
          bfd interval 300 min-rx 300 multiplier 3
          neighbor 10.10.10.0 remote-as 65000 state ESTAB up_time 2d20h40m creation_time 2016-08-11
          05:11:52
          neighbor 10.10.10.0 ebgp-multihop 5
          neighbor 10.10.10.4 remote-as 65001 state ESTAB up_time 17h5m26s creation_time 2016-08-11
          05:11:52
          neighbor 10.10.10.4 ebgp-multihop 5
          neighbor 10.10.10.10 remote-as 65002 state ESTAB up_time 17h5m30s creation_time 2016-08-11
          05:11:52
          neighbor 10.10.10.10 ebgp-multihop 5
          neighbor 10.10.10.12 remote-as 65003 state IDLE up_time 0h0m0s creation_time 2016-08-11
          05:11:52
          neighbor 10.10.10.12 ebgp-multihop 5
          neighbor 10.10.10.18 remote-as 65003 state ESTAB up_time 17h5m24s creation_time 2016-08-11
          05:11:52
          neighbor 10.10.10.18 ebgp-multihop 5
          address-family ipv4 unicast
           redistribute connected
           neighbor 10.10.10.0 allowas-in 5
           neighbor 10.10.10.4 allowas-in 5
           neighbor 10.10.10.10 allowas-in 5
           neighbor 10.10.10.12 allowas-in 5
           neighbor 10.10.10.18 allowas-in 5
           maximum-paths 8
           graceful-restart
           next-hop-recursion
          address-family l2vpn evpn
           retain route-target all
           neighbor 10.10.10.0 activate
           neighbor 10.10.10.0 allowas-in 5
           neighbor 10.10.10.0 next-hop-unchanged
           neighbor 10.10.10.4 activate
           neighbor 10.10.10.4 allowas-in 5
           neighbor 10.10.10.4 next-hop-unchanged
           neighbor 10.10.10.10 activate
           neighbor 10.10.10.10 allowas-in 5
           neighbor 10.10.10.10 next-hop-unchanged
           neighbor 10.10.10.12 activate
           neighbor 10.10.10.12 allowas-in 5
           neighbor 10.10.10.12 next-hop-unchanged
           neighbor 10.10.10.18 activate
           neighbor 10.10.10.18 allowas-in 5
           neighbor 10.10.10.18 next-hop-unchanged

Use ``bwc dcf show topology`` command to generate an IP Fabric topology map in a PDF
format (default format).

.. code-block:: shell

    $ bwc dcf show topology fabric=default --format=pdf --render_dir=/tmp

      Topology map generated: /tmp/topology_default_20160811-020715.pdf

Use any appropriate image reading software to open the topology file.

-----------------

---------------------------
bwc dcf inventory <command>
---------------------------
Registers, shows, deletes, or updates a list of switches.

Syntax
~~~~~~
.. code-block:: shell

    bwc dcf inventory register host=<ip_address> fabric=<fabric_name> user=<switch_user> passwd=<switch_password>
    bwc dcf inventory delete host=<ip_address>
    bwc dcf inventory update --fabric=<fabric_name> | --host=<ip_address> [user=<switch_user> passwd=<switch_password>]
    bwc dcf inventory list --fabric=<fabric_name> | --host=<ip_address>
    bwc dcf inventory show vcs links fabric=<fabric_name>
    bwc dcf inventory show lldp fabric=<fabric_name>

Parameters
~~~~~~~~~~
.. code-block:: guess
    :emphasize-lines: 1,4,7,10,13,16,19,22

    register
        Registers an IP address or fabric by name.
    
    delete
        Deletes a specific IP address.
    
    update
        Updates a specific fabric or a switch in the fabric.
    
    list
        Lists information by fabric name or IP address.
    
    show vcs links
        Lists VCS links by fabric name.
    
    show lldp
        Displays the contents of an LLDP status.
    
    host
        Specifies IP address of a VDX switch.
    
    fabric
        Specifies a fabric name.

Examples
~~~~~~~~

Use the ``bwc dcf inventory register`` command to register a switch to the default fabric.

.. code-block:: shell

    $ bwc dcf inventory register host=10.24.39.225 fabric=default user=admin passwd=password

      Inventory Add
      +--------------+---------+------------+----------+------+------+-------+---------+
      | IP           | Model   | Rbridge-Id | Firmware | Name | Role |   ASN | Fabric  |
      +--------------+---------+------------+----------+------+------+-------+---------+
      | 10.24.39.225 | VDX6740 |        225 | 7.1.0    | sw0  | Leaf | 65000 | default |
      +--------------+---------+------------+----------+------+------+-------+---------+

Use the ``bwc dcf inventory delete`` command to delete a switch from the server.

.. code-block:: shell

    $ bwc dcf inventory delete host=10.24.39.225

      Inventory Delete Successfully
      +--------------+---------+------------+----------+------+------+-------+---------+
      | IP           | Model   | Rbridge-Id | Firmware | Name | Role |   ASN | Fabric  |
      +--------------+---------+------------+----------+------+------+-------+---------+
      | 10.24.39.225 | VDX6740 |        225 | 7.1.0    | sw0  | Leaf | 65000 | default |
      +--------------+---------+------------+----------+------+------+-------+---------+

Use the ``bwc dcf inventory update`` command to update a switch on the server. (This provides a way
to change the username and password.)

.. code-block:: shell

    $ bwc dcf inventory update --host=10.24.39.225

      Inventory Update
      +--------------+---------+------------+----------+------+------+-------+---------+
      | IP           | Model   | Rbridge-Id | Firmware | Name | Role |   ASN | Fabric  |
      +--------------+---------+------------+----------+------+------+-------+---------+
      | 10.24.39.225 | VDX6740 |        225 | 7.1.0    | sw0  | Leaf | 65000 | default |
      +--------------+---------+------------+----------+------+------+-------+---------+

Use the ``bwc dcf inventory list`` command to list all registered switches.

.. code-block:: shell

    $ bwc dcf inventory list --fabric=default

      Inventory List
      +--------------+-------------+------------+----------+----------------+-------+-------+---------+
      | IP           | Model       | Rbridge-Id | Firmware | Name           | Role  |   ASN | Fabric  |
      +--------------+-------------+------------+----------+----------------+-------+-------+---------+
      | 10.24.39.225 | VDX6740     |        225 | 7.1.0    | sw0            | Leaf  | 65000 | default |
      | 10.24.39.229 | VDX6740     |        229 | 7.1.0    | VCS_VDX_39_229 | Leaf  |       | default |
      | 10.24.39.228 | VDX6740     |        228 | 7.1.0    | VCS_VDX_39_228 | Leaf  |       | default |
      | 10.24.39.227 | VDX6740     |        227 | 7.1.0    | sw0            | Leaf  |       | default |
      | 10.24.39.226 | VDX6740T    |         26 | 7.1.0    | sw0            | Leaf  |       | default |
      | 10.24.39.224 | VDX6740     |        224 | 7.1.0    | sw0            | Spine | 64512 | default |
      | 10.24.39.223 | VDX6740T-1G |        223 | 7.1.0    | sw0            | Spine |       | default |
      +--------------+-------------+------------+----------+----------------+-------+-------+---------+

Use the ``bwc dcf inventory update --fabric=default`` command to update all switches in the
*"default"* fabric.

.. code-block:: shell

    $ bwc dcf inventory update --fabric=default

      Inventory Update
      +--------------+-------------+------------+----------+----------------+-------+-------+---------+
      | IP           | Model       | Rbridge-Id | Firmware | Name           | Role  |   ASN | Fabric  |
      +--------------+-------------+------------+----------+----------------+-------+-------+---------+
      | 10.24.39.225 | VDX6740     |        225 | 7.1.0    | sw0            | Leaf  | 65000 | default |
      | 10.24.39.229 | VDX6740     |        229 | 7.1.0    | VCS_VDX_39_229 | Leaf  |       | default |
      | 10.24.39.228 | VDX6740     |        228 | 7.1.0    | VCS_VDX_39_228 | Leaf  |       | default |
      | 10.24.39.227 | VDX6740     |        227 | 7.1.0    | sw0            | Leaf  |       | default |
      | 10.24.39.226 | VDX6740T    |         26 | 7.1.0    | sw0            | Leaf  |       | default |
      | 10.24.39.224 | VDX6740     |        224 | 7.1.0    | sw0            | Spine | 64512 | default |
      | 10.24.39.223 | VDX6740T-1G |        223 | 7.1.0    | sw0            | Spine |       | default |
      +--------------+-------------+------------+----------+----------------+-------+-------+---------+

Use the ``bwc dcf inventory show vcs links`` command to show VCS link status for a two-node VCS
cluster.

.. code-block:: shell

    $ bwc dcf inventory show vcs links fabric=default

      Inventory Show VCS
      +-----------------------------+--------------+-----------------------------+--------------+---------+
      | Interface-1                 | IP-1         | Interface-2                 | IP-2         | Fabric  |
      +-----------------------------+--------------+-----------------------------+--------------+---------+
      | TenGigabitEthernet 228/0/10 | 10.24.39.228 | TenGigabitEthernet 229/0/10 | 10.24.39.229 | default |
      +-----------------------------+--------------+-----------------------------+--------------+---------+

Use the ``bwc dcf inventory show lldp`` command to show LLDP neighbors.

.. code-block:: shell

    $ bwc dcf inventory show lldp fabric=default

      Inventory Show LLDP
      +--------------+-------------------+-------------------+-------------------+-------------------+---------------+------------------------+
      | IP           | Local MAC         | Local Intf        | Remote MAC        | Remote Intf       | Remote System | Remote Management Addr |
      +--------------+-------------------+-------------------+-------------------+-------------------+---------------+------------------------+
      | 10.24.39.225 | 50:eb:1a:22:50:b9 | TenGigabitEtherne | 00:27:f8:c5:bf:c2 | TenGigabitEtherne |               | sw0                    |
      |              |                   | t 225/0/1         |                   | t 223/0/1         |               |                        |
      | 10.24.39.225 | 50:eb:1a:22:50:ba | TenGigabitEtherne | 50:eb:1a:16:1d:8f | TenGigabitEtherne | 10.24.39.224  | sw0                    |
      |              |                   | t 225/0/2         |                   | t 224/0/1         |               |                        |
      | 10.24.39.229 | 50:eb:1a:21:19:27 | FortyGigabitEther | 50:eb:1a:16:1d:c0 | FortyGigabitEther | 10.24.39.224  | sw0                    |
      |              |                   | net 229/0/49      |                   | net 224/0/50      |               |                        |
      | 10.24.39.229 | 50:eb:1a:21:19:28 | FortyGigabitEther | 00:27:f8:c5:bf:f3 | FortyGigabitEther |               | sw0                    |
      |              |                   | net 229/0/50      |                   | net 223/0/50      |               |                        |
      | 10.24.39.228 | 50:eb:1a:13:9e:9d | TenGigabitEtherne | 00:27:f8:c5:bf:c5 | TenGigabitEtherne |               | sw0                    |
      |              |                   | t 228/0/1         |                   | t 223/0/4         |               |                        |
      | 10.24.39.228 | 50:eb:1a:13:9e:cd | FortyGigabitEther | 50:eb:1a:16:1d:c1 | FortyGigabitEther | 10.24.39.224  | sw0                    |
      |              |                   | net 228/0/49      |                   | net 224/0/51      |               |                        |
      | 10.24.39.227 | 50:eb:1a:22:c9:a4 | FortyGigabitEther | 00:27:f8:c5:bf:f2 | FortyGigabitEther |               | sw0                    |
      |              |                   | net 227/0/49      |                   | net 223/0/49      |               |                        |
      | 10.24.39.227 | 50:eb:1a:22:c9:a5 | FortyGigabitEther | 50:eb:1a:16:1d:bf | FortyGigabitEther | 10.24.39.224  | sw0                    |
      |              |                   | net 227/0/50      |                   | net 224/0/49      |               |                        |
      | 10.24.39.226 | 50:eb:1a:35:29:75 | TenGigabitEtherne | 50:eb:1a:16:1d:90 | TenGigabitEtherne | 10.24.39.224  | sw0                    |
      |              |                   | t 26/0/1          |                   | t 224/0/2         |               |                        |
      | 10.24.39.226 | 50:eb:1a:35:29:77 | TenGigabitEtherne | 00:27:f8:c5:bf:c3 | TenGigabitEtherne |               | sw0                    |
      |              |                   | t 26/0/3          |                   | t 223/0/2         |               |                        |
      | 10.24.39.224 | 50:eb:1a:16:1d:8f | TenGigabitEtherne | 50:eb:1a:22:50:ba | TenGigabitEtherne |               | sw0                    |
      |              |                   | t 224/0/1         |                   | t 225/0/2         |               |                        |
      | 10.24.39.224 | 50:eb:1a:16:1d:90 | TenGigabitEtherne | 50:eb:1a:35:29:75 | TenGigabitEtherne |               | sw0                    |
      |              |                   | t 224/0/2         |                   | t 26/0/1          |               |                        |
      | 10.24.39.224 | 50:eb:1a:16:1d:bf | FortyGigabitEther | 50:eb:1a:22:c9:a5 | FortyGigabitEther |               | sw0                    |
      |              |                   | net 224/0/49      |                   | net 227/0/50      |               |                        |
      | 10.24.39.224 | 50:eb:1a:16:1d:c0 | FortyGigabitEther | 50:eb:1a:21:19:27 | FortyGigabitEther | 10.24.39.229  | VCS_VDX_39_229         |
      |              |                   | net 224/0/50      |                   | net 229/0/49      |               |                        |
      | 10.24.39.224 | 50:eb:1a:16:1d:c1 | FortyGigabitEther | 50:eb:1a:13:9e:cd | FortyGigabitEther | 10.24.39.228  | VCS_VDX_39_228         |
      |              |                   | net 224/0/51      |                   | net 228/0/49      |               |                        |
      | 10.24.39.223 | 00:27:f8:c5:bf:c2 | TenGigabitEtherne | 50:eb:1a:22:50:b9 | TenGigabitEtherne |               | sw0                    |
      |              |                   | t 223/0/1         |                   | t 225/0/1         |               |                        |
      | 10.24.39.223 | 00:27:f8:c5:bf:c3 | TenGigabitEtherne | 50:eb:1a:35:29:77 | TenGigabitEtherne |               | sw0                    |
      |              |                   | t 223/0/2         |                   | t 26/0/3          |               |                        |
      | 10.24.39.223 | 00:27:f8:c5:bf:c5 | TenGigabitEtherne | 50:eb:1a:13:9e:9d | TenGigabitEtherne | 10.24.39.228  | VCS_VDX_39_228         |
      |              |                   | t 223/0/4         |                   | t 228/0/1         |               |                        |
      | 10.24.39.223 | 00:27:f8:c5:bf:d0 | TenGigabitEtherne | 00:27:f8:c6:a6:a0 | TenGigabitEtherne |               | sw0                    |
      |              |                   | t 223/0/15        |                   | t 1/0/15          |               |                        |
      | 10.24.39.223 | 00:27:f8:c5:bf:f2 | FortyGigabitEther | 50:eb:1a:22:c9:a4 | FortyGigabitEther |               | sw0                    |
      |              |                   | net 223/0/49      |                   | net 227/0/49      |               |                        |
      | 10.24.39.223 | 00:27:f8:c5:bf:f3 | FortyGigabitEther | 50:eb:1a:21:19:28 | FortyGigabitEther | 10.24.39.229  | VCS_VDX_39_229         |
      |              |                   | net 223/0/50      |                   | net 229/0/50      |               |                        |
      +--------------+-------------------+-------------------+-------------------+-------------------+---------------+------------------------+

--------------------

--------------------
bwc dcf workflow bgp
--------------------

Executes a BGP workflow on a selected fabric.

Syntax
~~~~~~

.. code-block:: shell

    bwc dcf workflow bgp fabric=<fabric_name>

Parameters
~~~~~~~~~~

.. code-block:: guess
    :emphasize-lines: 1

    fabric=<fabric_name>
        Specifies the fabric name.


.. note::

    The spine has an additional parameter: ``retain route-target all`` under ``address-family l2vpn
    evpn``.

Examples
~~~~~~~~

Use the ``bwc dcf workflow bgp`` command to implement a workflow on a specific fabric.

.. code-block:: shell

    $ bwc dcf workflow bgp fabric=default

      BGP Workflow Result:

      Switch 10.24.39.225 (Leaf):
      rbridge-id 225
        router bgp
          local-as 65000
          bfd interval 300 min-rx 300 multiplier 3
          neighbor 10.10.10.1 remote-as 64512 state ESTAB up_time 2d20h40m creation_time 2016-08-11
          05:11:45
          neighbor 10.10.10.1 ebgp-multihop 5
          neighbor 10.10.10.3 remote-as 64513 state ESTAB up_time 17h5m24s creation_time 2016-08-11
          05:11:45
          neighbor 10.10.10.3 ebgp-multihop 5
          address-family ipv4 unicast
           redistribute connected
           neighbor 10.10.10.1 allowas-in 5
           neighbor 10.10.10.3 allowas-in 5
           maximum-paths 8
           graceful-restart
           next-hop-recursion
          address-family l2vpn evpn
           neighbor 10.10.10.1 activate
           neighbor 10.10.10.1 allowas-in 5
           neighbor 10.10.10.1 next-hop-unchanged
           neighbor 10.10.10.3 activate
           neighbor 10.10.10.3 allowas-in 5
           neighbor 10.10.10.3 next-hop-unchanged

      Switch 10.24.39.224 (Spine):
      rbridge-id 224
        router bgp
          local-as 64512
          bfd interval 300 min-rx 300 multiplier 3
          neighbor 10.10.10.0 remote-as 65000 state ESTAB up_time 2d20h40m creation_time 2016-08-11
          05:11:52
          neighbor 10.10.10.0 ebgp-multihop 5
          neighbor 10.10.10.4 remote-as 65001 state ESTAB up_time 17h5m26s creation_time 2016-08-11
          05:11:52
          neighbor 10.10.10.4 ebgp-multihop 5
          neighbor 10.10.10.10 remote-as 65002 state ESTAB up_time 17h5m30s creation_time 2016-08-11
          05:11:52
          neighbor 10.10.10.10 ebgp-multihop 5
          neighbor 10.10.10.12 remote-as 65003 state IDLE up_time 0h0m0s creation_time 2016-08-11
          05:11:52
          neighbor 10.10.10.12 ebgp-multihop 5
          neighbor 10.10.10.18 remote-as 65003 state ESTAB up_time 17h5m24s creation_time 2016-08-11
          05:11:52
          neighbor 10.10.10.18 ebgp-multihop 5
          address-family ipv4 unicast
           redistribute connected
           neighbor 10.10.10.0 allowas-in 5
           neighbor 10.10.10.4 allowas-in 5
           neighbor 10.10.10.10 allowas-in 5
           neighbor 10.10.10.12 allowas-in 5
           neighbor 10.10.10.18 allowas-in 5
           maximum-paths 8
           graceful-restart
           next-hop-recursion
          address-family l2vpn evpn
           retain route-target all
           neighbor 10.10.10.0 activate
           neighbor 10.10.10.0 allowas-in 5
           neighbor 10.10.10.0 next-hop-unchanged
           neighbor 10.10.10.4 activate
           neighbor 10.10.10.4 allowas-in 5
           neighbor 10.10.10.4 next-hop-unchanged
           neighbor 10.10.10.10 activate
           neighbor 10.10.10.10 allowas-in 5
           neighbor 10.10.10.10 next-hop-unchanged
           neighbor 10.10.10.12 activate
           neighbor 10.10.10.12 allowas-in 5
           neighbor 10.10.10.12 next-hop-unchanged
           neighbor 10.10.10.18 activate
           neighbor 10.10.10.18 allowas-in 5
           neighbor 10.10.10.18 next-hop-unchanged


--------------

--------------
bwc dcf fabric
--------------

Adds or deletes fabrics and user-created fabric parameters, and shows fabric and fabric configurations.

Syntax
~~~~~~

.. code-block:: shell

    bwc dcf fabric add fabric=<fabric_name>
    bwc dcf fabric delete fabric=<fabric_name>
    bwc dcf fabric config show fabric=<fabric_name>
    bwc dcf fabric config set fabric=<fabric_name> key=<key_name> value=<value>
    bwc dcf fabric config delete fabric=<fabric_name> key=<key>

Parameters
~~~~~~~~~~

.. code-block:: guess
   :emphasize-lines: 1,4,7

   fabric=<fabric_name>
       Specifies the fabric name.

   value
        Specifies the key's value.

   key
        Specifies the key.

Usage Guidelines
~~~~~~~~~~~~~~~~
The following key parameters and their values can be added with the ``bwc dcf fabric config
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

Use the ``bwc dcf fabric add`` command to add a fabric named **new_fabric**.

.. code-block:: shell

    $ bwc dcf fabric add fabric=new_fabric

      Fabric new_fabric added successfully

Use the ``bwc dcf fabric delete`` command to delete a fabric named **new_fabric**.

.. code-block:: shell

    $ bwc dcf fabric delete fabric=new_fabric

      Fabric new_fabric deleted successfully


Use the ``bwc dcf fabric config show`` command to show the configuration of the default
fabric (because no name is specified.)

.. code-block:: shell

    $ bwc dcf fabric config show fabric=default

      Fabric Config Show
      +----------------------+-----------------+
      | Field                | Value           |
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

Use the ``bwc dcf fabric add fabric=new_fabric`` command to add a fabric configuration to a fabric name
*"new_fabric"*.

.. code-block:: shell

    $ bwc dcf fabric add fabric=new_fabric

      Fabric new_fabric added successfully

    $ bwc dcf fabric config show fabric=new_fabric

      Fabric Config Show
      +----------------------+-----------------+
      | Field                | Value           |
      +----------------------+-----------------+
      | Fabric Name          | new_fabric      |
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

Use the ``bwc dcf fabric config delete`` command to delete a parameter from a specific fabric
configuration.

.. code-block:: shell

    $ bwc dcf fabric config delete fabric=new_fabric key=anycast_mac

      Key anycast_mac deleted successfully from fabric new_fabric
