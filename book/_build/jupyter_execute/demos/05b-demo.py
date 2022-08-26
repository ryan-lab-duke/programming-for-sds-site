#!/usr/bin/env python
# coding: utf-8

# # Time
# 
# Converting between time and date formats is a common task but one that is deceptively tricky. Tt can be difficult to keep track of what days or times are being referenced while dealing with different date formats, time zones, daylight savings time, and so on. Fortunately for us, Python has several modules that make it somewhat easier.
# 
# ```{image} images/clock.webp
# :alt: clock
# :class: bg-primary mb-1
# :width: 500px
# :align: center
# ```

# ## Standard date formats
# 
# Despite there being several different date formats (e.g. D M Y or M D Y), the International Organization for Standardization (ISO) developed a standardized format called [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) to facilitate the worldwide exchange and communication of date and time-related data. According to this format, date and time values are ordered from the largest to smallest unit of time: year, month (or week), day, hour, minute, second:
# 
# ```
# YYYY-MM-DD hh:mm:ss
# ```

# ## Computer time
# 
# Most of the computers count time from an arbitrary instant called the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time). This arbitrary date is **January 1st, 1970, at 00:00:00 hours UTC**. Coordinated Universal time (UTC) refers to the time at 0° longitude, popularly known as Greenwich Meridian Time (GMT). It is **not** adjusted for daylight saving time so there are always twenty-four hours in every day. 
# 
# ````{margin}
# ```{note}
# The acronym UTC is not a mistake but a compromise between English and French.
# ```
# ````
# 
# We can print the current **Unix time** using the built-in [`time`](https://docs.python.org/3/library/time.html) module which has a method called `time()` that returns the **current time** as a floating point number expressed in **seconds since the Unix epoch**, in UTC:

# In[121]:


import time

# Define a variable that represents current time
unix_time = time.time()
print(int(unix_time))


# ```{note}
# Note that `unix_time` updates every time we run this code block. We also used `int` to convert the floating point number to an integer for better readability.
# ```

# The number returned by `time()` may be converted into a more common time format (i.e. year, month, day, hour, etc.) in UTC by passing it to either `gmtime()`, which returns time in UTC, or `localtime()`, which returns local time.

# In[122]:


time.gmtime()


# In[123]:


time.localtime()


# These two functions return a [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time) object with a **named tuple** interface. In other words, values in this object can be accessed by their **index** *or* by **attribute name**. The year, month, and day can therefore be printed by typing:

# In[124]:


local = time.localtime()

# Print year, month, and day using index of struct_time object
local[0], local[1], local[2]


# Or:

# In[125]:


# Print year, month, and day using attribute name of struct_time object
local.tm_year, local.tm_mon, local.tm_mday


# ## Convert a `struct_time` object to a standard time format
# 
# We can print the current time in the ISO 8601 standard format (i.e. `YYYY-MM-DD hh:mm:ss`) using the [`strftime`](https://docs.python.org/3/library/time.html#time.strftime) function. This function takes two arguments. The first argument is a string which specifies the output format. The second argument (after the comma) specifies the time we want to convert.
# 
# ````{margin}
# ```{note}
# Remember to include the hyphens and colons when producing a standard time format.
# 
# ```
# ````

# In[126]:


time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# We can print the current time in any way we like.

# In[127]:


time.strftime("%a, %b %d %Y %I:%M:%S %p %Z", time.localtime())


# ```{note}
# For more options see the following [table](https://docs.python.org/3/library/time.html#time.strftime).
# ```

# ## Convert a string to a standard time format
# 
# Sometimes we are presented with strangely formatted dates and times that we would like to convert to a standard format. We can do that using the [`strptime`](https://docs.python.org/3/library/time.html#time.strptime) function. This function takes two arguments, a string that represents the time that we have been given and another string that specifies the format it is in.

# In[128]:


time.strptime('11/30/2022', "%m/%d/%Y")


# We could then use `strftime` to convert this `struct_time` object into standard time format. 
# 
# ````{margin}
# ```{note}
# Note that the forward slashes are converted to hyphens.
# 
# ```
# ````

# In[129]:


time.strftime("%Y-%m-%d %H:%M:%S", time.strptime('11/30/2022', "%m/%d/%Y"))


# ## Convert integers to standard time format
# 
# Another common case is when we have a spreadsheet that contains the year, month, day etc. in separate columns as integers. We can convert these integers into a single string variable by first using the built-in function `str` to convert the integers to strings and then using the `+` sign to concatenate the the individual strings.

# In[130]:


year = 2022
month = 11
day = 30

time_string = str(year) + str(month) + str(day)

time.strptime(time_string, "%Y%m%d")


# In[131]:


t = time.strptime(time_string, "%Y%m%d")

time.strftime("%Y-%m-%d %H:%M:%S", t)


# ```{note}
# The `time` library provides most of what we need but there are other Python libraries such as [`datetime`](https://docs.python.org/3/library/datetime.html) and [`dateutil`](https://dateutil.readthedocs.io/en/stable/) that provide even more functionality for manipulating dates and time. `Pandas` also contains extensive capabilities and features for working with time series data which we will cover in Week 7.
# ```

# In[ ]:




