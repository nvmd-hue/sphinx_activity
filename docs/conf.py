# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
from pathlib import Path
import sys

# 1. Target the directory containing this conf.py file (docs/source)
current_dir = Path(__file__).resolve().parent

# 2. Walk backwards to the root directory workspace (source -> docs -> sphinx_activity)
# .parents[1] cleanly targets the folder two levels up
project_root = current_dir.parents[1]

# 3. Inject the absolute location of your source package into the Python path
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../src'))
project = 'Sphinx_Documentation'
copyright = '2026, Brad Nederpelt'
author = 'Brad Nederpelt'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = 'sphinx_rtd_theme'

