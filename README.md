[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/EstebanAce/crc1211-tw2022/main?urlpath=lab)
[![Test notebooks](https://github.com/EstebanAce/crc1211-tw2022/workflows/Test%20notebooks/badge.svg)](https://github.com/EstebanAce/crc1211-tw2022/actions)

# Modelling biological diversity in a geological context

This repository contains a collection of [Jupyter](http://jupyter.org/)
notebooks to introduce two adaptive speciation models coupled with 
the landscape evolution model [Fastscape](https://github.com/fastscape-lem).
This short course is part of the [CRC 1211 Training Week 2022](https://sfb1211.uni-koeln.de/index.php/irtg/tw-2022) 
and builds on a previous [short-course]((https://github.com/fastscape-lem/crc-1211-short-course)) 
on the landscape evolution modelling framework Fastscape
for the CRC-1211 taught by [Jean Braun](https://github.com/jeanbraun) 
with the help of [Benoît Bovy](https://github.com/benbovy).

- [How to run the notebooks?](#how-to-run-the-notebooks)
    - [Run in the cloud (Binder)](#run-in-the-cloud-binder)
    - [Install and run locally (Docker)](#install-and-run-locally-docker)
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

### Install and run locally (Docker)
[Docker](https://www.docker.com/) images are built automatically for this
repository. Those images provide the whole computing environment, pre-installed
and pre-configured for running the notebooks. The only requirement is to
have Docker installed on your machine. It is available on all platforms
Linux/Windows/Mac and it can be installed from the Docker website or using one
of your platform's package managers.

First install and run docker. Then open a terminal and 
run the command below to first pull the latest image 
with the course material:

```bash
$ docker pull EstebanAce/crc1211-tw2022:latest
```

Then run the command below to start the Jupyterlab application from the Docker
container. Replace `crc1211-tw2022` by any other name you want to
give to your local container (optional). Also Replace
`/path/to/local-notebook-folder` by the full path to the directory on your
machine where you want to create/copy, edit and permanently store notebooks for
this training course.

```bash
$ docker run \
    -it \
    --name crc1211-tw2022 \
    -p 8888:8888 \
    -v /path/to/local-notebook-folder:/home/jovyan/my-local-folder \
    fastscape/crc1211-tw2022 \
    jupyter lab --ip 0.0.0.0
```

You can then enter in your browser the url and token provided to start using the
Jupyterlab application.

You may want to copy the `notebooks` folder in your local working folder mounted
in the docker container as `my-local-folder`. Open a terminal in Jupyterlab and
run the following command:

```bash
$ cp -R notebooks my-local-folder/
```

When you are done you can stop and remove the container:

``` bash
$ docker stop crc1211-tw2022
$ docker rm crc1211-tw2022
```

#### Troubleshooting

*The url I entered in my browser doesn't point to Jupyterlab*

You may already have another application running on localhost using the port
`8888`. Try another port when running the `docker run` command above, e.g.,
using `-p 8889:8888`. You also need to change the port in the entered url
accordingly (e.g., `localhost:8889`).

*The url I entered in my browser gives a page asking for a token*

Copy and paste the token given in the url. If the token is invalid, you may have
another Jupyterlab application already running on your machine. Try using
another port as described above.

Check [Docker's documentation](https://docs.docker.com/) for additional command
line help and options.

### Install and run locally (Conda)
Assuming that you have `git` and [conda](https://conda.io/docs/index.html)
installed, you can install all the packages required to run the notebooks in a
new conda environment using the following commands:

```bash
$ git clone https://github.com/EstebanAce/crc1211-tw2022
$ cd crc1211-tw2022
$ conda env create -f environment_eat.yml
$ conda activate crc1211-tw2022
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
$ conda env update -n crc1211-tw2022 --file environment-dev.yml 
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