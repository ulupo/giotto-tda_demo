![logo](https://raw.githubusercontent.com/giotto-ai/giotto-tda/master/doc/images/tda_logo.svg)

# Giotto-tda Jupyter demo

## What is it?

The purpose of this repository is to showcase the usage of the the [Giotto-tda](https://giotto-ai.github.io/gtda-docs) Python library. Have a look at our [NeurIPS workshop paper](https://openreview.net/forum?id=fjQtZJOCTXf) for more information.


## Getting started

Clone this repository on your local machine by running
```
git clone https://github.com/ulupo/giotto-tda_demo_POSTECH_MINDS.git
```
and move inside the root folder by running
```
cd giotto-tda_demo_POSTECH_MINDS
```

### If you use ``conda``

Spin up a ``conda`` virtual environment, activate it and install the required libraries:

```
conda create --name gtda_env python=3.9
conda activate gtda_env
conda install jupyter
python -m pip install -U -r requirements.txt
```

### If you use Python's ``venv``

Create and activate a Python 3 virtual environment with the in-built ``venv`` as explained in [the official Python API reference](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment). Then, from that environment, run
```
python -m pip install -U -r requirements.txt
```

### JupyterLab setup
To see the Plotly graphs in JupyterLab, some [extra steps](https://plotly.com/python/getting-started/#jupyterlab-support) might be required.


Enjoy!

## Requirements
In order to run the notebook, the following python packages are required:

- jupyter
- giotto-tda>=0.5.1
- pandas>=0.25.1
