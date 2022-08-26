# Assignment 8

If you are using the virtual environment, launch JupyterLab by clicking this button: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/owel-lab/programming-for-sds-site/HEAD).


If you have installed Python locally, launch JupyterLab by running:

```
conda activate sds
```
and
```
jupyter lab
```

```{attention}
Print all answers (except Task 3 and 4) in a human-readable way using **f-string** formatting.
```

```{image} images/projections.png
:alt: projections
:class: bg-primary mb-1
:width: 600px
:align: center
```

*****************************


## Task 1 (5 points)

Download the data for the assignment [here](https://www.dropbox.com/s/0oawhe0niq69nph/world_countries.zip?dl=0). This dataset contains the geographic boundaries for all countries in the world, along with attribute data about country population, gross domestic product, and economy. If you are interested, the data were downloaded from [here](https://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-admin-0-countries-2/). 

Read the data using `GeoPandas` and answer the following questions:

* a) How many rows and columnns are in this dataset?

* b) How many numeric columns are in this dataset?

* c) What is the **name** of the coordinate reference system? And what are the units?

*****************************

## Task 2 (5 points)

> Drop any countries that have a GDP (`GDP_MD`) or population (`POP_EST`) of **zero** or **-99** from this `GeoDataFrame`.

* a) Print a list of the top 10 countries by GDP. Use the `ADMIN` column to report country name.

* b) Print a list of the top 10 countries by population

> Add a new columm called **GDP_per_capita** using the GDP in million dollars (`GDP_MD`) and population (`POP_EST`) columns. 

* c) What are the five countries with the lowest GDP per capita? 

*****************************

## Task 3 (5 points)

Reproject and plot the data (using `plot()`) in the following coordinate reference systems. Projections can be found here: https://epsg.io/. 

* a) Bonne (EPSG:54024)

* b) Gall Stereographic (EPSG:54016)

* c) Eckert VI (EPSG:54010)

*****************************

## Task 4 (5 points)

* Make a new `GeoDataFrame` containing only the countries in Africa. 

* Reproject to **Albers Equal Area Conic** (https://epsg.io/102022). 

* Calculate the **area** of each country.

* Make a chloropleth map showing population density (i.e. population per km$^2$). 

*****************************

## Task 5 (5 points)

List the countries that are within 1,000 **miles** of the **centroid** of Nepal. 

*****************************

```{important} 
Save your notebook to your local course folder and submit assignment (in **.ipynb** format) to Canvas by the deadline.
```


























