# Assignment 6


If you have installed Python locally, launch JupyterLab by running:

```
conda activate sds
```

and

```
jupyter lab
```

## Plotting weather station data

In this activity, we will use `Pandas` and `Matplotlib` to make some visually-appealing plots of meteorological data which was collected by a weather station installed at Hayden Glacier in the Oregon Cascades. The data can be downloaded [here](https://www.dropbox.com/scl/fi/e69nmu4ywewlqd4kuo96t/hayden-glacier-aws-data-daily.csv?rlkey=pnoip8gcp0582ar4tewilhx9t&st=c9kfslby&dl=0). This dataset is similar to the one we used back in Week 3. Although this time, all the data have been provided as a **.csv** file. The dataset includes the following variables: pressure (mbar), solar radiation (W/m2), air temperature (C), relative humidity (%), wind speed (m/s), gust speed (m/s), wind direction (degrees), and rainfall (mm).  

```{image} images/aws.jpg
:alt: aws
:width: 600px
:align: center
```


*****************************

## Task 1 (10 points)

Read the data and answer the following questions:

* a) What time period does the data represent?

* b) Plot one variable using **pyplot style** (i.e. `plt.plot()`), including axis labels, a gridded background, and customized linestyle, linewdith, and color.

* c) Plot another variable, this time using the **object-oriented style** (i.e. `ax.plot()`), including axis labels, a gridded background, and customized linestyle, linewdith, and color.

* d) Make a multi-panel figure with two rows and one column that plots two different variables (one variable in each). Customize these plots again to include axis labels, a gridded background, and customized linestyle, linewdith, and color. This time, also add a legend. 

* Bonus point: 

*****************************

## Task 2 (10 points)

* a) Read the data again but, this time, parse the dates and make `Datetime` the index column. Print the first five rows to show your new DataFrame.

* b) Make a plot showing **air temperature** with a figure size 10 x 4 inches. 

* c) Format the x-axis labels as month day (i.e. Aug 10).

* d) Add a horizontal line to the figure that represents the **mean** air temperature

* e) Add a label to the horizontal line that says "mean = X F" where `X` is the mean air temperature in **Fahrenheit**.

* f) Add an arrow that points to the lowest air temperature value that says "lowest value"

* g) Add an arrow that points to the highest air temperature value that says "highest value"

* h) Limit the x-axis from Jul 02 to Sep 30. 

```{note} 
We will be taking points off if any of the labels are outside of the figure panel. We will also give bonus points to plots that are nicely formatted.
```

*****************************

## Task 3 (5 points)

* a) Make a four panelled figure with two columns and two rows. In each panel, show the relationship between two variables (i.e. a **scatterplot**).

* b) Annotate the figure so that each panel is labelled (a), (b), (c), and (d). 

* c) Label the y-axes of each panel. Label only the x-axes of panels (c) and (d)

* d) Customize the size and facecolors of the dots in the plots.

* e) Add a grid to each panel.

*****************************

```{important} 
Save your notebook to your local course folder and submit assignment (in **.pdf** format) to Canvas by the deadline.
```

































