import importlib.util
from pathlib import Path
from types import ModuleType

from flask import Blueprint, Flask, current_app


class BlueprintsLoader:
    """Automatically discover and register Flask blueprints.

    The `BlueprintsLoader` class provides functionality for dynamically
    loading and registering Flask blueprints.
    """

    def __init__(self, app: Flask | None = None) -> None:
        """Initializes the BlueprintsLoader instance."""
        if app:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initializes the Flask application with the BlueprintsLoader instance."""
        app.extensions["blueprints_loader"] = self
        self.path_name: str = app.config.setdefault("BLUEPRINTS_LOADER_PATH_NAME", "")
        self.module_name: str = app.config.setdefault("BLUEPRINTS_LOADER_MODULE_NAME", "views")
        self.unloads: str = app.config.setdefault("BLUEPRINTS_LOADER_UNLOADS", [])
        self.blueprints_path = Path(app.root_path) / self.path_name

        if not self.blueprints_path.exists():
            app.logger.error(f"Blueprints path {self.blueprints_path} does not exist.")

    @staticmethod
    def load_module(path: Path) -> ModuleType | None:
        """Loads a Python module from the specified path."""
        try:
            name = f"{path.parent}.{path.stem}"
            if spec := importlib.util.spec_from_file_location(name, path.as_posix()):
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return module
        except ImportError as error:
            current_app.logger.error(f"Error importing module: {name}", exc_info=error)

    def load_blueprint(self, path: Path) -> Blueprint | None:
        """Loads a Flask blueprint from the specified path."""
        module = self.load_module(path)
        return next(
            (
                attr_value
                for attr_name, attr_value in module.__dict__.items()
                if isinstance(attr_value, Blueprint) and attr_name not in self.unloads
            ),
            None,
        )

    def load_blueprints(self) -> None:
        """Loads and registers Flask blueprints."""
        for blueprint_path in self.blueprints_path.glob(f"*/{self.module_name}.py"):
            if blueprint := self.load_blueprint(blueprint_path):
                current_app.register_blueprint(blueprint)
