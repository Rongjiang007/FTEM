import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'PyQuake3D'
copyright = '2025, Luca Dal Zilio'
author = 'Luca Dal Zilio'
release = '1.0.0'

extensions = [
    "sphinx.ext.autodoc",     # pull in docstrings from your code
    "sphinx.ext.napoleon",    # support Google/NumPy style docstrings
    "sphinx.ext.mathjax",     # render LaTeX-style math
    "sphinxcontrib.bibtex",   # bibliography support
]

templates_path = ['_templates']
exclude_patterns = []

# Number equations and show (1), (2), … on the right
math_number_all = True
math_eqref_format = "({number})"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinxcontrib.bibtex",
]

# Sphinx-side numbering (original behavior you had)
math_number_all = True
math_eqref_format = "({number})"


html_theme = "sphinx_rtd_theme"
html_logo = "_static/logo.png"
html_static_path = ['_static']
html_css_files = ['custom.css']

# BibTeX file
bibtex_bibfiles = ["refs.bib"]
#exclude_patterns = ['references.rst']