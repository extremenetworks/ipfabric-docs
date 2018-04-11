Installation
============

Data Center Fabrics Automation Suite supports two different models for installation:

 * Virtual appliance or
 * RPM or Deb package-based installation

The virtual appliance has all components pre-installed and pre-configured. This is the fastest way to stand up a new system. Some users may still need to do a package-based installation due to their specific needs.

Deploying the Virtual Appliance
===============================
The virtual appliance can be downloaded from the `Extreme Portal <https://extremeportal.force.com/ExtrProductLanding?pf=Automation>`_

To deploy the OVA using VirtualBox, follow the steps below:

    1.	Download dcf-1.2.0_ewc-2.6.0.ova file from Extreme Portal download page
    2.	Start Oracle VirtualBox
    3.	File -> Import Appliance  (or) Ctrl+I
    4.	Select the downloaded .ova file and Open
    5.	Select the imported VM and click Start
    6.	After the VM starts, right click on the VM and select “Settings”
    7.	Select Network tab in the Settings window
    8.	Change Adapter setting from “NAT” to “Bridged Adapter”
    9.	Power Off and restart the VM
    10.	To access the Workflow Composer GUI, type ``https://<IP address of the VM>``
    11.	ST2 CLI can be accessed using ssh ``<IP Address of the VM>``

To find the IP Address of the VM:

    1.	Access the VM’s console
    2.	Login using default SSH credentials
    3.	Type ifconfig to find out the IP Address of the virtual machine.

.. note::
  By default, the VM uses DHCP to obtain an IP address. If your network does not have DHCP, you will need to
  statically configure an IP address, using `these instructions <https://help.ubuntu.com/lts/serverguide/network-configuration.html#ip-addressing>`_

Default credentials:
    •	SSH Credentials: ``ubuntu/ubuntu``
    •	GUI credentials: ``st2admin/Ch@ngeMe``

License Activation
------------------
Before using the software appliance, users must activate the appliance.  To obtain an evaluation license key, go to `Extreme Products Page <https://www.extremenetworks.com/product/workflow-composer/>`_. Your license key will be emailed to you. Use the commands below to activate the license:
   
    1.	Access the VM’s console
    2.	Login using default SSH credentials
    3.  ``st2-activate-license <license-key>``
    
RPM or Deb Package-based Installation
=====================================

.. warning::
    If you had previously installed the EWC 2.0 IP Fabric Automation Suite,
    we recommend installing the DC Fabric Automation Suite on a new Virtual Machine.

.. contents::
   :local:
   :depth: 2
   
System requirements
-------------------

The system requirements for |bwc| with DC Fabric Automation Suite are the same as the core platform requirements,
except the memory requirements outlined below will overwrite the system requirements in the platform page.
See the :doc:`system requirements documentation</install/system_requirements>` for more details.

+--------------------------------------+-----------------------------------+
|            Testing                   |         Production                |
+======================================+===================================+
|  * Dual CPU system                   | * Quad core CPU system            |
|  * 8GB RAM                           | * >16GB RAM                       |
|  * 10GB storage                      | * 40GB storage                    |
|  * Recommended EC2: **t2.large**     | * Recommended EC2: **m4.xlarge**  |
+--------------------------------------+-----------------------------------+

Installing Pre-requisites
-------------------------

Make sure you are running the latest version of ``curl``, to get the latest version, follow the instructions below:

On Ubuntu:

.. code-block:: bash

  sudo apt-get install curl ca-certificates

On Redhat/CentOS:

.. code-block:: bash

  sudo yum update curl nss

Simple Installation
-------------------

To quickly install |bwc| with DC Fabric Automation Suite, obtain a license key from
`www.extremenetworks.com/product/workflow-composer/ <https://www.extremenetworks.com/product/workflow-composer/>`_, and run the commands below, replacing
``${EWC_LICENSE_KEY}`` with the key you received when registering for evaluation or when
purchasing. These commands will install |bwc|, Network Essentials, DC Fabric Automation Suite,
and then configure all components to work together on a single host:

First, install |bwc| v2.6. This version is required for DC Fabric Automation Suite v1.2

.. code-block:: bash

  curl -SsL -O https://stackstorm.com/bwc/install.sh && chmod +x install.sh
  ./install.sh --user=st2admin --password=Ch@ngeMe --version=2.6.0 --license=${EWC_LICENSE_KEY}

After |bwc| is installed, to add DC Fabric Automation Suite,
run the following commands, replacing ``${EWC_LICENSE_KEY}`` with the key you received when 
registering for evaluation or when purchasing:

.. code-block:: bash

  curl -SsL -O https://stackstorm.com/bwc/install-suite.sh && chmod +x install-suite.sh
  ./install-suite.sh --user=st2admin --password=Ch@ngeMe --suite=dcfabric-suite --license=${EWC_LICENSE_KEY}

.. note::

  If you are adding DC Fabric Automation Suite to an existing |bwc| system, ensure it is running = v2.6. If you are using an
  older version of |bwc|, :doc:`upgrade the system </install/upgrades>` before installing DC Fabric Automation Suite.

If you have a more complex environment, or you just want to see exactly what the scripts are doing, read on.
The rest of this document will explain how to manually install and configure the individual components.

Custom Installation
-------------------

Components
~~~~~~~~~~

The DC Fabric Automation Suite installs on top of |bwc|. It adds an inventory & topology service, and
DC Fabric automation packs containing actions and workflows to simplify Data Center Fabric management.
It also includes the ``bwc dcf`` CLI, and Zero Touch Provisioning scripts for integration with :doc:`ZTP <ztp_reference>`.
This suite uses components of the :doc:`../essentials/overview` suite. If the Network Essentials Automation Suite is not
currently installed, it will automatically be installed during DC Fabric Automation Suite installation.

1. Install |bwc|
~~~~~~~~~~~~~~~~

To install |bwc|, follow the detailed installation instructions for your Linux flavor.
It will walk you through installing and configuring StackStorm first, and upgrade it
to |bwc| with the license key you received when registering for evaluation or when 
purchasing. This last step will also set up the |bwc| repository on your box.

* :doc:`/install/deb`
* :doc:`/install/rhel7`
* :doc:`/install/rhel6`


2. Install DC Fabric Suite
~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure that |bwc| repository is set up on the box.

Install the DC Fabric suite:

* On Ubuntu/Debian: ::

    sudo apt-get install -y dcfabric-suite

* On RHEL/CentOS: ::

    yum install -y dcfabric-suite

3. Configure Topology Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Generate an API key to connect the topology service to st2 API: ::

    st2 apikey create -k -m '{"used_for": "EWC topology service"}'

* Edit the configuration file ``/etc/brocade/bwc/bwc-topology-service.conf``,
  set ``st2_api_key`` value to the st2 API key, and change the default DB
  username and password to the desired values in the ``connection`` string. ::

    ...
    ## Postgres
    connection = 'postgresql://bwcuser:bwcsecret@localhost/bwc_topology'

    # StackStorm
    st2_auth_url = 'https://localhost/auth'
    st2_api_url = 'https://localhost:443/api'
    st2_api_key = '<ST2_API_KEY_GENERATED_ABOVE>'

* Run DB setup script (the script will pick DB name, username and
  password from the ``bwc-topology-service.conf`` file): ::

    sudo /opt/brocade/bwc-topology/bin/bwc_topology_db_setup.sh

* Fix the access rights to the log files: ::

    sudo chown -R bwc:bwc /var/log/brocade/bwc/

* Start the ``bwc-topology`` service:

  * On Ubuntu/Debian or RHEL/CentOS 6.x: ::

      sudo service bwc-topology start
      # Check that it is running indeed
      service bwc-topology status

  * On RHEL/CentOS 7.x: ::

      sudo systemctl bwc-topology start
      # Check that it is running indeed
      systemctl bwc-topology status

4. Verification of the Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run some ``bwc dcf`` CLI commands to see that everything is installed.

.. code-block:: bash

  bwc --version
  bwc --help
  bwc dcf fabric list
  
Upgrade from previous version
------------------------------
If you have previously installed DC Fabric Automation Suite v1.1 and want to upgrade to next version, please follow the instructions below:

**On Ubuntu/Debian or RHEL/CentOS 6.x:**

.. code-block:: bash

  # Upgrade bwc/dcfabric packages
  sudo apt-get update
  sudo apt-get install bwc-topology bwc-cli dcfabric-packs dcfabric-suite
 
  # Update Network Essentials Pack
  st2 pack install network_essentials

  # Restart Topology Service
  sudo service bwc-topology restart

  # For verification, run the following command to check the version number for network_essentials, network_inventory and dcfabric packs is v1.2.0 
  st2 pack list

**On RHEL/CentOS 7.x:**

.. code-block:: bash

  # Upgrade bwc/dcfabric packages
  sudo yum update bwc-cli bwc-topology dcfabric-packs dcfabric-suite 
 
  # Update Network Essentials Pack
  st2 pack install network_essentials

  # Restart Topology Service
  sudo service bwc-topology restart

  # For verification, run the following command to check the version number for network_essentials, network_inventory and dcfabric packs is v1.2.0 
  st2 pack list

.. rubric:: What's Next?

* New to |bwc|? Go to fundamentals - start with :doc:`/start`.
* Understand the DC Fabric operations - go over :doc:`./operation/overview`.
* Understand the DC Fabric CLI - read the :doc:`./dcf_cli/basic_cli`.
