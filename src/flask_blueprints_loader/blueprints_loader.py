import importlib.util
from pathlib import Path
from types import ModuleType

from flask import Blueprint, Flask, current_app


class BlueprintsLoader:
    """Automatically discover and register Flask blueprints.

    The `BlueprintsLoader` class provides functionality for dynamically loading and registering Flask blueprints.

    Args:
        app: The Flask application instance. (optional)

    Attributes:
        path_name: The name of the directory containing the blueprints.
        module_name: The name of the module containing the blueprints.
        unloads: A list of blueprint names to exclude from loading.
        blueprints_path: The full path to the directory containing the blueprints.
    """

    def __init__(self, app: Flask | None = None) -> None:
        """Initializes the BlueprintsLoader instance.

        Args:
            app (Flask | None, optional): The Flask application instance. Defaults to None.

        Returns:
            None:
        """
        if app:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initializes the Flask application with the BlueprintsLoader instance.

        Args:
            app (Flask): The Flask application instance.

        Returns:
            None:
        """
        app.extensions["blueprints_loader"] = self
        self.path_name: str = app.config.setdefault("BLUEPRINTS_LOADER_PATH_NAME", "")
        self.module_name: str = app.config.setdefault("BLUEPRINTS_LOADER_MODULE_NAME", "views")
        self.unloads: str = app.config.setdefault("BLUEPRINTS_LOADER_UNLOADS", [])
        self.blueprints_path = Path(app.root_path) / self.path_name

        if not self.blueprints_path.exists():
            app.logger.error(f"Blueprints path {self.blueprints_path} does not exist.")

    @staticmethod
    def load_module(path: Path) -> ModuleType | None:
        """Loads a Python module from the specified path.

        The `load_module` static method is used to load a Python module from the given path.
        It takes a `path` parameter of type `Path` representing the path to the module file.
        The method attempts to import the module using `importlib.util.spec_from_file_location` and `importlib.util.module_from_spec`.
        If the module is successfully imported, it is executed using `spec.loader.exec_module` and returned.

        Args:
            path (Path): The path to the module file.

        Returns:
            ModuleType | None: The loaded module if successful, or None if an error occurs during import.
        """
        try:
            name = f"{path.parent}.{path.stem}"
            if spec := importlib.util.spec_from_file_location(name, path.as_posix()):
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return module
        except ImportError as error:
            current_app.logger.error(f"Error importing module: {name}", exc_info=error)

    def load_blueprint(self, path: Path) -> Blueprint | None:
        """Loads a Flask blueprint from the specified path.

        The `load_blueprint` method is used to load a Flask blueprint from the given path.
        It iterates over the attributes of the views module and returns the first attribute that is an instance of `Blueprint` and is not in the `unloads` list.

        Args:
            path (Path): The path to the blueprint module file.

        Returns:
            Blueprint | None: The loaded blueprint if found, or None if no suitable blueprint is found.
        """
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
        """Loads and registers Flask blueprints.

        The `load_blueprints` method is used to load and register Flask blueprints.
        It iterates over the blueprint paths in the `blueprints_path` directory that match the specified module name.
        If a blueprint is successfully loaded, it is registered with the current Flask application using `current_app.register_blueprint`.

        Returns:
            None:
        """
        for blueprint_path in self.blueprints_path.glob(f"*/{self.module_name}.py"):
            if blueprint := self.load_blueprint(blueprint_path):
                current_app.register_blueprint(blueprint)
