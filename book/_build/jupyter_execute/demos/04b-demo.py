#!/usr/bin/env python
# coding: utf-8

# # Pandas DataFrames II
# 
# Since `Pandas` provides such an extensive set of tools for working with table data, it is worth doing another demo on it. In this demo, we will import a new dataset called `air_quality_no2_long.csv` which provides air quality data (Nitrogen Dioxide) from the measurement stations FR04014, BETR801 and London Westminster in Paris, Antwerp, and London, respectively.

# In[127]:


import pandas as pd
df1 = pd.read_csv('data/air_quality_no2_long.csv')
df1.head()


# Let's say we had another air quality dataset, except this time for particulate matter less than 2.5 micrometers (PM2.5). 

# In[128]:


df2 = pd.read_csv('data/air_quality_pm25_long.csv')
df2.head()


# ## Combining data from multiple tables
# 
# If we wanted a single DataFrame that included both these tables, we could use the `concat` function. The `concat` function performs the operation along one of the axes (row-wise or column-wise). By default concatenation is along `axis=0`, so the resulting table combines the **rows** of the input tables. 
# 
# ```{image} images/concat_row.svg
# :width: 700px
# :align: center
# ```

# In[129]:


air_quality = pd.concat([df1, df2], axis=0)


# ```{note}
# It's useful to know the shape of the DataFrames before (and after) the concatenation so we know that it worked as expected. 
# ```

# In[130]:


df1.shape, df2.shape, air_quality.shape


# We can also check that the DataFrames were concatenated properly by sorting by the `date.utc` columns. If we do so, we will find both `no2` and `pm25` values contained in the **parameter** column.

# In[131]:


air_quality.sort_values("date.utc").head(10)


# ## Joining multiple tables by a common identifier
# 
# The coordinates of the air quality measurement stations are stored in a separate file. It would be useful if we could add the coordinate information to the original air quality DataFrame. To do this, we can use the `merge` function. 
# 
# ```{image} images/merge_left.svg
# :width: 900px
# :align: center
# ```
# 

# In[132]:


stations_coord = pd.read_csv('data/air_quality_stations.csv')
stations_coord.head()


# Both tables have the column `location` in common which is used as a `key` to combine the information. By choosing the `left` merge, only the locations available in the `air_quality` (left) table, i.e. `FR04014`, `BETR801` and `London Westminster`, are returned in the new table. 

# In[133]:


air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
air_quality.head()


# We have one more table to merge with our original DataFrame. This table is called `air_quality_paramters`. 

# In[134]:


air_quality_parameters = pd.read_csv('data/air_quality_parameters.csv')
air_quality_parameters.head(6)


# Note that, compared to the previous example, there is **no common column name**. However, the `parameter` column in the `air_quality` table and the `id` column in the `air_quality_parameters` table both provide the measured variable in a common format. We could rename one of the columns. Alternatively, we could use the `left_on` and `right_on` arguments to make the link between the two tables.

# In[135]:


air_quality = pd.merge(air_quality, air_quality_parameters,
                       how='left', left_on='parameter', right_on='id')
air_quality.head()


# ## Dropping columns
# 
# There are various ways to drop one or multiple columns from a Dataframe. The easiest is the use the `drop` function. 

# In[136]:


# First create a new variable so that we add it later
name = air_quality['name']


# In[137]:


air_quality = air_quality.drop(['name'], axis=1)
air_quality.head()


# ## Adding columns
# 
# Likewise, we can add columns. To do this we can define a new columns (i.e. `name`) and set it equal to a list of values.

# In[138]:


air_quality['name'] = name
air_quality.head()


# ```{note}
# This will only work if the new data has the **same number of rows** as the original DataFrame. 
# ```

# ## Acknowledgments
# 
# This demo was inspired by the [Pandas API reference tutorial](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/08_combine_dataframes.html).  
# 
