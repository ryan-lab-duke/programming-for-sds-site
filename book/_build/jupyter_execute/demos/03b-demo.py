#!/usr/bin/env python
# coding: utf-8

# # Conditional statements
# 
# Most of the time when we are programming we are asking the computer to perform certain tasks if certain conditions are met. For example:
# 
# * If a person in the dataset is older than 30, then print out their name
# 
# * If a tweet contains a specific phrase, then automatically retweet it
# 
# * If  then say “Congratulations!"
# 
# In the second part of this week we will learn about conditional statements (`if`, `elif`, `else`), comparison operators (`>`, `<`, `==`), and Boolean values (`True`, `False`).

# ## A simple conditional statment
# 
# Here is an example. A messenger arrives at a crossroads and has to make a decision about which way to go. We would like them to turn **left**. This is what the code could look like:

# In[21]:


direction = 'left'

if direction == 'left':
    print("Turns left")


# There are two important Python elements presented in the code above: a **comparison** and a **conditional statement**. We compared whether the variable `direction` is **equal to** the value `left`. Then we printed `Turns left` if this condition was **True**. 

# Conditional statements are written in a similar way to `for` loops. The `if` statement checks to see whether the variable value is `True` or `False`. If a `True` is returned, then we execute the **indented** command below. 
# 
# Alternatively, the messenger might decide to turn **right**.

# In[25]:


direction = 'right'

if direction == 'left':
    print("Turns left")


# ````{margin}
# ```{note}
# Similar to `for` loops, Python uses colons (:) and whitespace (indentations) to structure conditional statements.
# ```
# ````

# This time the first statement (`if direction == 'left':`) was ignored because the value returned was `False`. Nothing was returned.

# ## `elif`
# 
# We can add more complexity in a conditional statement by usinga an `elif` statement. If we wanted to add an option for turning right we could write:

# In[26]:


direction = 'right'

if direction == 'left':
    print("Turns left")
elif direction == 'right':
    print("Turns right")


# ```{note}
# It is good practice to use `elif` statements beneath `if` statements to explicitly state that the cases are **mutually exclusive** (i.e. if we turn left, we cannot turn right).
# ```

# What happens if our messenger wanted to go **straight**?

# In[28]:


direction = 'straight'

if direction == 'left':
    print("Turns left")
elif direction == 'right':
    print("Turns right")


# Both statements return a `False` value, no commands are executed, and nothing is returned. 
# 
# ## `else`
# 
# To catch these alternative options, we can add an `else` statement.

# In[29]:


direction = 'straight'

if direction == 'left':
    print("Turns left")
elif direction == 'right':
    print("Turns right")
else: 
    print("Stay straight")


# The command beneath the `else` statement will be executed if all `if` and `elif` statements return `False`. 

# ```{note}
# The `else` clause is optional. If it is present, there can be only one and it must be specified last.
# ```

# ```{tip}
# Along with the `==` operator, there are a few more options to know about:
# 
# `>`: greater than
# `<`: less than
# `==`: equal to
# `!=`: does not equal
# `>=`: greater than or equal to
# `<=`: less than or equal to
# ```

# ## Boolean alegbra
# 
# Our conditional statements are not limited to strings, we can also use numbers. In addition, we might want to include logical operators such as `and`, `or`, and `not` into our conditions. We can do this as follows:

# In[52]:


temperature = 60

if (temperature > 90) or (temperature < 30):
    print("Stay at home")
else: 
    print("Cross the pass and deliver mail!")


# Here we combined two conditional statements using the `or` operator to determine whether our messenger should go and deliver mail.

# ```{note}
# An alternative for `and` is `&`. Likewise, `or` can be replaced with `|`
# ```

# ## Keeping track
# 
# We can use boolean conditional statements and `+=` operator to keep track of values. `+=` adds another value to the current value of the variable. Let's say our messenger wanted to buy an apple and an orange but did not know what fruit the shops had in stock. First we visit the fruit stand: 

# In[65]:


fruit_stand = ['lemons', 'oranges']
food = 0

if fruit_stand.count('apples') > 0:
    food += 1
if fruit_stand.count('pears') > 0:
    food += 1
else:
    pass

food


# ```{note}
# This time our statements are **not mutually exclusive** (i.e. it is possible that we can find both apples **and** pears) so it is OK to use two `if` statements. 
# ```

# ````{margin}
# ```{note}
# The **pass** command beneath the `else` statement. This is basically a placeholder for "do nothing". 
# ```
# ````

# Unfortunately, there were no apples and oranges for sale so our messenger still has no fruit to eat.

# In[1]:


corner_shop = ['apples', 'oranges', 'pears', 'melons', 'grapefruits']
items = 0

if corner_shop.count('apples') > 0:
    items += 1
if corner_shop.count('pears') > 0:
    items += 1
else:
    pass

items


# Luckily, the corner shop had apples and oranges so our messenger now has two pieces of fruit to eat. 

# ## Combining for loops and conditional statements
# 
# Conditional statements are often combined with for loops. Let's say we wanted to calculate how many days the messenger could cross the pass and deliver mail over a 50-day period. 

# In[2]:


# Import package
import numpy as np

# Make a new array of random temperatures between 10 and 60 for 50 days
temperatures = np.random.randint(10, 60, 50) 

# Set days equal to zero
days = 0

# Loop over every day
for i in temperatures:
    if (i > 90) or (i < 30):
        days += 1        
    else: 
        pass

print(f"The messenger delivered mail on {days} days")

