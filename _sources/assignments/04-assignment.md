# Assignment 4

If you are using the virtual environment, launch JupyterLab by clicking this button: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/owel-lab/programming-for-sds-site/HEAD)

<!-- #region -->
If you have installed Python locally, launch JupyterLab by running:

```
conda activate sds
```
and
```
jupyter lab
```

```{attention}
Print all answers in a human-readable way using **f-string** formatting.
```


```{image} images/world_map.png
:alt: world
:width: 800px
:align: center
```

*****************************
## Task 1 (5 points)

Download the `world_bank_data.csv` from [here](https://www.dropbox.com/s/fzmwei67w02dlhv/world_bank_data.csv?dl=0). Read the dataset using `Pandas` and answer the following questions:

* a) How many rows and columnns are in this table?

* b) What are the column names?

* c) What the column data types?

* d) Which country has the highest GNI per capita?

* e) Which country has the lowest population density?

*****************************

## Task 2 (5 points)

Answer the following questions:

* a) What is the **mean** GDP for this table?

* b) What is the most populous country in **Melanesia**?

* c) How many countries have a *GNI per capita* of between 5,000 and 6,000 USD?

* d) Which of the **ten most populous** countries in the world has the highest population density?

* e) What is the **mean** GDP of countries in North Africa?

*****************************

## Task 3 (5 points)

Produce a new DataFrame that groups the countries into regions and answer the following questions:

```{admonition} Click to reveal hint
:class: tip, dropdown
`count()` is useful for this task.
```

* a) Which region has the highest **mean** GNI per capita?

* b) Which **three** regions have the lowest GDP?

```{admonition} Click to reveal hint
:class: tip, dropdown
`sort_values()` and `head()` is useful for this task.
```

* c) Which **five** regions have the highest population density?

* e) What is the total population of South-eastern Asia?

*****************************
## Task 4 (5 points)

Write a `for` loop which saves the first letter of each country in a new list called `first_letter`. Add this list as a new column in the original DataFrame (i.e. `df['first_letter'] = first_letter`).

* a) What is the most common first letter of countries in this table?

* b) After grouping by their first letter, countries with which first letter have the highest total *GDP*?
<!-- #endregion -->

*****************************

```{important} 
Save your notebook to your local course folder and submit assignment (in **.pdf** format) to Canvas by the deadline.
```
