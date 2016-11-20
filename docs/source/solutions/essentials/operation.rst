Operation Overview
==================

Introduction
------------

This document provides an overview of how to use the Network Essentials suite
with Brocade VDX and SLX switches. These actions can be used as independent actions,
or as part of a more complex workflow. :doc:`Actions</actions>` can be manually triggered,
or they can be tied to :doc:`sensors </sensors>` using rules.

Essentials Actions
------------------

----------------------
configure_interface
----------------------


Configures the specified interface state, mode, VLANs.

Syntax
~~~~~~

.. code-block:: shell

    bwc ipf show config bgp --fabric=<fabric_name> | --host=<ip_address>
    bwc ipf show topology <fabric_name>  [--format=<format>] [--render_dir=<dir_path>]

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

-----------------

----------------------
configure_ntp
----------------------


Configures NTP servers

Syntax
~~~~~~

.. code-block:: shell

    bwc ipf show config bgp --fabric=<fabric_name> | --host=<ip_address>
    bwc ipf show topology <fabric_name>  [--format=<format>] [--render_dir=<dir_path>]

Parameters
~~~~~~~~~~

.. code-block:: guess
   :emphasize-lines: 1,4,7
    
   server
       NTP server IP address or hostname

   switch
       Switch to configure

       fabric=<fabric_name>
           Specifies the fabric name.


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