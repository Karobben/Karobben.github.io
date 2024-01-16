---
toc: true
url: py_gam
covercopy: © Karobben
priority: 10000
date: 2022-03-31 23:31:18
title: "Python GAM to fit"
ytitle: "Python GAM to fit"
description: "Python GAM to fit"
excerpt: "Python GAM to fit"
tags: [Plot, Python, Regression, Data Science]
category: [Python, Plot]
cover: "https://s1.ax1x.com/2022/06/18/XLliRg.md.png"
thumbnail: "https://s1.ax1x.com/2022/06/18/XLliRg.md.png"
---

 
## Python GAM to fit

Source: [pygam](https://pygam.readthedocs.io/en/latest/notebooks/tour_of_pygam.html)

```python
import numpy as np
import matplotlib.pyplot as plt
from pygam import LinearGAM, s, te
from pygam.datasets import mcycle

# X =  np.array([ [i] for i in Cell_fit.Class_size.to_list()])
# y =  np.array(Cell_fit.Size.to_list())

X, y = mcycle(return_X_y=True)

gam = LinearGAM(n_splines=25).gridsearch(X, y)
XX = gam.generate_X_grid(term=0, n=500)

plt.plot(XX, gam.predict(XX), 'r--')
plt.plot(XX, gam.prediction_intervals(XX, width=.95), color='b', ls='--')

plt.scatter(X, y, facecolor='gray', edgecolors='none')
plt.title('95% prediction interval');
```

|![](https://pygam.readthedocs.io/en/latest/_images/pygam_basis.png)|
|:-:|
|![](https://pygam.readthedocs.io/en/latest/_images/notebooks_tour_of_pygam_22_2.png)|
|[© pyGAM](https://pygam.readthedocs.io/en/latest/notebooks/tour_of_pygam.html)|

## Regression by numpy

Source: [W3 school](https://www.w3schools.com/python/python_ml_polynomial_regression.asp)


```python
x = X.flatten()
y = y.to_list()

mymodel = np.poly1d(np.polyfit(x, y, 3))
myline = np.linspace(2, 95, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
```

|![numpy model regression](https://imgur.com/8S5xbxS)|
|:-:|


## Other 

```python
X, y = mcycle(return_X_y=True)
gam = LogisticGAM(f(0) + s(1) + s(2)).gridsearch(X, y)

fig, axs = plt.subplots(1, 3)
titles = ['student', 'balance', 'income']

for i, ax in enumerate(axs):
    XX = gam.generate_X_grid(term=i)
    pdep, confi = gam.partial_dependence(term=i, width=.95)

    ax.plot(XX[:, i], pdep)
    ax.plot(XX[:, i], confi, c='r', ls='--')
    ax.set_title(titles[i]);

```
