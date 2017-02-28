Installation
============

Pre-requisites
--------------
Network Essentials pack requires gcc plus the libxml2-dev and libxslt1-dev libraries.

Before installing this pack, please run these commands:

On Ubuntu:

.. code-block:: bash

  sudo apt-get install build-essential libxml2-dev libxslt1-dev

For example, on Redhat/CentOS

.. code-block:: bash

  sudo yum groupinstall "Development Tools"
  sudo yum install libxml2-dev libxslt1-dev

After installing the above pre-requisites, install the pack using:

.. code-block:: bash

  st2 pack install network_essentials

To install DC Fabric Suite, follow the installation instructions for the :doc:`DC Fabric Automation Suite <../dcfabric/install>`

* New to |bwc|? Go to fundamentals - start with :doc:`/start`.
* Understand the Network Essentials :doc:`Actions and Workflows<workflows>`.
