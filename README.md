**IP fabric docs**

# Writing the Docs

Product documentation for IPfabric is maintained in this repository. These docs are built using
[Sphinx](http://www.sphinx-doc.org/en/stable/).

## Build and Run the Docs.

Follows these steps to build the docs locally:

```bash
git clone https://github.com/StackStorm/ipfabric-docs.git
cd ipfabric-docs
make docs
```

Keep in mind that the initial ``make docs`` run will take a while because it needs to install
all the Python dependencies which are needed to build the docs.

`make livedocs` builds the docs and runs the doc site live at [http://localhost:8000](http://localhost:8000) to
validate changes locally prior to committing any code.

## Sphinx Tricks

* If the whole section belongs in the Enterprise Edition, put the following note:
    ```
    .. note::

       Role Based Access Control (RBAC) is only available in StackStorm Enterprise Edition. For
       information about enterprise edition and differences between community and enterprise edition,
       please see `stackstorm.com/product <https://stackstorm.com/product/#enterprise>`_.
    ```
    Refer to Enterprise edition in passing with

        `see Enterprise Edition <https://stackstorm.com/product/#enterprise>`_

* TODO (Use [http://localhost:8000/todo.html](http://localhost:8000/todo.html) for full TODO list (must be empty when we ship)
:

    .. todo:: Here is a TODO

* Code fragment:

    .. code-block: bash

      # List all available triggers
        st2 trigger list

* Reference the document

    :doc:`/start`
    :doc:`in the Rules doc </rules>`

* Referencing an arbitrary section: for instance, there's examples section in sensors.rst. Define a reference on `examples` section in sensors.rst:

         .. _sensors-examples:

    and point to it as from this, or from other documents as:

           :ref:`sensors-examples`
           :ref:`My examples <sensors-examples>`

    Note that the leading `_` underscore is gone, and the reference is quoted.

    Name convention for references is `_filename-refname` (because they are unique across the docs).  Note that there is no way to reference just a point in the docs. See http://sphinx-doc.org/markup/inline.html#cross-referencing-syntax

* External links:

    `External link <http://webchat.freenode.net/?channels=stackstorm>`_

* Inlcude a document, full body:

    .. include:: /engage.rst

* Link to GitHub st2 repo

    :github_st2:`st2/st2common/st2common/operators.py </st2common/st2common/operators.py>`

* Link  to Github st2contrib repo:

    :github_contrib:`Link to docker README on st2contrib<packs/docker/README.md>`

* Link to st2contrib and st2incubator repos on Github (using a global we set up in source/conf.py)

    `st2contrib`_
    `st2incubator`_

* The pattern to include an example from `/st2/contrib/examples`: make example file name a reference on github. May say that it is deployed to `/usr/share/doc/st2/examples/`, and auto-include the file:

    Sample rule: :github_st2:`sample-rule-with-webhook.yaml
    </contrib/examples/rules/sample-rule-with-webhook.yaml>` :

    .. literalinclude:: /../../st2/contrib/examples/rules/sample_rule_with_webhook.yaml
        :language: json


## Pandoc - convert md <-> rst and more

pandoc - a super-tool to convert between formats. Sample for markdown conversion:

  sudo apt-get install pandoc
  pandoc --from=markdown --to=rst --output=README.rst README.md

## Running docs only

To make docs changes, without installing full development environment (e.g., on Mac or Windows):

```bash
git clone git@github.com:StackStorm/ipfabric-docs.git
cd ipfabric-docs
make docs
# make docs will fail; ignore the failure:
# it will get st2 and ipfabric and set up virtualenv with sphinx/shinx-autobuild
. virtualenv/bin/activate
sphinx-autobuild -H 0.0.0.0 -b html ./docs/source/ ./docs/build/html
```

To Generate Docs for Automation Suites run the following: 
* scripts/clone-essentials.sh
* scripts/clone-dcfabric.sh
* python scripts/generate-essentials-documentation.py
* python scripts/generate-dcfabric-documentation.py
* python scripts/generate-inventorydocumentation.py

This should update all the documentation after cloning the repos. You will have to change the branch of the repos you want to point to.
Edit, enjoy live updates.
