#!/usr/bin/env python
# coding: utf-8

# # Practice activity
# 
# ## Checkerboards and spatial autocorrelation
# 
# ```{image} images/checkerboard.png
# :alt: checkerboard
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```
# 
# Examples of spatial autocorrelation over a 5×5 regular grid.

# In[1]:


# Import modules
import numpy as np

# Define grids
grid_a = np.array([[1, 1, 1, 0, 0],
                   [1, 1, 1, 0, 0],
                   [1, 1, 1, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]]).astype('int8')

grid_b = np.array([[1, 0, 1, 0, 1],
                   [0, 1, 0, 1, 0],
                   [1, 0, 1, 0, 1],
                   [0, 1, 0, 1, 0],
                   [1, 0, 1, 0, 1]]).astype('int8')

grid_c = np.array([[1, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 1, 0, 1],
                   [1, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1]]).astype('int8')


# *****************************
# 
# ## Task 1 (6 points)
# 
# Run the grid cells above to define the three grids. Answer the following questions as **f-strings**:
# 
# * a) How many rows and columnns are in `grid_a`?
# 
# * b) How many elements in `grid_a`?
# 
# * c) Which grid has the most numbers equal to 1?
# 
# * d) Print the data type of `grid_a`?
# 
# * e) Print the data type of the first element in `grid_a`? (i.e. [0,0]). What does `int8` mean?
# 
# * f) What is the largest number that can be stored as `int8`? Show your working.
# 
# *****************************
# 
# ```{image} images/neighborhoods.png
# :alt: neighborhoods
# :class: bg-primary mb-1
# :width: 700px
# :align: center
# ```
# 
# ## Task 2 (12 points)
# 
# * a) What is the mean of the rook neighborhoods for element `[1,1]` in `grid_a`, `grid_b` and `grid_c`? (not including element `[1,1]`)
# 
# * b) Repeat **(a)** but for bishop neighborhoods.
# 
# * c) Repeat **(a)** but for queen neighborhoods.
# 
# Based on your answers to (a), (b), and (c):
# 
# * d) In which grid does the value of element `[1,1]` exhbit **positive** spatial autocorrelation?
# 
# * e) In which grid does the value of element `[1,1]` exhbit **negative** spatial autocorrelation?
# 
# *****************************
# 
# ## Task 3 (2 points)
# 
# * Add a title, your name, and date of this submission to your Jupyter Notebook using **Markdown text**.
# 
# * Add some more **Markdown text** to separate each task of this assignment and use **f-strings** to make yours answers clear.
# 
# ```{important} 
# Save your notebook to your local course folder and submit assignment (in **.pdf** format) to Canvas by the deadline.
# ```
