#!/usr/bin/env python
# coding: utf-8

# # Sampling raster data
# 
# Many GIS tasks involve both raster and vector data. In this demo, we have a shapefile containing the coordinates of four campsites in Mt. Rainier and we want to extract the elevation from a corresponding raster file (that was introduced in [Week 9](../demos/09a-demo.ipynb).

# In[132]:


import rasterio
from rasterio.mask import mask
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

# Import raster 
src = rasterio.open('data/N46W122.tif')
elevations = src.read(1)

# Import shapefile
campsites = gpd.read_file('data/campsites.shp')


# ## Check coordinates
# 
# Before we can extract the elevation values beneath the points, we must check that the two datasets have the same coordinate reference system. 

# In[81]:


campsites.crs


# In[82]:


src.crs


# It looks they are both projected in **WGS84 (EPSG:4325)** so we can move onto the next step.

# ## Plot

# In[138]:


# Plot data
fig, ax = plt.subplots(figsize=(8,8))
im = ax.imshow(elevations)
ax.set_title("Mt Rainier and Mt Adams", fontsize=14)
cbar = fig.colorbar(im, orientation='vertical')
cbar.ax.set_ylabel('Elevation', rotation=270, fontsize=14)
cbar.ax.get_yaxis().labelpad = 20


# ## Sampling the data
# 
# `Rasterio's` [`sample`](https://rasterio.readthedocs.io/en/latest/api/rasterio.sample.html) function expects a list of x, y coordinate pairs so we need to convert our `geometry` column using list comprehension. 

# In[84]:


coord_list = [(x,y) for x,y in zip(campsites['geometry'].x , campsites['geometry'].y)]
coord_list


# Now we can carry out the sample and store the results in new column called **elevation**. Note that if the image has more than one band, a value is returned for each band.

# In[85]:


campsites['elevation'] = [x for x in src.sample(coord_list)]
campsites.head()


# ## Buffer points
# 
# Sometimes it might be a little risky to sample only one cell per point. There may be errors or artifacts in the unerlying raster. A more robust method would be to sample multiple raster grid cells surrounding a point. To do this we could **buffer** the points by a set distance and sample the raster values again.  
# 
# `GeoPandas` has a method called [`buffer`](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.buffer.html) which expects a **distance** around each object. Since our shapefile is in WGS84 coordinate system, this distance would have to be in **degrees** which is a little confusing. A better option would be to reproject our shapefile so we can enter a buffer distance in **meters**. 

# In[86]:


campsites_utm = campsites.to_crs('EPSG:32610')
campsites_utm['buffer'] = campsites_utm.buffer(500)
campsites_utm


# Now we have two columns containing **geometry** values. But a `GeoDataFrame` can only have one active geometry. Since we intend to use our buffer geometry to sample the raster data, we will make our **buffer** column the active geometry.

# In[91]:


campsites_utm.set_geometry('buffer', inplace=True)


# We have to convert the DataFrame back to WGS84 so it has the same projection system as our raster data.

# In[92]:


campsites = campsites_utm.to_crs('EPSG:4326')


# To sample raster grid cells within polygons (rather than points) we use another `Rasterio` function called [`mask.mask`](https://rasterio.readthedocs.io/en/latest/api/rasterio.mask.html#). This function has a few arguments. The first is the raster dataset (i.e. `src` in our case). The second argument is the shape to mask. In the docs, it notes that the shapes must be:
# 
# > a GeoJSON-like dict or an object that implements the Python geo interface protocol (such as a Shapely Polygon)"
# 
# So we will have to specify only the **geometry** of our `GeoPandas` DataFrame, not the DataFrame object itself. The **Invert** argument determines whether pixels inside or outside shapes will be masked. The **nodata** argument allows us to set the no data value (i.e. values of pixels outside the mask). 

# In[100]:


campsite_mask, transform = mask(src, campsites.geometry, invert=False, nodata=0)


# Now when we plot our data, we should see four small dots that represent elevation values within 500 m of the campsites. All other elevation values are assigned a no data values. 

# In[101]:


plt.imshow(campsite_mask[0,:,:])


# ## Regionprops
# 
# The challenge is to extract the values of grid cells within the buffer. 

# In[157]:


from skimage.measure import label


# Convert to binary array (i.e. ones and zeros)

# In[112]:


campsites = np.where(campsite_mask[0,:,:] > 0, 1, 0)


# Label image

# In[116]:


label_img = label(campsites)


# Print unique labels

# In[117]:


np.unique(label_img)


# In[140]:


elevations[label_img == 0].shape


# In[141]:


elevations[label_img == 1].shape


# In[126]:


elevations[label_img == 1].mean(), elevations[label_img == 1].std()


# In[127]:


elevations[label_img == 2].mean(), elevations[label_img == 2].std()


# In[128]:


elevations[label_img == 3].mean(), elevations[label_img == 3].std()


# In[129]:


elevations[label_img == 4].mean(), elevations[label_img == 4].std()


# In[149]:




np.argwhere(label_img == 1)


# In[155]:


rasterio.transform.rowcol(src.transform, campsites['geometry'].x[0], campsites['geometry'].y[0]) in np.argwhere(label_img == 1)


# In[152]:


campsites['geometry']., campsites['geometry'].y[0]


# In[156]:


campsites


# It got a little messy at the end there but that's par for the course in geospatial analysis. 

# In[ ]:




