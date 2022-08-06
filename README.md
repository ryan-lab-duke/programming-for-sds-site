# Programming for Spatial Data Science

This repository hosts the code for the online textbook, **Programming for Spatial Data Science** designed by [Johnny Ryan](https://www.johnny-ryan.com/). The textbook can be accessed at [https://owel-lab.github.io/programming-for-sds-site/](https://owel-lab.github.io/programming-for-sds-site/). 

The goal of this course is to introduce students to basic programming concepts in Python and apply these skills to various geospatial problems. There are no pre-requisites and students do not need any previous programming experience. Each week we will have a short lecture that introduces a new topic. In the following assignment, students will apply these new concepts to solve common tasks involving geospatial data. During this course, students will become familiar with the main Python packages used for importing, analyzing, and visualizing geospatial data.

### Learning outcomes:

* Acquire basic Python coding skills

* Implement common programming techniques (e.g. conditional statements, loops, functions).

* Become familiar with object-oriented programming

* Identify common geospatial data formats and appropriate Python packages to work with them

* Perform basic data analysis on table, vector, and raster data

* Visualize different types of data using Python

* Recognize the importance of open-source software

## Repository Structure

The Python package [`jupyter-book`](https://jupyterbook.org/intro.html#install-jupyter-book) processes the Jupyter notebook files from this repository and outputs them as the publication-quality HTML files that generate the [corresponding website](https://owel-lab.github.io/programming-for-sds-site/).

The HTML files are currently hidden in this branch of the GitHub repository but can be found in the [gh-pages branch](https://github.com/owel-lab/programming-for-sds-site/tree/gh-pages).

## Build

The book can be updated by running:

`jupyter-book build book/`

`ghp-import -n -p -f book/_build/html`

## Acknowledgments

This course was inspired by course material designed by [Melanie Walsh](https://melaniewalsh.github.io/Intro-Cultural-Analytics/welcome.html), [David Shean](https://github.com/UW-GDA/gda_course_2021), and the [University of Helsinki](https://geo-python-site.readthedocs.io/en/latest/). 





