#!/usr/bin/env python
# coding: utf-8

# # Making simple plots
# 
# In this week, we wil learn how make figures in Python. The most widely used Python library for making figures (or plots) is called `Matplotlib`. This library has extremely comprehensive functionality and can be used to customize plots any way we like. After this week, we will never have to make plots in Excel again!

# ## Parts of a figure
# 
# A figure is made up of several elements including axes, tick labels, axis labels, title etc.
# 
# ```{image} images/sphx_glr_anatomy_001.webp
# :alt: anatomy
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```

# ## Basic usage
# 
# To use `Matplotlib`, we first import it, usually **as** `plt` to improve code readability.

# In[1]:


import matplotlib.pyplot as plt


# ## Coding styles
# 
# Just like other libraries we have used, `Matplotlib` contains a collection of functions that allow us to make specific changes to a figure (e.g., create a figure, plots lines, add some labels, etc.). However, unlike other libraries, we can use `Matplotlib` in two different ways. 
# 
# The first way is called the **pyplot style** which relies on `Matplotlib` to automatically keep track of changes we apply to the figure. The pyplot style can be very convenient for quick interactive work. We can make a simple line graph using the [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html) method and add a **title** to it using the [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html) methods. Finally, it is good practice to add the [`show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html) method to display the figure.

# In[35]:


plt.plot([1, 2, 3, 4])
plt.title('Line graph using pyplot style')
plt.show()


# The second way is called the **object-oriented style** where we explicitly create the axes and call methods on them. We recommend the object-oriented style because 1) it is easier to produce more sophisticated, multi-panel plots, 2) it is easier to re-use the code, and 3) it is the style used in many of the examples on the `Matplotlib` documentation page.

# In[36]:


fig, ax = plt.subplots()
ax.plot([1,2,3,4])
ax.set_title('Line graph using object-oriented style')
plt.show()


# ````{margin}
# ```{note}
# Now that because we are operating on an `AxesSubplot` object we use **`set_title`**.
# ```
# ````

# ## Styling
# 
# Once we have our figure, we can customize the style using keyword arguments. Most plotting methods have styling options which are accessible when the plotting method (i.e. `plot`) is called.

# In[37]:


fig, ax = plt.subplots()
ax.plot([1,2,3,4], color='green', linewidth=3, linestyle='--')
ax.set_title('Line graph using object-oriented style')
plt.show()


# Another type of plotting method is called [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html) which produces a scatter plot of two datasets. This type of plot allows us to customize the size of the marker, as well as the facecolor and edgecolor of the marker.

# In[38]:


fig, ax = plt.subplots()
ax.scatter([1,2,3,4], [4,5,3,4], s=200, facecolor='lightblue', edgecolor='black')
ax.set_title('Scatter plot using object-oriented style')
plt.show()


# ## Axis labels
# 
# As well as a title, we can add **x- and y-axis labels** using the [`set_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html) and [`set_ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html) methods. Labels can also be customized using keyword arguments such as `fontsize`. 

# In[43]:


fig, ax = plt.subplots()
ax.scatter([1,2,3,4], [4,5,3,4], s=200, facecolor='lightblue', edgecolor='black')
ax.set_title('Scatter plot using object-oriented style', fontsize=14)
ax.set_xlabel('Some numbers', fontsize=14)
ax.set_ylabel('Some more numbers', fontsize=14)
plt.show()


# ## Tick labels and scales
# 
# 

# In[ ]:





# ## Legends
# 
# 

# In[ ]:





# ## Multiple panels
# 
# 

# In[ ]:





# ## Layout
# 
# 

# In[ ]:





# ## Acknowledgements
# 
# https://matplotlib.org/stable/tutorials/introductory/usage.html
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# 
