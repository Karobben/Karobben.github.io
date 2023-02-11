---
title: "Python OpenCV: Blurt Detect"
description: "Python OpenCV: Blurt Detect | OpenCV 检测模糊图片"
url: cv_blurtdetect
date: 2020/10/25
toc: true
excerpt: "Some Online Tools"
tags: [Python, OpenCV, Image]
category: [Python, OpenCV]
cover: 'https://s3.ax1x.com/2020/11/11/BvMWm4.png'
thumbnail: 'https://s3.ax1x.com/2020/11/11/BvMWm4.png'
priority: 10000
---

## Python OpenCV: Blurt Detect

I settled a Raspberry pi for taking pictures for months to recording the pictures of my Eco-Tack. It is fun to see the changing of the plants in the tank after combined the pictures. But the problem is their are few blurt images in those hundreds of pictures. So, I wonder it is really cool that detect the blurt pictures by using python. So, I found two posts from internet and try to find the suitable one for me.
Two reference posts:
[技术挖掘者; 2019](https://blog.csdn.net/WZZ18191171661/article/details/96602043)
[Dontla; 2019](https://blog.csdn.net/dontla/article/details/102723962)

So, there have 574 photos in total and I have no idea which one is blurt images.

## 技术挖掘者

|Blurt|Clear|
|--|--|
|![BvVoMd.md.png](https://s3.ax1x.com/2020/11/11/BvVoMd.md.png)|![BvV7qI.md.png](https://s3.ax1x.com/2020/11/11/BvV7qI.md.png)|

## Dontla

|Blurt|Clear|
|--|--|
|![BveIHI.md.png](https://s3.ax1x.com/2020/11/11/BveIHI.md.png)|![BveTEt.md.png](https://s3.ax1x.com/2020/11/11/BveTEt.md.png)|

## Compare

By comparing the result of those to codes, I found that they used the exact same way: `cv2.Laplacian` to calculate...
I should really check the raw codes before executing them.
|First|Second|
|--|--|
|![BvMWm4.png](https://s3.ax1x.com/2020/11/11/BvMWm4.png)|![BvMWm4.png](https://s3.ax1x.com/2020/11/11/BvMWm4.png)|

The simplified codes should be:
```python
import cv2

imagePath = "img.png"

image = cv2.imread(imagePath)
## 将图片转换为灰度图片
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
## 计算灰度图片的方差
fm =  cv2.Laplacian(gray, cv2.CV_64F).var()
print(fm)
```

很不实用 =  = 真的单独一个算法来这么检测, 太水了.
## Plus
So, there are another good post about the blurt-detection by using python Opencv.
It applied 'Brenner', 'Laplacian', 'SMD', 'SMD2', etc to calculate. If you are interested in it, go to check [FUNNY AI](https://zhuanlan.zhihu.com/p/97024018).
