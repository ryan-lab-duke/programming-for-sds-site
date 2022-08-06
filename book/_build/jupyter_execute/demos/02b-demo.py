#!/usr/bin/env python
# coding: utf-8

# # Tidy outputs
# 
# In Week 1, we added some headings and formatted our text as **Markdown** to produce notebook submissions that were stuctured and tidy. Sometimes it is also nice to format the **numerical output** returned by a Python cell in a readable way. For example, we may want to change the number of decimal places. In this demo, we demonstrate some useful approaches for formatting your numerical answers.

# There are three approaches that can be used to manipulate strings in Python:
# 
# * the "old-school" %-formatting
# 
# * the str.format() method
# 
# * f-strings
# 
# ```{note}
# The f-string approach is recommended and the most modern. However, we are likely to find examples of the all approaches so it is useful to show how they work.
# ```

# ## Option 1: “Old-school” string formatting
# 
# String objects have a built-in operation using the `%` operator, which you can use to format strings. Here is an example:

# In[39]:


trail = 'Scott'
distance = 5

print('The %s Trail is about %i miles' % (trail, distance))


# In[40]:


print('The %s Trail is about %.2f miles' % (trail, distance))


# Where `%s` stands for **string**, `%i` stands for **integer**, `.2f` stands for a **float with 2 decimal places**.

# ## Option 2: str.format()
# 
# This newer way of getting the job done was introduced in Python 2.6. Here is an example:

# In[41]:


print("The {} Trail is about {} miles".format(trail, distance))


# In[42]:


print("The {} Trail is about {:.2f} miles".format(trail, distance))


# ## Option 3: f-Strings
# 
# Also called "formatted string literals", f-strings are string literals that have an `f` at the beginning and curly braces containing expressions that will be replaced with their values. Here is an example:

# In[43]:


f"The {trail} Trail is about {distance} miles"


# In[44]:


f"The {trail} Trail is about {distance:.2f} miles"


# There are many more ways you can use f-strings. Some further reading can be found [here](https://realpython.com/python-f-strings/).

# In[ ]:




