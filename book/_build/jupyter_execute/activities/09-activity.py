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
# ## Remote sensing in Python
# 
# ## Task 1 (10 points)
# 
# * a) Download the Landsat data from [here](https://www.dropbox.com/sh/k3bkxwa2j9fovta/AADX4yZiIAEHiG9VPcyCON2pa?dl=0).
# 
# * b) Read each band (i.e. `src1 = rasterio.open(files[0])`) and scale the values between 0 and 1 by dividing by the maximum value of a 16-bit integer (i.e. `band1 = src1.read(1) / 65536`).
# 
# * c) Compute all eight of the spectral indices on [this website](https://www.usgs.gov/landsat-missions/landsat-surface-reflectance-derived-spectral-indices). For each index, make a plot (with a colorbar and a different colormap for each one) to show your answers.
# 
# ```{note}
# Note that the images we are using are from **Landsat 8**.
# ```
# 
# ```{important} 
# Save your notebook to your local course folder and submit assignment (in **.pdf** format) to Canvas by the deadline.
# ```
# 
