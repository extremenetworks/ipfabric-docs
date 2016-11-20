Installation
============

To quickly install |bwc| with the Internet Exchange Automation Suite, obtain a license key from `Brocade.com/bwc <https://www.brocade.com/bwc>`_,
and run the commands below, replacing ``${BWC_LICENSE_KEY}`` with the key you received when registering for 
evaluation or purchasing. These commands will install |bwc|, Network Essentials, Internet Exchange suite, and configure all components to work
together on a single host:

.. warning::
    Make sure you are running the latest version of ``curl``. If you are using RHEL/CentOS, run ``sudo yum update curl nss``.
    For Ubuntu systems, run ``sudo apt-get install curl ca-certificates``. The commands below may fail if you do not update ``curl`` first.

.. code-block:: bash

  curl -SsL -O https://brocade.com/bwc/install/install.sh && chmod +x install.sh
  ./install.sh --user=st2admin --password=Ch@ngeMe --suite=bwc-ixp-suite --license=${BWC_LICENSE_KEY}

If you already have |bwc| installed, and want to add the Internet Exchange suite on top of an existing |bwc| installation,
run the following commands, replacing ``${BWC_LICENSE_KEY}`` with the key you received when 
registering for evaluation or purchasing:

.. code-block:: bash

  curl -SsL -O https://brocade.com/bwc/install/install-suite.sh && chmod +x install-suite.sh
  ./install-suite.sh --user=st2admin --password=Ch@ngeMe --suite=bwc-ixp-suite --license=${BWC_LICENSE_KEY}

If you have a more complex environment, or you just want to see exactly what the scripts are doing, read on.
The rest of this document will explain how to how to manually install and configure the individual components.

System requirements
-------------------

The system requirements for |bwc| with Internet Exchange suite are the same as the core platform requirements.
See the :doc:`system requirements documentation</install/system_requirements>` for more details.

Components
----------

The Internet Exchange suite installs on top of |bwc|. It provides workflows, actions, sensors and services
for managing Brocade network devices in Internet Exchange environments. The Internet Exchange suite uses
components of the :doc:`../essentials/overview` suite. If the Network Essentials suite is not currently
installed it will be automatically installed during Internet Exchange suite installation.

1. Install |bwc|
----------------

To install |bwc|, follow the detailed installation instructions for your Linux flavor.
It will walk you through installing and configuring StackStorm first, and upgrade it
to |bwc| with the license key you received when registering for evaluation or
purchasing. This last step will also set up the |bwc| repository on your box.

* :doc:`/install/deb`
* :doc:`/install/rhel7`
* :doc:`/install/rhel6`


2. Install Internet Exchange Suite
----------------------------------

Make sure that |bwc| repository is set up on the box.

Install Internet Exchange suite:

* On Ubuntu/Debian: ::

    sudo apt-get install -y bwc-ixp-suite

* On RHEL/CentOS: ::

    yum install -y bwc-ixp-suite


3. Smoke-check the Installation
-------------------------------

Run these CLI commands to check that the actions are now available:

.. code-block:: bash

  st2 action list --pack=ixp
  st2 action list --pack=essentials

You can also see the new "Internet Exchange" pack in the Web UI.

.. rubric:: What's Next?

* New to |BWC|? Go to fundamentals - start with :doc:`/start`.
* Understand the operations - go over :doc:`operation`.
