[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/EstebanAce/adascape-intro/main?urlpath=lab)
[![Test notebooks](https://github.com/EstebanAce/adascape-intro/workflows/Test%20notebooks/badge.svg)](https://github.com/EstebanAce/adascape-intro/actions)

# Modelling biological diversity in a geological context

This repository contains a collection of [Jupyter](http://jupyter.org/)
notebooks to introduce [AdaScape](https://github.com/fastscape-lem/adascape), 
a coupled adaptive speciation and  landscape evolution model build into the [FastScape Framework](https://github.com/fastscape-lem).
This short course war part of the [CRC 1211 Training Week 2022](https://sfb1211.uni-koeln.de/index.php/irtg/tw-2022) 
and San Pedro de Atacama field school. It builds on a previous course [short-course]((https://github.com/fastscape-lem/crc-1211-short-course)) 
on the landscape evolution modelling framework FastScape
for the CRC-1211 taught by [Jean Braun](https://github.com/jeanbraun) 
with the help of [Benoît Bovy](https://github.com/benbovy).

- [How to run the notebooks?](#how-to-run-the-notebooks)
    - [Run in the cloud (Binder)](#run-in-the-cloud-binder)
    - [Install and run locally (Conda)](#install-and-run-locally-conda)
    
## How to run the notebooks?

### Run in the cloud (Binder)

You can run the notebooks in your browser without installing anything thanks to
[binder](https://mybinder.org/). Just follow the link below or click on the
"launch binder" badge above and it will launch remotely a new notebook server
for you:

- [Run on binder](https://mybinder.org/v2/gh/EstebanAce/crc1211-tw2022/main?urlpath=lab)

This service is for demo purpose only, do not rely on it for doing more serious
work.

### Install and run locally (Conda)
Assuming that you have `git` and [conda](https://conda.io/docs/index.html)
installed, you can install all the packages required to run the notebooks in a
new conda environment using the following commands:

```bash
$ git clone https://github.com/EstebanAce/adascape-intro
$ cd adascape-intro
$ conda env create -f environment.yml
$ conda activate adascape-intro
```

Note: you could use [mamba](https://github.com/mamba-org/mamba) instead of
`conda`. `mamba` is a faster alternative to `conda`.

Note: If you have a new Mac with an M1 processor. FastScape has not been ported 
to this architecture yet. So you will need to install the intel version. This means that you
need to install the intel version of all other necessary packages in your environment.
For this, you need to change the command:

```bash
$ conda env create -f environment.yml
```

to:

```bash
$ CONDA_SUBDIR=osx-64 conda env create -f environment.yml
```

Finally run the command below to start the Jupyterlab application. It should
open a new tab in your browser.

```bash
$ jupyter lab
```

## How to contribute?

Your contribution is welcome! Your can do so by reporting issues, suggesting new
notebook examples or improvements to the current examples.

A few extra steps are required to prepare your contributions. You can first
update the conda environment using the following command:

```bash
$ conda env update -n adascape-intro --file environment-dev.yml 
```

This installs a few additional packages like
[pre-commit](https://pre-commit.com/), which is used to ensure that all notebook
cell outputs are cleared before adding or updating notebooks in this git
repository. Run the command below to enable pre-commit (you only need to do this
once):

```bash
$ pre-commit install
```

The script below is useful if you want to ensure that all notebooks are running
without error:

```bash
$ python execute_all_notebooks.py
```

This script (as well as a script to build the Docker image) is run each time you
open or update a pull-request on GitHub.