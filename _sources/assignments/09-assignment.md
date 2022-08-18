# Assignment 9

If you are using the virtual environment, launch JupyterLab by clicking this button: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/owel-lab/programming-for-sds-site/HEAD).


If you have installed Python locally, launch JupyterLab by running:

```
conda activate sds
```
and
```
jupyter lab
```

*****************************

## Task 1 (4 points)

Download the data for the assignment from [here](https://www.dropbox.com/sh/zop198jg5dksrgv/AACKuC1KjASxVTrix3FfOR-ja?dl=0). This is [WorldClim](https://www.worldclim.org/) version 2.1 **monthly precipitation data** averaged across the 1970-2000 period. The spatial resolution is **2.5 minutes** (around 21 km<sup>2</sup> at the equator). The numbers in the file name represent the month of the year (January is `01`; December is `12`).

Read in the January precipitation data (i.e. `wc2.1_2.5m_prec_01.tif`) and answer the following questions:

* a) How many rows and columns does this raster have?

* b) What is the coordinate reference system? 

* c) What is the data type?

* d) What value represents **NoData**

*****************************

## Task 2 (8 points)

Mask the **NoData** values and answer the following questions about the January precipitation data:

* a) Which row/column index represents the highest precipitation?

* b) Which row/column index represents the lowest precipitation? 

* c) What is the longitude/latitude of the highest precipitation? 

* d) What is the longitude/latitude of the lowest precipitation?

* e) What is the precipitation at grid cell index `1500`, `1200`?

* f) What is the precipitation at **87.8 E, 54.8 N**?

* g) What is the precipitation at **-5.1 N, 24.7 E**?

* h) What is the precipitation at **46.4 N, -106.8 E**?

*****************************

## Task 3 (5 points)

Read in the July precipitation data (i.e. `wc2.1_2.5m_prec_07.tif`, mask the **NoData** values, and provide the **longitude/latitude** for the following:

* a) Location with the largest absolute difference between January vs. July precipitation.

* b) Location with the smallest absolute difference between January vs. July precipitation?

* c) Location with the largest combined January and July precipitation?

*****************************

## Task 4 (3 points)

* a) Make a plot showing the **mean annual precipitation** for the world (i.e. by averaging over all twelve files).

```{admonition} Click to reveal hint
:class: tip, dropdown
Remember to specify the axis when using [`np.nanmean`](https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html). 
```

* b) Compute the **standard deviation** of precipitation across all twelve files and make a plot showing new variable. 

```{admonition} Click to reveal hint
:class: tip, dropdown
Consider using [`np.nanstd`](https://numpy.org/doc/stable/reference/generated/numpy.nanstd.html). 
```

*****************************

## Task 5 (5 points)

Download the Landsat data from [here](https://www.dropbox.com/sh/k3bkxwa2j9fovta/AADX4yZiIAEHiG9VPcyCON2pa?dl=0) and display the following:

* a) a [Normalized Difference Moisture Index](https://www.usgs.gov/landsat-missions/normalized-difference-moisture-index) image (i.e. (Band 5 - Band 6) / (Band 5 + Band 6))

* b) a [color infrared composite](https://www.usgs.gov/media/images/common-landsat-band-rgb-composites) (i.e. bands 5, 4, 3) with a percentile stretch.

* c) a [false color composite](https://www.usgs.gov/media/images/common-landsat-band-rgb-composites) (i.e. bands 7, 5, 3) with a percentile stretch.

*****************************

```{important}
Save your notebook to your local course folder and submit assignment (in **.ipynb** format) to Canvas by the deadline.
```

