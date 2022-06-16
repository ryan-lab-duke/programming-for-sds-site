# Assignment 5

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

Write a function that checks the validity of a lon/lat pair based on their range. (i.e. longitude should be between -180 and 180, and latitude should be between -90 and 90). The function should return `False` if the pair is invalid, and `True` otherwise. The function should rely on two sub-functions `is_lon_valid` and `is_lat_valid` .


```def is_lon_valid(lon):
    # complete the function
    return
```
```def is_lat_valid(lat):
    # complete the function
    return
```

```def is_lonlat_valid(lon, lat):
    # complete the function
    return
```

### Test your function by running the following:

* a) `print(is_lat_valid(-186))`

* b) `print(is_lon_valid(45))`

* c) `print(is_latlon_valid(38.2, 0.8))`

* d) `print(is_latlon_valid(270.3, -30.6))`

*****************************
## Task 2 (5 points)

Write a function called `convert_distance` which converts between **meters** (`m`), **kilometers** (`km`), and **miles** (`mi`). It should handle all combinations. If `in_unit == out_unit`, just return the same value.

```def convert_distance(area, in_unit, out_unit):
    # valid units: 'm','km','mi'
    
    # complete the function

    return converted_distance
```

### Test your function by running the following:

* a) `print(convert_area(1000,'m','km'))`

* b) `print(convert_area(100,'mi','km'))`

* c) `print(convert_area(10,'km','mi'))`

*****************************
## Task 3 (5 points)

* a) Print the current local time in ISO 8601 standard format (i.e. YYYY-MM-DD hh:mm:ss)

* b) Convert the string `Jun 19, 2022` to ISO 8601 standard format

* c) Convert the string `2022-06-19 220755` to ISO 8601 standard format (time order is hours, minutes, seconds)

* d) What day was it in Eugene when Unix time reached 1234567890 seconds?

* e) What year will it be when Unix time reaches 2,000,000,000 seconds?

*****************************

## Task 4 (5 points)

* Add a title, your name, and date of this submission to your Jupyter Notebook using **Markdown text**.

* Add some more **Markdown text** to separate each task of this assignment. 

*****************************

```{important} Save your notebook to your local course folder and submit assignment (in **.ipynb** format) to Canvas by the deadline.
```

