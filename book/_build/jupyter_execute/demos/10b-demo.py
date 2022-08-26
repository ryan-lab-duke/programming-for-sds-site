#!/usr/bin/env python
# coding: utf-8

# # Classifying raster data
# 
# In the previous week, we produced some nice looking maps of Florence from remote sensing data. We computed some band indices and learnt that positive NDWI values were likely to be associated with water (e.g lakes, rivers, ocean). 
# 
# However, we did not conduct any quantitative analysis. For example, what if someone wanted to know how much water or sand was in the image? To do this, we would first have to classify pixels that are likely to be water using a threshold. In this week, we will learn how to do this, and other quantitative analysis, by combining raster and vector data. 

# ```{image} images/dune.jpg
# :alt: dune
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```

# In[75]:


# Import modules
import numpy as np
import rasterio
from rasterio.mask import mask
import geopandas as gpd
from scipy import stats
import glob
import matplotlib.pyplot as plt


# ## Preparing the data

# In[76]:


# Define paths to data
raster = 'data/ndwi.tif'
shapefile = 'data/water.shp'

# Import raster data
src = rasterio.open(raster)
ndwi = src.read(1)

# Import shapefile
water = gpd.read_file(shapefile)


# The `ndwi.tif` is a raster file of Florence, OR containing the NDWI values we produced last week. 

# In[77]:


plt.imshow(ndwi)


# The `water.shp` file is a shapefile containing some polygons. Each polygon outlines areas of known water in the Landsat image. This shapefile could be produced using manual digitization in ArcGIS or QGIS.

# In[78]:


water.iloc[1].geometry


# Before we can extract the NDWI values that intersect the polygons, we must check that the two datasets have the same coordinate reference system. Since they are both projected in **UTM Zone 10N (EPSG:32610)** we can move onto the next step.

# In[79]:


src.crs


# In[80]:


water.crs


# ## Masking raster data using shapefile
# 
# `Rasterio` provides a function called [`mask.mask`](https://rasterio.readthedocs.io/en/latest/api/rasterio.mask.html#) for masking raster data using polygons. This function has a few arguments. The first is the raster dataset (i.e. `src` in our case). The second argument is the shape to mask. In the docs, it notes that this shape shold be a format that implements the Python geo interface protocol (such as a Shapely Polygon). 
# 
# So we will have to specify only the **geometry** of our `GeoPandas` DataFrame, not the DataFrame object itself. The **Invert** argument determines whether pixels inside or outside shapes will be masked. The **nodata** argument allows us to set the no data value (i.e. values of pixels outside the mask).

# In[81]:


water_mask, transform = mask(src, water.geometry, invert=False, nodata=np.nan)


# The `mask.mask` function returns an array where pixel values inside the mask are retained, while pixel values outside the mask are assigned a NaN value. 

# In[82]:


water_mask


# ## Determining a threshold
# 
# We can find the minimum, mean, and maximum value of pixels within the water mask using the following functions which **ignore NaN values** when computing statistics.

# In[83]:


np.nanmin(water_mask), np.nanmean(water_mask), np.nanmax(water_mask)


# ## Applying the threshold
# 
# Since we know that all values higher than the minimum NDWI value are likely to be water, we can use the minimum value to threshold our original image. Anything higher than the threshold will be classified as water, anything lower will be classified as non-water. We can do this using [`np.where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html) which assigns all elements a value depending on a condition. Here we assign a value of 1 to pixels that fufill the condition, and value of 0 for pixels that don't.

# In[84]:


classified = np.where(ndwi > np.nanmin(water_mask), 1, 0)


# In[85]:


plt.imshow(classified)


# We can compute the percentage of the image that is classified as water by dividing the sum of pixels classified as water by the total number of pixels. Note that since **non-water pixels** are classified as zero, we can just sum the values in the `classified` array. 

# In[86]:


np.sum(classified) / np.size(classified)


# ## Classify sand
# 
# Next we will classify the percentage of the image that is sand. When we first plotted the remote sensing image in [Week 9](../demos/09b-demo.ipynb), sand appeared very bright in the Band 1. First we will import a shapefile containing some sand values.

# In[8]:


# Import shapefile
shapefile = 'data/sand.shp'
sand = gpd.read_file(shapefile)
sand.iloc[1].geometry


# Next we will import the Red, Green, and Blue bands from the remote sensing image.

# In[12]:


# Define list of Landsat bands
files = sorted(glob.glob('data/landsat/*.tif'))

# Read R, G, B bands
src_1 = rasterio.open(files[0])
band_1 = src_1.read(1)


# In[13]:


# Plot dataset
fig, ax = plt.subplots(figsize=(8,8))
im = ax.imshow(band_1, cmap='gray')
ax.set_title("Band 1")
fig.colorbar(im, orientation='vertical')
plt.show()


# ## Mask the data

# In[66]:


sand_mask, transform = mask(src_1, sand.geometry, invert=False, nodata=0)


# ## Determine threshold 
# 
# Note that since our data type is not a `float` data type, we can't use `np.nan` as a no data value. So we will set our `nodata` value to `0` and mask out all values not equal (`!=`) to 0 before computing stats.

# In[67]:


sand_mask[sand_mask != 0]


# In[68]:


np.min(sand_mask[sand_mask != 0]), np.nanmean(sand_mask[sand_mask != 0]), np.nanmax(sand_mask[sand_mask != 0])


# Now we can choose a threshold and classify our image.

# In[69]:


classified = np.where(band_1 > np.min(sand_mask[sand_mask != 0]), 1, 0)
plt.imshow(classified)


# It looks like there is some sand in the lower of the image that was not classified as sand. This is probably because our threshold was too strict. Let's lower our threshold by 10%

# In[70]:


threshold = np.min(sand_mask[sand_mask != 0]) - (np.min(sand_mask[sand_mask != 0]) * 0.1)


# In[71]:


classified = np.where(band_1 > threshold, 1, 0)
plt.imshow(classified)


# This looks a bit more realistic. We can now compute the area of the image that is sand. 

# In[72]:


(np.sum(classified) / np.size(classified)) * 100


# In[74]:


np.sum(classified)

