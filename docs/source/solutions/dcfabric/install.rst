Installation
============

.. warning::
    If you had previously installed the BWC 2.0 IP Fabric Automation Suite,
    we recommend installing the DC Fabric Automation Suite on a new Virtual Machine.

.. contents::
   :local:
   :depth: 2
   
System requirements
-------------------

The system requirements for |bwc| with DC Fabric Automation Suite are same as the core platform requirements, except the memory requirements outlined below will overwrite the system requirements in the platform page.
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

Make sure you are running the latest version of ``curl``, to get the latest version follow the instructions below:

On Ubuntu:

.. code-block:: bash

  sudo apt-get install curl ca-certificates

On Redhat/CentOS:

.. code-block:: bash

  sudo yum update curl nss

Simple Installation
-------------------

.. warning::
   There is a known issue with installing the DC Fabric Automation Suite on |bwc| 2.4. At this time,
   you should only install the DC Fabric Automation Suite on |bwc| 2.2 or 2.3. Follow the instructions below
   to install |bwc| version 2.3.2.

   This issue will be resolved shortly.

To quickly install |bwc| with DC Fabric Automation Suite, obtain a license key from
`brocade.com/bwc <https://www.brocade.com/bwc>`_, and run the commands below, replacing
``${BWC_LICENSE_KEY}`` with the key you received when registering for evaluation or
purchasing. These commands will install |bwc|, Network Essentials, DC Fabric Automation Suite,
and configure all components to work together on a single host:

.. code-block:: bash

  curl -SsL -O https://brocade.com/bwc/install/install.sh && chmod +x install.sh
  ./install.sh --user=st2admin --password=Ch@ngeMe --license=${BWC_LICENSE_KEY} --version=2.3.2
  curl -SsL -O https://brocade.com/bwc/install/install-suite.sh && chmod +x install-suite.sh
  ./install-suite.sh --user=st2admin --password=Ch@ngeMe --suite=dcfabric-suite --license=${BWC_LICENSE_KEY}

If you already have |bwc| installed, and need to add DC Fabric on top of an existing |bwc| 2.2 or 2.3 installation,
run the following commands, replacing ``${BWC_LICENSE_KEY}`` with the key you received when 
registering for evaluation or purchasing:

.. code-block:: bash

  curl -SsL -O https://brocade.com/bwc/install/install-suite.sh && chmod +x install-suite.sh
  ./install-suite.sh --user=st2admin --password=Ch@ngeMe --suite=dcfabric-suite --license=${BWC_LICENSE_KEY}

If you attempt to install this on |bwc| 2.4, it will cause problems with the Web UI. If you have an existing
2.4 installation, you must downgrade to install the DC Fabric Automation Suite.

If you have a more complex environment, or you just want to see exactly what the scripts are doing, read on.
The rest of this document will explain how to how to manually install and configure the individual components.

Custom Installation
-------------------

Components
~~~~~~~~~~

The DC Fabric Automation Suite installs on top of |bwc|. It adds an inventory & topology service, and
DC Fabric automation packs containing actions and workflows to simplify Brocade Data Center Fabric management.
It also includes the ``bwc dcf`` CLI, and Zero Touch Provisioning scripts for integration with :doc:`ZTP <ztp_reference>`.
This suite uses components of the :doc:`../essentials/overview` suite. If the Network Essentials suite is not
currently installed it will be automatically installed during DC Fabric suite installation.

1. Install |bwc|
~~~~~~~~~~~~~~~~

To install |bwc|, follow the detailed installation instructions for your Linux flavor.
It will walk you through installing and configuring StackStorm first, and upgrade it
to |bwc| with the license key you received when registering for evaluation or
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

    st2 apikey create -k -m '{"used_for": "BWC topology service"}'

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
If you have previously installed DC Fabric Automation Suite and want to upgrade to next version, please follow the instructions below:

**On Ubuntu/Debian or RHEL/CentOS 6.x:**

.. code-block:: bash

  # Upgrade bwc/dcfabric packages
  sudo apt-get update
  sudo apt-get install bwc-topology bwc-cli dcfabric-packs dcfabric-suite
 
  # For Database migration from DCF 1.0 to DCF 1.1
  sudo -u postgres psql -d bwc_topology -a -f /usr/share/doc/bwc-topology/etc/migration.sql

  sudo -u postgres psql -d bwc_topology -c "GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO bwc;"

  sudo -u postgres psql -d bwc_topology -c "GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO bwc;"
 
  # Update Network Essentials Pack
  st2 pack install network_essentials

  # Restart Topology Service
  sudo service bwc-topology restart

  # For verification, run the following command to check the version number for network_essentials, network_inventory and dcfabric packs 
  st2 pack list

**On RHEL/CentOS 7.x:**

.. code-block:: bash

  # Upgrade bwc/dcfabric packages
  sudo yum update bwc-cli bwc-topology dcfabric-packs dcfabric-suite 
 
  # For Database migration from DCF 1.0 to DCF 1.1
  sudo -u postgres psql -d bwc_topology -a -f /usr/share/doc/bwc-topology/etc/migration.sql

  sudo -u postgres psql -d bwc_topology -c "GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO bwc;"

  sudo -u postgres psql -d bwc_topology -c "GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO bwc;"
 
  # Update Network Essentials Pack
  st2 pack install network_essentials

  # Restart Topology Service
  sudo service bwc-topology restart

  # For verification, run the following command to check the version number for network_essentials, network_inventory and dcfabric packs 
  st2 pack list

.. rubric:: What's Next?

* New to |BWC|? Go to fundamentals - start with :doc:`/start`.
* Understand the DC Fabric operations - go over :doc:`./operation/overview`.
* Understand the DC Fabric CLI - read the :doc:`./dcf_cli/basic_cli`.
