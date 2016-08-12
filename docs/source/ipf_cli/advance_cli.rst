Advance CLI (using st2)
=======================

.. note::
    All command line examples in this section begins with $ (dollar sign), which represents
    a shell command prompt. Do not enter another dollar sign. All commands should be entered 
    at the shell prompt.

To access |ipf| solution using |bwc| cli instead of |ip| specific cli use these commands.
However, assumption here is that you are familiar with the StackStorm components like actions,
workflows, rules, packs, execution list etc.

.. todo::
    Add links for st2 components and more details

----------

|bwc| consists of two packs to access inventory services and implement BGP workflow on the
default or user defined fabric. Inventory and Nos pack. These packs are installed, by default,
with |ipf|.

.. todo::
    Add more details/one line each on the packs

The actions in each pack have a small description on what it does.

.. code-block:: guess
    :emphasize-lines: 1,17

    $ st2 action list -p nos
    +--------------------------------+------+----------------------------------------------------+
    | ref                            | pack | description                                        |
    +--------------------------------+------+----------------------------------------------------+
    | nos.configure_anycast          | nos  | Affect an anycast gateway change on VDX switches   |
    | nos.configure_bgp              | nos  | Configure BGP on Brocade VDX Switches              |
    | nos.configure_bgp_neighbor     | nos  | Configure BGP neighbor on Brocade VDX Switches     |
    | nos.configure_bgp_redistribute | nos  | Configure BGP route redistribution on VDX switches |
    | nos.configure_fabric           | nos  | Configure IP fabric                                |
    | nos.configure_ip               | nos  | Configure IPs on Brocade VDX Switches              |
    | nos.configure_switch           | nos  | Configure switch                                   |
    | nos.configure_switch_bgp       | nos  | Configure bgp on switch                            |
    | nos.configure_switch_ifaces    | nos  | Configure switch interfaces                        |
    | nos.inventory                  | nos  | Query inventory service to constuct the inventory. |
    +--------------------------------+------+----------------------------------------------------+
    
    $ st2 action list -p inventory
    +--------------------------------+-----------+---------------------------------------------------------------------------------------+
    | ref                            | pack      | description                                                                           |
    +--------------------------------+-----------+---------------------------------------------------------------------------------------+
    | inventory.fabric_add           | inventory | Add a fabric to the inventory                                                         |
    | inventory.fabric_config_add    | inventory | Add/Update the specified fabric parameter for the specified fabric from the inventory |
    | inventory.fabric_config_delete | inventory | Delete the specified fabric parameter for the specified fabric from the inventory     |
    | inventory.fabric_delete        | inventory | Delete a fabric from the inventory                                                    |
    | inventory.fabric_list          | inventory | List all the fabrics in the inventory or the specified fabric details                 |
    | inventory.show_config_bgp      | inventory | Lists BGP config details in the inventory for the specified fabric or device IP       |
    | inventory.show_lldp_links      | inventory | List all the lldp links in the inventory for the specified fabric                     |
    | inventory.show_vcs_links       | inventory | List all the vcs links in the inventory for the specified fabric                      |
    | inventory.switch_add           | inventory | Add a switch to the inventory to a specified fabric                                   |
    | inventory.switch_delete        | inventory | Deletes the specified switch from the Fabric                                          |
    | inventory.switch_list          | inventory | List all the devices in the inventory for the specified fabric or device IP           |
    | inventory.switch_update        | inventory | Update a details of single switch or all the switches in the Fabric                   |
    | inventory.topology_generate    | inventory | Generate the topology for the specified Fabric                                        |
    +--------------------------------+-----------+---------------------------------------------------------------------------------------+

To get more details on each action under these packs use ``st2 action get <pack-name>.<action-name>``
command. You can also use the ``-y`` flag for output in YAML:

.. code-block:: guess
    :emphasize-lines: 1,41

    $ st2 action get inventory.switch_add
    +-------------+------------------------------------------------------------+
    | Property    | Value                                                      |
    +-------------+------------------------------------------------------------+
    | id          | 57acd58718971236df5b4599                                   |
    | uid         | action:inventory:switch_add                                |
    | ref         | inventory.switch_add                                       |
    | pack        | inventory                                                  |
    | name        | switch_add                                                 |
    | description | Add a switch to the inventory to a specified fabric        |
    | enabled     | True                                                       |
    | entry_point | switch_add.py                                              |
    | runner_type | run-python                                                 |
    | parameters  | {                                                          |
    |             |     "passwd": {                                            |
    |             |         "secret": true,                                    |
    |             |         "required": true,                                  |
    |             |         "type": "string",                                  |
    |             |         "description": "Password to connect to the device" |
    |             |     },                                                     |
    |             |     "host": {                                              |
    |             |         "required": true,                                  |
    |             |         "type": "string",                                  |
    |             |         "description": "IP address of the Device"          |
    |             |     },                                                     |
    |             |     "fabric": {                                            |
    |             |         "required": true,                                  |
    |             |         "type": "string",                                  |
    |             |         "description": "Name of the Fabric to add"         |
    |             |     },                                                     |
    |             |     "user": {                                              |
    |             |         "required": true,                                  |
    |             |         "type": "string",                                  |
    |             |         "description": "User to connect to the device"     |
    |             |     }                                                      |
    |             | }                                                          |
    | notify      |                                                            |
    | tags        |                                                            |
    +-------------+------------------------------------------------------------+
    
    $ st2 action get inventory.switch_add -y
    description: Add a switch to the inventory to a specified fabric
    enabled: true
    entry_point: switch_add.py
    id: 57acd58718971236df5b4599
    name: switch_add
    notify: {}
    pack: inventory
    parameters:
        fabric:
            description: Name of the Fabric to add
            required: true
            type: string
        host:
            description: IP address of the Device
            required: true
            type: string
        passwd:
            description: Password to connect to the device
            required: true
            secret: true
            type: string
        user:
            description: User to connect to the device
            required: true
            type: string
    ref: inventory.switch_add
    runner_type: run-python
    tags: []
    uid: action:inventory:switch_add

Every action in these packs have Required and Optional paramters. Those paramters can
either be accessed using ``st2 action get <pack-name>.<action-name>`` or
``st2 run <pack-name>.<action-name> -h`` command.

.. note::
    In some actions parameters are mutually exclusive hence they are placed in optional
    parameters section. For example: in following example fabric name or host (switch IP)
    are required, but are mutually exclusive.


.. code-block:: guess
    :emphasize-lines: 1

    $ st2 run inventory.switch_list -h
    List all the devices in the inventory for the specified fabric or
    device IP
    
    Optional Parameters:
        env
            Environment variables which will be available to the script(e.g.
            key1=val1,key2=val2)
            Type: object
    
        fabric
            Name of the Fabric for switches to be listed
            Type: string
    
        host
            IP of the device to be listed
            Type: string
    
        timeout
            Action timeout in seconds. Action will get killed if it doesn't finish
            in timeout seconds.
            Type: integer
            Default: 600
    
Next we will go through the cli required to create |ipf| workflow. Exploring each action
in these packs is beyond the scope of this document.
