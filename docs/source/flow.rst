Workflow Designer
=================

Workflow Designer is a web-based GUI for creating and editing :doc:`Orquesta </orquesta/index>`
and :doc:`Mistral </mistral>` workflows. Using a web browser, you can visualize existing workflows,
and create new ones.

.. image:: /_static/images/flow/pkg_promote_workflow.png
    :align: center

All your workflows are still stored as code on your system, but the GUI simplifies the workflow
development process. Updates to the graphical view are immediately updated in the underlying code,
and vice-versa.

.. contents:: Contents
   :local:


Launching Workflow Designer
---------------------------

Launch Workflow Designer from the main |ewc| Web UI. First login to your |ewc| system at
https://YOUR_HOST_IP/. You can launch Designer in two different ways - either by creating a new
workflow, or by editing an existing workflow:

Create a New Workflow
~~~~~~~~~~~~~~~~~~~~~

From the Web UI, click on the "Actions" button at the top of the screen. From there, click the round
"+" button at the bottom center of the screen:

.. image:: /_static/images/flow/launch_designer.png
    :align: center

This will launch Workflow Designer with a new, blank workflow:

.. image:: /_static/images/flow/new_workflow.png
    :align: center

Edit an Existing Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~

You can also edit existing workflows. Using the |ewc| Web UI, go the Actions tab, and navigate to
an Orquesta or Mistral workflow. Select the workflow and click "Edit" at the right of the workflow details pane:

.. image:: /_static/images/flow/existing_workflow.png
    :align: center

This will launch a new browser tab with your workflow:

.. image:: /_static/images/flow/pkg_promote_workflow.png
    :align: center


Using Workflow Designer
-----------------------

The interface has three main parts: the Library of installed actions, the Workflow Canvas, and the Details panel.

The Library shows all installed actions. You can filter from the list, or just scroll to a pack, and
pick an action. Drag it onto the canvas to add it to the workflow.

The Workflow Canvas has buttons for Undo, Redo, Redraw, Save and Run:

 .. image:: /_static/images/flow/workflow_toolbar.png
    :align: center

You can undo or redo multiple steps. Redraw will automatically lay out the workflow. Warning: this
will change your saved positions!

You must "Save" the workflow before you can run it. Clicking "Save" will save the workflow and its
metadata to disk and the |ewc| database.

If your workflow requires inputs, clicking "Run" will prompt for them:

 .. image:: /_static/images/flow/run_workflow.png
    :align: center

You can also adjust or reset the zoom, using the buttons on the right-hand side of the canvas:

 .. image:: /_static/images/flow/zoom.png
    :align: center

Metadata
~~~~~~~~

The "Metadata" defines data about the workflow, rather than the workflow itself.

This is defined in the "Meta" tab of the Details panel:

 .. image:: /_static/images/flow/metadata.png
    :align: center


All workflows must have a Runner Type. The default is "Orquesta" - we recommend this for all new
workflows. Mistral will be deprecated in a future release.

You **must** choose a workflow name. This will be how you reference the workflow in future with
``st2 run``, or as part of another workflow.

If you do not choose a pack, the "default" pack is used. We recommend using your own pack.

The Description is optional. It's a good idea to set this - it will remind future you what this
workflow does.

The "Entry point" is the file the workflow is saved to. Typically this is
``workflows/<workflow_name>.yaml``. This will be used if you do not pick a custom entry point.

Parameters
~~~~~~~~~~

Parameters are used as inputs to your workflow. They can be used to pass in dynamic information
when you run this workflow. Most workflows will have at least one input parameter.

To add Parameters, go to the Parameters tab. Click "Add Parameter":

.. image:: /_static/images/flow/parameters.png
   :align: center

You must provide a name, and a type (string, boolean, number, object, integer, array). You can mark
the parameter as "Required" - that is, it **must** be provided when the workflow is run, and you
can provide a default value if one is not provided. You can also mark the parameter as "secret",
so it is masked in logs.

For more information about parameters, see the :doc:`Actions </actions>` documentation.

Tasks
~~~~~

The Library on the left shows actions installed on this system that can be added to your workflow.
These are grouped by Pack. If you want to install more actions, check the "Packs" tab in the Web UI.

You can filter from the available list of actions by typing in a partial keyword, e.g.:

.. image:: /_static/images/flow/filtered_actions.png
   :align: center

Find the actions you want to use in your workflow, and drag them onto the canvas. Repeat as required.

.. image:: /_static/images/flow/basic_workflow.png
   :align: center

To configure a task, select it. You can then use the Details panel to rename the task, and configure
task parameters, properties and transitions.

.. image:: /_static/images/flow/task_parameters.png
   :align: center

To rename a task, click "Edit", and rename.

Input parameters can use hard-coded values, or use other variables available, such as input parameters.
For Orquesta workflows, this might look like ``<% ctx().my_input %>``.

The "Properties" tab lets you set advanced controls, such as "with-items" - to run multiple actions
across a list of inputs, and "Join", to wait for parallel tasks to complete before proceeding.

The Transitions tab lets you control Transition behavior - which tasks should we execute next, under
which conditions? See below for more.

To delete a task, select it, then click the "Trash" icon:

.. image:: /_static/images/flow/delete_task.png
   :align: center


Transitions
~~~~~~~~~~~

Transitions are how we move from one task to another. Orquesta gives us powerful controls over task
transition. We can choose simple success/failure paths, or we can branch based upon conditions such
as returned result values.

We can run multiple actions in parallel, or we can run sequential actions. Using the "join" option,
we can wait for parallel tasks to complete, before proceeding.

Workflow Designer lets us draw transitions between tasks, add conditions, and even set colors for the
transition arrow. After all, it's not just as simple as "Green for success, Red for failure."

To add a transition, select a task:

.. image:: /_static/images/flow/task_selected.png
   :align: center

Click and drag the connector to the next task you want to transition to. You can repeat this multiple
times if you have multiple transitions:

.. image:: /_static/images/flow/transition_added.png
   :align: center

By default, new transitions have no criteria. That is, they will always transition to the next task
upon completion. Common criteria to add is ``<% succeeded() %>`` or ``<% failed() %>``, for simple
success/failure. More complex criteria can branch based upon other variables - for example if a task result has more than 3 entries. See the :doc:`Orquesta
documentation</orquesta/languages/orquesta>` for more details.

You can also choose the transition arrow color. Pick a color from the drop-down selector, or type
in a `color name or hex code <https://htmlcolorcodes.com>`_:

.. image:: /_static/images/flow/transitions.png
   :align: center

Transitions often include publishing some or all of the task result. It can then be used as
an input to future tasks.

To publish a value, select the transition, then enable the "Publish" option. Give it a name, and
the item you want to publish. Typically this will be ``<% result().<something> %>``, e.g.:

.. image:: /_static/images/flow/publish_status_code.png
   :align: center

We can now refer to ``<% ctx().status_code %>`` elsewhere in our workflows - for example, we could
use it as part of the message we send via ``chatops.post_message``.

To remove a transition, select the transition arrow, then click the "Trash" icon to remove it.

Code View
~~~~~~~~~

Workflow Designer is a visual tool for creating and editing workflows. But the workflows themselves
are always stored as code. You can switch to this code view by clicking the icon at the top right
of the details panel:

.. image:: /_static/images/flow/code_view.png
   :align: center
