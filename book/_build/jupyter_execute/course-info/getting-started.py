#!/usr/bin/env python
# coding: utf-8

# # Completing assignments

# In this course we will use [**JupyterLab**](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) to complete assignments. JupyterLab is a **free**, interactive development environment (IDE) which runs in your web browser.

# ```{admonition} Launch JupyterLab
# We can launch JupyterLab by clicking this button: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/owel-lab/programming-for-sds-site/HEAD)
# ```

# It takes a minute to spin-up but eventually we will see a new JupyterLab environment.
# 
# The JupyterLab interface consists of different components such as a file browser, terminal, console, text editor, etc. The main JupyterLab component we will use during this course is **Jupyter Notebook** (with `.ipynb` extension) which can contain computer code and rich text elements (headings, lists, figures, links, etc.). Jupyter Notebooks are great for sharing code between instructor and students, executing code, and completing assignments.

# ## Start assignment
# 
# ```{admonition} Open a new notebook
# By clicking the **Python 3 (ipykernel)** panel under **notebook**.
# ```
# 
# ```{image} images/jupyterlab.png
# :alt: jupyterlab
# :class: bg-primary mb-1
# :width: 1000px
# :align: center
# ```

# ## Check everything is working
# 
# Copy and paste the code below into the first cell of your Jupyter Notebook.

# In[2]:


import numpy as np
c = np.add(2,3)
c


# Run the cells by pressing <kbd>Shift</kbd> + <kbd>Enter</kbd>. If everything is working correctly, this code block should return the number `5`.

# ```{note}
# If you are using cloud-based computing environments (i.e. Binder) to complete weekly assignments, they can be accessed from anywhere with any computer as long as you have a good internet connection. 
# ```

# ## Save assignment
# 
# Save the notebook by clicking **File** --> **Save Notebook As...** and naming the file something like `assignment-x.ipynb`, where `x` stands for the assignment number.

# ```{warning}
# Regularly download a copy of your work! The cloud computing environments are temporary and Python3 kernel will automatically shut down after 10 minutes of inactivity (if you leave a jupyterlab window open in the foreground, this will generally be counted as "activity").
# ```
# 
# ```{admonition} Tip
# If you have a short period of inactivity, the kernel can be restarted by clicking **No Kernel** in the top right and selecting **Python 3 (ipykernel)**.
# ```
# 

# ## Submit assignment
# 
# When you are finished with the assignment, you can download the notebook by clicking **File** --> **Download**. This `.ipynb` file should be moved to your local course folder and submitted via Canvas.

# ## JupyterLab
# 
# These instructions are just the absolute basics. For more information about JupyterLab, we suggest referring to their docs. The following pages are particularly relevant:
# 
# * [The JupyterLab Interface](https://jupyterlab.readthedocs.io/en/stable/user/interface.html)
# * [Working with Files](https://jupyterlab.readthedocs.io/en/stable/user/files.html)
# * [The Text Editor](https://jupyterlab.readthedocs.io/en/stable/user/file_editor.html)
# * [Notebooks](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html)
# * [Terminals](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html)
# * [Managing Kernels and Terminals](https://jupyterlab.readthedocs.io/en/stable/user/running.html)

# In[ ]:




