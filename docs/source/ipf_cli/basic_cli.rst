IP Fabric Solution CLI
======================

.. note::
  All command line examples in this section begins with $ (dollar sign), which represents
  a shell command prompt. Do not enter another dollar sign. All commands should be entered
  at the shell prompt.

|bwc| |ipf| CLI is an easy to use CLI for |ipf|.

.. todo::
   Add more details on the basic and advance CLI



bwc ipf help
------------

Displays information (help) about all or a specified command.

**Syntax**

.. code:: shell
   
    bwc help [ --help ] [ command [ args... ] ]

**Parameters**

    *command*
        Specifies the name of the command.
    *args*
        Specifies any additional arguments.

**Usage Guidelines**
 
Refer to :command:`bwc <command> --help` for more information on a specific command.

**Examples**
  
Use the bwc --help command to display Brocade Workflow Composer commands and their functions.

.. code:: shell
   
    $ bwc --help
    <ADD OUTPUT>

bwc ipf show
------------
    
Shows the state of BGP peers and other configurations that have been configured on the switches.

**Syntax**

.. code:: shell

    bwc show [ --help ]
    bwc show config bgp [ --fabric=fabric_name ]
    bwc show topology [ --fabric=fabric_name ] [--format=format ]
    bwc show version

**Parameters**

    :command:`--help`  Displays help.

    *config bgp*    Displays the BGP configuration.
    
    :command:`--fabric=<fabric_name>`  Specifies the fabric name.

    *topology*  Specifies the fabric name and format of the topology display.
    
    :command:`--fabric=fabric_name` Specifies the fabric name.
    
    :command:`--format=format`   Specifies the output type of the file to show the topology (PDF, JPEG, or PNG). The default is PDF.

    *version*    Displays the version of Brocade Workflow Composer Server.

**Examples**

.. code:: shell
    
    $ bwc show config bgp
    <ADD OUTPUT>

Use the bwc show topology command to generate an IP Fabric topology map in a PDF format.

.. code:: shell
    
    $ bwc show topology --fabric=default --format=pdf

Open the topology file that was generated using the appropriate software.

Use the bwc show version command to display the current version of Brocade Workflow Composer.

.. code:: shell
    
    $ bwc show version
    <ADD OUTPUT>
