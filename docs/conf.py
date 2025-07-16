# Configuration file for the Sphinx documentation builder.

project = 'microbest'
author = 'James Pol'
release = '1.0'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'

# Add both _static and _images to static path
html_static_path = ['_static', '_images']

# Custom CSS
html_css_files = ['custom.css']

# Optional: if you have a logo
html_logo = '_images/Enter_Product_Key.png'

# Set master doc
master_doc = 'index'
