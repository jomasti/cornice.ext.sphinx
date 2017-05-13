#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import cornice

sys.path.insert(0, os.path.abspath(cornice.__file__))
extensions = ['cornice_sphinx']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Cornice Sphinx'
copyright = '2017, Pass'
author = 'Pass'

version = ''
release = ''

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

todo_include_todos = False

html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'CorniceSphinxdoc'

latex_documents = [
    (master_doc, 'CorniceSphinx.tex', 'Cornice Sphinx Documentation',
     'Pass', 'manual'),
]

man_pages = [
    (master_doc, 'cornicesphinx', 'Cornice Sphinx Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'CorniceSphinx', 'Cornice Sphinx Documentation',
     author, 'CorniceSphinx', 'One line description of project.',
     'Miscellaneous'),
]



