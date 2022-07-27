# Configuration file for the Sphinx documentation builder.

#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information

project = 'FAIR Island Generic Data Policy'
author = 'FAIR Island Project'

release = '1.0.0'
version = '1.0.0'

# -- General configuration

# extensions = ["sphinx_comments", "myst_parser"]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_logo = "_static/DataCite-Logo_secondary-white.png"

html_theme_options = {
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': True
}

# -- Options for EPUB output
epub_show_urls = 'footnote'


# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

