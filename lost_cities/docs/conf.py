import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'lost-cities'
copyright = '2023, Bela Homor'
author = 'Bela Homor'
release = '1.0.0'
extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc"]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'alabaster'
html_static_path = ['_static']
