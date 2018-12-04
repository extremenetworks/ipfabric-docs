Installation
============

.. warning::
    If you had previously installed the DC Fabric Automation Suite, please do not install this pack, wait for the new release of the DC Fabric Automation Suite. When you install the DC Fabric Automation Suite, it will also install the compatible version of Network Essentials pack automatically.

Installing Pre-requisites
-------------------------
Network Essentials pack requires gcc plus the libxml2-dev and libxslt1-dev libraries. Before installing the Network Essentials pack, please run these commands:

On Ubuntu:

.. code-block:: bash

  sudo apt-get install build-essential libxml2-dev libxslt1-dev

On Redhat/CentOS:

.. code-block:: bash

  sudo yum install gcc libxml2-devel libxslt-devel

Installing Network Essentials
-----------------------------
After installing the above pre-requisites, you can now install the Network Essentials pack using:

.. code-block:: bash

  st2 pack install network_essentials

To install the DC Fabric Suite, follow the installation instructions for the :doc:`DC Fabric Automation Suite <../dcfabric/install>`

* New to |bwc|? Go to fundamentals - start with :doc:`/start`.
* Understand the Network Essentials :doc:`Actions and Workflows<workflows>`.
