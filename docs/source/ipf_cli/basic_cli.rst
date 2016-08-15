IP Fabric Solution CLI
======================

.. note::
  All command line examples in this section begins with $ (dollar sign), which represents
  a shell command prompt. Do not enter another dollar sign. All commands should be entered
  at the shell prompt.

|bwc| |ipf| CLI provides a simple way to interrogate and configure your IP Fabric.

.. todo::
   Add more details on the basic and advanced CLI

------------

------------
bwc ipf help
------------

.. todo::
  Unclear below if it should be --help, or just help.

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

Use the ``bwc --help`` command to display Brocade Workflow Composer commands and their functions.

.. code-block:: guess

    $ bwc --help
    Brocade Workflow composer CLI

    optional arguments:
      --version            show program's version number and exit
      -v, --verbose        Increase verbosity of output. Can be repeated.
      -q, --quiet          Suppress output except warnings and errors.
      --log-file LOG_FILE  Specify a file to log output. Disabled by default.
      -h, --help           Show help message and exit.
      --debug              Show tracebacks on errors.

    Commands:
      complete       print bash completion command
      help           print detailed help for another command
      ipf fabric add  Add a new Fabric
      ipf fabric config add  Set or update Fabric properties
      ipf fabric config delete  Delete Fabric property
      ipf fabric config show  Display Fabric configuration for the specified Fabric
      ipf fabric delete  Delete an existing Fabric
      ipf fabric list  List all the Fabrics
      ipf inventory delete  Delete device
      ipf inventory list  List a specific device details or all the devices in the specified Fabric
      ipf inventory register  Add devices to a Fabric
      ipf inventory show lldp  List LLDP details for the specified switch or fabric
      ipf inventory show vcs links  List VCS link details for the specified switch or fabric
      ipf inventory update  Update inventory details for the specified device or entire Fabric
      ipf show config bgp  Display Fabric configuration for the specified Fabric
      ipf show topology  Generates Topology for the specified Fabric
      ipf workflow bgp  Execute the IP Fabric Workflow and display the details

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
    bwc ipf show config bgp fabric=<fabric_name>
    bwc ipf show topology fabric=<fabric_name>  [--format=<format>] [--render_dir=<dir_path>]

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

    $ bwc ipf show config bgp

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

Use the bwc ipf show topology command to generate an IP Fabric topology map in a PDF format.

.. code-block:: shell

    $ bwc ipf show topology fabric=default --format=pdf --render_dir=/tmp

    Topology map generated: /tmp/topology_default_20160811-020715.pdf

Open the topology file that was generated using the appropriate software.


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

    $ bwc ipf inventory register ip=10.24.39.223 fabric=default user=admin passwd=password

    Inventory Add
    +--------------+---------+------------+----------+------+------+-------+---------+
    | IP           | Model   | Rbridge-Id | Firmware | Name | Role |   ASN | Fabric  |
    +--------------+---------+------------+----------+------+------+-------+---------+
    | 10.24.39.225 | VDX6740 |        225 | 7.1.0    | sw0  | Leaf | 65000 | default |
    +--------------+---------+------------+----------+------+------+-------+---------+

Use the ``bwc ipf inventory delete`` command to delete a switch from the server.

.. code:: shell

    $ bwc ipf inventory delete ip=10.24.39.223

    Inventory Delete Successfully
    +--------------+---------+------------+----------+------+------+-------+---------+
    | IP           | Model   | Rbridge-Id | Firmware | Name | Role |   ASN | Fabric  |
    +--------------+---------+------------+----------+------+------+-------+---------+
    | 10.24.39.225 | VDX6740 |        225 | 7.1.0    | sw0  | Leaf | 65000 | default |
    +--------------+---------+------------+----------+------+------+-------+---------+

Use the ``bwc ipf inventory update`` command to update a switch on the server (provides a way
to change the username and password).

.. code:: shell

    $ bwc ipf inventory update --ip=10.24.39.225

    Inventory Update
    +--------------+---------+------------+----------+------+------+-------+---------+
    | IP           | Model   | Rbridge-Id | Firmware | Name | Role |   ASN | Fabric  |
    +--------------+---------+------------+----------+------+------+-------+---------+
    | 10.24.39.225 | VDX6740 |        225 | 7.1.0    | sw0  | Leaf | 65000 | default |
    +--------------+---------+------------+----------+------+------+-------+---------+

Use the ``bwc ipf inventory list`` command to list all switches registered in the server.

.. code:: shell

    $ bwc ipf inventory list --fabric=default

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

Use the ``bwc ipf inventory update --fabric=default`` command to update all switches in the
*"default"* fabric.

.. code:: shell

    $ bwc ipf inventory update --fabric=default

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

Use the ``bwc ipf inventory show vcs-links`` command to show VCS link status for a two-node VCS
cluster.

.. code:: shell

    $ bwc ipf inventory show vcs links fabric=default

    Inventory Show VCS
    +-----------------------------+--------------+-----------------------------+--------------+---------+
    | Interface-1                 | IP-1         | Interface-2                 | IP-2         | Fabric  |
    +-----------------------------+--------------+-----------------------------+--------------+---------+
    | TenGigabitEthernet 228/0/10 | 10.24.39.228 | TenGigabitEthernet 229/0/10 | 10.24.39.229 | default |
    +-----------------------------+--------------+-----------------------------+--------------+---------+

Use the ``bwc ipf inventory show lldp`` command to show the LLDP neighbor.

.. code:: shell

    $ bwc ipf inventory show lldp links fabric=default

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
bwc ipf workflow bgp
--------------------

Executes a BGP workflow on a selected fabric.

Syntax
~~~~~~

.. code:: shell

    bwc ipf workflow bgp fabric=<fabric_name>

Parameters
~~~~~~~~~~

.. code-block:: shell
    :emphasize-lines: 1

    --fabric=<fabric_name>
        Specifies the fabric name.

Usage Guidelines
~~~~~~~~~~~~~~~~

.. todo::
   Feels like this line is a bit isolated? Doesn't really relate to usage, more just some info about what people will see in the output?

The spine has an additional parameter: retain route-target all under address-family l2vpn
evpn.

Examples
~~~~~~~~

Use the ``bwc ipf workflow bgp`` command to implement a workflow on a specific fabric.

.. code-block:: shell

    $ bwc ipf workflow bgp fabric=default

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
bwc ipf fabric
--------------

Adds or deletes fabrics and user-created fabric parameters, and shows fabric and fabric configurations.

Syntax
~~~~~~

.. code-block:: shell

    bwc ipf fabric add fabric=<fabric_name>
    bwc ipf fabric delete fabric=<fabric_name>
    bwc ipf fabric config show fabric=<fabric_name>
    bwc ipf fabric config add fabric=<fabric_name> key=<key_name> value=<value>
    bwc ipf fabric config delete fabric=<fabric_name> key=<key>

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
.. todo::
   I wonder if we need to explain more about what the parameters do, not just what syntax they take?
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

    $ bwc ipf fabric add fabric=test

    Fabric test Added successfully

Use the ``bwc ipf fabric delete`` command to delete a fabric named *"test"*.

.. code-block:: shell

    $ bwc ipf fabric delete fabric=test

    Fabric test Delete successfully


Use the ``bwc ipf fabric config show`` command to show the configuration of the default
fabric (because no name is specified.)

.. code-block:: shell

    $ bwc ipf fabric config show fabric=default

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

Use the ``bwc ipf fabric add fabric=test`` command to add a fabric configuration to a fabric name
*"test"*.

.. code-block:: shell

    $ bwc ipf fabric add fabric=test

    Fabric test Added successfully

    $ bwc ipf fabric config show fabric=test

    Fabric Config Show
    +----------------------+-----------------+
    | Field                | Value           |
    +----------------------+-----------------+
    | Fabric Name          | test         |
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

Use the ``bwc ipf fabric config delete`` command to delete a parameter from a specific fabric
configuration.

.. code-block:: shell

    $ bwc ipf fabric config delete fabric=test key=foo

     Key foo Delete successfully from fabric test1
