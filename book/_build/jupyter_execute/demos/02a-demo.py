#!/usr/bin/env python
# coding: utf-8

# # NumPy arrays
# 
# While Python contains a few, general built-in tools, specialized tools are provided by libraries that have to be imported.
# 
# One of the most commonly used libraries is called `NumPy`, which stands for **Numerical Python**. In general, we should be using this library when we are working with numbers. 
# 
# We can access the functions provided by `NumPy` using the import statement and module name (e.g. `import numpy`). However, it is standard procedure to shorten the imported name to `np` for better code readability. This is a widely adopted convention that we should follow so that anyone working with our code can easily understand it.

# In[1]:


import numpy as np


# Special types of lists called `ndarrays`. We can define an array using the function `np.array` with some parentheses and square brackets. Let's define an array containing the populations of the twenty-two largest countries (to the nearest million).

# In[16]:


population = np.array([70000000,   67000000,  213000000,   90000000,  274000000, 
                       102000000,  221000000, 1380000000,   84000000,  329000000,
                       84000000,  110000000,  206000000,  165000000,  144000000, 
                       97000000,   67000000,  126000000,  115000000,   83000000, 
                       1411000000,  129000000])


# ## Shape and size
# 
# Once our data is in `ndarray` format, we can use `NumPy` functions to investigate our data.  We can find the total number of elements in the array by running:

# In[17]:


np.size(population)


# And we can find the shape (number of rows, columns) of the array by running:

# In[18]:


np.shape(population)


# ## Statistics
# 
# We can also use `NumPy` functions to find statistics of our data. For example:

# In[19]:


# Mean
np.mean(population)


# In[20]:


# Median
np.median(population)


# In[21]:


# Max
np.max(population)


# In[22]:


# Min
np.min(population)


# In[23]:


# Standard deviation
np.std(population)


# In[24]:


# Sum
np.sum(population)


# ## Mathematical operations
# 
# `NumPy` has functions for performing mathematical operations. First let's define some arrays containing the populations of the largest twenty-two countries in 1960 and 2020.

# In[31]:


# Populations of 22 largest countries in 1960
pop_1960 = np.array([667000000, 451000000, 181000000,  88000000,  45000000,  72000000,
                     45000000,  48000000, 120000000,  38000000,  93000000,  22000000, 
                     26000000,  27000000,  33000000,  15000000,  27000000,  22000000, 
                     73000000,  27000000,  47000000,  52000000])

# Populations of 22 largest countries in 2020
pop_2020 = np.array([1411000000, 1380000000, 329000000, 274000000, 221000000, 
                     213000000,  206000000,  165000000,  144000000, 129000000, 
                     126000000,  115000000,  110000000,  102000000, 97000000, 
                     90000000,   84000000,   84000000,   83000000,   70000000, 
                     67000000,   67000000])

# Population of world in 1960
world_1960 = 3032000000

# Population of world in 2020
world_2020 = 7762000000


# Let's say we wanted to find the population of each country as a percentage of the total population in 1960. 

# In[32]:


np.divide(pop_1960, world_1960) * 100


# ```{note}
# An operation between an array and a single number **or** between arrays of two different sizes is termed [**broadcasting**](https://numpy.org/doc/stable/user/basics.broadcasting.html).
# ```

# Now let's calculate the population change between 1960 and 2020.

# In[33]:


np.subtract(pop_2020, pop_1960)


# ```{note}
# Since the arrays are the **same size**, NumPy performs an **element-by-element** operation (i.e. the first number of array1 is subtracted from the first number of array1, the second number of array1 is subtracted from the second number of array2... etc.).
# ```

# What about the percentage change in population for each country?

# In[34]:


np.divide(np.subtract(pop_2020, pop_1960), pop_1960) * 100


# `NumPy` has many other matematical operations. See [here](https://numpy.org/doc/stable/reference/routines.math.html) for a full list.

# ## Searching
# 
# We can use `NumPy` to find specific elements of our array. We can find the index of the smallest value in our array using the `np.argmin` function.

# In[40]:


# Define a new variable that contains population growth as a percentage of population
pop_growth = np.divide(np.subtract(pop_2020, pop_1960), pop_1960) * 100

# Find index for smallest growth
np.argmin(pop_growth)


# In[41]:


# Find index for largest growth
np.argmax(pop_growth)


# This is useful since the populations in our array correspond to countries in the list below:

# In[37]:


country = ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh',
          'Russian Federation', 'Mexico', 'Japan', 'Ethopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 
           'Turkey', 'Iran','Germany', 'Thailand', 'France', 'United Kingdom']


# So we can use list indexing to find the country with the lowest growth rate between 1960 and 2020:

# In[38]:


country[np.argmin(pop_growth)]


# Or highest growth rate:

# In[39]:


country[np.argmax(pop_growth)]


# ## Multi-dimensional arrays
# 
# We will often use `NumPy` in Spatial Data Science to perform operations on multi-dimensional arrays  or matrices (i.e. arrays with 2, 3 or more dimensions). Let's say we have a small grid of points that represent elevation values (i.e. a digital elevation model or **DEM**). We could represent it as a 2D `ndarray` like so:

# In[66]:


dem = np.array([[10, 9, 4, 4], [11, 8, 5, 4], [12, 7, 6, 4]])
print(dem)


# This time our array has three rows and four columns (i.e. 3 x 4) and 12 elements.

# In[67]:


np.shape(dem)


# In[68]:


np.size(dem)


# So what happens when we perform mathematical operations (e.g. `np.mean`) on the array? The default option is to compute the mean of all elements in the array.

# In[69]:


np.mean(dem)


# But we can also **specify** which axis we would like to perform the operation on. If wanted to calculate the mean along each **column**, we would add `axis=0` as an argument. See the docs for [`np.mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html).

# In[74]:


np.mean(dem, axis=0)


# Alternatively, we could calculate the mean along each **row** by adding `axis=1` as an argument. 

# In[73]:


np.mean(dem, axis=1)


# Or perform a different operation...

# In[77]:


np.sum(dem, axis=1)


# The figure below shows which axis is which. 

# ```{image} images/np_axes.png
# :alt: cells
# :class: bg-primary mb-1
# :width: 500px
# :align: center
# ```

# ```{note}
# In a 3D array, the third (or depth) axis would be `axis=2`.
# ```

# ## Matrix operations
# 
# We can perform element-by-element operations or broadcasting on the array.

# In[78]:


np.add(dem, 1)


# In[79]:


np.multiply(dem, 2)


# ## Matrix indexing and slicing
# 
# We can index and slice NumPy arrays in the same way we slice Python lists - using square brackets. Remember that indexing in Python starts at **0**. 

# In[84]:


dem


# Since the array is **2D**, we need to use two numbers to access elements in the array. The order is `array[row, col]` So if we wanted the value in the second row and first column we would type:

# In[85]:


dem[1,0]


# We may also want to access the entire row or column. We can do this by using a colon sign which means "all". To return the second column, we would type:

# In[94]:


dem[:,1]


# Or the third row:

# In[95]:


dem[2,:]


# Recall that leaving either side of the colon blank means start from (or go to) the end of the list. So if we wanted the values in the third row, but only in the second and third columns we could type: 

# In[96]:


dem[2,1:]


# ## Comparison operators
# 
# If we wanted to return specific values, we can use comparison operators such as those in the table below:
# 
# | **Comparison operator** | **Explanation** |
# |:-------------:|:-------------------------:|
# | `x == y `     | `True` if x is equal to y |
# | `x != y `     | `True` if x is **not** equal to y |,
# | `x > y`       | `True` if x is greater than y |
# | `x < y`       | `True` if x is less than y | 
# | `x >= y`      | `True` if x is greater than or equal to y |
# | `x <= y`      | `True` if x is less than or equal to y    |

# In[111]:


mask = (dem > 8)
dem[mask]


# ```{note}
# Here we produced **boolean mask** which has the same shape as the original array but each value is either `True` or `False` (depending on whether the value was greater or less than 8). We then returned values of the original array where the mask was `True`.
# ```

# Likewise, we can also just get values equal to 10:

# In[112]:


mask = (dem == 10)
dem[mask]


# Or **not** 10:

# In[113]:


mask = (dem != 10)
dem[mask]


# ## Matrix searching 
# 
# Sometimes we want to find the location (or index) of specific values. To do this, we can combine our comparison operators with a useful function called `np.where`. 

# In[114]:


# Find indices of values greater than 9
np.where(dem > 9)


# This could be used find the number of values greater than 9 (similar to what we did with **masks** before).

# In[87]:


dem[np.where(dem > 9)].size


# We could also use this approach to derive values from other arrays so long as they have the same shape.

# In[98]:


array = np.array([[[178, 189, 567], [145, 239, 445], [197, 345, 678]], [[56, 78, 190], [46, 10, 11], [6, 2, 1]], [[45, 118, 203], [72, 119, 34], [87, 9, 5]]])


# In[100]:


np.mean(array, axis=2)


# ## Acknowledgments
# 
# This demo was inspired by [NumPy docs](https://numpy.org/doc/stable/user/absolute_beginners.html).
