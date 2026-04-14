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

import datetime

project = "AI4FM | AI for Formal Methods"
copyright = f"{datetime.date.today().year}, AI4FM Research Group"  # noqa: A001
author = "AI4FM Research Group"
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
    "sphinxext.opengraph",
    "sphinx_sitemap",
]

templates_path = ["_templates"]
exclude_patterns = ["drafts/*", "archive/*"]

# Ablog configuration options
blog_authors = {
    "AI4FM": ("AI4FM Research Group", "https://github.com/LoyolaChicagoCS/ai4fm"),
    "GKT": ("George K. Thiruvathukal", "https://gkt.sh/"),
    "KL": ("Konstantin Läufer", "https://laufer.cs.luc.edu/"),
    "MA": ("Mohammed Abuhamad", "https://abuhamad.cs.luc.edu/"),
    "TNW": ("TaiNing Wang", "https://taining.github.io/"),
    "AB": ("Arslan Bisharat", "https://marslan.cs.luc.edu/"),
}
blog_default_author = "AI4FM"
blog_languages = {
    "en": ("English", None),
}
blog_default_language = "en"
post_show_prev_next = False
blog_title = "AI4FM Research Updates"
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
    "logo": {
        "image_light": "_static/images/logo-text.jpeg",
        "image_dark": "_static/images/logo-text.jpeg",
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/LoyolaChicagoCS/ai4fm",
            "icon": "fa-brands fa-github",
        },
    ],
}
html_title = project

# Sitemap settings
sitemap_url_scheme = "{link}"

# OpenGraph / social preview tags
ogp_site_url = "https://ai4fm.cs.luc.edu/"
ogp_image = "https://ai4fm.cs.luc.edu/_static/images/favicon.png"
ogp_description_length = 200
ogp_type = "website"
ogp_custom_meta_tags = [
    '<meta name="description" content="AI4FM — AI for Formal Methods research group at Loyola University Chicago. Advancing TLA+, formal verification, and LLM evaluation for rigorous system design.">',
    '<meta name="keywords" content="formal methods, TLA+, LLMs, model checking, Loyola University Chicago, AI, verification">',
    '<meta name="twitter:card" content="summary">',
    '<meta name="google-site-verification" content="04K9THhTvTqHTgt9pjOMw5pqkSi5_83nQCXMMrDnFsc" />',
]
