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
tags: [Plot, Python, Regression]
category: [Python, Plot]
cover: "https://s1.ax1x.com/2022/06/18/XLliRg.md.png"
thumbnail: "https://s1.ax1x.com/2022/06/18/XLliRg.md.png"
---

 
## Python GAM to fit

Source: [pygam](https://pygam.readthedocs.io/en/latest/notebooks/tour_of_pygam.html)

```python
from pygam import GAM, s, te

X =  np.array([ [i] for i in Cell_fit.Class_size.to_list()])
y =  np.array(Cell_fit.Size.to_list())

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

## Normal Regression

Source: [W3 school](https://www.w3schools.com/python/python_ml_polynomial_regression.asp)
