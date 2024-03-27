# Assignment 10

If you are using the virtual environment, launch JupyterLab by clicking this button: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/owel-lab/programming-for-sds-site/HEAD).


If you have installed Python locally, launch JupyterLab by running:

```
conda activate sds
```
and
```
jupyter lab
```

```{image} images/mowich_glacier.jpg
:alt: mowich
:class: bg-primary mb-1
:width: 600px
:align: center
```

*****************************

## Task 1 (15 points)

Download elevation data for Mt Rainier [here](https://www.dropbox.com/s/ej4rdh93qkhlyj7/N46W122.tif?dl=0) and a shapefile containing the outlines of the major glaciers [here](https://www.dropbox.com/sh/oxk2gs8uuuhvbuf/AACruLfktDICu8PxMZ6wKqoka?dl=0). The shapefile is from the [Global Land Ice Measurements from Space (GLIMS) project](https://www.glims.org/) which has mapped the extent of all glaciers on Earth. 

* a) Which are the five largest glaciers by **area**?

* b) Which five glaciers have the **highest mean** elevation?

* c) Which five glaciers have the **highest minimum** elevation?

* d) Which five glaciers span the most elevation (i.e. difference between maximum and minimum elevation)? 

*****************************

## Task 2 (15 points)

Download the Landsat data from [here](https://www.dropbox.com/sh/k3bkxwa2j9fovta/AADX4yZiIAEHiG9VPcyCON2pa?dl=0).

* a) Compute a [Normalized Difference Vegetation Index](https://www.usgs.gov/landsat-missions/landsat-normalized-difference-vegetation-index) using bands 4 and 5. 

* b) Compute a [Normalized Difference Moisture Index](https://www.usgs.gov/landsat-missions/normalized-difference-moisture-index) using bands 5 and 6.

* c) Find the area of water in the **NDWI** image.

* d) Find the area of sand in **Band 1** image 

* e) Calculate the area of **healthy vegetation** and **non-vegetation** in the **NDVI** image. Note that you may need to subtract the sand and water pixels from non-vegetation classification - a pixel should only have one land cover. 

* f) Compute the area of all four land covers in $km^{2}$.


*****************************

```{important}
Save your notebook to your local course folder and submit assignment (in **.pdf** format) to Canvas by the deadline.
```
