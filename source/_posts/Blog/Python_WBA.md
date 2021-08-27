---
title: "Analyzing DNA/Protein Band with Opencv, Python"
description: "Analyzing DNA/Protein Band like ther result of Western blot with Opencv, Python"
url: python_wba
date: 2020/12/13
toc: true
excerpt: "Analyzing DNA/Protein Band like ther result of Western blot with Opencv, Python"
tags: [Python, OpenCV]
category: [Python, OpenCV]
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
covercopy: '© getcodify.com'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## Analyzing DNA/Protein Band with Opencv, Python

Before starting:
You can find some fundamental codes of Opencv at: [My Blog](https://karobben.github.io/2020/09/12/Python/OpenCV/)
You can also find the image `img1.tif` at [My GitHub](https://github.com/Karobben/Western_blot/tree/master/img)
## Loading img

```python
import numpy as np
import cv2

img = cv2.imread('img/img1.tif',0)

while(True):
   cv2.imshow('image',img)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
       break
```


## Selecting the Bands

```python
def Draw_rect(img, X,Y,width=100,height=50):
  # This function is for plot an rectangle by giving perimeters
  ptLeftTop = (X, Y)
  ptRightBottom = (X+width, Y+height)
  point_color = (0, 0, 255) # BGR
  thickness = 2
  lineType = 8
  img = cv2.rectangle(img, ptLeftTop, ptRightBottom, point_color, thickness, lineType)
  return img

def Rect_listP(img,List,W,H):
  # This function is for plot a group of equality rectangles by giving perimeters
  for i in List:
    img = Draw_rect(img,i[0],i[1],W,H)
  return img

def List_M(X1, X2, Y, Num):
  Result = []
  Inter = int((X2-X1)/Num)
  for i in range(Num):
    Result += [[X1+i*Inter,Y]]
  return Result

def Band_list(List,W,H):
    # Create The list for the Bands
    Result = []
    for i in List:
      Result += [[i[0],i[1],W,H]]
    return Result
```

## Targeting the Bands
```python
import numpy as np
import cv2

img = cv2.imread('img/img1.tif',0)

X1, X2, Y, Num, W, H = (275,1985,280,10, 170, 70)
img = Rect_listP(img,List_M(X1, X2, Y, Num),W,H)

while(True):
   cv2.imshow('image',img)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
       break
```

Result:
![U0d41I.md.png](https://s1.ax1x.com/2020/07/15/U0d41I.md.png)


## Calculating the Grey-Grades

```python
Bands = Band_list( List_M(X1, X2, Y, Num),W,H)

for i in Bands:


img = cv2.imread('img/img1.tif',0)

X1, X2, Y, Num = (275,1985,280,10)
##img = Rect_listP(img,List_M(X1, X2, Y, Num),170,70)

Grey = []
N_tmp = 0
for i in Bands:
  N_tmp += 1
  img2 = img[i[1]:i[1]+H,i[0]:i[0]+W]
  # Saving the sliced bands
  cv2.imwrite("bands_"+str(N_tmp)+'.png',img2)
  Grey += [img2.sum()]

print(Grey)
```

Result:
```
[2317178, 2927580, 2033594, 2125166, 2420660, 2427925, 2370562, 2135051, 1559149, 1549062]
```

![Sliced Bands.png](https://s1.ax1x.com/2020/07/15/U0dh9A.png)

```R
library(ggplot2)
TB = c(2317178, 2927580, 2033594, 2125166, 2420660, 2427925, 2370562, 2135051, 1559149, 1549062)
TB = abs(TB[2] - TB)

A = data.frame(TB)
A$ID = factor(row.names(A),levels = c(1:10))
ggplot(A,aes(ID,TB)) + geom_bar(stat = 'identity')
```

![U0d5ct.png](https://s1.ax1x.com/2020/07/15/U0d5ct.png)



BiliBili：[史上最不正經的生物狗](https://space.bilibili.com/393056819)
