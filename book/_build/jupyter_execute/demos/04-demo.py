#!/usr/bin/env python
# coding: utf-8

# # Pandas DataFrames
# 
# One of the pillars Spatial Data Science is a Python library called `Pandas` which provides functions to import tabular data from various file formats (e.g. `.csv`, `.xlsx`) and many other data manipulation operations such as merging, reshaping, selecting, cleaning, and wrangling. In this week, we will introduce some basic `Pandas` operations. In Week 7, we will progress to more advanced usage of `Pandas`. 
# 
# ```{note}
# The name "Pandas" is derived from the "panel data", an econometrics term for data sets that include observations over multiple time periods.
# ```
# 
# ## Data structure
# 
# The main `Pandas` data structure is called a **DataFrame** which looks similar to an Excel spreadsheets. A typical DataFrame is a 2-D array with rows, columns, indices, and column names. We can import the `Pandas` and define a DataFrame like so:

# In[2]:


import pandas as pd

df = pd.DataFrame({"city": ['Belfast', 'Cardiff', 'Edinburgh', 'London'],
                   "country": ['Northern Ireland', 'Wales', 'Scotland', 'England']})

df.head()


# ````{margin}
# ```{note}
# Similar to `NumPy`, it is standard practice to shorten the imported name to `pd` for better code readability.
# ```
# ````

# So what do we have here? We now have a small table containing countries in the United Kingdom and their capital cities. The table has **two labeled columns**, one called "city" and one called "country". The table has **four rows**, with each row corresponding to an **index** between 0 and 3. 

# ````{margin}
# ```{note}
# Column names must be unique.
# ```
# ````

# ## Reading data
# 
# In reality, we rarely make a table from scratch. Instead we **read** files that already contain data and store the contents of those files into variables. We can do this using `.read_csv()` which is a general function for reading data files separated by commas, spaces, or other common separators. The function takes a **path string** and returns a `DataFrame` object. 

# In[6]:


df = pd.read_csv('data/euro_cities.csv')

# "df" stands for DataFrame
type(df)


# A concise way of checking what is contained in our `df` object is the `.head()` method which prints the first five rows of the data.

# In[7]:


df.head()


# Alternatively, we could check the last five rows of the data:

# In[24]:


df.tail()


# Or the last 10 rows:

# In[25]:


df.tail(10)


# ## DataFrame properties
# 
# To check the data types of each column, we can use `Pandas` method called `.dtypes`:

# In[27]:


df.dtypes


# Here we see that population is an **integer** (with 64-bit precision) and the other two columns are **objects** (`Pandas` stores string data types as "objects" by default).
# 
# We can also retrieve the column names of the DataFrame using the `column` method.

# In[30]:


df.columns


# And, just like `NumPy` arrays, we can find the shape of our DataFrame using the `shape` method.

# In[31]:


df.shape


# ## Indexing 
# 
# We can select specific columns based on the column values. The basic syntax is `dataframe[value]`, where value can be a single column name, or a list of column names.

# In[32]:


df['city']


# In[34]:


df[['city', 'country']]


# We can select specific rows using the `.iloc` method.

# In[41]:


df.iloc[6]


# The syntax for selecting the top 10 cities should be quite familiar.

# In[54]:


df.iloc[0:10]


# If we wanted to find the city with the highest/lowest population we could use `.idxmax()`/`idxmin()` which returns the index of the highest/lowest value in the column.

# In[170]:


df['population'].idxmax()


# In[135]:


index_high = df['population'].idxmax()

city_high = df.iloc[index_high]['city']

f"The city with the largest population in Europe is {city_high}"


# ## Descriptive statistics
# 
# `Pandas` provides basic functions to calculate descriptive statistics - similar to what we might usuaally do with Microsoft Excel.

# In[45]:


df['population'].mean()


# In[46]:


df['population'].max()


# In[47]:


df['population'].min()


# We can get all descriptive statistics at once using the `describe()` function

# In[50]:


df['population'].describe()


# Where the `25%, 50%, and 75%` are the [inter-quartile ranges](https://en.wikipedia.org/wiki/Quartile). Often the output of `describe()` is more readable if we **round** these data to two decimal places.

# In[51]:


round(df['population'].describe(), 2)


# ## Slicing
# 
# Let's say we wanted to find how many cities in Germany made it into this top 100 list. We would first produce a **Boolean** mask (i.e. valus equal to `True` or `False`) using the `==` comparison operator.

# In[63]:


mask = df['country'] == 'Germany'
mask


# We could then apply this mask to our original DataFrame.

# In[64]:


df[mask]


#  We could do something similar if we wanted to find cities with populations of over 2 million. 

# In[69]:


df[df['population'] > 2000000]


# We can add logical operators to find cities with populations of between 700,000 and 800,000

# In[75]:


df[(df['population'] < 800000) & (df['population'] > 700000)]


# ````{margin}
# ```{note}
# Note the use the parentheses
# ```
# ````

# ## Grouping
# 
# If we wanted to find the total population living in these cities for each country, we **could** write a `for` loop. To do this, we would have to produce a list of individual countries, loop over each country, compute the total, and append to a new list... and then put it back into a new DataFrame. 
# 
# This is what that would look like:

# In[84]:


countries = pd.unique(df['country'])

total_pop = []
for country in countries:
    
    country_df = df[df['country'] == country]
    
    total_pop.append(country_df['population'].sum())


# In[91]:


new_df = pd.DataFrame({'country': countries,
                       'population': total_pop})
new_df.head(10)


# **Or** we could use the `groupby()` function.

# In[96]:


df.groupby('country')['population'].sum()


# The first argument `groupby` takes is the **which** column we want group our data into (`country` in our case). Next, it takes a column (or list of columns) to summarize (`population`). Finally, this function does nothing until we specific **how** we want to group our data.
# 
# It's actually nice to reset the index after using `groupby` so that we end up with another DataFrame. 

# In[99]:


new_df = df.groupby('country')['population'].sum().reset_index()
new_df.head(10)


# We hope you will agree that the `groupby` method is much cleaner and interpretable. It is also a lot faster which may be important when we have very large DataFrames with millions of rows. 

# ```{note}
# To summarize multiple columns we could include a list of columns like so: `df.groupby('country')[['city','population']].sum()` but this would not produce anything different in our case because a string variable cannot be **summed**.
# ```

# ## Sorting
# 
# Similar to lists, we can **sort** DataFrames using the `sort_values` function. This function takes two arguments, `by` and `ascending` which determine which column and which order we would like to sort by. So to find the 10 largest cities in Europe by population we could type:

# In[175]:


df.sort_values(by='population', ascending=False).head(10)


# Another way of doing this would be to use the `nlargest()` or `nsmallest()` function. Documentation [here](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html).

# ## Saving 
# 
# We can save our DataFrames just as easy as reading the original file using the `.to_csv` function

# In[112]:


new_df.to_csv('data/new.csv')

