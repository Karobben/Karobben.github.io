---
toc: true
url: image
covercopy: <a href='https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html'>© scipy</a>
priority: 10000
date: 2023-03-07 20:25:35
title: "Image skills for python"
ytitle: "Image skills for python"
description: "Image skills for python"
excerpt: "Python is a popular programming language used in image processing and analysis due to its simplicity, ease of use, and large collection of libraries such as OpenCV, NumPy, and scikit-image. Python allows developers to easily manipulate and analyze images, apply complex algorithms, and create custom image processing pipelines. <a title='ChatGPT3'>Who said this?</a>"
tags: [Python, Image]
category: [Python]
cover: "https://docs.scipy.org/doc/scipy/_images/scipy-ndimage-gaussian_filter-1.png"
thumbnail: "https://docs.scipy.org/doc/scipy/_images/scipy-ndimage-gaussian_filter-1.png"
---


## Read tiff files

[skimage](https://biomedicalhub.github.io/python-data/skimage.html)
```python
import skimage.io as skio
imstack1    = skio.imread("FILENAME.TIF", plugin="tifffile")
```


## Gaussian Smoothing

[scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html)

```python
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(50, step=2).reshape((5,5))
b = gaussian_filter(a, sigma=3)

fig, axs = plt.subplots(1,2)
axs[0].imshow(a)
axs[1].imshow(b)

plt.show()
```

![Gaussian Smoothing](https://s1.ax1x.com/2023/03/08/ppe5dzD.png)

|![Gaussian example from scipy](https://docs.scipy.org/doc/scipy/_images/scipy-ndimage-gaussian_filter-1.png)|
|:-:|
|[© scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html)|

## Turn image to DataFrame

### Grey image

```python
import pandas as pd
import numpy as np

# create a 2D image array
image_array = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# convert to pandas dataframe
df = pd.DataFrame(image_array)
# print dataframe
print(df)
```



<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
