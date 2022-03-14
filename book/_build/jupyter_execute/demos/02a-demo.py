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


# Special types of lists called `ndarrays`. We can define an array using the function `np.array` with some parentheses and square brackets. 

# In[18]:


# Define an array with containing populations of 22 largest countries
population = np.array([69799978,   67391582,  212559409,   89561404,  273523621,
                       102334403,  220892331, 1380004385,   83992953,  329484123,
                       84339067,  109581085,  206139587,  164689383,  144104080,
                       97338583,   67215293,  125836021,  114963583,   83240525,
                       1410929362,  128932753])


# ## Shape and size
# 
# Once our data is in `ndarray` format, we can use `NumPy` functions to investigate our data.  We can find the total number of elements in the array by running:

# In[34]:


np.size(population)


# And we can find the shape (number of rows, columns) of the array by running:

# In[35]:


np.shape(population)


# ## Statistics
# 
# We can also use `NumPy` functions to find statistics of our data. For example:

# In[37]:


# Mean
np.mean(population)


# In[39]:


# Median
np.median(population)


# In[38]:


# Max
np.max(population)


# In[42]:


# Min
np.min(population)


# In[43]:


# Standard deviation
np.std(population)


# In[46]:


# Sum
np.sum(population)


# ## Mathematical operations
# 
# `NumPy` has functions for performing mathematical operations. First let's define some arrays.

# In[48]:


# Populations of 22 largest countries in 1960
pop_1960 = np.array([667070000, 450547675, 180671000, 87751066, 44988690, 72179235, 45138460,
                     48013505, 119897000, 37771861, 93216000, 22151284, 26269741, 26632891,
                     32670048, 15248256, 27472339, 21906909, 72814900, 27397208, 46621688, 
                     52400000])

# Populations of 22 largest countries in 2020
pop_2020 = np.array([1410929362, 1380004385, 329484123, 273523621, 220892331, 212559409,
                     206139587, 164689383, 144104080, 128932753, 125836021, 114963583,
                     109581085, 102334403, 97338583, 89561404, 84339067, 83992953, 
                     83240525, 69799978, 67391582, 67215293])

# Population of world in 1960
world_1960 = 3032156070

# Population of world in 2020
world_2020 = 7761620146


# Let's say we wanted to find the population of each country as a percentage of the total population in 1960. 

# In[56]:


np.divide(pop_1960, world_1960) * 100


# ```{note}
# An operation between an array and a single number **or** between arrays of two different sizes is termed [**broadcasting**](https://numpy.org/doc/stable/user/basics.broadcasting.html).
# ```

# Now let's calculate the population change between 1960 and 2020.

# In[51]:


np.subtract(pop_2020, pop_1960)


# ```{note}
# Since the arrays are the **same size**, NumPy performs an **element-by-element** operation (i.e. the first number of array1 is subtracted from the first number of array1, the second number of array1 is subtracted from the second number of array2... etc.).
# ```

# What about the percentage change in population for each country?

# In[57]:


np.divide(np.subtract(pop_2020, pop_1960), pop_1960) * 100


# `NumPy` has many other matematical operations. See [here](https://numpy.org/doc/stable/reference/routines.math.html) for a full list.

# ## Searching
# 
# We can use `NumPy` to find specific elements of our array. We can find the index of the smallest value in our array using the `np.argmin` function.

# In[59]:


# Define a new variable that contains population growth as a percentage of population
pop_growth = np.divide(np.subtract(pop_2020, pop_1960), pop_1960) * 100

# Find index for smallest growth
np.argmin(pop_growth)


# In[64]:


# Find index for largest growth
np.argmax(pop_growth)


# This is useful since the populations in our array correspond to countries in the list below:

# In[62]:


country = ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh',
          'Russian Federation', 'Mexico', 'Japan', 'Ethopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 
           'Turkey', 'Iran','Germany', 'Thailand', 'France', 'United Kingdom']


# So we can use list indexing to find the country with the lowest growth rate between 1960 and 2020:

# In[67]:


country[np.argmin(pop_growth)]


# Or highest growth rate:

# In[68]:


country[np.argmax(pop_growth)]


# ## Multi-dimensional arrays
# 
# We will often use `NumPy` in Spatial Data Science to perform operations on multi-dimensional arrays  or matrices (i.e. arrays with 2, 3 or more dimensions). Let's say we have a small grid of points that represent elevation values (i.e. a digital elevation model). We could represent it as a 2D `ndarray` like so:

# In[82]:


dem = np.array([[10, 9, 4], [11, 8, 5], [12, 7, 6]])
print(dem)


# This time our array has three rows and three columns (i.e. 3 x 3) and 9 elements.

# In[83]:


np.shape(dem)


# In[124]:


np.size(dem)


# ## Matrix operations
# 
# We can perform element-by-element operations or broadcasting on the array.

# In[84]:


np.add(dem, dem)


# In[85]:


np.multiply(dem, 2)


# ## Matrix indexing and slicing
# 
# We can index and slice NumPy arrays in the same way we slice Python lists - using square brackets. Remember that indexing in Python starts at **0**. 
# 
# Since the array is **2D**, we need to use two numbers to access elements in the arry. The order is `array[row, col]` So if we wanted the value in the second row and first column we would type:

# In[93]:


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
# If we wanted to return specific values, we can use comparison operators (i.e. `==`, `>`, `<`). 

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


# This could be used find all values greater than 9 (similar to what we did with **masks** before).

# In[115]:


dem[np.where(dem > 9)]


# We could also use this approach to derive values from other arrays so long as they have the same shape.

# This demo was inspired by [NumPy docs](https://numpy.org/doc/stable/user/absolute_beginners.html).
