from collections.abc import Generator
from pathlib import Path
from typing import Any

import pytest
from flask import Flask

from flask_blueprints_loader import BlueprintsLoader


def flask_app(tmp_path) -> Flask:
    package = tmp_path / "myapp"
    package.mkdir(exist_ok=True)
    app_module = package / "__init__.py"
    app_module.write_text("from flask import Flask\napp = Flask(__name__)")
    app = __import__(package.name).app
    app.config["TESTING"] = True
    app.config["BLUEPRINTS_LOADER_PATH_NAME"] = "blueprints"
    app.config["BLUEPRINTS_LOADER_MODULE_NAME"] = "routes"
    return app


@pytest.fixture()
def app(tmp_path, monkeypatch) -> Generator[Flask, Any, None]:
    # SetUp
    monkeypatch.syspath_prepend(tmp_path.as_posix())
    yield flask_app(tmp_path)  # noqa: PT022
    # TearDown


@pytest.fixture()
def loader(app: Flask) -> BlueprintsLoader:
    loader = BlueprintsLoader(app)
    loader.blueprints_path.mkdir(exist_ok=True)
    return loader


@pytest.fixture()
def blueprint_module_path(loader: BlueprintsLoader) -> Path:
    package_path = loader.blueprints_path / "blueprint_package"
    package_path.mkdir(exist_ok=True)
    module_path = package_path / f"{loader.module_name}.py"
    module_path.write_text("from flask import Blueprint\nmybp= Blueprint('mybp', __name__)")
    return module_path
