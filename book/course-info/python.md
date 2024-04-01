# Install Python (optional)

You are welcome to install Python on your own computer. In order to do this, you will need to install a Python distribution with the necessary packages. We recommend using `conda`, an open-source package management system which can be installed using Miniconda (a lightweight version of [Anaconda](https://www.anaconda.com/products/individual)). 

## Install Miniconda

The latest version of Miniconda can be accessed from the [dowload page](https://docs.conda.io/en/latest/miniconda.html). Download the corresponding package for your operating system.

## Test installation

After installation is complete, you can test that the package manager `conda` works by opening an **Anaconda Prompt (miniconda3)** (Windows) or **Terminal** (Mac). 

In the command prompt (or Terminal) run the following:
```
conda --version
```

If the command returns a version number of conda (e.g. `conda 4.11.0`) everything is working correctly.

## Create course environment

The Python libraries needed for this course can be installed using an `environment.yml` file which can be downloaded from [here](https://www.dropbox.com/s/vq6yf1acpypdrf2/environment.yml?dl=0). 

You can install `environment.yml` by opening an Anaconda Prompt (Windows) or Terminal (Mac), navigating to the file (i.e. `cd Downloads/`) and running the following command:

```
conda env create -f environment.yml
```

````{margin}
```{note}
More information about managing environments can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
```
````

This will take some time so we recommend doing this before lab. But, if all goes well, you will have a new environment called `sds`. To activate this environment, type:

```
conda activate sds
```

Now launch `JupyterLab` by typing:

```
jupyter lab
```

Once launched, we can follow the instructions [here](../course-info/getting-started.ipynb) to make a new Jupyter Notebook, save it, and submit it on Canvas. The benefits of this approach are that this JupyterLab environment is permanent so it can be accessed without internet connection and will **not** shutdown after periods of inactivity.

