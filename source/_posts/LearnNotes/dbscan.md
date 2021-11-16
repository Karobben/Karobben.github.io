---
toc: true
url: dbscan
covercopy: <a href="https://www.mdpi.com/1996-1073/12/19/3722/htm">© Li, X, et al</a>
priority: 10000
date: 2021-11-06 15:48:47
title: "DBSCAN"
ytitle: "DBSCAN"
description: "DBSCAN"
excerpt: "DBSCAN"
tags: [Statistic, Cluster]
category: [Notes, Statistic, Distribution]
cover: "https://www.mdpi.com/energies/energies-12-03722/article_deploy/html/images/energies-12-03722-g008.png"
thumbnail: "https://e7.pngegg.com/pngimages/339/67/png-clipart-science-technology-engineering-and-mathematics-logo-pi-math-white-text.png"
---

## DBSCAN

video instroctrions:
- [Machine Learning TV: DBSCAN: Part 1; 2019; Youtube](https://www.youtube.com/watch?v=sKRUfsc8zp4)
- [Machine Learning TV: DBSCAN: Part 1; 2019; Youtube](https://www.youtube.com/watch?v=sKRUfsc8zp4)
- [Machine Learning TV: DBSCAN: Part 2; 2019; Youtube](https://www.youtube.com/watch?v=6jl9KkmgDIw)

Blog and Papers:
- [Li, X.; Zhang, P.; Zhu, G. DBSCAN Clustering Algorithms for Non-Uniform Density Data and Its Application in Urban Rail Passenger Aggregation Distribution. Energies 2019, 12, 3722. https://doi.org/10.3390/en12193722 ](https://www.mdpi.com/1996-1073/12/19/3722/htm)
- [Kelvin Salton do Prado: How DBSCAN works and why should we use it?; 2017](https://towardsdatascience.com/how-dbscan-works-and-why-should-i-use-it-443b4a191c80)

## The ideas of DBscan

|![DBscan](https://www.mdpi.com/energies/energies-12-03722/article_deploy/html/images/energies-12-03722-g006.png)|
|:-:|
|[© Li, X, et al](https://www.mdpi.com/1996-1073/12/19/3722/htm)|
DBscan is cluster a group of nodes by the spatial distribution density.
It divided the nodes to "core point"; "border point", and "outlier point"
By given the pre-assigned diameters (of the sphere) and number of the adjacent nodes, it scan the nodes randomly.
- The node fit our expectation is ==core node==.
- The node failed to achieve the expectation but adjacent to the core point(a) is ==border point==.
- Rest of nodes are ==outlier points==  

The advantage of DBscan is
- Outlier points (Noises) is tolerated. (Unlike k-means)
- It can detect the cluster under a cluster. (Not like spherical-shape cluster)


## DNscan in python

Source codes: [sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)
```python
from sklearn.cluster import DBSCAN
import numpy as np
X = np.array([[1, 2], [2, 2], [2, 3],
      [8, 7], [8, 8], [25, 80]])
 = DBSCAN(eps=3, min_samples=2).fit(X)
clustering.labels_
array([ 0,  0,  0,  1,  1, -1])
clustering
```

<pre>
DBSCAN(eps=3, min_samples=2)
</pre>

More examples: from SKlearn
| [![Click me to show more](https://scikit-learn.org/stable/_images/sphx_glr_plot_dbscan_001.png)](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py)   |
|:-:|
[![Click me to show more](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_001.png)](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py)|
