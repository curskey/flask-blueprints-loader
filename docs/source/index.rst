
Flask-Blueprints-Loader's documentation
=======================================

Flask-Blueprints-Loader is an extension for `Flask`_  that automatically
discovers and registers `Blueprint`_ for your application.

.. _Flask: https://flask.palletsprojects.com/
.. _Blueprint: https://flask.palletsprojects.com/en/3.0.x/blueprints/

Features
--------

* Automatic loading and registration of Flask blueprints.
* Easy configuration via Flask app configuration variables.


Why Use Flask-Blueprints-Loader?
--------------------------------

Flask-Blueprints-Loader is particularly useful for `Large Applications as Packages`_
that heavily rely on blueprints. Instead of manually registering each blueprint, this
extension allows you to automate the process by automatically discovering and
registering all blueprints for your application.

.. _Large Applications as Packages: https://flask.palletsprojects.com/en/3.0.x/patterns/packages/

Installation
------------

Flask-Blueprints-Loader is available on `PyPI`_ and can be installed with
various Python `Application dependency management`_ tools. Install using `pip`_:

.. code-block:: sh

   $ pip install flask-blueprints-loader

.. _PyPI: https://pypi.org/project/flask-blueprints-loader/
.. _pip: https://pip.pypa.io/en/stable/
.. _Application dependency management: https://packaging.python.org/en/latest/guides/tool-recommendations/


Initialize the Extension
------------------------

Application Instance Pattern

.. code-block:: py3

   from flask import Flask
   from flask_blueprints_loader import BlueprintsLoader

   app = Flask(__name__)
   loader = BlueprintsLoader(app)

   with app.app_context():
      loader.load_blueprints()


Application Factories Pattern

.. code-block:: py3

   from flask import Flask
   from flask_blueprints_loader import BlueprintsLoader

   loader = BlueprintsLoader()

   def create_app():
      app = Flask(__name__)
      loader.init_app(app)

      with app.app_context():
         loader.load_blueprints()

      return app

Directory Structure
-------------------

Flask-Blueprints-Loader expects your blueprints to be organized in a specific directory structure.
By default, it looks for blueprints under the :py:data:`current_app.root_path` directory,
with each blueprint in its own package containing a :py:mod:`views.py` module that defines
the :py:obj:`Blueprint` instance and route definitions.

Here is a structured  Flask application with two blueprints, `auth` and `blog`

.. code-block:: text

   myapp/
   ├── __init__.py
   ├── auth/
   │ ├── __init__.py
   │ └── views.py
   ├── blog/
   │ ├── __init__.py
   │ └── views.py
   ├── templates/
   │ ├── auth/
   │ │ ├── login.html
   │ │ └── register.html
   │ └── blog/
   │ ├── index.html
   │ └── post.html
   ├── config.py
   └── wsgi.py

Configuration
-------------

.. py:data:: BLUEPRINTS_LOADER_PATH_NAME
   :type: (str)
   :value: ""

   The name of the subdirectory containing the blueprints. By default blueprints are under the :py:data:`current_app.root_path`.

.. py:data:: BLUEPRINTS_LOADER_MODULE_NAME
   :type: (str)
   :value: views

   The name of the module containing the blueprints. By default, it is set to "views".

.. py:data:: BLUEPRINTS_LOADER_UNLOADS
   :type: (list)
   :value: []

   A list of blueprint names to exclude from loading. By default, it is an empty list.

Constraints and Drawbacks
-------------------------

Flask-Blueprints-Loader has the following constraints and drawbacks:

* Blueprints are expected to be organized in a specific way, with a :py:mod:`views.py` module containing the :py:obj:`Blueprint` instance in each blueprint package.
* If your blueprints are not organized in this way, you may need to make changes to your code to use Flask-Blueprints-Loader.

Additional Information
----------------------

.. toctree::
   :maxdepth: 2

   api
   changes
   license
