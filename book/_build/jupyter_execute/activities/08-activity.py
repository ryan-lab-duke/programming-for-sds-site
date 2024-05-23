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
# ## Where are buildings in Eastern Oregon
# 
# ```{image} images/harney.jpeg
# :alt: checkerboard
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```
# 
# In this activity, we will combine several vector datasets to investigate the spatial distribution of buildings in Eastern Oregon. The building footprints can be downloaded from [here](https://www.dropbox.com/scl/fi/e5fhrozgfv2bsj224w87r/eastern-oregon-buildings.geojson?rlkey=ci2ycqrm5y1ouhky578ye9h4m&st=9xy0bsho&dl=0). This a subset of buildings from the dataset produced by Microsoft using AI. See the [GitHub page](https://github.com/Microsoft/USBuildingFootprints) for more information about the data. The other datasets we will need is the highways dataset which can be downloaded from [here](https://www.dropbox.com/scl/fi/k7le95ttz1ekgq83muxej/highways.zip?rlkey=wu09bsduthq1mr323fauodg2r&st=kkorc7b2&dl=0) and the Census tracts dataset which can be downloaded from [here](https://www.dropbox.com/scl/fi/mi4nh71pqaqtfv34nsg0t/tracts.zip?rlkey=q90fkkoekrto3o2wa1g1enbet&st=qgxjo890&dl=0). A "tract" is a subdivision used by the Census Bureau that is smaller than a county and usually contains between 1,200 and 8,000 people.
# 
# ## Task 1 (10 points)
# 
# Load the building dataset.
# 
# * a) How many rows and columns does this file have?
# 
# * b) What is the coordinate reference system of this file?
# 
# * c) What type of geometries does this file contain? (i.e. points, lines, or polygons?)
# 
# Load the Census tracts dataset
# 
# * e) How many rows and columns does this file have?
# 
# * f) What is the coordinate reference system of this file?
# 
# * g) What type of geometries does this file contain?
# 
# Load the highways dataset.
# 
# * h) How many rows and columns does this file have?
# 
# * i) What is the coordinate reference system of this file?
# 
# * j) What type of geometries does this file contain?

# ## Task 2 (5 points)
# 
# * Reproject all three files to UTM Zone 11N (EPSG:32611)

# ## Task 3 (5 points)
# 
# * Perform a **spatial join** (i.e. `sjoin`) between the building footprints and the tracts GeoDataFrames so that each building has the attributes of the tracts GeoDataFrame.
# 
# * Which **county** (`COUNTYFP`) in Eastern Oregon contains the **most** buildings? Looking for a name here (not a number).
# 
# ```{note}
# We can find the name of the county that corresponds to the `COUNTYFP` code [here](https://unicede.air-worldwide.com/unicede/unicede_oregon_fips.html)
# ```
# 
# * Which **county** (`COUNTYFP`) in Eastern Oregon contains the **least** buildings?

# ## Task 4 (5 points)
# 
# * a) Produce an interactive plot (i.e. using `explore()`) showing buildings in Wheeler County

# ## Task 5 (10 points)
# 
# * a) Produce a new GeoDataFrame that only contains highways within Harney County (i.e. using `sjoin()`).
# 
# * b) Produce another new GeoDataFrame containing only the buildings within Harney County.
# 
# * c) Buffer the Harney Highwway GeoDataFrame by 1/2 mile.
# 
# ```{note}
# The [`buffer()`](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.buffer.html) function is useful for this.
# ```
# 
# * d) Set the active geometry of the Harney Highways GeoDataFrame as the new buffer column.
# 
# ```{note}
# We can use [`set_geometry()`](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.set_geometry.html) to do this.
# ```
# 
# * e) Group the buffered polygons into a single `MultiPolygon` using the [`dissolve()`](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.dissolve.html) function. There should only be one row after performing this step. 
# 
# 
# * f) What percentage of buildings in Harney County that are within 1/2 of the highway? 
# 
# ```{note}
# May have to drop the `index_right` columns before running this function.
# ```
# 
# * g) Make a plot of buildings in Harney County that are within 1/2 mile of the highway using `explore()`.

# In[ ]:




