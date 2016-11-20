Installation
============

To quickly install |bwc| with Network Essentials, obtain a license key from `Brocade.com/bwc <https://www.brocade.com/bwc>`_,
and run the commands below, replacing ``${BWC_LICENSE_KEY}`` with the key you received when registering for 
evaluation or purchasing. These commands will install |bwc|, Network Essentials, and configure all components to work
together on a single host:

.. warning::
    Make sure you are running the latest version of ``curl``. If you are using RHEL/CentOS, run ``sudo yum update curl nss``.
    For Ubuntu systems, run ``sudo apt-get install curl ca-certificates``. The commands below may fail if you do not update ``curl`` first.

.. code-block:: bash

  curl -SsL -O https://brocade.com/bwc/install/install.sh && chmod +x install.sh
  ./install.sh --user=st2admin --password=Ch@ngeMe --suite=bwc-essentials-suite --license=${BWC_LICENSE_KEY}

If you already have |bwc| installed, and want to add Network Essentials on top of an existing |bwc| installation,
run the following commands, replacing ``${BWC_LICENSE_KEY}`` with the key you received when 
registering for evaluation or purchasing:

.. code-block:: bash

  curl -SsL -O https://brocade.com/bwc/install/install-suite.sh && chmod +x install-suite.sh
  ./install-suite.sh --user=st2admin --password=Ch@ngeMe --suite=bwc-essentials-suite --license=${BWC_LICENSE_KEY}

If you have a more complex environment, or you just want to see exactly what the scripts are doing, read on.
The rest of this document will explain how to how to manually install and configure the individual components.

System requirements
-------------------

The system requirements for |bwc| with Network Essentials are the same as the core platform requirements.
See the :doc:`system requirements documentation</install/system_requirements>` for more details.

Components
----------

The Network Essentials suite installs on top of |bwc|. It adds a set of common basic actions for
configuring Brocade VDX and SLX switches. 

1. Install |bwc|
----------------

To install |bwc|, follow the detailed installation instructions for your Linux flavor.
It will walk you through installing and configuring StackStorm first, and upgrade it
to |bwc| with the license key you received when registering for evaluation or
purchasing. This last step will also set up the |bwc| repository on your box.

* :doc:`/install/deb`
* :doc:`/install/rhel7`
* :doc:`/install/rhel6`


2. Install Network Essentials
-----------------------------

Make sure that |bwc| repository is set up on the box.

Install Network Essentials:

* On Ubuntu/Debian: ::

    sudo apt-get install -y bwc-essentials-suite

* On RHEL/CentOS: ::

    yum install -y bwc-essentials-suite


3. Smoke-check the Installation
-------------------------------

Run this CLI command to check that the actions are now available:

.. code-block:: bash

  st2 action list --pack=essentials

You can also see the new "Essentials" pack in the Web UI.

.. rubric:: What's Next?

* New to |BWC|? Go to fundamentals - start with :doc:`/start`.
* Understand the operations - go over :doc:`overview`.
