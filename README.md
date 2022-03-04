# Programming for Spatial Data Science

This repository hosts the code for the online textbook, *Programming for Spatial Data Science* designed by [Johnny Ryan](https://www.johnny-ryan.com/). The textbook can be accessed at [https://owel-lab.github.io/gds-applications-site/](https://owel-lab.github.io/gds-applications-site/). 

The course...

Learning outcomes:

* Learn how think computationally and statistically

* Improve Python skills

etc. 

## Repository Structure

The Python package [`jupyter-book`](https://jupyterbook.org/intro.html#install-jupyter-book) processes the Jupyter notebook files from this repository and outputs them as the publication-quality HTML files that generate the [corresponding website](https://owel-lab.github.io/gds-applications-site/).

The HTML files are currently hidden in this branch of the GitHub repository, but you can find them in the [gh-pages branch](https://github.com/owel-lab/gds-applications-site/tree/gh-pages).

## Build

The book can be updated by running:

`jupyter-book build book/`

`ghp-import -n -p -f book/_build/html`

## Acknowledgments






