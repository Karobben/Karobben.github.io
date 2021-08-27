---
title: "Python 缩小图片轮廓"
description: "Python 缩小图片轮廓"
url: ghlobk
date: 2020/6/26
toc: true
excerpt: "Python 缩小图片轮廓"
tags: [Python, OpenCV]
category: [Python, OpenCV]
cover: 'https://s1.ax1x.com/2020/06/26/NsFi1e.png'
thumbnail: 'https://s1.ax1x.com/2020/06/26/NsFi1e.png'
priority: 10000
---

## Python 缩小图片轮廓

![NsFi1e.png](https://s1.ax1x.com/2020/06/26/NsFi1e.png)
![NsFPpD.png](https://s1.ax1x.com/2020/06/26/NsFPpD.png)

原图轮廓太粗，希望细一些- -但是不会PS GIMP。所以想用Python解决。<br />思路： 保留四周都有有效颜色的点

```python
import numpy as np
import cv2

def Reduice(img):
    Result=[]
    for i in range(1,H-1):
        for ii in range(1,W-1):
            pix = [list(img[i-1][ii]), # LEFT
                   list(img[i+1][ii]), # RIGHT
                   list(img[i][ii-1]), # UP
                   list(img[i][ii+1]), # DOWN
                   list(img[i-1][ii-1]), # LU
                   list(img[i+1][ii-1]), # RU
                   list(img[i-1][ii+1]), # LD
                   list(img[i+1][ii+1]), # RD
                  ]
            if pix ==[[0,0,0,], [0,0,0,], [0,0,0,], [0,0,0,], [0,0,0,], [0,0,0,], [0,0,0,], [0,0,0,]]:
                Result +=[[i,ii]]
    return Result

img = cv2.imread('111.png')
H = len(img)
W = len(img[0])

##赋值到另一个图片：
for i in range(5):
    Result = Reduice(img)
    img2 = np.array(img)
    img2[img2!=254]=254
    for i in Result:
        img2[i[0],i[1]]=img[i[0],i[1]]
    img =np.array(img2)

cv2.imwrite('5.png',img)
## 接下来，减一次，输出一张图

Num = 5
for i in range(5):
    Num +=1
    Result = Reduice(img)
    img2 = np.array(img)
    img2[img2!=254]=254
    for i in Result:
        img2[i[0],i[1]]=img[i[0],i[1]]
    img =np.array(img2)
    cv2.imwrite(str(Num)+'.png',img)

def View(img):
    while(True):
        #img = cv2.imread('111.png')
        cv2.imshow('image',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
```

![NsFF6H.png](https://s1.ax1x.com/2020/06/26/NsFF6H.png)





