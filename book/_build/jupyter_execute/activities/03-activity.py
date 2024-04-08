#!/usr/bin/env python
# coding: utf-8

# # Practice activity
# 
# ## Glacier melt modeling
# 
# ```{image} images/aws.png
# :alt: aws
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```
# 
# In this activity, we will use `for` loops and conditional statements to model glacier melt. We will use a simple (but common) approach called the **positive degree day method** which assumes that the amount of snow and ice that melts is assumed to be proportional to the number of positive degree days. 
# 
# To explain this method, we will take one step at a time... First, import the data below into your notebook.
# 
# ```
# data = np.array([11.2,11.4,9.8,12.1,11.6,11.6,12.5,12.0,8.2,9.1,8.5,9.6,12.8,15.4,13.5,8.9,12.5,14.1,14.0,14.4,13.9,14.2,
#           7.8,7.2,10.0,8.7,10.4,10.2,10.0,11.0,12.4,12.3,12.1,8.3,6.8,5.8,8.0,11.2,8.8,10.2,12.2,13.4,13.0,17.9,18.0,
#           18.5,14.5,11.9,13.0,12.8,9.9,4.0,6.6,10.5,10.3,11.6,13.7,14.7,5.1,5.8,6.1,3.4,5.0,3.4,4.5,8.2,6.3,6.0,7.6,
#           9.4,9.7,8.8,7.7,9.4,11.9,13.5,12.6,9.8,7.7,5.2,-2.0,-2.6,1.2,1.3,0.4,1.1,-1.4,-2.5,-0.7,0.7,-1.4])
# ```
# 

# ## Task 1 (5 points)
# 
# This dataset contains mean air temperature from a weather station that was installed on Hayden Glacier in the Oregon Cascades between Jul 2 and Sep 30 (91 days). Let's first get some intuition about our dataset. 
# 
# * What was the mean air temperature?
# 
# * What was the lowest/highest air temperaterature recorded?
# 
# * How many days was the air temperature above 0°C?
# 
# * How many days was the air temperature below 0°C?

# ## Task 2 (5 points)
# 
# ### Degree day factor
# 
# A degree day factor (also known as the melt factor) is the amount of melt that occurs **per positive degree day**. Degree day factors are expressed as meters of water-equivalent per degree per day (mm w.e. °C-1 day-1). So if the degree day factor was 0.003 m w.e. °C-1 d-1 and the average daily temperature is +1°C, then the daily melt will be 0.003 m w.e. If the average temperature is +2°C, then there will be 0.006 m w.e. of melt on that day. However, if the average temperature is -1°C, then there will not be any melt on that day.
# 
# So when mean daily air temperature > 0°C:
# 
# $$
#   melt = melt factor * temperature
# $$
# 
# When mean daily air temperature < 0°C:
# 
# $$
#   melt = 0
# $$
# 
# Let's assume that the melt factor is equal to `0.003`.
# 
# * Write a for loop that keeps track of **melt** over our study period. 
# 
# ```{admonition} Click to reveal hint
# :class: tip, dropdown
# The boolean conditional statements (i.e. `if` and `else`) will be useful here, as is the `+=` operator.
# ```
# 
# * What is the total melt that occurs durnig our study period?
# 

# ### Task 3 (5 points)
# 
# Glaciers consist mainly of ice but, during the winter, they are covered in a layer of snow. We can use our melt model to keep track of the snow depth (as well as melt). 
# 
# Let's assume our snow depth at the start of our study period is equal to `1 m`.
# 
# * Modify your for loop so that it keeps track of the **snow depth** during our study period.
# 
# * By the end of the season, what is the snow depth?
# 
# ```{admonition} Click to reveal hint
# :class: tip, dropdown
# Don't worry if it's negative number.
# ```

# ### Task 4 (5 points)
# 
# Snow is much brighter than glacier ice so it therefore absorbs less solar radiation. To account for this, positive degree day models usually include two different melt factors (one for ice and one for snow).
# 
# Let's assume that our melt factor for ice is `0.008` and the melt factor for snow is `0.003`.
# 
# * Modify your for loop so that it accounts for the different melt rates of snow and ice. 
# 
# * What is the total melt that occurs during our study period? How much larger is it than the previous model that assumed a constant melt factor of `0.003`?
# 
