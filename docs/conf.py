"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
# -- Project information -----------------------------------------------------

project = "WETO Software Stack"
author = "Rafael Mudafort, National Renewable Energy Laboratory"
copyright = "2024 Alliance for Sustainable Energy, LLC"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinxcontrib.mermaid",
    "sphinxcontrib.youtube",
    "sphinx_simplepdf",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# -- MyST options ------------------------------------------------------------

# This allows us to use ::: to denote directives, useful for admonitions
myst_enable_extensions = ["colon_fence", "linkify"]

# -- Internationalization ----------------------------------------------------

# specifying the natural language populates some key tags
language = "en"

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_logo = "_static/images/logo.svg"
html_favicon = "_static/images/logo.svg"
html_sourcelink_suffix = ""
html_last_updated_fmt = ""  # to reveal the build date in the pages meta

html_theme_options = {
    "header_links_before_dropdown": 3,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/natlabrockies/wetostack",
            "icon": "fa-brands fa-github",
        },
    ],
    "logo": {
        "text": "WETO Stack",
    },
    "use_edit_page_button": True,
    "show_toc_level": 2,
    # [left, content, right] For testing that the navbar items align properly
    "navbar_align": "left",
    # "show_nav_level": 2,
    # "announcement": "https://raw.githubusercontent.com/pydata/pydata-sphinx-theme/main/docs/_templates/custom-template.html",
    # "show_version_warning_banner": True,
    "navbar_center": ["navbar-nav"], #["version-switcher", "navbar-nav"],
    # "navbar_start": ["navbar-logo"],
    # "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    # "primary_sidebar_end": ["custom-template", "sidebar-ethical-ads"],
    # "article_footer_items": ["test", "test"],
    # "content_footer_items": ["test", "test"],
    "footer_start": ["copyright"],
    # "footer_center": ["sphinx-version"],
    "secondary_sidebar_items": {
        "**/*": ["page-toc", "edit-this-page", "sourcelink"],
    },
    # "back_to_top_button": False,
    "search_as_you_type": True,
    "analytics": {
        "google_analytics_id": "G-XK6LTW8XM7",
    },
}

html_sidebars = {
    "index": [],  # full-width landing page, no left sidebar
}

html_context = {
    "default_mode": "light",
    "github_user": "natlabrockies",
    "github_repo": "wetostack",
    "github_version": "main",
    "doc_path": "docs",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["filtering.css"]
html_js_files = ["filtering.js"]
