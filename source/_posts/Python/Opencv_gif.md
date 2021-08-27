---
title: "Opencv & gif"
description: "Opencv & gif"
url: opencv_gif2
date: 2020/09/12
toc: true
excerpt: "Display gif in OpenCV"
tags: [Python, OpenCV]
category: [Python, OpenCV]
cover: 'https://opencv.org/wp-content/uploads/2021/01/OpenCV-logo.png'
thumbnail: 'https://opencv.org/wp-content/uploads/2021/01/OpenCV-logo.png'
priority: 10000
---

## Opencv & gif

reference: [https://blog.csdn.net/qq_41500251/article/details/82820806](https://blog.csdn.net/qq_41500251/article/details/82820806)
```python
import time, cv2
from PIL import Image
import numpy as np

def GIF(file):
    List = []
    im = Image.open(file)
    im.seek(1)#skip to the second frame
    try:
        while 1:
            List += [cv2.cvtColor(np.asarray(im.convert()),cv2.COLOR_RGB2BGR)]
            im.seek(im.tell()+1)
    except EOFError:#the sequence ends
        pass
    Num = 0
    while Num < len(List)*2:
        Num +=1
        ID = Num%(len(List))
        cv2.imshow("OpenCV",List[ID])
        print(ID)
        cv2.waitKey(1)
        time.sleep(0.1)
    cv2.destroyAllWindows()
```


for Videos:

```python
from cv2 import cv2
import imageio
import numpy
# Collection of the imgs
frames_list = []

# Tossed frames per FPS. When FPS = 1, all frame are saved.
FPS = 1

cap=cv2.VideoCapture("test_1.mp4")
while (True):
  ret,frame=cap.read()
  #img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  img = cv2.resize(frame, (460,360))
  frames_list.append(img)


frames = []

Num =0
for img in frames_list:
  Num +=1
  if Num %3 == 0:
    frames.append(img)

gif=imageio.mimsave('test_3.gif',frames,'GIF',duration=1/8)

```
