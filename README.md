# Programming for Spatial Data Science

This repository hosts the code for the online textbook **Programming for Spatial Data Science** designed by [Johnny Ryan](https://www.johnny-ryan.com/). 

## Repository Structure

The Python package [`jupyter-book`](https://jupyterbook.org/intro.html#install-jupyter-book) processes the Jupyter notebook files from this repository and outputs them as the publication-quality HTML files that generate the [corresponding website](https://cleo-lab.github.io/programming-for-sds-site/).

The HTML files are currently hidden in this branch of the GitHub repository but can be found in the [gh-pages branch](https://github.com/cleo-lab/programming-for-sds-site/tree/gh-pages).

## Build

The book can be updated by running:

`jupyter-book build book/`

`ghp-import -n -p -f book/_build/html`

## Acknowledgments

This course was inspired by course material designed by [Melanie Walsh](https://melaniewalsh.github.io/Intro-Cultural-Analytics/welcome.html), [David Shean](https://github.com/UW-GDA/gda_course_2021), and the [University of Helsinki](https://geo-python-site.readthedocs.io/en/latest/). 

## License

This book is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/).





