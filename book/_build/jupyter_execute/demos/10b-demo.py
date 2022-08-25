#!/usr/bin/env python
# coding: utf-8

# # Classifying raster data
# 
# In the previous week, we produced some nice looking maps of Florence from remote sensing data. We computed some band indices and learnt that positive NDWI values were likely to be associated with water (e.g lakes, rivers, ocean). 
# 
# However, we did not conduct any quantitative analysis. For example, what if someone wanted to know how much water was in the image? To do this, we would first have to classify pixels that are likely to be water using a threshold. In this week, we will learn how to do this, and other quantitative analysis, by combining raster and vector data. 

# In[80]:


# Import modules
import numpy as np
import rasterio
from rasterio.mask import mask
import geopandas as gpd
from scipy import stats
import matplotlib.pyplot as plt


# ## Preparing the data

# In[81]:


# Define paths to data
raster = 'data/ndwi.tif'
shapefile = 'data/water.shp'

# Import raster data
src = rasterio.open(raster)
ndwi = src.read(1)

# Import shapefile
water = gpd.read_file(shapefile)


# The `ndwi.tif` is a raster file of Florence, OR containing the NDWI values we produced last week. 

# In[82]:


plt.imshow(ndwi)


# The `water.shp` file is a shapefile containing some polygons. Each polygon outlines areas of known water in the Landsat image. This shapefile could be produced using manual digitization in ArcGIS or QGIS.

# In[92]:


water.iloc[1].geometry


# Before we can extract the NDWI values that intersect the polygons, we must check that the two datasets have the same coordinate reference system. Since they are both projected in **UTM Zone 10N (EPSG:32610)** we can move onto the next step.

# In[93]:


src.crs


# In[94]:


water.crs


# ## Masking raster data using shapefile
# 
# `Rasterio` provides a function called [`mask.mask`](https://rasterio.readthedocs.io/en/latest/api/rasterio.mask.html#) for masking raster data using polygons. This function has a few arguments. The first is the raster dataset (i.e. `src` in our case). The second argument is the shape to mask. In the docs, it notes that the shapes must be:
# 
# > a GeoJSON-like dict or an object that implements the Python geo interface protocol (such as a Shapely Polygon)"
# 
# So we will have to specify only the **geometry** of our `GeoPandas` DataFrame, not the DataFrame object itself. The **Invert** argument determines whether pixels inside or outside shapes will be masked. The **nodata** argument allows us to set the no data value (i.e. values of pixels outside the mask). 

# In[95]:


water_mask, transform = mask(src, water.geometry, invert=False, nodata=np.nan)


# The `mask.mask` function returns an array where pixel values inside the mask are retained, while pixel values outside the mask are assigned a NaN value. 

# In[87]:


water_mask


# ## Determining a threshold
# 
# We can find the minimum, mean, and maximum value of pixels within the water mask using the following functions which **ignore NaN values** when computing statistics.

# In[88]:


np.nanmin(water_mask), np.nanmean(water_mask), np.nanmax(water_mask)


# ## Applying the threshold
# 
# Since we know that all values higher than the minimum NDWI value are likely to be water, we can use the minimum value to threshold our original image. Anything higher than the threshold will be classified as water, anything lower will be classified as non-water. We can do this using [`np.where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html) which assigns all elements a value depending on a condition. Here we assign a value of 1 to pixels that fufill the condition, and value of 0 for pixels that don't.

# In[112]:


classified = np.where(ndwi > np.nanmin(water_mask), 1, 0)


# In[113]:


plt.imshow(classified)


# We can compute the percentage of the image that is classified as water by dividing the sum of pixels classified as water by the total number of pixels. Note that since **non-water pixels** are classified as zero, we can just sum the values in the `classified` array. 

# In[117]:


np.sum(classified) / np.size(classified)


# 

# In[118]:


# Import shapefile
shapefile = 'data/sand.shp'
sand = gpd.read_file(shapefile)


# In[119]:


sand


# When deciding which threshold to classify water, we want to make sure we don't classify too many non-water pixels as water. So instead of using the minimum NDWI value of pixels within the water mask, we should probably use the 10th percentile (i.e. the value at which only 10% of values are **lower** than).

# In[ ]:


threshold = np.nanpercentile(water_mask, 10)


# ## Overlay analysis 
# 
# ### Zonal stats?
# 

# In[ ]:





# ## Clip a raster
