---
toc: true
url: dots_tracking
covercopy: © Karobben
priority: 10000
date: 2023-02-28 21:32:57
title:
ytitle:
description:
excerpt:
tags:
category:
cover:
thumbnail:
---

## Dots tracking based on sorting nearest distance


```python
import numpy as np
from scipy.spatial.distance import cdist

# Generate two lists of 2D points
np.random.seed(1)
points1 = np.random.rand(10, 2)
np.random.seed(100)
points2 = np.random.rand(10, 2)

# Calculate the pairwise distances between the points
distances = cdist(points1, points2)

# Sort the distances and get the indices of the sorted elements
sorted_indices = np.argsort(distances, axis=None)

# Keep track of which points have already been paired
paired_points1 = set()
paired_points2 = set()

# Loop through the sorted distances and pair the closest points
pairs = []
for index in sorted_indices:
    i1, i2 = np.unravel_index(index, distances.shape)
    if i1 not in paired_points1 and i2 not in paired_points2:
        paired_points1.add(i1)
        paired_points2.add(i2)
        pairs.append((points1[i1], points2[i2]))

# Print the pairs
print(pairs)
```

<pre>
[(array([0.14675589, 0.09233859]), array([0.18532822, 0.10837689])),
 (array([0.20445225, 0.87811744]), array([0.21969749, 0.97862378])),
 (array([0.417022  , 0.72032449]), array([0.42451759, 0.84477613])),
 (array([0.02738759, 0.67046751]), array([0.13670659, 0.57509333])),
 (array([0.14038694, 0.19810149]), array([0.00471886, 0.12156912])),
 (array([0.41919451, 0.6852195 ]), array([0.67074908, 0.82585276])),
 (array([0.39676747, 0.53881673]), array([0.54340494, 0.27836939])),
 (array([0.4173048 , 0.55868983]), array([0.81622475, 0.27407375])),
 (array([0.18626021, 0.34556073]), array([0.81168315, 0.17194101])),
 (array([1.14374817e-04, 3.02332573e-01]), array([0.89132195, 0.20920212]))]
</pre>

Now, lets visualize them with a scatter plots

```python
import pandas as pd
import matplotlib.pyplot as plt

Dots = pd.DataFrame(pairs)

plt.plot([i[0] for i in Dots[0]], [i[1] for i in Dots[0]], 'bo')
plt.plot([i[0] for i in Dots[1]], [i[1] for i in Dots[1]], 'ro')

for i in range(len(Dots)):
  plt.plot([i[0] for i in Dots.iloc[i,:].to_list()], [i[1] for i in Dots.iloc[i,:].to_list()])

plt.show()
```

This is how it would like
![](https://s1.ax1x.com/2023/03/01/ppinxWF.png)


If we have a good data, it could looks like this:
![](https://s1.ax1x.com/2023/03/01/ppiuEFK.png)

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
