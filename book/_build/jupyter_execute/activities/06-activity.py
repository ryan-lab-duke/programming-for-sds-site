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
# ## Plotting tabular data
# 
# In this activity, we will use `Pandas` and `Matplotlib` to practice our plotting skills. The data can be downloaded [here](https://www.dropbox.com/scl/fi/4m16i3lkbvi9tyo3kpyxe/avg-precip-months-seasons.csv?rlkey=09r6ki4nr5vkrvc4yyzhadyk6&st=y4jg83yq&dl=0) and [here](https://www.dropbox.com/scl/fi/8n2k7ux98a5uofi29n046/glaciers.csv?rlkey=f2eeam6rckhs96ni6s19tz9zb&st=phtclcvn&dl=0). The first dataset contains average monthly rainfall in inches. The second dataset contains the average loss of global glaciers from 1945 to the present from NOAA data.

# *****************************
# 
# ## Task 1 (5 points)
# 
# * a) Read in `avg-precip-months-seasons.csv`
# 
# * b) Produce a basic plot using `plot()`
# 
# * c) Set an appropriate **xlabel**, **ylabel**, and **title**.
# 
# * d) Use the `linestyle` parameter to modify the line style to something other than solid.
# 
# * e) Change the color to something other than the default blue.

# *****************************
# 
# ## Task 2 (5 points)
# 
# * a) Produce a **bar** plot using `ax.bar()`
# 
# * b) Set an appropriate **xlabel**, **ylabel**, and **title**.
# 
# * c) Use the `edgecolor` and `color` parameters to modify the colors of your plot to something other than blue.

# *****************************
# 
# ## Task 3 (5 points)
# 
# * a) Above we produced two separate plots. Now make a single figure that contains two subplots stacked on top of each other. The first should be the line plot, the second should be the bar chart.
# For the figure do the following:
# 
# * b) Add an overal title to your figure using `plt.suptitle()`
# 
# * c) Reduce whitespace using `layout='constrained'`

# *****************************
# 
# ## Task 4 (5 points)
# 
# * a) Read in `glaciers.csv` 
# 
# * b) Parse the dates from the .csv file and assign the `date` column as the **index**.
# 
# * c) Plot your data making sure `date` is on the x-axis and `Cumulative mass balance` is on the y-axis.
# 
# * d) Set an appropriate **xlabel**, **ylabel**, and **title**.
# 
# * e) Change the x limits to range from **1940** to **2020** using the `ax.set_xlim()` argument.

# *****************************
# 
# ## Task 5 (0 points)
# 
# * Add a title, your name, and date of this submission to your Jupyter Notebook using **Markdown text**.
# 
# * Add some more **Markdown text** to separate each task of this assignment.
# 
# 
# ```{important} 
# Save your notebook to your local course folder and submit assignment (in **.pdf** format) to Canvas by the deadline.
# ```
# 
# ## Acknowledgments
# 
# This activity is based on the [Earth Data Analytics Online Certificate](https://www.earthdatascience.org/courses/scientists-guide-to-plotting-data-in-python/plot-activities/plot-time-series-data-python/) plotting chapter. 
# 
