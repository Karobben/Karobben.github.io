---
toc: true
url: jupyter
covercopy: <a href="https://www.dataquest.io/blog/jupyter-notebook-tutorial/">© dataquest.io</a>
priority: 10000
date: 2021-10-31 16:14:28
title: "Jupyter Notebook"
ytitle: "Jupyter Notebook"
description: "Jupyter Notebook"
excerpt: "Jupyter Notebook"
tags: [Python, Jupyter Notebook]
category: [Python, others]
cover: "https://jupyter.org/assets/homepage/main-logo.svg"
thumbnail: "https://jupyter.org/assets/homepage/main-logo.svg"
---


## Install

```python
pip install notebook
```

## Sattel for the online Jupiter server

Reference:[qcyfred 2018](https://blog.csdn.net/qcyfred/article/details/82767965)

1. generate a config fire `jupyter notebook --generate-config`
2. Modify the config file `vim ~/.jupyter/jupyter_notebook_config.py`


```diff
# c.ConnectionFileMixin.ip = ''
+c.ConnectionFileMixin.ip = '0.0.0.0'

# c.NotebookApp.ip = 'localhost'
+c.NotebookApp.ip = '172.18.108.101'

# c.NotebookApp.password = ''
+c.NotebookApp.allow_password_change = True
+c.NotebookApp.password = '12345678'
```


Note book buttons: [technologger, 2019](https://medium.com/@technologger/how-to-interact-with-jupyter-33a98686f24e)


## For R

### Plot size

It works both for `ggplot` and `plot` functions
[user41871](https://stackoverflow.com/questions/45473128/r-changing-ggplot-plot-size-in-jupyter)
```r
options(repr.plot.width=20, repr.plot.height=8)
```
