Installation
============

To quickly install |bwc| with |ipf|, obtain a license key from `Brocade.com/bwc <https://www.brocade.com/bwc>`_, and
run the commands below, replacing ``${BWC_LICENSE_KEY}`` with the key you received when registering for 
evaluation or purchasing. These commands will install |bwc|, |ipf|, and configure all components to work
together on a single host:

.. warning::
    Make sure you are running the latest version of ``curl``. If you are using RHEL/CentOS, run ``sudo yum update curl nss``.
    For Ubuntu systems, run ``sudo apt-get install curl``. The commands below may fail if you do not update ``curl`` first.

.. code-block:: bash

  curl -SsL -O https://brocade.com/bwc/install/install.sh && chmod +x install.sh
  ./install.sh --user=st2admin --password=Ch@ngeMe --suite=bwc-ipfabric-suite --license=${BWC_LICENSE_KEY}

If you already have |st2| installed, and need to add |ipf| on top of an existing |st2| installation,
run the following commands, replacing ``${BWC_LICENSE_KEY}`` with the key you received when 
registering for evaluation or purchasing.

.. code-block:: bash

  curl -SsL -O https://brocade.com/bwc/install/install-suite.sh && chmod +x install-suite.sh
  ./install-suite.sh --user=st2admin --password=Ch@ngeMe --suite=bwc-ipfabric-suite --license=${BWC_LICENSE_KEY}

If you have a more complex environment, or you just want to see exactly what the scripts are doing, read on.
The rest of this document will explain how to how to manually install and configure the individual components.

System requirements
-------------------

|st2| requires 64-bit version of Ubuntu/Debian, RHEL, or CentOS. The table below lists the supported
versions, along with Vagrant Boxes Vagrant Boxes and Amazon AWS instances we use for
testing. Yes, using exactly the same boxes will improve your evaluation experience.

+-------------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Linux (64 bit)    | Vagrant Box                                                                  | Amazon AWS AMI                                                                                                                                                    |
+===================+==============================================================================+===================================================================================================================================================================+
| Ubuntu 14.04      | `bento/ubuntu-14.04 <https://atlas.hashicorp.com/bento/boxes/ubuntu-14.04>`_ | `Ubuntu Server 14.04 LTS (HVM)  <https://aws.amazon.com/marketplace/pp/B00JV9TBA6/ref=srh_res_product_title?ie=UTF8&sr=0-3&qid=1457037882965>`_                   |
+-------------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RHEL 7 / CentOS 7 | `bento/centos-7.2 <https://atlas.hashicorp.com/bento/boxes/centos-7.2>`_     | `Red Hat Enterprise Linux (RHEL) 7.2 (HVM)  <https://aws.amazon.com/marketplace/pp/B019NS7T5I/ref=srh_res_product_title?ie=UTF8&sr=0-2&qid=1457037671547>`_       |
+-------------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RHEL 6 / CentOS 6 | `bento/centos-6.7 <https://atlas.hashicorp.com/bento/boxes/centos-6.7>`_     | `Red Hat Enterprise Linux (RHEL) 6 (HVM)  <https://aws.amazon.com/marketplace/pp/B00CFQWLS6/ref=srh_res_product_title?ie=UTF8&sr=0-8&qid=1457037733401>`_         |
+-------------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

While the system can operate with lower specs, these are the recommendations
for the best experience while testing or deploying |st2|:

+--------------------------------------+-----------------------------------+
|            Testing                   |         Production                |
+======================================+===================================+
|  * Dual CPU system                   | * Quad core CPU system            |
|  * 1GB RAM                           | * >16GB RAM                       |
|  * 10GB storage                      | * 40GB storage                    |
|  * Recommended EC2: **t2.medium**    | * Recommended EC2: **m4.xlarge**  |
+--------------------------------------+-----------------------------------+

Components
----------

The |ipf| installs on top of |bwc|. It adds an inventory & topology service, and IP Fabric automation
packs containing actions and workflows to simplify Brocade IP Fabric management. It also includes
the ``bwc ipf`` CLI, and Zero Touch Provisioning scripts for integration with :doc:`ZTP <ztp/index>`.
Optionally you can add the VDX pack for building custom workflows for automating Brocade VDX switches.

1. Install |bwc|
----------------

To install |bwc|, follow the detailed installation instructions for your Linux flavor.
It will walk you through installing and configuring StackStorm first, and upgrade it
to |bwc| with the license key you received when registering for evaluation or
purchasing. This last step will also set up the |bwc| repository on your box.

* :doc:`/install/deb`
* :doc:`/install/rhel7`
* :doc:`/install/rhel6`


2. Install |ipf|
----------------

Make sure that |bwc| repository is set up on the box.

Install the |ipf|:

* On Ubuntu/Debian: ::

    sudo apt-get install -y bwc-ipfabric-suite

* On RHEL/CentOS: ::

    yum install -y bwc-ipfabric-suite

3. Configure Topology Service
-----------------------------

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

* Run DB setup script (the script will pick DB name, username and password from the ``bwc-topology-service.conf`` file): ::

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

4. Smoke-check the Installation
-------------------------------

Run some |ipf| CLI commands to see that everything is installed.

.. code-block:: bash

  bwc --version
  bwc --help
  bwc ipf fabric list

5. (Optional) Install VDX Pack
------------------------------

If you want to write your own workflows that integrate with Brocade VDX switches, you might like
to try out our `VDX <https://github.com/StackStorm/st2contrib/tree/master/packs/vdx>`_ pack.

First make sure you have the prerequisite libraries installed. On Ubuntu/Debian: ::

      sudo apt-get install libxml2-dev libxslt1-dev

On RHEL/CentOS: ::

      sudo yum install libxml2-dev libxslt1-dev

Then install the pack: ::

      st2 run packs.install packs=vdx

This will give you a wide range of VDX-specific actions you can use in any workflow. Try it out!


.. rubric:: What's Next?

* New to |BWC|? Go to fundamentals - start with :doc:`/start`.
* Understand the |ipf| operations - go over :doc:`./operation/overview`.
* Understand the |ipf| CLI - read the :doc:`./ipf_cli/basic_cli`.
