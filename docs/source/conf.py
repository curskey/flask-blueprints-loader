# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from pallets_sphinx_themes import ProjectLink, get_version

project = "Flask-Blueprints-Loader"
copyright = "2023, curskey"
author = "curskey"
release, version = get_version("flask_blueprints_loader")


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "pallets_sphinx_themes",
    "sphinx_issues",
]
autodoc_typehints = "description"
issues_github_path = "curskey/flask-blueprints-loader"

templates_path = ["_templates"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "flask": ("https://flask.palletsprojects.com/", None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "flask"
html_title = f"Flask-Blueprints-Loader Documentation ({version})"
html_static_path = ["_static"]
html_theme_options = {"index_sidebar_logo": False}
html_show_sourcelink = False
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html"],
}
html_context = {
    "project_links": [
        ProjectLink("PyPI Releases", "https://pypi.org/project/flask-blueprints-loader/"),
        ProjectLink("Source Code", "https://github.com/curskey/flask-blueprints-loader/"),
        ProjectLink("Issue Tracker", "https://github.com/curskey/flask-blueprints-loader/issues/"),
    ]
}
