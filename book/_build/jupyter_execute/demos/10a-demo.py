#!/usr/bin/env python
# coding: utf-8

# # Sampling raster data
# 
# Many GIS tasks involve both raster and vector data. In this demo, we have a shapefile containing the coordinates of four campsites in Mt. Rainier and we would like to extract elevation data from a corresponding raster file (that was introduced in [Week 9](../demos/09a-demo.ipynb)).

# In[32]:


import rasterio
from rasterio.mask import mask
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Import raster 
src = rasterio.open('data/N46W122.tif')
elevations = src.read(1)

# Import shapefile
campsites = gpd.read_file('data/campsites.shp')


# ```{image} images/rainier.jpeg
# :alt: rainier
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```

# ## Check coordinates
# 
# Before we can extract the elevation values beneath the points, we must check that the two datasets have the same coordinate reference system. 

# In[33]:


campsites.crs


# In[34]:


src.crs


# It looks they are both projected in **WGS84 (EPSG:4326)** so we can move onto the next step.

# ## Plot
# 
# It's always useful to plot the data so we know it has been read correctly.

# In[35]:


# Plot data
fig, ax = plt.subplots(figsize=(8,8))
im = ax.imshow(elevations)
ax.set_title("Mt Rainier and Mt Adams", fontsize=14)
cbar = fig.colorbar(im, orientation='vertical')
cbar.ax.set_ylabel('Elevation', rotation=270, fontsize=14)
cbar.ax.get_yaxis().labelpad = 20


# ## Sampling the data using points
# 
# To sample the raster data at the campsite locations we can use `Rasterio's` [`sample`](https://rasterio.readthedocs.io/en/latest/api/rasterio.sample.html) function. This function expects a list of x, y coordinate pairs so we need to convert our `geometry` column using list comprehension. 

# In[36]:


coord_list = [(x,y) for x,y in zip(campsites['geometry'].x , campsites['geometry'].y)]
coord_list


# Now we can carry out the sample and store the results in new column called **elevation**. Note that if the image has more than one band, a value is returned for each band.

# In[37]:


campsites['elevation'] = [x for x in src.sample(coord_list)]
campsites.head()


# ## Buffer points
# 
# Sometimes it might be a little risky to sample only one cell per point. There may be errors or artifacts in the unerlying raster. A more robust method would be to sample multiple raster grid cells surrounding a point. To do this we could **buffer** the points by a set distance and sample the raster values within the buffer.  
# 
# `GeoPandas` has a method called [`buffer`](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.buffer.html) which expects a **distance** around each object. Since our shapefile is in WGS84 coordinate system, this distance would have to be in **degrees** which is a little confusing. A better option would be to reproject our shapefile into a **projected coordinate system** so we can enter a buffer distance in **meters**. 

# In[38]:


campsites_utm = campsites.to_crs('EPSG:32610')
campsites_utm['buffer'] = campsites_utm.buffer(500)
campsites_utm


# Now we have two columns containing **geometry** values. But a `GeoDataFrame` can only have one active geometry. Since we intend to use our buffer geometry to sample the raster data, we will make our **buffer** column the active geometry.

# In[39]:


campsites_utm.set_geometry('buffer', inplace=True)


# We have to convert the DataFrame back to WGS84 so it has the same projection system as our raster data.

# In[40]:


campsites = campsites_utm.to_crs('EPSG:4326')


# ## Sampling grid cells using polygons
# 
# There is a package called [`rasterstats`](https://pythonhosted.org/rasterstats/) that makes this task pretty straightforward. In the docs, it recommends installing using `pip`. We can actually do this directly from a Jupyter Notebook by using the `!` mark which allows us execute commands from the underlying operating system.

# In[41]:


get_ipython().system('pip install rasterstats')


# After successfully installing `rasterstats`, we can go ahead and import the function we need. 

# In[42]:


from rasterstats import zonal_stats


# The [`zonal_stats`](https://pythonhosted.org/rasterstats/manual.html#zonal-statistics) function requires a shapefile or polygon, a raster file or array, the geotransform of the array, and the stats we'd like to compute. 

# In[76]:


stats = zonal_stats(campsites.geometry, elevations, affine=src.transform, 
            stats=['mean', 'std', 'count'], nodata=src.nodata)
stats


# The `mean` value provides a robust measure of elevation surrounding each campsite. By including the `count` option we can see that there were 1198/1199 grid cells sampled for each 500 m buffer. The `std` option provides the variance of elevations in the buffer.
# 
# We can add these data to our original GeoDataFrame. Luckily for us, `Pandas` can implicitly convert a **list of dictionaries** to a `DataFrame`. Since `zonal_stats` preserves the order of campsites, we can use the index to **merge** the two DataFrames. 

# In[75]:


campsite_stats = campsites.merge(pd.DataFrame(stats), left_index=True, right_index=True)
campsite_stats

