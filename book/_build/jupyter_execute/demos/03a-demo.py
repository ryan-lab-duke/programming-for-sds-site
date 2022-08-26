#!/usr/bin/env python
# coding: utf-8

# # For loops
# 
# In progamming, we often want to repeat the same operation many times without having to re-type the same instructions. 
# 
# ```{image} images/west.jpg
# :alt: west
# :class: bg-primary mb-1
# :width: 300px
# :align: center
# ```
# 
# ## The problem
# 
# Let's say someone had provided us with a list of of states nearby but they didn't capitalize the first letter!

# In[4]:


states = ['washington', 'oregon', 'california', 'arizona', 'nevada', 'idaho', 'utah']


# We could use the string method `.capitalize()` to change the first letter of each item in the list to uppercase like so:

# In[6]:


state1 = states[0].capitalize()
state2 = states[1].capitalize()
state3 = states[2].capitalize()
state4 = states[3].capitalize()
state5 = states[4].capitalize()
state6 = states[5].capitalize()
state7 = states[6].capitalize()

states_capitalized = [state1, state2, state3, state4, state5, state6, state7]
states_capitalized


# But what if this list contained 100 or 1000 place names? It would take a long time (and be extremely boring) to type this all out. When you find yourself repetivitely typing the same thing but only changing one number of character... you know it's time to write a **for loop**! 

# ## Basic `for` loop format
# 
# For loops **iterate** over lists, repeating the same instructions for each element. We can write one like this:

# In[7]:


# Define empty list
states_capitalized = []

for state in states:
    
    # Capitalize place name
    new_name = state.capitalize()
    
    # Append to new list
    states_capitalized.append(new_name)

states_capitalized


# OK so what happened here? There are a couple of things going on so let's break down what we did. 
# 
# * We defined an **empty list** (to put our capitalized place names)
# 
# 
# * We initiated the loop using the standard `for item in list` syntax. This basically means "...for every item in the list". Note that this statement must end with a **colon** (`:`). 
# 
#  
# * The code that is executed as part of the loop must be **indented** beneath the for loop statement. The typical indentation is four <kbd>space</kbd> keys or one <kbd>Tab</kbd> key.
# 
# 
# * For every state, we:
#   1. Capitalized the the first letter of the state name.
#   
#   2. Added the capitalized state name to our empty list using the `.append` method.
#  

# Note that the variables `state` and `new_name` used in the for loop are just normal variables and still exist after the loop has completed. They are equal to the **last** item in the list. 

# In[9]:


state


# In[10]:


new_name


# ## Looping with an index
# 
# We can use a loop to iterate over any collection of values in Python. For example, we can also write a loop that performs a calculation for a sequence of integers using the built-in function called `range`. 

# In[11]:


range(5)


# ```{tip}
# `range` can accept one, two, or three parameters.
# 
# * If one parameter is given, `range` generates a sequence of that length, starting at zero and incrementing by 1. For example, `range(3)` produces the numbers `0, 1, 2`.
# 
# 
# * If two parameters are given, `range` starts at the first and ends just before the second, incrementing by one. For example, `range(2, 5)` produces `2, 3, 4`.
# 
# 
# * If `range` is given three parameters, it starts at the first one, ends just before the second one, and increments by the third one. For example, `range(3, 10, 2)` produces `3, 5, 7, 9`
# ```

# We can write the same for loop as before to capitalize the state names.

# In[13]:


# Define empty list
states_capitalized = []

for i in range(7):
    
    # Print iteration
    print(i)
    
    # Capitalize place name
    new_name = states[i].capitalize()
    
    # Append to new list
    states_capitalized.append(new_name)

states_capitalized   


# This time we looped over every integer between 0 and 4 (i.e. 0, 1, 2, 3, 4). We used this integer to **index** every item in our list and capitalize it. 

# ```{note}
# The variable `i` is commonly used to denote the **index** variable in loops. If we have multiple for loops in our script, we might consider using `j` or `k` etc.
# ```

# ## Looping through two lists
# 
# This might seem a strange, convoluted way of doing the same thing as before but it is quite useful. Let's say we had another list containing the total area of these states:

# In[16]:


area = [184661, 254799, 423967, 295234, 286380, 216630, 219890]


# We could use the index approach to print pairs in a single loop:

# In[17]:


for i in range(len(states_capitalized)):
    
    print(f"The total area of {states_capitalized[i]} is {area[i]} square kilometers")


# ```{note}
# In the example above, we used the **length** of the states list in the `range()` function but we could have just as easily used the length of the area list to define `i` since both lists are the same length.
# ```

# In[ ]:




