Ubuntu / Debian
===============

This guide provides step-by step instructions for installing StackStorm on a single Ubuntu/Debian system per
the :doc:`Reference deployment <overview>`.

.. rubric:: TL;DR

That's OK! You're busy, we get it. How do you just get started? Get yourself a clean box, and run this command:

::

   curl -sSL https://stackstorm.com/packages/install.sh | bash -s -- --user=st2admin --password=<CHANGEME>

.. contents::

Supported versions
------------------

We support Ubuntu 14.04

Sizing the server
-----------------
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

Minimal installation
--------------------

Install Dependencies
~~~~~~~~~~~~~~~~~~~~



Setup repositories
~~~~~~~~~~~~~~~~~~

The following script will detect your platform and architecture and setup the repo accordingly. It will also install the GPG key for repo signing.

  .. code-block:: bash

    curl -s https://packagecloud.io/install/repositories/StackStorm/stable/script.deb.sh | sudo bash

Install StackStorm components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  .. code-block:: bash

      sudo apt-get install -y st2 st2mistral
