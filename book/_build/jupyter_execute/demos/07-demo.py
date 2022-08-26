#!/usr/bin/env python
# coding: utf-8

# # Analyzing table data
# 
# In this week, we will analyze some real-world data, building on the techniques we covered in Week 4. Our dataset contains water temperature (in C) and discharge (in cubic feet per second) from the [Middle Fork of the Willamette River](https://en.wikipedia.org/wiki/Middle_Fork_Willamette_River) near Jasper. This river drains an area of the Cascade Range southeast of Eugene. The [gauge](https://waterdata.usgs.gov/monitoring-location/14150000/#parameterCode=00065&period=P7D) is located in Elijah Bristow State Park, a few miles below Dexter Reservoir. 
# 
# ```{image} images/willamette.jpg
# :alt: willamette
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```

# ## Visualize
# 
# With any new project, it is usually a good practice to visualize the data to get a sense of what we are working with.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
df = pd.read_csv('data/middle_fork_willamette.csv', parse_dates=['date'], index_col=['date'])
df


# In[3]:


fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(df['discharge'], linewidth=2, label='discharge')
ax1.set_title('Middle Fork of the Willamette River', fontsize=14)
ax1.tick_params(axis='both', labelsize=14)
ax1.set_ylabel('Discharge (ft$^3$ s$^{-1}$)', fontsize=14, color='C0')
ax1.tick_params(axis='both', labelsize=14)
ax1.tick_params(axis='y', labelcolor='C0')

ax2 = ax1.twinx()  # add a second axes that shares the same x-axis
ax2.plot(df['temp'], color='C1', linewidth=2, label='temperature')
ax2.tick_params(axis='y', labelcolor='C1')
ax2.tick_params(axis='both', labelsize=14)
ax2.set_ylabel('Temperature (C)', fontsize=14, color='C1')

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
ax1.grid()

plt.show()


# ## Missing values
# 
# The first stage of data cleaning and preparation involves handling missing values which are a feature of nearly all "real life" datasets. Before handling missing values, we need to count the number of missing values in the DataFrame. We can use the [`info()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html) method to provide information about a DataFrame including the data types, column names, non-null values, and memory usage.

# In[4]:


df.info()


# From the data summary, we can see that there are six missing (or null) values in the dicharge column. There are many ways to handle these values and there is no "best" way that can be used for every task. We will zoom in on one of these missing values to demonstrate.

# In[5]:


df_missing = df[286:293]
df_missing


# We have a missing value on July 16. One option we have is to drop this value completely by making a **boolean mask** that depends on whether the discharge value is `notna()`.

# In[6]:


df_missing[df_missing['discharge'].notna()]


# We can also fill the missing values with the values that come before or after it using [`fillna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html). This method is used quite often in time series analysis. The `ffill` method will **propagate forward**, filling the missing value with the value before. The `bfill` method will **propagate backward**, filling the missing value with the value after.

# In[7]:


df_missing.fillna(method='ffill')


# In[8]:


df_missing.fillna(method='bfill')


# We could also linearly [`interpolate`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html) the missing value using the values before and after.

# In[9]:


df_missing.interpolate()


# We will apply this method to the whole dataset so that we no longer have any missing values.

# In[10]:


df = df.interpolate()
df.isnull().sum()


# ## Resample
# 
# Since `Pandas` is "aware" that our index column represents dates, we can easily [`resample`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html) our data to a a different sampling frequency. For example, we can produce a **mean monthly** temperature record:

# In[11]:


df_monthly_mean = df['temp'].resample('1M').mean()
df_monthly_mean.head()


# ```{tip} 
# The frequencies after `resample` are called **offset aliases**. A table of valid offset aliases can be found [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases).
# ```

# Alternatively, instead of averaging the temperatures in each month, we could **sum** the **discharges** in each month:

# In[12]:


df_monthly_sum = df['discharge'].resample('1M').sum()
df_monthly_sum.head()


# We could also choose different time frequency such as the median over 10 days.

# In[13]:


df_10day_mean = df['discharge'].resample('10D').median()
df_10day_mean.head()


# Resampling is useful for summarizing our data at different temporal frequencies so we can reliably compare one year to the next. We can plot one of the resampled data to check that it looks right. 

# In[15]:


fig, ax1 = plt.subplots(figsize=(12, 5))
ax1.plot(df['temp'], linewidth=2, label='daily')
ax1.plot(df_monthly_mean, linewidth=2, marker='o', linestyle='dashed', label='monthly')
ax1.set_title('Middle Fork of the Willamette River', fontsize=14)
ax1.tick_params(axis='both', labelsize=14)
ax1.set_ylabel('Discharge (ft$^3$ s$^{-1}$)', fontsize=14)
ax1.tick_params(axis='both', labelsize=14)

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
ax1.grid()
ax1.legend(fontsize=14)

plt.show()


# ## Rolling windows
# 
# Similar to resampling, [rolling windows](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html) split and aggregate the data into time windows with a function such as `mean()`, `median()`, `sum()`, etc. However, unlike **resampling** where the bins do not overlap so the output is at a lower frequency than the input, **rolling windows** overlap (or "roll") along at the same frequency as the data, so the transformed time series is at the same frequency as the original time series.

# In[16]:


weekly_discharge = df['discharge'].rolling(7, center=True).mean()
monthly_discharge = df['discharge'].rolling(30, center=True).mean()
seasonal_discharge = df['discharge'].rolling(91, center=True).mean()


# ```{note} 
# We use the `center=True` argument to label each window at its midpoint
# ```

# In[18]:


fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(df['discharge'], linewidth=2, label='daily')
ax1.plot(weekly_discharge, linewidth=3, linestyle='dashed', label='weekly')
ax1.plot(monthly_discharge, linewidth=3, linestyle='dotted', label='monthly')
ax1.plot(seasonal_discharge, linewidth=2, linestyle='dashdot', label='seasonal')

ax1.set_title('Middle Fork of the Willamette River', fontsize=14)
ax1.tick_params(axis='both', labelsize=14)
ax1.set_ylabel('Discharge (ft$^3$ s$^{-1}$)', fontsize=14)
ax1.tick_params(axis='both', labelsize=14)

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
ax1.grid()
ax1.legend(fontsize=14)

plt.show()


# As we can see from the figure above, the rolling windows are smoother than the original discharge data because higher frequency variability has been averaged out. These kind of operations can be useful for **removing noise** from our data.

# ## Linear regression
# 
# One of the most common tasks in spatial data science is to determine whether there is a statistically significant relationship between two (or more) variables. In the first plot we made, it looked like river discharge and water temperature were **negatively correlated** (i.e. as discharge increases, water temperature decreases). We can determine whether this correlation is statistically significant by performing [linear regression](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html) using the `scipy` library.

# In[19]:


from scipy.stats import linregress


# In[20]:


slope, intercept, r, p, se = linregress(df['discharge'], df['temp'])


# In[21]:


print(f"R-squared: {r**2:.3f}\n", f"p-value: {p:.5f}")


# We find that the two variables are significantly **linearly** correlated (*p*-value) with a correlation coefficient (R-sqaured) of 0.235. Let's plot the two variables on a scatter plot.

# In[23]:


fig, ax = plt.subplots(figsize=(12, 6))
ax.scatter(df['discharge'], df['temp'], s=100, edgecolor='k', zorder=2)
ax.set_xlabel('River discharge (ft$^3$ s$^{-1}$)', fontsize=14)
ax.set_ylabel('Temperature (C)', fontsize=14)
ax.grid(ls='dashed', lw=1.5, zorder=1)
ax.tick_params(axis='both', labelsize=14)
plt.show()


# Although there is significant linear correlation, it does not look like a linear relationship is the best fit between these two variables. When discharges are low (< 4000), water temperature rapidly decreases with as discharge increases. But when discharges are high (> 4000), water temperature do not appear very sensitive to changing discharge. Instead a polynomial regression might provide a better fit but we will leave that for another day.

# In[ ]:




