# Flask-Blueprints-Loader

[![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/curskey/flask-blueprints-loader/tests.yml?label=tests)](https://github.com/curskey/flask-blueprints-loader/actions/workflows/tests.yml)
[![Codecov](https://img.shields.io/codecov/c/github/curskey/flask-blueprints-loader)](https://codecov.io/gh/curskey/flask-blueprints-loader)

Flask-Blueprints-Loader is an extension for [Flask](https://flask.palletsprojects.com/) that automatically discovers and registers [Blueprint](https://flask.palletsprojects.com/en/3.0.x/blueprints/) for your application.

## Features

- Automatic loading and registration of Flask blueprints.
- Easy configuration via Flask app configuration variables.

## Why Use Flask-Blueprints-Loader?

Flask-Blueprints-Loader is particularly useful for [Large Applications as Packages](https://flask.palletsprojects.com/en/3.0.x/patterns/packages/) that heavily rely on blueprints. Instead of manually registering each blueprint, this extension allows you to automate the process by automatically discovering and registering all blueprints for your application.

## Installation

Flask-Blueprints-Loader is available on [PyPI](https://pypi.org/project/flask-blueprints-loader/) and can be installed with various Python [Application dependency management](https://packaging.python.org/en/latest/guides/tool-recommendations/) tools.

Install using `pip`:

```sh
pip install flask-blueprints-loader
```

## Initialize the Extension

- Application Instance Pattern

```python
from flask import Flask
from flask_blueprints_loader import BlueprintsLoader

app = Flask(__name__)
loader = BlueprintsLoader(app)

with app.app_context():
    loader.load_blueprints()
```

- Application Factories Pattern

```python
from flask import Flask
from flask_blueprints_loader import BlueprintsLoader

loader = BlueprintsLoader()

def create_app():
    app = Flask(__name__)
    loader.init_app(app)

    with app.app_context():
        loader.load_blueprints()

    return app
```

## Directory Structure

Flask-Blueprints-Loader expects your blueprints to be organized in a specific directory structure. By default, it looks for blueprints under the current_app.root_path directory or in the subdirectory specified by the BLUEPRINTS_LOADER_PATH_NAME configuration parameter. Each blueprint should be in its own package and contain a module named "views" (or as specified by the BLUEPRINTS_LOADER_MODULE_NAME configuration parameter) that defines the Blueprint instance and route definitions. If your blueprints are not organized in this way, you may need to make changes to your code to use Flask-Blueprints-Loader.

Here is a structured Flask application with two blueprints, auth and blog:

myapp/
├── __init__.py
├── auth/
│   ├── __init__.py
│   └── views.py
├── blog/
│   ├── __init__.py
│   └── views.py
├── templates/
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   └── blog/
│       ├── index.html
│       └── post.html
├── config.py
└── wsgi.py

## Configuration

BLUEPRINTS_LOADER_PATH_NAME (str)
    : The name of the subdirectory containing the blueprints. By default, blueprints are under the current_app.root_path.

BLUEPRINTS_LOADER_MODULE_NAME (str)
    : The name of the module containing the blueprints. By default, it is set to "views".

BLUEPRINTS_LOADER_UNLOADS (list)
    : A list of blueprint names to exclude from loading. By default, it is an empty list.

## Links

- [PyPI Releases](https://pypi.org/project/flask-blueprints-loader/)
- [Source Code](https://github.com/curskey/flask-blueprints-loader/)
- [Issue Tracker](https://github.com/curskey/flask-blueprints-loader/issues/)

## License

This project is under the [MIT](https://github.com/curskey/flask-blueprints-loader/blob/main/LICENSE) license.
