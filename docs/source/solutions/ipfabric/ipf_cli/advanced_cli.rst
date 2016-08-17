Advanced CLI (using st2)
========================

.. note::
    All command line examples in this section begins with $ (dollar sign), which represents
    a shell command prompt. Do not enter another dollar sign. All commands should be entered 
    at the shell prompt.

To access |ipf| using |bwc| CLI instead of |ipf| specific CLI use these commands.
However, assumption here is that you are familiar with the StackStorm components like actions,
workflows, rules, packs, execution list etc.

.. todo::
    Add links for st2 components and more details

----------

|bwc| consists of two packs to access bwc-topology services and implement BGP workflow on the
default or user defined fabric. **bwc-topology** and **bwc-ipfabric** pack. These packs
are installed, by default, with |ipf|.

.. todo::
    Add more details/one line each on the packs

The actions in each pack have a small description on what it does.

.. code-block:: guess
    :emphasize-lines: 1,17

    $ st2 action list -p bwc-ipfabric
    +-----------------------------------------+---------------+----------------------------------------------------+
    | ref                                     | pack          |              description                           |
    +-----------------------------------------+---------------+----------------------------------------------------+
    | bwc-ipfabric.configure_anycast          | bwc-ipfabric  | Affect an anycast gateway change on VDX switches   |
    | bwc-ipfabric.configure_bgp              | bwc-ipfabric  | Configure BGP on Brocade VDX Switches              |
    | bwc-ipfabric.configure_bgp_neighbor     | bwc-ipfabric  | Configure BGP neighbor on Brocade VDX Switches     |
    | bwc-ipfabric.configure_bgp_redistribute | bwc-ipfabric  | Configure BGP route redistribution on VDX switches |
    | bwc-ipfabric.configure_fabric           | bwc-ipfabric  | Configure IP fabric                                |
    | bwc-ipfabric.configure_ip               | bwc-ipfabric  | Configure IPs on Brocade VDX Switches              |
    | bwc-ipfabric.configure_switch           | bwc-ipfabric  | Configure switch                                   |
    | bwc-ipfabric.configure_switch_bgp       | bwc-ipfabric  | Configure bgp on switch                            |
    | bwc-ipfabric.configure_switch_ifaces    | bwc-ipfabric  | Configure switch interfaces                        |
    | bwc-ipfabric.inventory                  | bwc-ipfabric  | Query inventory service to constuct the inventory. |
    +-----------------------------------------+---------------+----------------------------------------------------+ 
    
    $ st2 action list -p bwc-topology
    +-----------------------------------+--------------+---------------------------------------------------------------------------------------+
    | ref                               |    pack      | description                                                                           |
    +-----------------------------------+--------------+---------------------------------------------------------------------------------------+
    | bwc-topology.fabric_add           | bwc-topology | Add a fabric to the inventory                                                         |
    | bwc-topology.fabric_config_add    | bwc-topology | Add/Update the specified fabric parameter for the specified fabric from the inventory |
    | bwc-topology.fabric_config_delete | bwc-topology | Delete the specified fabric parameter for the specified fabric from the inventory     |
    | bwc-topology.fabric_delete        | bwc-topology | Delete a fabric from the inventory                                                    |
    | bwc-topology.fabric_list          | bwc-topology | List all the fabrics in the inventory or the specified fabric details                 |
    | bwc-topology.show_config_bgp      | bwc-topology | Lists BGP config details in the inventory for the specified fabric or device IP       |
    | bwc-topology.show_lldp_links      | bwc-topology | List all the lldp links in the inventory for the specified fabric                     |
    | bwc-topology.show_vcs_links       | bwc-topology | List all the vcs links in the inventory for the specified fabric                      |
    | bwc-topology.switch_add           | bwc-topology | Add a switch to the inventory to a specified fabric                                   |
    | bwc-topology.switch_delete        | bwc-topology | Deletes the specified switch from the Fabric                                          |
    | bwc-topology.switch_list          | bwc-topology | List all the devices in the bwc-topology for the specified fabric or device IP        |
    | bwc-topology.switch_update        | bwc-topology | Update a details of single switch or all the switches in the Fabric                   |
    | bwc-topology.topology_generate    | bwc-topology | Generate the topology for the specified Fabric                                        |
    +-----------------------------------+--------------+---------------------------------------------------------------------------------------+

For more details about actions in these packs use ``st2 action get <pack-name>.<action-name>``
command. The output can also be displayed in YAML format by appending the command with ``-y``
flag.

.. code-block:: guess
    :emphasize-lines: 1,41

    $ st2 action get bwc-topology.switch_add
    +-------------+------------------------------------------------------------+
    | Property    | Value                                                      |
    +-------------+------------------------------------------------------------+
    | id          | 57acd58718971236df5b4599                                   |
    | uid         | action:bwc-topology:switch_add                             |
    | ref         | bwc-topology.switch_add                                    |
    | pack        | bwc-topology                                               |
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
    
    $ st2 action get bwc-topology.switch_add -y
    description: Add a switch to the inventory to a specified fabric
    enabled: true
    entry_point: switch_add.py
    id: 57acd58718971236df5b4599
    name: switch_add
    notify: {}
    pack: bwc-topology
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
    ref: bwc-topology.switch_add
    runner_type: run-python
    tags: []
    uid: action:bwc-topology:switch_add

Every action in these packs have *Required* and *Optional* paramters. These paramters can
either be accessed using ``st2 action get <pack-name>.<action-name>`` or
``st2 run <pack-name>.<action-name> -h`` command.

.. note::
    In some actions parameters are mutually exclusive hence they are placed in optional
    parameters section. For example: in following example fabric name or host (switch IP)
    are required, but are mutually exclusive.


.. code-block:: guess
    :emphasize-lines: 1

    $ st2 run bwc-topology.switch_list -h
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
    
Next, we will go through the CLI required for |ipf| workflow. Exploring each action
in these packs is beyond the scope of this document.

-----------------

-----------------
Fabric Management
-----------------

Fabric List
-----------

The concept of fabric, *default* or user defined and switch roles i.e *spine* or *leaf* is
|bwc| specific. The VDX switches doesn't have any information about it.

Let us start with ``bwc-topology.fabric_list`` to get the details about the *default* fabric.
This is a |ipf| out of the box fabric consisting specific paramters for IP fabric creation:

.. code-block:: guess
    :emphasize-lines: 1

    $ st2 run bwc-topology.fabric_list

    .
    id: 57b201fc1897122c79575bdf
    status: succeeded
    parameters: None
    result:
      exit_code: 0
      result:
      - fabric_name: default
        fabric_settings:
          allowas_in: '5'
          anycast_mac: aabb.ccdd.eeff
          bfd_multiplier: '3'
          bfd_rx: '300'
          bfd_tx: '300'
          bgp_multihop: '5'
          evpn_enabled: 'Yes'
          leaf_asn_block: 65000-65534
          loopback_ip_range: 172.32.254.0/24
          loopback_port_number: '1'
          max_paths: '8'
          p2p_link_range: 10.10.10.0/23
          spine_asn_block: 64512-64999
      stderr: 'st2.actions.python.ListFabric: DEBUG    GET http://127.0.0.1:8888/v1/fabrics
    
        '
      stdout: 'Successfully retrieved the fabric details.  Object details:
    
        '

For detail on fabric paramters refer :doc:`./basic_cli` 's ``bwc ipf fabric config`` section.

----------

On the side note, the values in the output can also be accessed using ``--attr`` and ``-k`` flag:

.. code-block:: guess
   :emphasize-lines: 1,9

   $ st2 run bwc-topology.fabric_list -k result[0].fabric_settings
   .
   {u'bgp_multihop': u'5', u'spine_asn_block': u'64512-64999', u'leaf_asn_block': u'65000-65534',
   u'allowas_in': u'5', u'max_paths': u'8', u'bfd_multiplier': u'3', u'p2p_link_range':
   u'10.10.10.0/23', u'loopback_port_number': u'1', u'bfd_tx': u'300', u'anycast_mac':
   u'aabb.ccdd.eeff', u'evpn_enabled': u'Yes', u'loopback_ip_range': u'172.32.254.0/24',
   u'bfd_rx': u'300'}
   
   $ st2 run bwc-topology.fabric_list --attr result.result[0].fabric_settings
   .
   result.result[0].fabric_settings:
     allowas_in: '5'
     anycast_mac: aabb.ccdd.eeff
     bfd_multiplier: '3'
     bfd_rx: '300'
     bfd_tx: '300'
     bgp_multihop: '5'
     evpn_enabled: 'Yes'
     leaf_asn_block: 65000-65534
     loopback_ip_range: 172.32.254.0/24
     loopback_port_number: '1'
     max_paths: '8'
     p2p_link_range: 10.10.10.0/23
     spine_asn_block: 64512-64999

----------

Create User Defined Fabric
--------------------------

|ipf| supports user-defined fabric with user-defined parameters.

.. note::
    **default** fabric has *p2p_link_range* with a range of IP address which results in
    IP numbered fabric. To get IP unnumbered fabric the *p2p_link_range* should be set
    as string **"unnumbered"**.

1. First create a user-defined custom fabric:

.. code-block:: shell
    
   $ st2 run bwc-topology.fabric_add fabric=new_fabric
   .
   id: 57b23ac61897122c79575c30
   status: succeeded
   parameters:
     fabric: new_fabric
   result:
     exit_code: 0
     result:
       Fabric: new_fabric
     stderr: 'st2.actions.python.AddFabric: DEBUG    POST http://127.0.0.1:8888/v1/fabric
     with data <module ''json'' from ''/usr/lib/python2.7/json/__init__.pyc''>
   
       '
     stdout: 'Successfully added the fabric.  Object details:
   
       '

2. Add parameters to the custom fabric:

.. warning::
   The mandatory paramters i.e. **leaf_asn_block**, **spine_asn_block**, **loopback_ip_range**,
   **loopback_port_number**, **p2p_link_range** cannot be edited. Please double check before 
   Otherwise switch registration to this fabric will fail.

.. code-block:: shell
   :emphasize-lines: 1,21,41,61,81
   
   $ st2 run bwc-topology.fabric_config_add fabric=new_fabric key=p2p_link_range value="unnumbered"
   .
    id: 57b23c4d1897122c79575c33
    status: succeeded
    parameters:
      fabric: new_fabric
      key: p2p_link_range
      value: unnumbered
    result:
      exit_code: 0
      result:
        p2p_link_range: unnumbered
      stderr: 'st2.actions.python.AddFabricConfig: DEBUG    PUT http://127.0.0.1:8888/v1/fabric
      with data {''value'': ''unnumbered'', ''fabric'': ''new_fabric'', ''key'': ''p2p_link_range''}
    
        '
      stdout: 'Successfully added/updated the fabric parameter.  Object details:
    
        '

   $ st2 run bwc-topology.fabric_config_add fabric=new_fabric key=leaf_asn_block value=6500-6600
   .
    id: 57b23cc61897122c79575c36
    status: succeeded
    parameters:
      fabric: new_fabric
      key: leaf_asn_block
      value: 6500-6600
    result:
      exit_code: 0
      result:
        leaf_asn_block: 6500-6600
      stderr: 'st2.actions.python.AddFabricConfig: DEBUG    PUT http://127.0.0.1:8888/v1/fabric
      with data {''value'': ''6500-6600'', ''fabric'': ''new_fabric'', ''key'': ''leaf_asn_block''}
    
        '
      stdout: 'Successfully added/updated the fabric parameter.  Object details:
    
        '

   $ st2 run bwc-topology.fabric_config_add fabric=new_fabric key=spine_asn_block value=6000-6400
    ..
    id: 57b23dc61897122c79575c39
    status: succeeded
    parameters:
      fabric: new_fabric
      key: spine_asn_block
      value: 6000-6400
    result:
      exit_code: 0
      result:
        spine_asn_block: 6000-6400
      stderr: 'st2.actions.python.AddFabricConfig: DEBUG    PUT http://127.0.0.1:8888/v1/fabric
      with data {''value'': ''6000-6400'', ''fabric'': ''new_fabric'', ''key'': ''spine_asn_block''}
    
        '
      stdout: 'Successfully added/updated the fabric parameter.  Object details:
    
        '

   $ st2 run bwc-topology.fabric_config_add fabric=new_fabric key=loopback_ip_range value=172.32.254.0/24
   .
    id: 57b23e751897122c79575c3c
    status: succeeded
    parameters:
      fabric: new_fabric
      key: loopback_ip_range
      value: 172.32.254.0/24
    result:
      exit_code: 0
      result:
        loopback_ip_range: 172.32.254.0/24
      stderr: 'st2.actions.python.AddFabricConfig: DEBUG    PUT http://127.0.0.1:8888/v1/fabric
      with data {''value'': ''172.32.254.0/24'', ''fabric'': ''new_fabric'', ''key'': ''loopback_ip_range''}
    
        '
      stdout: 'Successfully added/updated the fabric parameter.  Object details:
    
        '

   $ st2 run bwc-topology.fabric_config_add fabric=new_fabric key=loopback_port_number value=1
   .
    id: 57b23ec81897122c79575c3f
    status: succeeded
    parameters:
      fabric: new_fabric
      key: loopback_port_number
      value: '1'
    result:
      exit_code: 0
      result:
        loopback_port_number: '1'
      stderr: 'st2.actions.python.AddFabricConfig: DEBUG    PUT http://127.0.0.1:8888/v1/fabric
      with data {''value'': ''1'', ''fabric'': ''new_fabric'', ''key'': ''loopback_port_number''}
    
        '
      stdout: 'Successfully added/updated the fabric parameter.  Object details:
    
        '
.. note::
    The user-defined fabric should have all the mandatory values i.e **leaf_asn_block**,
    **spine_asn_block**, **loopback_ip_range**, **loopback_port_number**, **p2p_link_range**.
    Otherwise switch registration to this fabric will fail.

3. (Optional) Add optional parameters to the *custom-fabric*, if required, otherwise values from
   **default** fabric are used:

.. code-block:: shell
    :emphasize-lines: 1,21,41,61,81,101,121

    $ st2 run bwc-topology.fabric_config_add fabric=new_fabric key=anycast_mac value=ccff.aadd.eeff
    .
    id: 57b242451897122c79575c45
    status: succeeded
    parameters:
      fabric: new_fabric
      key: anycast_mac
      value: ccff.aadd.eeff
    result:
      exit_code: 0
      result:
        anycast_mac: ccff.aadd.eeff
      stderr: 'st2.actions.python.AddFabricConfig: DEBUG    PUT http://127.0.0.1:8888/v1/fabric
      with data {''value'': ''ccff.aadd.eeff'', ''fabric'': ''new_fabric'', ''key'': ''anycast_mac''}
    
        '
      stdout: 'Successfully added/updated the fabric parameter.  Object details:
    
        '
    
    $ st2 run bwc-topology.fabric_config_add fabric=new_fabric key=max_paths value=8
    .
    id: 57b2426b1897122c79575c48
    status: succeeded
    parameters:
      fabric: new_fabric
      key: max_paths
      value: '8'
    result:
      exit_code: 0
      result:
        max_paths: '8'
      stderr: 'st2.actions.python.AddFabricConfig: DEBUG    PUT http://127.0.0.1:8888/v1/fabric
      with data {''value'': ''8'', ''fabric'': ''new_fabric'', ''key'': ''max_paths''}
    
        '
      stdout: 'Successfully added/updated the fabric parameter.  Object details:
    
        '
    
    $ st2 run bwc-topology.fabric_config_add fabric=new_fabric key=bfd_multiplier value=5
    .
    id: 57b242951897122c79575c4b
    status: succeeded
    parameters:
      fabric: new_fabric
      key: bfd_multiplier
      value: '5'
    result:
      exit_code: 0
      result:
        bfd_multiplier: '5'
      stderr: 'st2.actions.python.AddFabricConfig: DEBUG    PUT http://127.0.0.1:8888/v1/fabric
      with data {''value'': ''5'', ''fabric'': ''new_fabric'', ''key'': ''bfd_multiplier''}
    
        '
      stdout: 'Successfully added/updated the fabric parameter.  Object details:
    
        '
    
    $ st2 run bwc-topology.fabric_config_add fabric=new_fabric key=bfd_rx value=400
    .
    id: 57b243151897122c79575c4e
    status: succeeded
    parameters:
      fabric: new_fabric
      key: bfd_rx
      value: '400'
    result:
      exit_code: 0
      result:
        bfd_rx: '400'
      stderr: 'st2.actions.python.AddFabricConfig: DEBUG    PUT http://127.0.0.1:8888/v1/fabric
      with data {''value'': ''400'', ''fabric'': ''new_fabric'', ''key'': ''bfd_rx''}
    
        '
      stdout: 'Successfully added/updated the fabric parameter.  Object details:
    
        '
    
    $ st2 run bwc-topology.fabric_config_add fabric=new_fabric key=bfd_tx value=400
    .
    id: 57b243171897122c79575c51
    status: succeeded
    parameters:
      fabric: new_fabric
      key: bfd_tx
      value: '400'
    result:
      exit_code: 0
      result:
        bfd_tx: '400'
      stderr: 'st2.actions.python.AddFabricConfig: DEBUG    PUT http://127.0.0.1:8888/v1/fabric
      with data {''value'': ''400'', ''fabric'': ''new_fabric'', ''key'': ''bfd_tx''}
    
        '
      stdout: 'Successfully added/updated the fabric parameter.  Object details:
    
        '
    
    $ st2 run bwc-topology.fabric_config_add fabric=new_fabric key=bgp_multihop value=8
    .
    id: 57b2431a1897122c79575c54
    status: succeeded
    parameters:
      fabric: new_fabric
      key: bgp_multihop
      value: '8'
    result:
      exit_code: 0
      result:
        bgp_multihop: '8'
      stderr: 'st2.actions.python.AddFabricConfig: DEBUG    PUT http://127.0.0.1:8888/v1/fabric
      with data {''value'': ''8'', ''fabric'': ''new_fabric'', ''key'': ''bgp_multihop''}
    
        '
      stdout: 'Successfully added/updated the fabric parameter.  Object details:
    
        '
    
    $ st2 run bwc-topology.fabric_config_add fabric=new_fabric key=evpn_enabled value=no
    .
    id: 57b2431e1897122c79575c57
    status: succeeded
    parameters:
      fabric: new_fabric
      key: evpn_enabled
      value: 'no'
    result:
      exit_code: 0
      result:
        evpn_enabled: 'no'
      stderr: 'st2.actions.python.AddFabricConfig: DEBUG    PUT http://127.0.0.1:8888/v1/fabric
      with data {''value'': ''no'', ''fabric'': ''new_fabric'', ''key'': ''evpn_enabled''}
    
        '
      stdout: 'Successfully added/updated the fabric parameter.  Object details:
    
        '

4. Similarly following commands can be used to delete the custom fabric and fabric parameters:

.. code:: shell

    st2 run bwc-topology.fabric_config_delete fabric=new_fabric key=anycast_mac

    st2 run bwc-topology.fabric_delete fabric=new_fab

----------

-----------------
Switch Management
-----------------

Register, delete and update switch
----------------------------------

After creating *custom fabric* we can register/update/delete switches to the fabric or add
switches to the *default* fabric:

.. code-block:: shell
    :emphasize-lines: 1,40,80

    $ st2 run bwc-topology.switch_add fabric=default host=10.24.39.224 user=admin passwd=password
    ...
    id: 57b24efb1897122c79575c66
    status: succeeded
    parameters:
      fabric: default
      host: 10.24.39.224
      passwd: '********'
      user: admin
    result:
      exit_code: 0
      result:
        asn: 64517
        fabric:
          fabric_id: 1
          fabric_name: default
        firmware: 7.1.0
        id: 9
        ip_address: 10.24.39.224
        model: VDX6740
        name: VDX_224
        rbridge_id: 224
        role: Spine
        serial: CPL2519K02F
        uuid: 93acc03c-acfc-5d3e-8238-64dc43bb4c57
      stderr: 'No handlers could be found for logger "st2.st2common.services.access"
    
        st2.actions.python.None: AUDIT    Setting value in the datastore (name=switch.10.24.39.224.user)
    
        st2.actions.python.None: AUDIT    Setting value in the datastore (name=switch.10.24.39.224.passwd)
    
        st2.actions.python.AddSwitchAction: DEBUG    POST http://127.0.0.1:8888/v1/switch with data
        <module ''json'' from ''/usr/lib/python2.7/json/__init__.pyc''>
    
        '
      stdout: 'Successfully registered the device.  Object details:
    
        '
    
    $ st2 run bwc-topology.switch_update fabric=default host=10.24.39.224 user=admin passwd=password
    ..
    id: 57b24f471897122c79575c6e
    status: succeeded
    parameters:
      fabric: default
      host: 10.24.39.224
      passwd: '********'
      user: admin
    result:
      exit_code: 0
      result:
      - - Object updated
        - asn: 64517
          fabric:
            fabric_id: 1
            fabric_name: default
          firmware: 7.1.0
          id: 9
          ip_address: 10.24.39.224
          model: VDX6740
          name: VDX_224
          rbridge_id: 224
          role: Spine
          serial: CPL2519K02F
          uuid: 93acc03c-acfc-5d3e-8238-64dc43bb4c57
      stderr: 'No handlers could be found for logger "st2.st2common.services.access"
    
        st2.actions.python.None: AUDIT    Setting value in the datastore (name=switch.10.24.39.224.user)
    
        st2.actions.python.None: AUDIT    Setting value in the datastore (name=switch.10.24.39.224.passwd)
    
        st2.actions.python.UpdateSwitch: DEBUG    PUT http://127.0.0.1:8888/v1/switch with data
        {''fabric_name'': u''default'', ''ip_address'': u''10.24.39.224'', ''password'': u''password'', ''user_name'': u''admin''}
    
        '
      stdout: 'Successfully updated devices in fabric.  Object details:
    
        '
    
    $ st2 run bwc-topology.switch_delete host=10.24.39.224
    .
    id: 57b24f5f1897122c79575c71
    status: succeeded
    parameters:
      host: 10.24.39.224
    result:
      exit_code: 0
      result:
        asn: 64517
        fabric:
          fabric_id: 1
          fabric_name: default
        firmware: 7.1.0
        id: 9
        ip_address: 10.24.39.224
        model: VDX6740
        name: VDX_224
        rbridge_id: 224
        role: Spine
        serial: CPL2519K02F
        uuid: 93acc03c-acfc-5d3e-8238-64dc43bb4c57
      stderr: 'st2.actions.python.DeleteSwitch: DEBUG    Delete http://127.0.0.1:8888/v1/switch with data
      {''ip_address'': u''10.24.39.224''}
    
        No handlers could be found for logger "st2.st2common.services.access"
    
        st2.actions.python.None: AUDIT    Deleting value from the datastore (name=switch.10.24.39.224.user)
    
        st2.actions.python.None: AUDIT    Deleting value from the datastore (name=switch.10.24.39.224.passwd)
    
        '
      stdout: 'Successfully deleted the device.  Object details:
    
        '

All the switches in the fabric can be updated at once by giving ``fabric=<fabric name>``
to ``st2 run bwc-topology.switch_update`` command instead of switch IP address:

.. code:: shell

   $ st2 run bwc-topology.switch_update fabric=default
   ...
   id: 57b256f71897122c79575d43
   status: succeeded
   parameters:
     fabric: default
   result:
     exit_code: 0
     result:
     - - Object updated
       - asn: ''
         fabric:
           fabric_id: 1
           fabric_name: default
         firmware: 7.1.0
         id: 12
         ip_address: 10.24.39.225
         model: VDX6740
         name: sw0
         rbridge_id: 225
         role: Leaf
         serial: CPL2526K050
         uuid: f1582418-22fa-5fa9-bd55-8b53e9f33860
     - - Object updated
       - asn: ''
         fabric:
           fabric_id: 1
           fabric_name: default
         firmware: 7.1.0
         id: 11
         ip_address: 10.24.39.224
         model: VDX6740
         name: VDX_224
         rbridge_id: 224
         role: Spine
         serial: CPL2519K02F
         uuid: 93acc03c-acfc-5d3e-8238-64dc43bb4c57
     - - Object updated
       - asn: ''
         fabric:
           fabric_id: 1
           fabric_name: default
         firmware: 7.1.0
         id: 14
         ip_address: 10.24.39.229
         model: VDX6740
         name: VCS_VDX_39_229
         rbridge_id: 229
         role: Leaf
         serial: CPL2526K04N
         uuid: f5f5c65b-0301-5705-ae9c-fe406781d246
     - - Object updated
       - asn: ''
         fabric:
           fabric_id: 1
           fabric_name: default
         firmware: 7.1.0
         id: 13
         ip_address: 10.24.39.228
         model: VDX6740
         name: VCS_VDX_39_228
         rbridge_id: 228
         role: Leaf
         serial: CPL2517K04C
         uuid: ac584c8c-0867-539e-89ec-bef9e87e3883
     stderr: 'st2.actions.python.UpdateSwitch: DEBUG    PUT http://127.0.0.1:8888/v1/switches with data {''fabric_name'': u''default''}
   
       '
     stdout: 'Successfully updated devices in fabric.  Object details:
   
       '

--------------

------------
BGP Workflow
------------

After you have registered all the switches in the fabric. Use following command to execute BGP
workflow:

.. code-block:: shell
  
   $ st2 run bwc-ipfabric.configure_fabric
   ...........................................
   id: 57b252a31897122c79575c79
   action.ref: bwc-ipfabric.configure_fabric
   parameters: None
   status: failed
   start_timestamp: 2016-08-15T23:39:15.578086Z
   end_timestamp: 2016-08-15T23:40:44.828279Z
   +------------------------------+-------------------------+------------------------------------+-----------------------------------------+-------------------------------+
   | id                           | status                  | task                               | action                                  | start_timestamp               |
   +------------------------------+-------------------------+------------------------------------+-----------------------------------------+-------------------------------+
   |   57b252a41897122c79575c7c   | succeeded (16s elapsed) | get_inventory                      | bwc-ipfabric.inventory                  | Mon, 15 Aug 2016 23:39:16 UTC |
   | + 57b252b41897122c79575c7e   | succeeded (27s elapsed) | configure_switches                 | bwc-ipfabric.configure_switch           | Mon, 15 Aug 2016 23:39:32 UTC |
   |  + 57b252b61897122c79575c86  | succeeded (20s elapsed) | configure_interfaces               | bwc-ipfabric.configure_switch_ifaces    | Mon, 15 Aug 2016 23:39:34 UTC |
   |     57b252b81897122c79575c8c | failed (5s elapsed)     | configure_interface                | bwc-ipfabric.configure_ip               | Mon, 15 Aug 2016 23:39:36 UTC |
   |     57b252be1897122c79575c98 | succeeded (9s elapsed)  | configure_interface                | bwc-ipfabric.configure_ip               | Mon, 15 Aug 2016 23:39:42 UTC |
   | + 57b252b51897122c79575c80   | succeeded (66s elapsed) | configure_switches                 | bwc-ipfabric.configure_switch           | Mon, 15 Aug 2016 23:39:33 UTC |
   |  + 57b252b81897122c79575c92  | succeeded (34s elapsed) | configure_interfaces               | bwc-ipfabric.configure_switch_ifaces    | Mon, 15 Aug 2016 23:39:36 UTC |
   |     57b252ba1897122c79575c94 | succeeded (5s elapsed)  | configure_interface                | bwc-ipfabric.configure_ip               | Mon, 15 Aug 2016 23:39:38 UTC |
   |     57b252c01897122c79575c9c | succeeded (11s elapsed) | configure_interface                | bwc-ipfabric.configure_ip               | Mon, 15 Aug 2016 23:39:44 UTC |
   |     57b252cb1897122c79575c9e | succeeded (9s elapsed)  | configure_interface                | bwc-ipfabric.configure_ip               | Mon, 15 Aug 2016 23:39:55 UTC |
   |     57b252d51897122c79575ca8 | succeeded (3s elapsed)  | configure_interface                | bwc-ipfabric.configure_ip               | Mon, 15 Aug 2016 23:40:05 UTC |
   |  + 57b252db1897122c79575cae  | succeeded (23s elapsed) | configure_bgp                      | bwc-ipfabric.configure_switch_bgp       | Mon, 15 Aug 2016 23:40:11 UTC |
   |     57b252dc1897122c79575cb0 | succeeded (4s elapsed)  | configure_bgp                      | bwc-ipfabric.configure_bgp              | Mon, 15 Aug 2016 23:40:12 UTC |
   |     57b252e11897122c79575cb6 | succeeded (3s elapsed)  | configure_bgp_redistributed_routes | bwc-ipfabric.configure_bgp_redistribute | Mon, 15 Aug 2016 23:40:17 UTC |
   |     57b252e51897122c79575cb8 | succeeded (5s elapsed)  | configure_bgp_peers                | bwc-ipfabric.configure_bgp_neighbor     | Mon, 15 Aug 2016 23:40:21 UTC |
   |     57b252e51897122c79575cba | succeeded (9s elapsed)  | configure_bgp_peers                | bwc-ipfabric.configure_bgp_neighbor     | Mon, 15 Aug 2016 23:40:21 UTC |
   |     57b252e61897122c79575cc0 | succeeded (9s elapsed)  | configure_bgp_peers                | bwc-ipfabric.configure_bgp_neighbor     | Mon, 15 Aug 2016 23:40:21 UTC |
   |     57b252e61897122c79575cbd | succeeded (8s elapsed)  | configure_bgp_peers                | bwc-ipfabric.configure_bgp_neighbor     | Mon, 15 Aug 2016 23:40:21 UTC |
   |     57b252e61897122c79575cbf | succeeded (9s elapsed)  | configure_bgp_peers                | bwc-ipfabric.configure_bgp_neighbor     | Mon, 15 Aug 2016 23:40:22 UTC |
   | + 57b252b51897122c79575c82   | succeeded (62s elapsed) | configure_switches                 | bwc-ipfabric.configure_switch           | Mon, 15 Aug 2016 23:39:33 UTC |
   |  + 57b252b71897122c79575c8a  | succeeded (20s elapsed) | configure_interfaces               | bwc-ipfabric.configure_switch_ifaces    | Mon, 15 Aug 2016 23:39:35 UTC |
   |     57b252b81897122c79575c90 | succeeded (6s elapsed)  | configure_interface                | bwc-ipfabric.configure_ip               | Mon, 15 Aug 2016 23:39:36 UTC |
   |     57b252bf1897122c79575c9a | succeeded (10s elapsed) | configure_interface                | bwc-ipfabric.configure_ip               | Mon, 15 Aug 2016 23:39:43 UTC |
   |  + 57b252cc1897122c79575ca0  | succeeded (29s elapsed) | configure_bgp                      | bwc-ipfabric.configure_switch_bgp       | Mon, 15 Aug 2016 23:39:56 UTC |
   |     57b252cd1897122c79575ca4 | succeeded (10s elapsed) | configure_bgp                      | bwc-ipfabric.configure_bgp              | Mon, 15 Aug 2016 23:39:57 UTC |
   |     57b252d81897122c79575caa | succeeded (5s elapsed)  | configure_bgp_redistributed_routes | bwc-ipfabric.configure_bgp_redistribute | Mon, 15 Aug 2016 23:40:08 UTC |
   |     57b252de1897122c79575cb4 | succeeded (7s elapsed)  | configure_bgp_peers                | bwc-ipfabric.configure_bgp_neighbor     | Mon, 15 Aug 2016 23:40:14 UTC |
   |    57b252ea1897122c79575cc2  | succeeded (5s elapsed)  | configure_anycast_gateway          | bwc-ipfabric.configure_anycast          | Mon, 15 Aug 2016 23:40:26 UTC |
   | + 57b252b51897122c79575c84   | succeeded (61s elapsed) | configure_switches                 | bwc-ipfabric.configure_switch           | Mon, 15 Aug 2016 23:39:33 UTC |
   |  + 57b252b71897122c79575c88  | succeeded (20s elapsed) | configure_interfaces               | bwc-ipfabric.configure_switch_ifaces    | Mon, 15 Aug 2016 23:39:35 UTC |
   |     57b252b81897122c79575c8e | succeeded (5s elapsed)  | configure_interface                | bwc-ipfabric.configure_ip               | Mon, 15 Aug 2016 23:39:36 UTC |
   |     57b252be1897122c79575c96 | succeeded (11s elapsed) | configure_interface                | bwc-ipfabric.configure_ip               | Mon, 15 Aug 2016 23:39:42 UTC |
   |  + 57b252cc1897122c79575ca2  | succeeded (29s elapsed) | configure_bgp                      | bwc-ipfabric.configure_switch_bgp       | Mon, 15 Aug 2016 23:39:56 UTC |
   |     57b252ce1897122c79575ca6 | succeeded (10s elapsed) | configure_bgp                      | bwc-ipfabric.configure_bgp              | Mon, 15 Aug 2016 23:39:58 UTC |
   |     57b252d91897122c79575cac | succeeded (4s elapsed)  | configure_bgp_redistributed_routes | bwc-ipfabric.configure_bgp_redistribute | Mon, 15 Aug 2016 23:40:09 UTC |
   |     57b252de1897122c79575cb2 | succeeded (7s elapsed)  | configure_bgp_peers                | bwc-ipfabric.configure_bgp_neighbor     | Mon, 15 Aug 2016 23:40:14 UTC |
   |    57b252ec1897122c79575cc4  | succeeded (4s elapsed)  | configure_anycast_gateway          | bwc-ipfabric.configure_anycast          | Mon, 15 Aug 2016 23:40:28 UTC |
   +------------------------------+-------------------------+------------------------------------+-----------------------------------------+-------------------------------+

.. note::
    This command runs on **default** fabric if fabric name is not provided.


Detail of each action execution in the workflow can be found using the execution id.
Use ``st2 execution get <execution id>`` command to get the details:


-------------

-------------
Show commands
-------------

There are few show commands to get details about BGP configuration, vcs links and lldp neighbor
and command to generate topology:

Show BGP configuration on the switches
--------------------------------------

After BGP workflow execution:

.. code:: shell
   
   bgp


Show LLDP links among the neighbors
-----------------------------------

After discovering the switches:

.. code:: shell

   $ st2 run bwc-topology.show_lldp_links fabric=default
   .
   id: 57b256631897122c79575d40
   status: succeeded
   parameters:
     fabric: default
   result:
     exit_code: 0
     result:
     - asn: 65003
       id: 14
       ip_address: 10.24.39.229
       lldp_data:
       - local_int_mac: 50:eb:1a:21:19:27
         local_int_name: FortyGigabitEthernet 229/0/49
         remote_chassis_id: 50eb.1a16.1d88
         remote_int_mac: 50:eb:1a:16:1d:c0
         remote_int_name: FortyGigabitEthernet 224/0/50
         remote_management_address: 10.24.39.224
         remote_system_name: VDX_224
       - local_int_mac: 50:eb:1a:21:19:28
         local_int_name: FortyGigabitEthernet 229/0/50
         remote_chassis_id: 0027.f8c5.bfbb
         remote_int_mac: 00:27:f8:c5:bf:f3
         remote_int_name: FortyGigabitEthernet 223/0/50
         remote_management_address: ''
         remote_system_name: sw0
       model: VDX6740
       rbridge_id: 229
       role: Leaf
       serial: CPL2526K04N
     - asn: 64514
       id: 11
       ip_address: 10.24.39.224
       lldp_data:
       - local_int_mac: 50:eb:1a:16:1d:8f
         local_int_name: TenGigabitEthernet 224/0/1
         remote_chassis_id: 50eb.1a22.50b2
         remote_int_mac: 50:eb:1a:22:50:ba
         remote_int_name: TenGigabitEthernet 225/0/2
         remote_management_address: ''
         remote_system_name: sw0
       - local_int_mac: 50:eb:1a:16:1d:90
         local_int_name: TenGigabitEthernet 224/0/2
         remote_chassis_id: 50eb.1a35.296e
         remote_int_mac: 50:eb:1a:35:29:75
         remote_int_name: TenGigabitEthernet 26/0/1
         remote_management_address: ''
         remote_system_name: sw0
       - local_int_mac: 50:eb:1a:16:1d:bf
         local_int_name: FortyGigabitEthernet 224/0/49
         remote_chassis_id: 50eb.1a22.c96d
         remote_int_mac: 50:eb:1a:22:c9:a5
         remote_int_name: FortyGigabitEthernet 227/0/50
         remote_management_address: ''
         remote_system_name: sw0
       - local_int_mac: 50:eb:1a:16:1d:c0
         local_int_name: FortyGigabitEthernet 224/0/50
         remote_chassis_id: 50eb.1a21.18f0
         remote_int_mac: 50:eb:1a:21:19:27
         remote_int_name: FortyGigabitEthernet 229/0/49
         remote_management_address: 10.24.39.229
         remote_system_name: VCS_VDX_39_229
       - local_int_mac: 50:eb:1a:16:1d:c1
         local_int_name: FortyGigabitEthernet 224/0/51
         remote_chassis_id: 50eb.1a13.9e96
         remote_int_mac: 50:eb:1a:13:9e:cd
         remote_int_name: FortyGigabitEthernet 228/0/49
         remote_management_address: 10.24.39.228
         remote_system_name: VCS_VDX_39_228
       model: VDX6740
       rbridge_id: 224
       role: Spine
       serial: CPL2519K02F
     - asn: 65004
       id: 12
       ip_address: 10.24.39.225
       lldp_data:
       - local_int_mac: 50:eb:1a:22:50:b9
         local_int_name: TenGigabitEthernet 225/0/1
         remote_chassis_id: 0027.f8c5.bfbb
         remote_int_mac: 00:27:f8:c5:bf:c2
         remote_int_name: TenGigabitEthernet 223/0/1
         remote_management_address: ''
         remote_system_name: sw0
       - local_int_mac: 50:eb:1a:22:50:ba
         local_int_name: TenGigabitEthernet 225/0/2
         remote_chassis_id: 50eb.1a16.1d88
         remote_int_mac: 50:eb:1a:16:1d:8f
         remote_int_name: TenGigabitEthernet 224/0/1
         remote_management_address: 10.24.39.224
         remote_system_name: VDX_224
       model: VDX6740
       rbridge_id: 225
       role: Leaf
       serial: CPL2526K050
     - asn: 65003
       id: 13
       ip_address: 10.24.39.228
       lldp_data:
       - local_int_mac: 50:eb:1a:13:9e:9d
         local_int_name: TenGigabitEthernet 228/0/1
         remote_chassis_id: 0027.f8c5.bfbb
         remote_int_mac: 00:27:f8:c5:bf:c5
         remote_int_name: TenGigabitEthernet 223/0/4
         remote_management_address: ''
         remote_system_name: sw0
       - local_int_mac: 50:eb:1a:13:9e:cd
         local_int_name: FortyGigabitEthernet 228/0/49
         remote_chassis_id: 50eb.1a16.1d88
         remote_int_mac: 50:eb:1a:16:1d:c1
         remote_int_name: FortyGigabitEthernet 224/0/51
         remote_management_address: 10.24.39.224
         remote_system_name: VDX_224
       model: VDX6740
       rbridge_id: 228
       role: Leaf
       serial: CPL2517K04C
     stderr: 'st2.actions.python.ShowLLDPLinks: DEBUG    GET http://127.0.0.1:8888/v1/switches/lldp?fabric_name=default
   
       st2.actions.python.ShowLLDPLinks: INFO     Successfully retrieved the lldp links details.  Object details:
   
       '
     stdout: ''


Show VCS links between the leaves
---------------------------------

If the fabric consists of switches in VCS mode, this command will show the status of 
links between principle and secondary node:

.. code:: shell

   $ st2 run bwc-topology.show_vcs_links fabric=default
   .
   id: 57b256311897122c79575d3d
   status: succeeded
   parameters:
     fabric: default
   result:
     exit_code: 0
     result:
     - - fabric: default
         id: 13
         interface: TenGigabitEthernet 228/0/10
         ip_address: 10.24.39.228
         role: Leaf
       - fabric: default
         id: 14
         interface: TenGigabitEthernet 229/0/10
         ip_address: 10.24.39.229
         role: Leaf
       - is_missing: 'No'
         missing_time: ''
     stderr: 'st2.actions.python.ShowVcsLinks: DEBUG    GET http://127.0.0.1:8888/v1/switches/vcs/links?fabric_name=default
   
       st2.actions.python.ShowVcsLinks: INFO     Successfully retrieved the vcs links details.  Object details:
   
       '
     stdout: ''
   
