Installation
============

To install |bwc| with |ipf|, obtain the lisense key from `Brocade.com/bwc <https://www.brocade.com/bwc>`_, and
run the command below, replacing the ``${ENTERPRISE_LICENSE_KEY}`` with the
key you received when registering for evaluation or purchasing.

.. code-block:: bash

  curl -sSL https://brocade.com/bwc/install/install.sh | bash -s -- --user=st2admin --password=Ch@ngeMe --staging --unstable --suite=bwc-ipfabric-suite --license=${ENTERPRISE_LICENSE_KEY}

.. TODO:: Doesn't work yet, for now please use this for testing:

  .. code-block:: bash

    wget https://stackstorm.com/bwc/install.sh && chmod +x install.sh

    ./install.sh --user=st2admin --password=Ch@ngeMe --staging --unstable --license=8a33..

    curl -SsL https://stackstorm.com/bwc/install-suite.sh |  bash -s -- --user=st2admin --password=Ch@ngeMe --staging --unstable --suite=bwc-ipfabric-suite --license=8a33..

With luck, it will install |bwc|, |ipf|, and configures all components
to work together on a signle host.

.. note:: These script is NOT an installer: it just codifies the installation steps, to serve
  as an inspiration for your own automation. While we do the best to test it on some systems,
  it is not guaranteed to work on any system, due to all the permutations of distros, versions, and environment. For best results, please read, understand, and follow the
  installation instructions below.


System requirements
-------------------

Components
----------
|ipf| installs on top of |bwc|. It adds topology service, ip-fabric automation packs
that actions and workflows , `bwc ipfabric` CLI th, zero-touch-provisioning script
to trigger automation on adding a new switch, and optional VDX pack for building custom workflows.


1. Install |bwc|
----------------

To install |bwc|, follow installation instructions for your OS:

* :doc:`/install/deb`
* :doc:`/install/rhel7`
* :doc:`/install/rhel6`

At the last step there, you will set up BWC Enterprise repository access
with the license key you received when registering for evaluation or purchasing.


2. Install |ipf|
----------------
  Make sure that |bwc| Enterprise repository access is set up on the box.



  * On Ubuntu/Debian: ::

      sudo apt-get install bwc-ipfabric-suite

  * On RHEL/CentOS: ::

      yum install bwc-ipfabric-suite

  We recommend to install them only when: its

3. Configure Topology Service
-----------------------------

* Generate an API key to connect topology service to st2 API. ::

    st2 apikey -k -m '{"used_for": "BWC topology service"}'

* Edit a file ``/etc/brocade/bwc/bwc-topology-service.conf``. Set ``st2_api_key`` value to
  the generated API key. Set a password for DB as desired.

* Run DB setup script (it will pick DB name, user and password from the ``.conf`` file): ::

    sudo /opt/brocade/bwc/bin/bwc_topology_db_setup.sh

* Fix the access rights to the log files: ::

    sudo chown -R bwc:root /var/log/brocade/bwc/

.. dz: this is quite unusual step, why??

* Start the ``bwc-topology`` service:

  * On Ubuntu/Debian: ::

      service bwc-topology start

  * On RHEL/CentOS: ::

      systemctl bwc-topology start


4. Check if everything is in place
----------------------------------

.. TODO:: add some basic BWC commands

.. rubric:: What is Next?

* New to |BWC|? Go to fundamentals - start with :doc:`/start`.
* Understand the |ipf| operations - go over :doc:`operations/overview`.
* Understand the |ipf| CLI - read the :doc:`ipf-cli/basic_cli`.
