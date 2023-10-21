from pathlib import Path
from types import ModuleType

from flask import Blueprint


def test_init_app(app, loader):
    assert loader.path_name == "blueprints"
    assert loader.module_name == "routes"
    assert loader.blueprints_path == Path(app.root_path) / "blueprints"


def test_load_module(loader, blueprint_module_path):
    module = loader.load_module(blueprint_module_path)
    assert isinstance(module, ModuleType)


def test_load_blueprint(loader, blueprint_module_path):
    attr_value = loader.load_blueprint(blueprint_module_path)
    assert isinstance(attr_value, Blueprint)


def test_load_blueprints(loader, app, blueprint_module_path):
    with app.app_context():
        loader.load_blueprints()
    assert any(app.blueprints)
