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
shopping_list = ['Lettuce', 'Carrots', 'Bananas', 4, 10, 'Fries']
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

sentence = 'Please leave the mail around the back'
```

```{admonition} Click to reveal hint
:class: tip, dropdown
The `.count()` method is useful for this task.
```

*****************************
## Task 4 (5 points)

Staying with our messenger example... here is a list of daily discharges for July.

```
discharge = np.array([0.35566225, 0.22860853, 1.61016786, 2.33536627, 0.8870465 ,
       1.59367912, 1.58019839, 0.12487782, 2.28879693, 1.46785715,
       1.55437207, 1.51479052, 0.99618413, 2.2102335 , 2.857399  ,
       2.60550631, 2.80640146, 2.88803859, 0.60201065, 2.8673259 ,
       2.17486724, 1.05056674, 1.05193519, 0.30746037, 1.64589355,
       0.42026095, 1.52437286, 0.28315257, 0.95309955, 1.5090727 ])
```

* Our messenger can wade across river when it is flowing at **less than** 1 cubic meter per second.

* Our messenger can boat across the river when it is flowing **between** 1 and 2 cubic meters per second.

* Our messenger cannot cross the river if it is flowing **greater than** 3 cubic meters per second.


* a) Compute how many days our messenger **can travel** across the river using a **for loop and conditional statements**


* b) Compute how many days our messenger **cannot travel** across the river using **NumPy**

*****************************
## Task 5 (5 points)

Something about cities and climate classification 'hot', 'mild', or 'cold' during winter

Print something like Eugene, with a mean tenperature of x is x during winter

*****************************


```{important} Save your notebook to your local course folder and submit assignment (in **.ipynb** format) to Canvas by the deadline.
```

