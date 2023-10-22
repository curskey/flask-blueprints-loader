Flask-Blueprints-Loader
=======================

.. image:: https://img.shields.io/github/actions/workflow/status/curskey/flask-blueprints-loader/tests.yml?label=tests
   :alt: GitHub Workflow Status (with event)

.. image:: https://img.shields.io/codecov/c/github/curskey/flask-blueprints-loader
   :alt: Codecov

Flask-Blueprints-Loader is an extension for `Flask`_  that automatically discovers and registers `Blueprint`_ for your application.

.. _Flask: https://flask.palletsprojects.com/
.. _Blueprint: https://flask.palletsprojects.com/en/3.0.x/blueprints/

Installing
----------

Install using `pip`_:

.. code-block:: sh

   $ pip install -U flask-blueprints-loader

.. _pip: https://pip.pypa.io/en/stable/

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

Links
-----

-   `Documentation`_
-   `PyPI Releases`_
-   `Source Code`_
-   `Issue Tracker`_

.. _Documentation: https://flask-blueprints-loader.readthedocs.io/en/latest/
.. _PyPI Releases: https://pypi.org/project/flask-blueprints-loader/
.. _Source Code: https://github.com/curskey/flask-blueprints-loader/
.. _Issue Tracker: https://github.com/curskey/flask-blueprints-loader/issues/
