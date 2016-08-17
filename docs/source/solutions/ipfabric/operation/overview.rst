|ipf| operation overview
========================

Introduction
------------
.. todo::
   Add details


The |ipf| supports easy integration with Zero-Touch Provisioning (ZTP).
It can also be used without ZTP, but switches must be provisioned manually.

.. todo::
   Add reference to the fabric section for default fabric and its parameters

.. figure:: ../../../_static/images/bwc_components.jpg
    :align: center

    **Components of Brocade Flow Composer**

.. note::
    The VCS ID for spine and leaves should be different in both the ZTP-enabled
    configuration and non-ZTP enabled configuration. If the VCS IDs are same, the switch will
    automatically form Ethernet fabric. For example, VCS ID for spines can be 1 and VCS ID for
    leaves can be 2.

Configuring an IP Fabric with ZTP enabled
-----------------------------------------

|ipf| can automatically provision a Brocade VDX switch and create an IP Fabric on the switch
if the switch has ZTP enabled and if no management IP address has been assigned to the switch.

.. note::
    For detailed information about ZTP, refer to ZTP section **<reference required>**.

If the switch has ZTP enabled, complete the following steps:

    1.  Ensure that DHCP and FTP servers to be used in the fabric have been installed.
    2.  Ensure that |bwc| and |ipf| have been installed.
    3.  After the process has finished executing, enter the ``bwc ipf show config bgp`` command
        using |ipf| CLI.

.. note::
    Make sure switches have not been powered on. Connect the switches in a leaf-spine topology.
    |ipf| assigns management IP addresses to the switches, registers the switches in its 
    database, and creates an IP Fabric.

.. todo::
    - Add reference to the Brocade Network OS IP Fabric Configuration Guide.
    - Add reference to the ZTP guide 

.. code:: shell

    $ bwc ipf show config bgp
    <PASTE OUTPUT HERE>

Configuring an IP Fabric without ZTP enabled
--------------------------------------------

If the Brocade VDX switch does not have ZTP enabled or if you want to configure IP Fabrics
manually, complete the following steps. Before using |ipf| to configure an IP Fabric without
ZTP enabled, confirm the following prerequisites:

 * Switches are physically connected in a leaf-spine topology.
 * Each switch has a management IP address assigned.

.. note::
    The first switch that is added to the server must always be a **spine**. If it is not,
    delete the leaf switch from the |ipf| server and add a spine first. After that,
    the order does not matter.

Use the |ipf| CLI to configure an IP Fabric by completing the following steps:

1. Register the switches in the Brocade Workflow Composer database by entering the
   bwc inventory register command.

   ``$ bwc ipf inventory register --ip=<switch IP address> --fabric=default``
   
   NOTE: This example is for the *default* fabric. The --fabric field is mandatory is
   this command.

.. todo::
   How username and password is entered for the switch using this CLI ?

--
   For example, registering switch with IP: 10.24.39.216.The default username is “admin”
   and default password is “password” fo all the VDX switches.

.. code:: shell

      $ bwc ipf inventory register --ip=10.24.39.216 --fabric=default

         <PASTE OUTPUT HERE and UPDATE CLI FOE USERNAME PASSWORD>

2. Verify that the switches are registered by entering the bwc ipf inventory list command.

.. code:: shell

      $ bwc ipf inventory list

      <PASTE OUTPUT HERE>

3. Repeat the step 1 through step 2 to register the remaining switches.

4. Execute the BGP workflow by entering the command bwc workflow bgp command.

.. code:: shell

     $ bwc ipf workflow bgp

5. After the command executes, enter the bwc show config bgp command and review
   the information displayed.

.. code:: shell

     $ bwc ipf show config bgp --fabric=default

     <PASTE OUTPUT HERE>

.. note::
    If you want to add a new spine or leaf to the existing fabric using |ipf|
    for the BGP workflow to run smoothly, you must remove the existing
    configuration on the switch. After removing the existing configurations,
    add the switch to the fabric and run the BGP workflow again.

