Workflow Designer
=================

Workflow Designer is an HTML5-based graphical tool for managing workflows.  Using a web browser,
users can quickly create new workflows and modify existing ones. 

Workflow Designer provides a graphical representation of workflow, side-by-side with the underlying code.
Users can quickly add new actions to the workflow, and connect them together. Updates to the graphical 
workflow are immediately reflected in the code, and vice-versa.

.. figure:: /_static/images/flow/workflow_designer.png
    :align: center

Workflow Designer is launched from the main |bwc| Web UI. First login to https://YOUR_HOST_IP/.
You can launch Designer in two different ways - either by creating a new workflow, or by editing an
existing workflow:

Create a New Workflow
---------------------

From the Web UI, click on the "Actions" button at the top of the screen. From there, click the round
"+" button at the bottom center of the screen:

.. figure:: /_static/images/flow/launch_designer.png
    :align: center

This will launch Workflow Designer with a new, blank workflow:

.. figure:: /_static/images/flow/new_workflow.png
    :align: center

Edit an Existing Workflow
-------------------------

You can also edit existing workflows

.. note::
  Note that Workflow Designer can only be used to edit :doc:`mistral` workflows. It can not be
  used to edit :doc:`actionchain` workflows.

Using the |bwc| Web UI, go the Actions tab, and navigate to a mistral-v2 workflow. Select the workflow
and click "Edit" at the bottom of the workflow details pane:

.. figure:: /_static/images/flow/existing_workflow.png
    :align: center

This will launch a new browser tab with your workflow:

.. figure:: /_static/images/flow/bgp_workflow.png
    :align: center

Using Workflow Designer
-----------------------

Add Action
~~~~~~~~~~

The left-hand side of the screen shows all available actions installed on this system,
grouped by pack. You can search for actions, and drag them into the centre. Do this with
all the actions you need.

Link Actions
~~~~~~~~~~~~

Actions can be linked together to form complex workflows. The workflow can take different
branches, depending on whether a step succeeds or fails. To link actions together, hover
over an action. You will see three icons appear beneath the action:

.. figure:: /_static/images/flow/action_options.png
    :align: center

These represent paths to take "on-success", "on-error" or "on-complete". Click and hold
on an option, then move your mouse to the next action you want to link to. Release your mouse,
and a new link will be added.

It is a common pattern to take different paths for success or error. This allows you to build
complex workflows.

Edit/Remove Action
~~~~~~~~~~~~~~~~~~

Clicking on the "Pen" icon on an action will let you rename the action.

Click on the "X" on an action and it will be removed from the canvas.

.. note::
  All the above steps - adding, linking, editing actions - can also be done using the code
  window on the right-hand side. Changes made to the code are immediately reflected in the
  central pane. Similarly, changes made in the central pane are immediately updated in the
  code.

Settings
~~~~~~~~

Click on the "gears" icon at the top centre to access workflow settings. Here you can
specify which pack the workflow belongs to, its name, and whether it should be enabled:

.. figure:: /_static/images/flow/workflow_settings.png
    :align: center

You can also add input parameters to the workflow, to allow sensors and other actions
to pass data into this workflow.

Toolbar
~~~~~~~

The toolbar at the top of the canvas provides quick access to these actions:

 * **Undo**: undo previous actions. Click multiple times to go back multiple steps.
 * **Redo**: redo the action that was just undron. Click multiple times to go forward multiple steps.
 * **Redraw**: re-draw the workflow layout to suit the current screen size.
 * **Save**: save the workflow to the database.
 * **Run**: manually run the workflow.

 .. figure:: /_static/images/flow/workflow_toolbar.png
    :align: center
