#!/usr/bin/env python
# coding: utf-8

# # Variables, data types, and structures
# 
# Welcome to the **first demo** of the course! In these demos, the instructor will work through some key programming concepts and demonstrate with plenty of examples. Understanding these concepts will be required to complete the weekly assignments. 

# ## It's a calculator
# 
# A Python interpreter can be used as a calculator.

# In[2]:


3 + 3


# In[3]:


3 * 3


# In[32]:


3 / 3


# ## Variables
# 
# This is great but to do something more useful with data, we need to assign its value to a **variable**. Variables are one of the fundamental building blocks of Python. A variable is like a tiny container where you store values and data, such as filenames, words, numbers, collections of words and numbers. In Python, we can assign a variable using the equals sign `=`. For example, we can track the height of a tree by assigning an integer value of `30` to a variable `height_m`.

# In[1]:


height_m = 30


# We can also make a **string** variable by adding single (`'`) or double quotes (`"`) around some text. 

# In[2]:


tree = 'douglas_fir'


# ```{note}
# Python is "dynamically typed" meaning that it automatically interprets the correct data type at run-time
# ```

# ### Variable usage

# Once we have data stored with variable names, we can make use of it in calculations. We may want to store our tree height value in feet as well as meters

# In[3]:


height_ft = height_m * 3.281


# Likewise, we might want to add a suffix to our tree so we can identify it later.

# In[4]:


tree1 = tree + '_1'


# ### Variable names
# 
# It is good practice to make variable names as descriptive as possible. They can include:
# 
# ✅ upper and lower-case letters (`a-z`, `A-Z`)
# 
# ✅ digits (`0-9`)
# 
# ✅ underscores (`_`)
# 
# However, variable names **cannot** include:
# 
# ❌ other punctuation (`-.!?@`)
# 
# ❌ spaces (` `)
# 
# ❌ a reserved Python word (e.g. `print`, `type`)
# 

# ## Built-in functions

# Python has a number of built-in functions to carry out common tasks with data and variables. For example, we can use the `print` function to **display information** to the screen.

# In[5]:


print(height_ft)


# In[6]:


print(tree1)


# ````{margin}
# ```{note}
# Note the use of parentheses `()` to let the function know which value we want to display.
# ```
# ````

# Python also has a built-in function called `type` which outputs a value's **data type**

# In[7]:


type(height_ft)


# In[8]:


type(tree1)


# The three most common data types that we will come across in Spatial Data Science are integer numbers (`int`), floating-point numbers (`float`) and strings (`str`). We may also encounter boolean data types (`bool`) which may have one of two values, `True` or `False`.
# 
# | Data Type     | Explanation          | Example  |
# | ------------- |:-------------:| -----:|
# | String        | Text | ```"july"``` |
# | Integer       | Whole numbers      |   ```42``` |
# | Float         | Decimal numbers      |   ```84.2``` |
# | Boolean       | True/False     |   ```False``` |
# 
# We can use another built-in function to change the data type of our variable (e.g. to `int`).

# In[9]:


int(height_ft)


# In[10]:


evergreen = True
type(evergreen)


# In[11]:


int(evergreen)


# A full list of built-in functions and their usage can be found [here](https://docs.python.org/3/library/functions.html).

# ## Lists
# 
# Sometimes we might want to store a **collection of items** in a single variable. The simplest type of collection in Python is a `list` which can be defined using square brackets `[` and commas `,`.

# In[2]:


places = ['Eugene', 'Veneta', 'Noti', 'Mapleton', 'Florence']


# In[3]:


type(places)


# ### Indexing
# 
# We can access individual items in a list using an **index** value. An index value is a **number** that refers to a position in the list. We can access the **second** value of the list by running:

# In[7]:


places[1]


# ````{margin}
# ```{note}
# Python uses **zero-based indexing** meaning that the first item of a list is accessed using the index value **0**.
# ```
# ````

# We can find the number of items in a list using the `len()` function. 

# In[8]:


len(places)


# If we know the number of items in the list, we can access the last item by running:

# In[9]:


places[4]


# But if the number of items in the list changes, we would have to update our code. A more robust way of finding the last item of the list is to run:

# In[10]:


places[len(places) - 1]


# We can also refer to the last item using **negative numbers** which index the list in **reverse**. The shortest, most Pythonic way to find the last element is a list is therefore to use `-1`.

# In[11]:


places[-1]


# ### Slicing
# 
# Slicing is similar to indexing except that we are looking to return a subset of items based their indices. We use a colon `:` to slice lists. For example, we can return the second and third items from out list.

# In[12]:


places[1:3]


# ````{margin}
# ```{note}
# The first number represents index item to include and second number is the index item to stop at *without including it in the slice*.
# ```
# ````

# Leaving either side of the colon blank means start from (or go to) the end of the list. For example:

# In[13]:


places[3:]


# In[14]:


places[:3]


# ### Stepping
# 
# We can use double colons `::` to set the interval at which items are included in the slice. So we can get every **second** item in the list (starting from index `0` by running:

# In[15]:


places[::2]


# If we wanted to start at index `1`, we could run:

# In[16]:


places[1::2]


# ## List methods
# 
# Methods are similar to the built-in functions we used earlier but are called on the object itself. A complete list of list methods can be found [here](https://www.w3schools.com/python/python_ref_list.asp). Here are some examples.
# 
# We can add items to a list using the `.append` method.

# In[17]:


places.append("Coos Bay")


# ````{margin}
# ```{note}
# Adding items to lists is a very common task in programming (e.g. in `for loops`) so we will see this `.append` method again and again during this course.
# ```
# ````

# In[18]:


print(places)


# ### Other useful list methods
# 
# We can use methods to count the number of occurences of an item:

# In[19]:


places.count('Eugene')


# Find the index value of a given item in a list:

# In[49]:


places.index('Eugene')


# Reverse list

# In[50]:


places.reverse()
print(places)


# Sort a list alphabetically

# In[51]:


places.sort()
print(places)


# Remove an item from the list

# In[52]:


places.remove('Coos Bay')
print(places)


# ```{note}
# Some methods return numbers so we can use the `=` sign to assign the output as a variable (e.g. `number = places.count('Eugene')`). Other methods update the variable automatically so we don't need an `=` sign.
# ```

# ## Acknowledgments
# 
# This lesson was inspired by [Programming in Python lessons](https://swcarpentry.github.io/python-novice-inflammation/01-intro/index.html) by [Software Carpentary](https://software-carpentry.org/) and the [Geo-Python](https://geo-python-site.readthedocs.io/en/latest/notebooks/L1/a-taste-of-python.html) course taught at the University of Helsinki. 

# In[ ]:




