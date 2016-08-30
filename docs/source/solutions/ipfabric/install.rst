Installation
============

To install |bwc| with |ipf|, obtain the license key from `Brocade.com/bwc <https://www.brocade.com/bwc>`_, and
run the commands below, replacing the ``${BWC_LICENSE_KEY}`` with the
key you received when registering for evaluation or purchasing.

.. code-block:: bash

  wget https://brocade.com/bwc/install.sh && chmod +x install.sh
  ./install.sh --user=st2admin --password=Ch@ngeMe --suite=bwc-ipfabric-suite --license=${BWC_LICENSE_KEY}

This will install |bwc|, |ipf|, and configures all components to work together on a single host.

If you already have |st2| installed, and need to add |ipf| on top of existing |st2| installation,
run the following command, replacing

.. code-block:: bash

  curl -SsL https://brocade.com/bwc/install-suite.sh |  bash -s -- --user=st2admin --password=Ch@ngeMe --staging --unstable --suite=bwc-ipfabric-suite --license=${BWC_LISENSE_KEY}

Read on to understand the installation and configuration of individual components,
or follow instructions below to install manually.

.. TODO:: before the final redirects are set and we are still on staging/unstable, use the following:

  .. code-block:: bash

    # To install BWC and IP fabric on a clean box:
    wget https://stackstorm.com/bwc/install.sh && chmod +x install.sh
    ./install.sh --user=st2admin --password=Ch@ngeMe --suite=bwc-ipfabric-suite --staging --unstable --license=${BWC_LICENSE_KEY}

    # To install suite on top of BWC/st2:
    curl -SsL https://stackstorm.com/bwc/install-suite.sh |  bash -s -- --user=st2admin --password=Ch@ngeMe --staging --unstable --suite=bwc-ipfabric-suite --license=${BWC_LISENSE_KEY}


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
|ipf| installs on top of |bwc|. It adds topology service, ip-fabric automation packs
that actions and workflows , `bwc ipf` CLI makes using IP Fabric easier, zero-touch-provisioning script
to integrate automation with :doc:`ZTP <ztp/index>`, and optional VDX pack for building custom workflows.


1. Install |bwc|
----------------

To install |bwc|, follow the detailed installation instructions for your Linux flavor.
It will work you through installing and configuring community edition first,
and upgrade it to |bwc| with the license key you received when registering for evaluation
or purchasing. This last step will also set up enterprise repository access on your box.

* :doc:`/install/deb`
* :doc:`/install/rhel7`
* :doc:`/install/rhel6`


2. Install |ipf|
----------------

Make sure that |bwc| enterprise repository access is set up on the box.

Install the |ipf| suite:

* On Ubuntu/Debian: ::

    sudo apt-get install -y bwc-ipfabric-suite

* On RHEL/CentOS: ::

    yum install -y bwc-ipfabric-suite

3. Configure Topology Service
-----------------------------

* Generate an API key to connect topology service to st2 API. ::

    st2 apikey create -k -m '{"used_for": "BWC topology service"}'

* Edit a configuration file ``/etc/brocade/bwc/bwc-topology-service.conf``,
  set ``st2_api_key`` value to the st2 API key, and change default DB
  username and password to a desired one in ``connection`` string. ::

  ...
  ## Postgres
  connection = 'postgresql://bwcuser:bwcsecret@localhost/bwc_topology'

  # StackStorm
  st2_auth_url = 'https://localhost/auth'
  st2_api_url = 'https://localhost:443/api'
  st2_api_key = 'ZDNkMjJiNmFkYzFiMmEyNjRiMmQ2NGRjNGYzODhmYmZhNmU2NGM3NTI0ZmM5M2U2MTY1YWZjMWM3NjllNzcwNA'

* Run DB setup script (the script will pick DB name, username and password from the ``bwc-topology-service.conf`` file): ::

    sudo /opt/brocade/bwc-topology/bin/bwc_topology_db_setup.sh

* Fix the access rights to the log files: ::

    sudo chown -R bwc:bwc /var/log/brocade/bwc/


* Start the ``bwc-topology`` service:

  * On Ubuntu/Debian: ::

      service bwc-topology start
      # Check that it is running indeed
      service bwc-topology status

  * On RHEL/CentOS: ::

      systemctl bwc-topology start
      # Check that it is running indeed
      systemctl bwc-topology status

4. Smoke-check the installation
-------------------------------
Run few |ipf| CLI commands to see that everything is installed.

.. code-block::

  bwc --version
  bwc --help
  bwc ipf fabric list


.. rubric:: What is Next?

* New to |BWC|? Go to fundamentals - start with :doc:`/start`.
* Understand the |ipf| operations - go over :doc:`./operation/overview`.
* Understand the |ipf| CLI - read the :doc:`./ipf_cli/basic_cli`.
