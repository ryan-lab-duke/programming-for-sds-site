#!/usr/bin/env python
# coding: utf-8

# # Functions
# 
# When we write code, we want it to be as concise as possible while retaining readability. Sometimes we find ourselves writing out the same block over and over again. If we are doing this, it may be time to define a **function**, a self-contained program that can perform a specific task repeatedly in your code. 

# ## Anatomy of a function
# 
# Examples can be very useful for communicating new concepts so let's get straight into it and define our first function:

# In[7]:


def fahr_to_celsius(temp_fahrenheit):
    
    temp_celsius = (temp_fahrenheit - 32) * (5/9)
    
    return temp_celsius


# So what is going on here?
# 
# * The function definition opens with the keyword `def` followed by the **name** of the function and a list of **parameters** in parentheses. 
# 
# 
# * The **body** of the function — the code that is executed when it runs — is **indented** below the definition line.
# 
# 
# * At the end of the function, we use a `return` statement to define the value that should be output when the function is called.
# 
# 
# * Defining a function does nothing other than make it available for use in our notebooks. 
# 
# 
# * In order to use the function we need to call it using the **name** of the function with the provided value(s) inside **parentheses**. 

# In[12]:


fahr_to_celsius(90)


# We can also assign the output of the function to a new variable:

# In[13]:


celsius = fahr_to_celsius(90)
celsius


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# This is an insight into how larger programs are built. We first define some basic operations, then we combine them in ever-larger chunks to produce the effect we want.
