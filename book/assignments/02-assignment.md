# Assignment 2

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

In your new Jupyter Notebook, write some **Python code** that returns the following:

* a) a variable named `willamette` that contains the length of the Willamette River (187 miles) **in kilometers**

* b) a variable named `mckenzie` that contains the length of the McKenzie River (145 km) **in miles**

* c) a variable named `combined` that contains the combined length of the Willamette and McKenzie rivers **in kilometers**

Note that we can convert from **miles** to **kilometers** by multiplying the length value by 1.609. 

*****************************

## Task 2 (5 points)

Write some **Python code** that prints the **data types** of the following variables:

```
a) city = 'Eugene'

b) distance = 10.5

c) coins = 3

d) beans = '3.0'

e) time = 14.32
```
*****************************

## Task 3 (5 points)

Here is a list of apple varieties:

```
apples = ['empire', 'fuji', 'pink lady', 'gala', 'golden delicious', 'granny smith', 'honeycrisp', 'mcintosh', 'red delicious', 'braeburn', 'holstein', 'cameo', 'lady alice', 'envy', 'pazazz', 'jazz', 'hidden rose', 'ambrosia', 'jonagold', 'gravenstein', 'liberty', 'winesap', 'mutsu', 'opal', 'pacific rose']
```

Copy and paste this list into your notebook and write some Python code to answer the following:

* a) How many items are in this list?

* b) Which is the seventh item in this list?

```{admonition} Click to reveal hint
:class: tip, dropdown
Remember that Python indexing starts at **zero**.
```

* c) Which is the last item in this list?

* d) After sorting alphabetically, which is fifth item in the list?

* e) After sorting reverse alphabetically, which is twelfth item in the list? 

*****************************

## Task 4 (5 points)

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

```{hint}
Remember to `import numpy as np`.
```

Copy and paste this 2D array into your notebook and answer the following questions:

* a) How many rows and columns does this array have?

* b) What is the mean and standard deviation of this array?

* c) How many values are equal to 0?

* d) How many values are greater than 7?

* e) What is the mean value of the seventh row?


*****************************

## Task 5 (5 points)

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

## Task 6 (5 points)

* Add a title, your name, and date of this submission to your Jupyter Notebook using **Markdown text**.

* Add some more **Markdown text** to separate each task of this assignment and use **f-strings** to make yours answers clear.

*****************************

```{important} 
Save your notebook to your local course folder and submit assignment (in **.pdf** format) to Canvas by the deadline.
```






