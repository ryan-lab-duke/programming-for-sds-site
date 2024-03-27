# Assignment 3

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

Write a **for loop** that converts this list of vegetables from uppercase to lowercase.

```
veggies = ['LETTUCE', 'CARROT', 'PEA', 'CABBAGE']
```

```{hint}
Look for the string method you need [here](https://www.w3schools.com/python/python_ref_string.asp)
```
*****************************
## Task 2 (5 points)

Produce a variable containing only the **strings** in this list using a for loop and conditional statements

```
shopping_list = ['Lettuce', 'Carrots', 'Bananas', 4, 10, 'Potatoes']
```

```{admonition} Click to reveal hint
:class: tip, dropdown
The `type()` function is useful for this task.
```

*****************************
## Task 3 (5 points)

Write a for loop that counts the number of vowels in the sentence below.

```
vowels = 'aeiouAEIOU'

sentence = 'Please leave the package by the back door'
```

```{admonition} Click to reveal hint
:class: tip, dropdown
The `.count()` method is useful for this task.
```

*****************************
## Task 4 (5 points)

```
city = 'Eugene'
country = 'USA'
number_months = 7
max_monthly_temp = 66.9
```

Write a conditional statement that returns `True` if Eugene is a city in the USA.

*****************************
## Task 5 (5 points)

A "cool-summer Mediterranean climate" is defined as having warm and dry summers. In this climate classification, more than four months should have average temperatures of 50 F or higher (`number_months`) **and** no average monthly temperatures should exceed 72 F (`max_monthly_temp`).

* a) Write a conditional statement that returns `True` if Eugene has a cool-summer Mediterranean climate.

```
city = 'Porto'
country = 'Portugal'
number_months = 11
max_monthly = 69.4
```

* b) Write a conditional statement that returns `True` if **Porto** has a cool-summer Mediterranean climate.

*****************************
## Task 6 (5 points)

Here is a list of daily river discharges for July.

```
discharge = np.array([0.3, 0.2, 1.6, 2.3, 0.8, 1.5, 1.5, 0.1, 2.2, 1.4,
       1.5, 1.5, 0.9, 2.2, 2.8, 2.6, 2.8, 2.8, 0.6, 2.8, 2.1, 1.0, 1.0, 
       0.3, 1.6, 0.4, 1.5, 0.2, 0.9, 1.5])
```

> Our messenger can wade across river when it is flowing at **less than** 1 cubic meter per second.

> Our messenger can boat across the river when it is flowing **between** 1 and 2 cubic meters per second.

> Our messenger cannot cross the river if it is flowing **greater than** 3 cubic meters per second.


* a) Compute how many days our messenger **can travel** across the river using a **for loop and conditional statements**


* b) Compute how many days our messenger **cannot travel** across the river using **NumPy**

*****************************

```{important} Save your notebook to your local course folder and submit assignment (in **.pdf** format) to Canvas by the deadline.
```

