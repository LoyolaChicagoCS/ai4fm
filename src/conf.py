"""
Sphinx configuration file.

Copyright (C) 2025 George K. Thiruvathukal.
"""

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "LUC-FMitF | Formal Methods in the Field"
copyright = "2025, LUC-FMitF Research Group"  # noqa: A001
author = "LUC-FMitF Research Group"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ablog",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinxcontrib.youtube",
]

templates_path = ["_templates"]
exclude_patterns = ["drafts/*", "archive/*"]

# Ablog configuration options
blog_authors = {
    "FMitF": ("LUC-FMitF Research Group", "https://github.com/LUC-FMitF"),
    "GKT": ("George K. Thiruvathukal", "https://gkt.sh/"),
    "KL": ("Konstantin Läufer", "https://laufer.cs.luc.edu/"),
    "MA": ("Mohammed Abuhamad", "https://abuhamad.cs.luc.edu/"),
    "TNW": ("TaiNing Wang", "https://taining.github.io/"),
}
blog_default_author = "FMitF"
blog_languages = {
    "en": ("English", None),
}
blog_default_language = "en"
post_show_prev_next = False
blog_title = "LUC-FMitF Research Updates"
blog_feed_fulltext = True

# Sphinx auto section label settings
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_extra_path = ["CNAME"]
html_css_files = ["custom.css"]
html_baseurl = "https://ai4fm.cs.luc.edu/"

# Sphinx Book Theme Settings
html_theme_options = {
    "show_navbar_depth": 0,
    "max_navbar_depth": 2,
    "collapse_navbar": True,
    "use_sidenotes": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/LUC-FMitF",
            "icon": "fa-brands fa-github",
        },
    ],
}
html_title = project
