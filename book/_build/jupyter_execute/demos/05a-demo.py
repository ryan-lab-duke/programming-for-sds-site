#!/usr/bin/env python
# coding: utf-8

# # Functions
# 
# When we write code, we want it to be as concise as possible while retaining readability. Sometimes we find ourselves writing out the same block over and over again. If we are doing this, it may be time to define a **function**, a self-contained program that can perform a specific task repeatedly in your code. 

# ## Anatomy of a function
# <br>
# <br>
# 
# ```{image} images/python-function.png
# :alt: function example
# :class: mb-1
# :width: 400px
# :align: center
# ```
# <br>
# <br>

# Let's define our first function

# In[7]:


def fahr_to_celsius(temp_fahrenheit):
    
    temp_celsius = (temp_fahrenheit - 32) * (5/9)
    
    return temp_celsius


# The function definition opens with the keyword `def` followed by the **name** of the function and a list of **parameters** in parentheses. The **body** of the function — the code that is executed when it runs — is **indented** below the definition line.
# 
# When we call the function, the values we pass to it are assigned to the corresponding parameter variables so that we can use them inside the function. At the end of the function, we use a `return` statement to define the value that should be returned when the function is called.
# 
# Defining a function does nothing other than make it available for use in our notebooks. In order to use the function we need to call it.

# In[10]:


fahr_to_celsius(63)


# In[ ]:




