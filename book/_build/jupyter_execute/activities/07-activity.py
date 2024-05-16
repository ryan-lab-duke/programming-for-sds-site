#!/usr/bin/env python
# coding: utf-8

# # Practice activity
# 
# If you have installed Python locally, launch JupyterLab by running:
# 
# ```
# conda activate sds
# ```
# and
# 
# ```
# jupyter lab
# ```
# 
# *****************************
# 
# ## Analyzing table data
# 
# In this activity, we will use `Pandas` and `Matplotlib` to do some more advanced data analysis.. The data can be downloaded [here](https://www.dropbox.com/scl/fi/tesoyfuc1do9oagvpl2h5/hayden-glacier-aws-data.csv?rlkey=zbjlb5zre4u9g9t7ccrlcygzy&st=1o7e0cdb&dl=0). We have seen this dataset before! It's weather station data from Hayden Glacier but this time it is provided at 15-minute interval. 

# *****************************
# 
# ## Task 1 (10 points)
#  
#  * a) Read the weather station data, parse the `Datetime` column, and set the index column to `Datetime`
# 
#  * b) What time was solar radiation highest on July 3?
# 
#  * c) Make a plot showing solar radiation and annotate it to show the value of highest solar radiation
# 
#  * d) Resample the data to **mean daily** values
# 
#  * e) On what date was solar radiation (mean daily) highest?
# 
#  * f) Make a plot showing mean daily solar radiation
# 
#  * g) Perform a 30-day median filter using a rolling window
# 
#  * h) Make a figure showing both the daily solar radiation and median filtered solar radiation on the same plot
# 
#  * i) By how much does mean daily solar radiation change during the study period (July 07 to Sep 16)? Looking for a value in W m^-2^ d^-1^.
# 
#  * j) Based on this rate, what will be the mean solar radiation on Oct 30, 2023?

# *****************************
# 
# ## Task 2 (0 points)
# 
# * Add a title, your name, and date of this submission to your Jupyter Notebook using **Markdown text**.
# 
# * Add some more **Markdown text** to separate each task of this assignment.
# 
# 
# ```{important} 
# Save your notebook to your local course folder and submit assignment (in **.pdf** format) to Canvas by the deadline.
# ```
