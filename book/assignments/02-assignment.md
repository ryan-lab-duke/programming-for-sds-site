# Assignment 2

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

## Task 1 (5 points)

```
array = np.array([[6, 7, 4, 9, 0, 4, 2, 3, 8, 2],
       [2, 3, 2, 0, 4, 8, 7, 7, 9, 2],
       [0, 4, 9, 3, 9, 7, 0, 1, 1, 1],
       [5, 7, 3, 5, 0, 1, 7, 0, 5, 9],
       [3, 3, 10, 8, 4, 6, 2, 0, 6, 4],
       [5, 5, 2, 1, 6, 1, 4, 8, 3, 1],
       [7, 7, 9, 9, 1, 3, 5, 6, 7, 3],
       [9, 0, 7, 9, 5, 2, 9, 3, 6, 1],
       [1, 2, 4, 0, 6, 7, 4, 2, 8, 8],
       [4, 6, 7, 9, 5, 4, 9, 1, 1, 7]])
```

Copy and paste this 2D array into your notebook and answer the following questions:

* a) How many rows and columns does this array have?

* b) What is the mean and standard deviation of this array?

* c) How many values are equal to 0?

* d) How many values are greater than 7?

* e) What is the mean value of the seventh row?


*****************************

## Task 2 (5 points)

* a) Calculate the Euclidean distance between Point A (10 E, 10 N) and Point B (30 E, 30 N) using NumPy and the following formula.

$$
  distance = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

```{admonition} Click to reveal hint
:class: tip, dropdown
Consider using `np.sqrt` and `np.square`.
```

* b) Calculate the Euclidean distance between Los Angeles (385213 E, 3768641 N) and Eugene (493046 E, 4877663 N) **in kilometers**.

```{hint}
The units of the coordinates are in meters.
```

Print both your answers in a human-readable way using **f-string** formatting.

*****************************

## Task 3 (5 points)

* Define two **NumPy arrays** (i.e. `np.array()`), one called `lat` and one called `lon`, that contain the latitudes and longitudes, respectively, of **five** global cities.

* Define a **list** containing the corresponding names of the cities (as **strings**).

* Print both the **name** and **latitude** of the most northly city using **f-string** formatting.

* Repeat for the for city with the most easterly longitude.

* Print the **mean** latitude and **mean** longitude of your five cities. 

Geographic coordinates for your cities can be found from [this website](https://www.latlong.net/). 


*****************************

## Task 4 (5 points)

```
array = np.array([[[178, 189, 567], [145, 239, 445], [197, 345, 678]], [[56, 78, 190], [46, 10, 11], [6, 2, 1]], [[45, 118, 203], [72, 119, 34], [87, 9, 5]]])
```

Copy and paste this array into your notebook and answer the following questions:

* a) How many dimensions does this array have?

* b) What is the mean and standard deviation of this array?

* c) How many values are less than 10?

* d) What is the **index** of the highest value?

* e) What is the **index** of the lowest value?

*****************************
## Task 5 (5 points)

* Add a title, your name, and date of this submission to your Jupyter Notebook using **Markdown text**.

*****************************

```{important} 
Save your notebook to your local course folder and submit assignment (in **.ipynb** format) to Canvas by the deadline.
```






