#!/usr/bin/env python
# coding: utf-8

# # Formatting notebooks
# 
# The second demo of this week provides an introduction to formatting assignment submissions. Jupyter Notebooks are powerful because we can add documentation in **Markdown**, a lightweight markup language for creating formatted text using a plain-text editor.

# ## Cells
# 
# There are two main types of cell in Jupyter Notebooks: Code and Markdown.
# 
# In **code** cells, the text is treated as statements in a programming language of current kernel (Python in our case).  When such cell is run, the result is displayed in an output cell. 
# 
# In **Markdown** cells, the text is formatted using markdown language. All kinds of formatting features are available like making text **bold** and *italic*, displaying ordered or unordered list, rendering tabular contents etc. Markdown cells are especially useful for providing documentation to a notebook.
# 
# We can choose the cell type by clicking on the drop-down list at the the top of the page.

# ```{image} images/cells.png
# :alt: cells
# :class: bg-primary mb-1
# :width: 1000px
# :align: center
# ```

# ## Markdown
# 
# ### Headings
# 
# We can add headings to our notebooks using the number sign (`#`) followed by a blank space:

# ````
# # for titles
# 
# ## for major headings
# 
# ### for subheadings
# 
# #### for 4th level subheadings
# ````

# ### Emphasis
# 
# We can format text as bold, italic, or monospace font using underscores, asterisks, and grave accents:

# ````
# Bold text: __string__ or **string**
# 
# Italic text: _string_ or *string*
# 
# Monospace text: `string`
# ````

# ### Lists
# 
# We can make bullet point lists using hyphens or asterisks followeed by a space. Each bullet point must be on its own line.

# ````
# - A hyphen (-)
# * An asterisk (*)
# ````

# ### Graphics
# 
# We can add graphics, figures, and images to our notebook using the following syntax: 

# ````
# ![Image title](filename.png)
# ````

# ````{margin}
# ```{note}
# Only works when `filename.png` is located in the **same folder** as your Jupyter Notebook.
# ```
# ````

# ### Tables
# 
# We can even make tables:

# ````
# | This | is    |
# |------|-------|
# | a    | table |
# ````
