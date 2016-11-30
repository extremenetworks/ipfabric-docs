Advanced CLI (using st2)
========================

.. note::
    All command line examples in this section begins with ``$`` (dollar sign), which represents
    a shell command prompt. Do not enter another dollar sign. All commands should be entered 
    at the shell prompt.

This section is about accessing |ipf| with original |bwc| CLI instead of |ipf|-specific CLI.
You will need to familiarise yourself with |bwc| components like actions, workflows, packs, 
execution list etc.

See the |bwc| :doc:`CLI reference documentation </reference/cli>` for more details.


----------

|bwc| consists of two packs for |ipf| services and workflows: **bwc_topology** and **bwc_ipfabric** pack. 
These packs are automatically installed with the |ipf|.

* **bwc_topology**: Topology-related actions such as show topology, configure BGP, etc. Includes lightweight topology 
  service providing database of network topology (device details, interfaces, LLDP neighbors, etc.).  
* **bwc_ipfabric**: Actions for manipulating inventory, and performing lower-level device configuration.

The actions in each pack include a short description:

.. code-block:: guess
    :emphasize-lines: 1,17

    $ st2 action list -p bwc_ipfabric
      +-----------------------------------------+---------------+----------------------------------------------------+
      | ref                                     | pack          |              description                           |
      +-----------------------------------------+---------------+----------------------------------------------------+
      | bwc_ipfabric.configure_anycast          | bwc_ipfabric  | Affect an anycast gateway change on VDX switches   |
      | bwc_ipfabric.configure_bgp              | bwc_ipfabric  | Configure BGP on Brocade VDX Switches              |
      | bwc_ipfabric.configure_bgp_neighbor     | bwc_ipfabric  | Configure BGP neighbor on Brocade VDX Switches     |
      | bwc_ipfabric.configure_bgp_redistribute | bwc_ipfabric  | Configure BGP route redistribution on VDX switches |
      | bwc_ipfabric.configure_fabric           | bwc_ipfabric  | Configure IP fabric                                |
      | bwc_ipfabric.configure_ip               | bwc_ipfabric  | Configure IPs on Brocade VDX Switches              |
      | bwc_ipfabric.configure_switch           | bwc_ipfabric  | Configure switch                                   |
      | bwc_ipfabric.configure_switch_bgp       | bwc_ipfabric  | Configure bgp on switch                            |
      | bwc_ipfabric.configure_switch_ifaces    | bwc_ipfabric  | Configure switch interfaces                        |
      | bwc_ipfabric.inventory                  | bwc_ipfabric  | Query inventory service to constuct the inventory. |
      +-----------------------------------------+---------------+----------------------------------------------------+ 
    
    $ st2 action list -p bwc_topology
      +-----------------------------------+--------------+---------------------------------------------------------------------------------------+
      | ref                               |    pack      | description                                                                           |
      +-----------------------------------+--------------+---------------------------------------------------------------------------------------+
      | bwc_topology.fabric_add           | bwc_topology | Add a fabric to the inventory                                                         |
      | bwc_topology.fabric_config_set    | bwc_topology | Add/Update the specified fabric parameter for the specified fabric from the inventory |
      | bwc_topology.fabric_config_delete | bwc_topology | Delete the specified fabric parameter for the specified fabric from the inventory     |
      | bwc_topology.fabric_delete        | bwc_topology | Delete a fabric from the inventory                                                    |
      | bwc_topology.fabric_list          | bwc_topology | List all the fabrics in the inventory or the specified fabric details                 |
      | bwc_topology.show_config_bgp      | bwc_topology | Lists BGP config details in the inventory for the specified fabric or device IP       |
      | bwc_topology.show_lldp_links      | bwc_topology | List all the lldp links in the inventory for the specified fabric                     |
      | bwc_topology.show_vcs_links       | bwc_topology | List all the vcs links in the inventory for the specified fabric                      |
      | bwc_topology.switch_add           | bwc_topology | Add a switch to the inventory to a specified fabric                                   |
      | bwc_topology.switch_delete        | bwc_topology | Deletes the specified switch from the Fabric                                          |
      | bwc_topology.switch_list          | bwc_topology | List all the devices in the bwc_topology for the specified fabric or device IP        |
      | bwc_topology.switch_update        | bwc_topology | Update a details of single switch or all the switches in the Fabric                   |
      | bwc_topology.topology_generate    | bwc_topology | Generate the topology for the specified Fabric                                        |
      +-----------------------------------+--------------+---------------------------------------------------------------------------------------+

For more details about the actions in these packs, use the ``st2 action get <pack-name>.<action-name>``
command. The output can also be displayed in YAML format by appending ``-y`` to the command.
Similarly, for JSON use ``-j``.

.. code-block:: guess
    :emphasize-lines: 1,41

    $ st2 action get bwc_topology.switch_add
      +-------------+------------------------------------------------------------+
      | Property    | Value                                                      |
      +-------------+------------------------------------------------------------+
      | id          | 57acd58718971236df5b4599                                   |
      | uid         | action:bwc_topology:switch_add                             |
      | ref         | bwc_topology.switch_add                                    |
      | pack        | bwc_topology                                               |
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
    
    $ st2 action get bwc_topology.switch_add -y
      description: Add a switch to the inventory to a specified fabric
      enabled: true
      entry_point: switch_add.py
      id: 57acd58718971236df5b4599
      name: switch_add
      notify: {}
      pack: bwc_topology
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
      ref: bwc_topology.switch_add
      runner_type: run-python
      tags: []
      uid: action:bwc_topology:switch_add

Most of the actions have *Required* and *Optional* parameters. These parameters can either
be accessed using ``st2 action get <pack-name>.<action-name>`` or
``st2 run <pack-name>.<action-name> -h`` command.

.. note::
    In some actions parameters are mutually exclusive. Hence, they are placed in optional
    parameters section. For example, in the following example either fabric name or host
    (switch IP) are required, but are mutually exclusive.


.. code:: shell

    $ st2 run bwc_topology.switch_list -h
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
|bwc|-specific. By default, a VDX switch doesn't have any information about its role. In order for
|bwc| to be able to determine the switch role, the first switch added to the fabric must be a **Spine**.

Let us start with ``bwc_topology.fabric_list`` to get the details about the *default* fabric.
This is the set of parameters such as ASN range, IP address range etc. required to build an IP fabric:

.. code:: shell

    $ st2 run bwc_topology.fabric_list
      
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

For detail on fabric parameters refer :doc:`./basic_cli` 's ``bwc ipf fabric config`` section.

----------

On a side note, the values in the output can also be accessed using ``--attr`` and ``-k`` flag:

.. code-block:: guess
   :emphasize-lines: 1,9

   $ st2 run bwc_topology.fabric_list -k result[0].fabric_settings
     .
     {u'bgp_multihop': u'5', u'spine_asn_block': u'64512-64999', u'leaf_asn_block': u'65000-65534',
     u'allowas_in': u'5', u'max_paths': u'8', u'bfd_multiplier': u'3', u'p2p_link_range':
     u'10.10.10.0/23', u'loopback_port_number': u'1', u'bfd_tx': u'300', u'anycast_mac':
     u'aabb.ccdd.eeff', u'evpn_enabled': u'Yes', u'loopback_ip_range': u'172.32.254.0/24',
     u'bfd_rx': u'300'}
   
   $ st2 run bwc_topology.fabric_list --attr result.result[0].fabric_settings
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

|ipf| supports user-defined fabric with custom parameters.

.. note::
    **default** fabric has *p2p_link_range* with a range of IP address which results in
    IP numbered fabric. To get IP unnumbered fabric the *p2p_link_range* should be set
    as string **"unnumbered"**.

1. First create a user-defined custom fabric:

.. code:: shell
    
   $ st2 run bwc_topology.fabric_add fabric=new_fabric
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
   These parameters are mandatory: **leaf_asn_block**, **spine_asn_block**, **loopback_ip_range**,
   **loopback_port_number**, **p2p_link_range** and cannot be edited. Please double check before
   entering these parameters.

.. code-block:: shell
   :emphasize-lines: 1,21,41,61,81
   
   $ st2 run bwc_topology.fabric_config_set fabric=new_fabric key=p2p_link_range value="unnumbered"
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

   $ st2 run bwc_topology.fabric_config_set fabric=new_fabric key=leaf_asn_block value=6500-6600
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

   $ st2 run bwc_topology.fabric_config_set fabric=new_fabric key=spine_asn_block value=6000-6400
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

   $ st2 run bwc_topology.fabric_config_set fabric=new_fabric key=loopback_ip_range value=172.32.254.0/24
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

   $ st2 run bwc_topology.fabric_config_set fabric=new_fabric key=loopback_port_number value=1
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

3. (Optional) Add optional parameters to the *custom-fabric*, otherwise values from
   **default** fabric are used:

.. code-block:: shell
    :emphasize-lines: 1,21,41,61,81,101,121

    $ st2 run bwc_topology.fabric_config_set fabric=new_fabric key=anycast_mac value=ccff.aadd.eeff
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
    
    $ st2 run bwc_topology.fabric_config_set fabric=new_fabric key=max_paths value=8
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
    
    $ st2 run bwc_topology.fabric_config_set fabric=new_fabric key=bfd_multiplier value=5
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
    
    $ st2 run bwc_topology.fabric_config_set fabric=new_fabric key=bfd_rx value=400
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
    
    $ st2 run bwc_topology.fabric_config_set fabric=new_fabric key=bfd_tx value=400
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
    
    $ st2 run bwc_topology.fabric_config_set fabric=new_fabric key=bgp_multihop value=8
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
    
    $ st2 run bwc_topology.fabric_config_set fabric=new_fabric key=evpn_enabled value=no
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

4. Similarly, the following commands can be used to delete the user-defined fabric and its parameters:

.. code:: shell

    $ st2 run bwc_topology.fabric_config_delete fabric=new_fabric key=anycast_mac

    $ st2 run bwc_topology.fabric_delete fabric=new_fab

----------

-----------------
Switch Management
-----------------

Register, delete and update switch
----------------------------------

After creating a *custom fabric* we can register/update/delete switches to the fabric:

.. code-block:: shell
    :emphasize-lines: 1,40,80

    $ st2 run bwc_topology.switch_add fabric=default host=10.24.39.224 user=admin passwd=password
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
    
    $ st2 run bwc_topology.switch_update fabric=default host=10.24.39.224 user=admin passwd=password
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
    
    $ st2 run bwc_topology.switch_delete host=10.24.39.224
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

The same commands can be used for the *default* fabric.

All the switches in a fabric can also be updated by providing fabric name: ``fabric=<fabric name>``
to ``st2 run bwc_topology.switch_update`` command instead of a switch IP address:

.. code:: shell

   $ st2 run bwc_topology.switch_update fabric=default
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

After you have registered all switches, use the following command to execute the BGP
workflow:

.. code:: shell

   $ st2 run bwc_ipfabric.configure_fabric fabric=default
     ............................................................
     id: 57b4bf0518971232c98e6f25
     action.ref: bwc_ipfabric.configure_fabric
     parameters:
       fabric: default
     status: succeeded
     start_timestamp: 2016-08-17T19:46:13.794381Z
     end_timestamp: 2016-08-17T19:48:23.215888Z
     +------------------------------+-------------------------+------------------------------------+-----------------------------------------+-------------------------------+
     | id                           | status                  | task                               | action                                  | start_timestamp               |
     +------------------------------+-------------------------+------------------------------------+-----------------------------------------+-------------------------------+
     |   57b4bf0618971232c98e6f28   | succeeded (7s elapsed)  | get_inventory                      | bwc_ipfabric.inventory                  | Wed, 17 Aug 2016 19:46:14 UTC |
     | + 57b4bf0e18971232c98e6f2a   | succeeded (51s elapsed) | configure_switches                 | bwc_ipfabric.configure_switch           | Wed, 17 Aug 2016 19:46:22 UTC |
     |  + 57b4bf1018971232c98e6f38  | succeeded (13s elapsed) | configure_interfaces               | bwc_ipfabric.configure_switch_ifaces    | Wed, 17 Aug 2016 19:46:24 UTC |
     |     57b4bf1218971232c98e6f3e | succeeded (5s elapsed)  | configure_interface                | bwc_ipfabric.configure_ip               | Wed, 17 Aug 2016 19:46:26 UTC |
     |     57b4bf1818971232c98e6f47 | succeeded (5s elapsed)  | configure_interface                | bwc_ipfabric.configure_ip               | Wed, 17 Aug 2016 19:46:31 UTC |
     |  + 57b4bf1f18971232c98e6f4e  | succeeded (24s elapsed) | configure_bgp                      | bwc_ipfabric.configure_switch_bgp       | Wed, 17 Aug 2016 19:46:39 UTC |
     |     57b4bf2218971232c98e6f54 | succeeded (6s elapsed)  | configure_bgp                      | bwc_ipfabric.configure_bgp              | Wed, 17 Aug 2016 19:46:42 UTC |
     |     57b4bf2918971232c98e6f5c | succeeded (5s elapsed)  | configure_bgp_redistributed_routes | bwc_ipfabric.configure_bgp_redistribute | Wed, 17 Aug 2016 19:46:49 UTC |
     |     57b4bf2f18971232c98e6f66 | succeeded (6s elapsed)  | configure_bgp_peers                | bwc_ipfabric.configure_bgp_neighbor     | Wed, 17 Aug 2016 19:46:55 UTC |
     |    57b4bf3918971232c98e6f72  | succeeded (5s elapsed)  | configure_anycast_gateway          | bwc_ipfabric.configure_anycast          | Wed, 17 Aug 2016 19:47:05 UTC |
     | + 57b4bf0e18971232c98e6f2c   | succeeded (61s elapsed) | configure_switches                 | bwc_ipfabric.configure_switch           | Wed, 17 Aug 2016 19:46:22 UTC |
     |  + 57b4bf1018971232c98e6f32  | succeeded (24s elapsed) | configure_interfaces               | bwc_ipfabric.configure_switch_ifaces    | Wed, 17 Aug 2016 19:46:24 UTC |
     |     57b4bf1218971232c98e6f3c | succeeded (5s elapsed)  | configure_interface                | bwc_ipfabric.configure_ip               | Wed, 17 Aug 2016 19:46:26 UTC |
     |     57b4bf1818971232c98e6f48 | succeeded (4s elapsed)  | configure_interface                | bwc_ipfabric.configure_ip               | Wed, 17 Aug 2016 19:46:32 UTC |
     |     57b4bf1c18971232c98e6f4a | succeeded (4s elapsed)  | configure_interface                | bwc_ipfabric.configure_ip               | Wed, 17 Aug 2016 19:46:36 UTC |
     |     57b4bf2118971232c98e6f52 | succeeded (3s elapsed)  | configure_interface                | bwc_ipfabric.configure_ip               | Wed, 17 Aug 2016 19:46:41 UTC |
     |  + 57b4bf2a18971232c98e6f5e  | succeeded (29s elapsed) | configure_bgp                      | bwc_ipfabric.configure_switch_bgp       | Wed, 17 Aug 2016 19:46:49 UTC |
     |     57b4bf2b18971232c98e6f60 | succeeded (7s elapsed)  | configure_bgp                      | bwc_ipfabric.configure_bgp              | Wed, 17 Aug 2016 19:46:51 UTC |
     |     57b4bf3318971232c98e6f6a | succeeded (4s elapsed)  | configure_bgp_redistributed_routes | bwc_ipfabric.configure_bgp_redistribute | Wed, 17 Aug 2016 19:46:59 UTC |
     |     57b4bf3818971232c98e6f70 | succeeded (10s elapsed) | configure_bgp_peers                | bwc_ipfabric.configure_bgp_neighbor     | Wed, 17 Aug 2016 19:47:03 UTC |
     |     57b4bf3818971232c98e6f6d | succeeded (9s elapsed)  | configure_bgp_peers                | bwc_ipfabric.configure_bgp_neighbor     | Wed, 17 Aug 2016 19:47:03 UTC |
     |     57b4bf3818971232c98e6f6f | succeeded (8s elapsed)  | configure_bgp_peers                | bwc_ipfabric.configure_bgp_neighbor     | Wed, 17 Aug 2016 19:47:04 UTC |
     | + 57b4bf0e18971232c98e6f2e   | succeeded (51s elapsed) | configure_switches                 | bwc_ipfabric.configure_switch           | Wed, 17 Aug 2016 19:46:22 UTC |
     |  + 57b4bf1018971232c98e6f34  | succeeded (13s elapsed) | configure_interfaces               | bwc_ipfabric.configure_switch_ifaces    | Wed, 17 Aug 2016 19:46:24 UTC |
     |     57b4bf1118971232c98e6f3a | succeeded (4s elapsed)  | configure_interface                | bwc_ipfabric.configure_ip               | Wed, 17 Aug 2016 19:46:25 UTC |
     |     57b4bf1518971232c98e6f42 | succeeded (4s elapsed)  | configure_interface                | bwc_ipfabric.configure_ip               | Wed, 17 Aug 2016 19:46:29 UTC |
     |  + 57b4bf1f18971232c98e6f4c  | succeeded (26s elapsed) | configure_bgp                      | bwc_ipfabric.configure_switch_bgp       | Wed, 17 Aug 2016 19:46:38 UTC |
     |     57b4bf2018971232c98e6f50 | succeeded (5s elapsed)  | configure_bgp                      | bwc_ipfabric.configure_bgp              | Wed, 17 Aug 2016 19:46:40 UTC |
     |     57b4bf2618971232c98e6f5a | succeeded (4s elapsed)  | configure_bgp_redistributed_routes | bwc_ipfabric.configure_bgp_redistribute | Wed, 17 Aug 2016 19:46:46 UTC |
     |     57b4bf2b18971232c98e6f62 | succeeded (6s elapsed)  | configure_bgp_peers                | bwc_ipfabric.configure_bgp_neighbor     | Wed, 17 Aug 2016 19:46:51 UTC |
     |    57b4bf3918971232c98e6f74  | succeeded (6s elapsed)  | configure_anycast_gateway          | bwc_ipfabric.configure_anycast          | Wed, 17 Aug 2016 19:47:05 UTC |
     | + 57b4bf0e18971232c98e6f30   | succeeded (56s elapsed) | configure_switches                 | bwc_ipfabric.configure_switch           | Wed, 17 Aug 2016 19:46:22 UTC |
     |  + 57b4bf1018971232c98e6f36  | succeeded (19s elapsed) | configure_interfaces               | bwc_ipfabric.configure_switch_ifaces    | Wed, 17 Aug 2016 19:46:24 UTC |
     |     57b4bf1218971232c98e6f40 | succeeded (5s elapsed)  | configure_interface                | bwc_ipfabric.configure_ip               | Wed, 17 Aug 2016 19:46:26 UTC |
     |     57b4bf1718971232c98e6f44 | succeeded (6s elapsed)  | configure_interface                | bwc_ipfabric.configure_ip               | Wed, 17 Aug 2016 19:46:31 UTC |
     |  + 57b4bf2418971232c98e6f56  | succeeded (24s elapsed) | configure_bgp                      | bwc_ipfabric.configure_switch_bgp       | Wed, 17 Aug 2016 19:46:44 UTC |
     |     57b4bf2518971232c98e6f58 | succeeded (6s elapsed)  | configure_bgp                      | bwc_ipfabric.configure_bgp              | Wed, 17 Aug 2016 19:46:45 UTC |
     |     57b4bf2c18971232c98e6f64 | succeeded (5s elapsed)  | configure_bgp_redistributed_routes | bwc_ipfabric.configure_bgp_redistribute | Wed, 17 Aug 2016 19:46:52 UTC |
     |     57b4bf3218971232c98e6f68 | succeeded (6s elapsed)  | configure_bgp_peers                | bwc_ipfabric.configure_bgp_neighbor     | Wed, 17 Aug 2016 19:46:58 UTC |
     |    57b4bf3e18971232c98e6f76  | succeeded (3s elapsed)  | configure_anycast_gateway          | bwc_ipfabric.configure_anycast          | Wed, 17 Aug 2016 19:47:10 UTC |
     |   57b4bf4c18971232c98e6f78   | succeeded (56s elapsed) | show_bgp_config                    | bwc_topology.show_config_bgp            | Wed, 17 Aug 2016 19:47:24 UTC |
     +------------------------------+-------------------------+------------------------------------+-----------------------------------------+-------------------------------+


.. note::
    This command runs on the **default** fabric if fabric name is not provided.


Detail of each action execution in the workflow can be found using the execution id.
Use ``st2 execution get <execution id>`` command to get the details. Last execution ID
shows bgp configuration on switches, after successful execution:

.. code:: shell

   $ st2 execution get 57b4bf4c18971232c98e6f78
     id: 57b4bf4c18971232c98e6f78
     status: succeeded (56s elapsed)
     parameters:
       fabric: default
     result:
       exit_code: 0
       result: "
     Switch 10.24.39.224 (Spine):
     rbridge-id 224
       router bgp
         local-as 64512
         bfd interval 300 min-rx 300 multiplier 3
         neighbor 10.10.10.0 remote-as 65000 state ESTAB up_time 0h0m17s creation_time 2016-08-17 19:47:39
         neighbor 10.10.10.0 ebgp-multihop 5
         neighbor 10.10.10.2 remote-as 65001 state ESTAB up_time 0h0m19s creation_time 2016-08-17 19:47:39
         neighbor 10.10.10.2 ebgp-multihop 5
         neighbor 10.10.10.4 remote-as 65001 state ESTAB up_time 0h0m17s creation_time 2016-08-17 19:47:39
         neighbor 10.10.10.4 ebgp-multihop 5
         address-family ipv4 unicast
          redistribute connected
          neighbor 10.10.10.0 allowas-in 5
          neighbor 10.10.10.2 allowas-in 5
          neighbor 10.10.10.4 allowas-in 5
          maximum-paths 8
          graceful-restart
          next-hop-recursion
         address-family l2vpn evpn
          retain route-target all
          neighbor 10.10.10.0 activate
          neighbor 10.10.10.0 allowas-in 5
          neighbor 10.10.10.0 next-hop-unchanged
          neighbor 10.10.10.2 activate
          neighbor 10.10.10.2 allowas-in 5
          neighbor 10.10.10.2 next-hop-unchanged
          neighbor 10.10.10.4 activate
          neighbor 10.10.10.4 allowas-in 5
          neighbor 10.10.10.4 next-hop-unchanged
     
     Switch 10.24.39.225 (Leaf):
     rbridge-id 225
       router bgp
         local-as 65000
         bfd interval 300 min-rx 300 multiplier 3
         neighbor 10.10.10.1 remote-as 64512 state ESTAB up_time 0h0m31s creation_time 2016-08-17 19:47:52
         neighbor 10.10.10.1 ebgp-multihop 5
         address-family ipv4 unicast
          redistribute connected
          neighbor 10.10.10.1 allowas-in 5
          maximum-paths 8
          graceful-restart
          next-hop-recursion
         address-family l2vpn evpn
          neighbor 10.10.10.1 activate
          neighbor 10.10.10.1 allowas-in 5
          neighbor 10.10.10.1 next-hop-unchanged
     
     Switch 10.24.39.228 (Leaf):
     rbridge-id 228
       router bgp
         local-as 65001
         bfd interval 300 min-rx 300 multiplier 3
         neighbor 10.10.10.3 remote-as 64512 state ESTAB up_time 0h0m45s creation_time 2016-08-17 19:48:06
         neighbor 10.10.10.3 ebgp-multihop 5
         address-family ipv4 unicast
          redistribute connected
          neighbor 10.10.10.3 allowas-in 5
          maximum-paths 8
          graceful-restart
          next-hop-recursion
         address-family l2vpn evpn
          neighbor 10.10.10.3 activate
          neighbor 10.10.10.3 allowas-in 5
          neighbor 10.10.10.3 next-hop-unchanged
     
     Switch 10.24.39.229 (Leaf):
     rbridge-id 229
       router bgp
         local-as 65001
         bfd interval 300 min-rx 300 multiplier 3
         neighbor 10.10.10.5 remote-as 64512 state ESTAB up_time 0h0m58s creation_time 2016-08-17 19:48:19
         neighbor 10.10.10.5 ebgp-multihop 5
         address-family ipv4 unicast
          redistribute connected
          neighbor 10.10.10.5 allowas-in 5
          maximum-paths 8
          graceful-restart
          next-hop-recursion
         address-family l2vpn evpn
          neighbor 10.10.10.5 activate
          neighbor 10.10.10.5 allowas-in 5
          neighbor 10.10.10.5 next-hop-unchanged
     "
       stderr: 'st2.actions.python.ShowBGPConfig: DEBUG    GET http://127.0.0.1:8888/v1/switches?fabric_name=default
     
         st2.actions.python.ShowBGPConfig: DEBUG    GET http://127.0.0.1:8888/v1/bgp?fabric_name=default&fetch_state=true
     
         '
       stdout: 'Successfully retrieved the switch(es) BGP config details.  Object details:
     
         '

-------------

-------------
Show commands
-------------

These commands can be used to get details about BGP configuration, VCS links
and LLDP neighbors and generate topology (default: pdf in /tmp folder):

Show BGP configuration on the switches
--------------------------------------

After BGP workflow execution:

.. code:: shell
   
   $ st2 run bwc_topology.show_config_bgp fabric=default
     ...........................
     id: 57b4c21118971232c98e6f83
     status: succeeded
     parameters:
       fabric: default
     result:
       exit_code: 0
       result: "
     Switch 10.24.39.224 (Spine):
     rbridge-id 224
       router bgp
         local-as 64512
         bfd interval 300 min-rx 300 multiplier 3
         neighbor 10.10.10.0 remote-as 65000 state ESTAB up_time 0h12m5s creation_time 2016-08-17 19:59:00
         neighbor 10.10.10.0 ebgp-multihop 5
         neighbor 10.10.10.2 remote-as 65001 state ESTAB up_time 0h12m7s creation_time 2016-08-17 19:59:00
         neighbor 10.10.10.2 ebgp-multihop 5
         neighbor 10.10.10.4 remote-as 65001 state ESTAB up_time 0h12m5s creation_time 2016-08-17 19:59:00
         neighbor 10.10.10.4 ebgp-multihop 5
         address-family ipv4 unicast
          redistribute connected
          neighbor 10.10.10.0 allowas-in 5
          neighbor 10.10.10.2 allowas-in 5
          neighbor 10.10.10.4 allowas-in 5
          maximum-paths 8
          graceful-restart
          next-hop-recursion
         address-family l2vpn evpn
          retain route-target all
          neighbor 10.10.10.0 activate
          neighbor 10.10.10.0 allowas-in 5
          neighbor 10.10.10.0 next-hop-unchanged
          neighbor 10.10.10.2 activate
          neighbor 10.10.10.2 allowas-in 5
          neighbor 10.10.10.2 next-hop-unchanged
          neighbor 10.10.10.4 activate
          neighbor 10.10.10.4 allowas-in 5
          neighbor 10.10.10.4 next-hop-unchanged
     
     Switch 10.24.39.225 (Leaf):
     rbridge-id 225
       router bgp
         local-as 65000
         bfd interval 300 min-rx 300 multiplier 3
         neighbor 10.10.10.1 remote-as 64512 state ESTAB up_time 0h12m18s creation_time 2016-08-17 19:59:40
         neighbor 10.10.10.1 ebgp-multihop 5
         address-family ipv4 unicast
          redistribute connected
          neighbor 10.10.10.1 allowas-in 5
          maximum-paths 8
          graceful-restart
          next-hop-recursion
         address-family l2vpn evpn
          neighbor 10.10.10.1 activate
          neighbor 10.10.10.1 allowas-in 5
          neighbor 10.10.10.1 next-hop-unchanged
     
     Switch 10.24.39.228 (Leaf):
     rbridge-id 228
       router bgp
         local-as 65001
         bfd interval 300 min-rx 300 multiplier 3
         neighbor 10.10.10.3 remote-as 64512 state ESTAB up_time 0h12m33s creation_time 2016-08-17 19:59:53
         neighbor 10.10.10.3 ebgp-multihop 5
         address-family ipv4 unicast
          redistribute connected
          neighbor 10.10.10.3 allowas-in 5
          maximum-paths 8
          graceful-restart
          next-hop-recursion
         address-family l2vpn evpn
          neighbor 10.10.10.3 activate
          neighbor 10.10.10.3 allowas-in 5
          neighbor 10.10.10.3 next-hop-unchanged
     
     Switch 10.24.39.229 (Leaf):
     rbridge-id 229
       router bgp
         local-as 65001
         bfd interval 300 min-rx 300 multiplier 3
         neighbor 10.10.10.5 remote-as 64512 state ESTAB up_time 0h12m45s creation_time 2016-08-17 20:00:06
         neighbor 10.10.10.5 ebgp-multihop 5
         address-family ipv4 unicast
          redistribute connected
          neighbor 10.10.10.5 allowas-in 5
          maximum-paths 8
          graceful-restart
          next-hop-recursion
         address-family l2vpn evpn
          neighbor 10.10.10.5 activate
          neighbor 10.10.10.5 allowas-in 5
          neighbor 10.10.10.5 next-hop-unchanged
     "
       stderr: 'st2.actions.python.ShowBGPConfig: DEBUG    GET http://127.0.0.1:8888/v1/switches?fabric_name=default
     
         st2.actions.python.ShowBGPConfig: DEBUG    GET http://127.0.0.1:8888/v1/bgp?fabric_name=default&fetch_state=true
     
         '
       stdout: 'Successfully retrieved the switch(es) BGP config details.  Object details:
     
         '


Show LLDP links among the neighbors
-----------------------------------

After discovering the switches:

.. code:: shell

   $ st2 run bwc_topology.show_lldp_links fabric=default
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


Show VCS links between switches
-------------------------------

If the fabric consists of VDX switches in VCS mode, this command will show the status of 
links between principle and secondary nodes:

.. code:: shell

   $ st2 run bwc_topology.show_vcs_links fabric=default
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

Generate Topology
-----------------
To generate a topology (default format: pdf) for switches discovered in the fabric
use the following command:

.. code:: shell

   $ st2 run bwc_topology.topology_generate fabric=default
     .
     id: 57b6367f18971268b72d7fdf
     status: succeeded
     parameters:
       fabric: default
     result:
       exit_code: 0
       result: 'Topology map generated: /tmp/topology_default_20160818-222816.pdf'
       stderr: 'st2.actions.python.GenerateTopology: DEBUG    GET http://127.0.0.1:8888/v1/switches?fabric_name=default
     
         st2.actions.python.GenerateTopology: DEBUG    GET http://127.0.0.1:8888/v1/switch?id=9
     
         st2.actions.python.GenerateTopology: DEBUG    GET http://127.0.0.1:8888/v1/switch?id=10
     
         st2.actions.python.GenerateTopology: DEBUG    GET http://127.0.0.1:8888/v1/switch?id=11
     
         st2.actions.python.GenerateTopology: DEBUG    GET http://127.0.0.1:8888/v1/switch?id=12
     
         st2.actions.python.GenerateTopology: DEBUG    GET http://127.0.0.1:8888/v1/switches/links?fabric_name=default
     
         st2.actions.python.GenerateTopology: DEBUG    GET http://127.0.0.1:8888/v1/switches/vcs/links?fabric_name=default
     
         '
       stdout: ''
