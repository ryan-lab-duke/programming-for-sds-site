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
# ## Golf courses in Oregon
# 
# In this activity, we will use `Pandas` to conduct some data analysis on golf courses in Oregon. The data can be downloaded [here](https://www.dropbox.com/scl/fi/7reqx12fh954vi2tjb5p7/golf-oregon.csv?rlkey=musbdorxqutxe2e4ck2aihko3&dl=0) and [here](https://www.dropbox.com/scl/fi/x93b8cr6qmedvturck00u/or-zip-codes-data.csv?rlkey=7ffg3jma51rmnc1614vc3eacg&dl=0). The first dataset is a table of golf courses in Oregon. The second dataset is provides population data for each zip code in Oregon.  
# 
# ```{image} images/golf-course.jpeg
# :alt: golf
# :width: 600px
# :align: center
# ```

# *****************************
# 
# ## Task 1 (5 points)
# 
# Read the the golf course dataset and answer the following questions:
# 
# * How many rows and columns are in this dataset?
# 
# * What are the names of the columns?
# 
# * When was the first golf course built in Oregon?
# 
# * What is the name and the town of the oldest course?
# 
# * What is the name (and cost) of the course with the highest green fees?

# *****************************
# 
# ## Task 2 (5 points)
# 
# Read the the zip code population dataset and answer the following questions:
# 
# * How many rows and columns are in this dataset?
# 
# * What is the mean population?
# 
# * How many zip codes have more than 40,000 people?
# 
# * Which county has the most cities?
# 
# * Which city has the most zip codes?

# *****************************
# 
# ## Task 3 (5 points)
# 
# * Merge the two Dataframes
# 
# * How many zip codes do not have a single golf course?
# 
# * Which zip code has the most golf courses?
# 
# * Which city has the most golf courses per capita (i.e. per person)?
# 
# * Which county has the most golf courses per capita?

# *****************************
# 
# ## Task 4 (0 points)
# 
# * Add a title, your name, and date of this submission to your Jupyter Notebook using **Markdown text**.
# 
# * Add some more **Markdown text** to separate each task of this assignment and use **f-strings** to make yours answers clear.
# 
# ```{important} 
# Save your notebook to your local course folder and submit assignment (in **.pdf** format) to Canvas by the deadline.
# ```
