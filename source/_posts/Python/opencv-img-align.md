---
toc: true
url: opencv_img_align
covercopy: © Karobben
priority: 10000
date: 2021-04-21 19:50:06
title: "Image align by opencv in Python"
ytitle: "Python: 图片拼接排列 opencv"
description: "Align your images into a frame with opencv in Python"
excerpt: "Align your images into a frame with opencv in Python"
tags: [Python, OpenCV]
category: [Python, OpenCV]
cover: "https://z3.ax1x.com/2021/04/21/cqF1E9.md.png"
thumbnail: "https://z3.ax1x.com/2021/04/21/cqF1E9.md.png"
---

## Align


```python
import cv2
import numpy as np

img1 = cv2.imread('/home/ken/Desktop/test/IMG_20210421_143828.jpg')
img2 = cv2.imread('/home/ken/Desktop/test/IMG_20210421_143832.jpg')
img3 = cv2.imread('/home/ken/Desktop/test/IMG_20210421_143834.jpg')
img4 = cv2.imread('/home/ken/Desktop/test.png')

img_result = cv2.resize(img1, (900,400))
img_1 = cv2.resize(img1, (300,200))
img_2 = cv2.resize(img2, (300,200))
img_3 = cv2.resize(img3, (300,200))
img_4 = cv2.resize(img4, (900,200))

img_result[0:200, 0:300] = img_1
img_result[0:200, 300:600] = img_2
img_result[0:200, 600:900] = img_3
img_result[200:400, 0:900] = img_4

cv2.imwrite('batch.png',img_result)
```

|![image align](https://z3.ax1x.com/2021/04/21/cqF1E9.md.png)|
|:-:|
