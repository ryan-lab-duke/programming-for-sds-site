# Assignment 3

If you are using the virtual environment, launch JupyterLab by clicking this button: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/owel-lab/programming-for-sds-site/HEAD)


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
array = np.array([[[178, 189, 567], [145, 239, 445], [197, 345, 678]], [[56, 78, 190], [46, 10, 11], [6, 2, 1]], [[45, 118, 203], [72, 119, 34], [87, 9, 5]]])
```

Copy and paste this array into your notebook and answer the following questions:

* a) How many dimensions does this array have?

* b) What is the mean and standard deviation of this array?

* c) How many values are less than 10?

* d) What is the **index** of the highest value? Looking for three numbers here (i.e. an index for each dimension).

```{admonition} Click to reveal hint
:class: tip, dropdown
The `np.where()` function is useful for this task.
```

* e) What is the **index** of the lowest value?

*****************************

## Task 2 (5 points)

* Define a **list** containing the names of **five** cities (as **strings**).

* Define two **NumPy arrays** (i.e. `np.array()`), one called `lat` and one called `lon`, that contain the latitudes and longitudes, respectively, of **five** global cities to **two decimal places**.

* Print the **name** and **latitude** of the most northly city using **f-string** formatting.

* Repeat for the for city with the most easterly longitude.

* Print the **mean** latitude and **mean** longitude of your five cities to **two decimal places**. 

Geographic coordinates for your cities can be found from [this website](https://www.latlong.net/). 

*****************************

## Task 3 (10 points)


* Write a for loop that **prints** each city followed by its latitude and longitude (two decimal places). 

* Write a **for loop** that converts every character of your cities to uppercase.

```{hint}
Look for the string method you need [here](https://www.w3schools.com/python/python_ref_string.asp)
```

* Write a for loop that **counts** the number of characters of each city and saves it to a new list.

* Write a for loop that prints the name of the city, only if its more northerly than the mean latitude of all your cities (i.e. `np.mean(lat)`)

### Extra credit (5 points)

* Write a for loop that counts the number of vowels in each city. 

```{admonition} Click to reveal hint
:class: tip, dropdown
The `count()` method is useful for this task.
```

*****************************
## Task 4 (5 points)

* Combine a for loop with a conditional statement that returns `True` for every city that is located in the **Northern Hemisphere** (and **False** if not).

Make a new list of containing the countries and continents of your cities.

* Combine a for loop with a conditional statement that returns `True` for every city that is **not** located in **Asia** (and **False** if not).

* Combine a for loop with a conditional statement that returns `True` for every city that is located in the **USA** (and **False** if not).

*****************************
## Task 5 (5 points)

Here is a list of daily river discharges for July.

```
discharge = np.array([0.3, 0.2, 1.6, 2.3, 0.8, 1.5, 1.5, 0.1, 2.2, 1.4,
       1.5, 1.5, 0.9, 2.2, 2.8, 2.6, 2.8, 2.8, 0.6, 2.8, 2.1, 1.0, 1.0, 
       0.3, 1.6, 0.4, 1.5, 0.2, 0.9, 1.5])
```

> Our messenger can wade across river when it is flowing at **less than** 1 cubic meter per second.

> Our messenger can boat across the river when it is flowing **between** 1 and 2 cubic meters per second.

> Our messenger cannot cross the river if it is flowing **greater than** 3 cubic meters per second.


* a) Compute how many days our messenger can travel across the river **by foot** using a **for loop and conditional statements**

* b) Compute how many days our messenger can travel across the river **by boat** using a **for loop and conditional statements**

*****************************

```{important} Save your notebook to your local course folder and submit assignment (in **.pdf** format) to Canvas by the deadline.
```

