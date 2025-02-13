# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import subprocess

project = "pygments-minimessage"
copyright = "2025, KyoriPowered"
author = "KyoriPowered"
version = subprocess.run(["poetry", "dynamic-versioning", "show"], stdout=subprocess.PIPE).stdout.decode().strip()

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "sphinx.ext.autodoc",
  "myst_parser",
  "sphinx_design",
  "sphinx_github_changelog",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# General style

smartquotes = True
language = "en"

pygments_style = "friendly"
pygments_dark_style = "dracula"

myst_enable_extensions = [
  "colon_fence",
  "deflist",
  "fieldlist",
  "dollarmath",
  "html_admonition",
  "replacements",
  "smartquotes",
  "tasklist",
  "attrs_inline",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_baseurl = "https://pygments-minimessage.kyori.net/"
html_title = f"pygments-minimessage v{version}"
html_favicon = "_static/favicon.ico"

html_theme_options = {
  "light_css_variables": {
    "color-brand-primary": "#2f2850",
    "color-brand-content": "#6355aa",
  },
  "dark_css_variables": {
    "color-brand-primary": "#b597d3",
    "color-brand-content": "#7767c9",
  },
  # 'sidebar_hide_name': True
}
