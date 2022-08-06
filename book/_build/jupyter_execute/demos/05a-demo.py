#!/usr/bin/env python
# coding: utf-8

# # Functions
# 
# When we write code, we want it to be as concise as possible while retaining readability. Sometimes we find ourselves copying and pasting the same block of code over and over again. Instead of repeating this block of code, we can bundle it up into a **function**. We've encountered some **built-in** functions already:
# 
# - `print()`
# - `len()`
# - `type()`
# 
# But we can also define our own functions.

# ## Anatomy of a function
# 
# Examples can be very useful for communicating new concepts so let's get straight to it and define our first function:

# In[2]:


def fahr_to_celsius(temp_fahrenheit):
    
    temp_celsius = (temp_fahrenheit - 32) * (5/9)
    
    return temp_celsius


# So what is going on here?
# 
# * The function definition opens with the keyword `def` (short for **define**) followed by the **name** of the function, a list of **parameters** in parentheses (`()`) and a colon (`:`). 
# 
# 
# * The **body** of the function — the code that is executed when it runs — is **indented** below the definition line.
# 
# 
# * At the end of the function, we use a `return` statement to define the value that should be output when the function is called.
# 
# 
# Defining a function does nothing other than make it available for use in our notebooks. In order to use the function we need to **call** it using the **name** of the function with the provided value(s) inside **parentheses**. As you can probaly tell, this function converts temperatures from Fahrenheit to Celsius. 

# In[3]:


fahr_to_celsius(90)


# We can also write a function to convert from Celsius to Kelvin:

# In[5]:


def celsius_to_kelvin(temp_celsius):
    return temp_celsius + 273.15

print("The freezing point of water is {} K".format(celsius_to_kelvin(0)))


# ## Functions within a function
# 
# Now say we wanted to convert from Fahrenheit to Kelvin, we could just include a function within a function.

# In[11]:


def fahr_to_kelvin(temp_fahr):
    temp_celsius = fahr_to_celsius(temp_fahr)
    temp_kelvin = celsius_to_kelvin(temp_celsius)
    return temp_kelvin

print("The boiling point of water is {} K".format(fahr_to_kelvin(212)))


# ## Variable scope
# 
# When we composed our temperature conversion functions, we created variables inside of those functions called `temp_celsius` and `temp_kelvin`. We refer to these variables as **local variables** because they no longer exist once the function has executed. If we try to access their values outside of the function, we will encounter an error:

# In[12]:


temp_celsius


# If we wanted to reuse the temperature in Kelvin after we converted it using `fahr_to_kelvin`, we can store the result of the function as a variable. 

# In[21]:


celsius = fahr_to_kelvin(60)
celsius


# Since the variable is defined outside the function, it is called a **global variable**. Understanding the difference between local and global variables is crucial since many bugs and issues are caused by misunderstanding of the two. So to recap:
# 
# * A **global variable** is visible everywhere in a notebook.
# 
# * A **local variable** is visible only within a function.
# 
# Generally, we want to avoid using too many global variables when we are programming because they can make debugging more difficult. 

# ## Functions with multiple parameters
# 
# It is also possible to define a function with multiple parameters. Here we will define a simple temperature calculator function that accepts temperatures in Fahrenheit and returns the temperature in either Celsius or Kelvin. The function will have two input parameters:
# 
# * `temp_fahr` = the temperature in Fahrenheit
# 
# * `convert_to` = the output units in Celsius or Kelvin (using the string `C` or `K` accordingly)

# In[25]:


def temp_calculator(temp_fahr, convert_to):
    
    if convert_to == "C":
        
        converted_temp = fahr_to_celsius(temp_fahr)
        
    elif convert_to == "K":
        
        converted_temp = fahr_to_kelvin(temp_fahr)
        
    return converted_temp


# ````{margin}
# ```{note}
# Note the conditional statements that check whether the desired output temperature should be in Celsius or Kelvin.
# ```
# ````

# In[26]:


temp_calculator(75, 'C')


# In[27]:


temp_calculator(75, 'K')


# ## Documenting code
# 
# It is important to document code, either for our future selves or for collaborators who might want to use and adapt our code. We can do that using **block comments** that start with a single hash sign (`#`) followed by a single space and a text string. The Python interpreter will ignore these lines and display them as a different color.

# In[ ]:


def temp_calculator(temp_fahr, convert_to):
    
    # Check if user wants the temperature in Celsius
    if convert_to == "C":
        
        # Convert the value to Celsius
        converted_temp = fahr_to_celsius(temp_fahr)
    
    # Check if user wants the temperature in Kelvin
    elif convert_to == "K":
        
        # Convert the value to Kelvin
        converted_temp = fahr_to_kelvin(temp_fahr)
    
    # Return converted temperature
    return converted_temp


# When writing functions, it is good practice to include even more documentation such as the data type of the expected input/output and example usage. For example, it is not clear whether `convert_to` is expecting the letter `C` or the word `Celsius`. We can do that using a **docstring** which is a multi-line comment that starts and ends with triple quotes (`"""`).

# In[37]:


def temp_calculator(temp_fahr, convert_to):
    
    """
    Function for converting temperature in Fahrenheit to Celsius or Kelvin.

    Parameters
    ----------
    temp_fahr: <numerical>
        Temperature value in Fahrenheit
    convert_to: <str>
        Temperature unit in either Celsius ('C') or Fahrenheit ('F').

    Returns
    -------
    converted_temp: <float>
        Converted temperature.
        
    Example
    --------
    >>> temp_calculator(75, 'K')
    297.0388888888889    
    
    """
    # Check if user wants the temperature in Celsius
    if convert_to == "C":
        
        # Convert the value to Celsius
        converted_temp = fahr_to_celsius(temp_fahr)
    
    # Check if user wants the temperature in Kelvin
    elif convert_to == "K":
        
        # Convert the value to Kelvin
        converted_temp = fahr_to_kelvin(temp_fahr)
    
    # Return converted temperature
    return converted_temp


# Now it would be much easier for another person to use our function. In fact, we can use the `help()` function in Python to find out how our function should be used.

# In[38]:


help(temp_calculator)


# Producing our own functions with docstrings provides an insight into how larger software is developed in Python. We first define some basic operations, then we combine them into bigger chunks to compute what we want. In Week 2, we used several functions available in the `NumPy` library. If we call `help` on one of these functions, we will see that it contains docstrings just like the one we just wrote.

# In[44]:


import numpy as np
help(np.mean)


# ## Acknowledgments
# 
# https://swcarpentry.github.io/python-novice-inflammation/08-func/index.html
# 
# https://geo-python-site.readthedocs.io/en/latest/notebooks/L4/functions.html
