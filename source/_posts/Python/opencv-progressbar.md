---
toc: true
url: opencv_progressbar
covercopy: © Karobben
priority: 10000
date: 2021-06-01 18:48:14
title: "Opencv add a Progress Bar for video| Python"
ytitle: "Opencv, 给视频加一个进度条"
description: "Adding a progress bar for video automatically with opencv in python"
excerpt: "Adding a progress bar for video automatically with opencv in python"
tags: [Python, OpenCV]
category: [Python, OpenCV]
cover: "https://z3.ax1x.com/2021/06/05/2NlpZj.md.png"
thumbnail: "https://z3.ax1x.com/2021/06/05/2NlpZj.md.png"
---

## Opencv Progress Bar

Prepare your video, gif, png

## Sample progress bar

We can use a rectangle to be the progress bar

```python
import cv2 as cv2

# Vdieo source
Video = "/run/media/ken/Data/Vlog/Tank_rasbbery/test.avi"

cap=cv2.VideoCapture(Video)
Video_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_total = cap.get(cv2.CAP_PROP_FRAME_COUNT)
Num = 0
print(frame_total, Num)
while Num <= frame_total-1:
  # caculate the current frame
  # The width of the progress bar = (current frame /Total frame) * Width of the frame
  Width = int((( Num/frame_total)*420))
  Num +=1
  print(Num, frame_total, width)
  # features for rectangle
  ptLeftTop = (0, 0)
  ptRightBottom = (Width, 20)
  point_color = (0, 0, 255) # BGR
  thickness = 20
  lineType = 8
  # frame
  ret,frame=cap.read()
  frame = cv2.resize(frame, (420,360), interpolation = cv2.INTER_AREA)
  frame = cv2.rectangle(frame, ptLeftTop, ptRightBottom, point_color, thickness, lineType)
  cv2.imshow("video",frame)
  # 在播放每一帧时，使用cv2.waitKey()设置适当的持续时间。如果设置的太低视频就会播放的非常快，如果设置的太高就会播放的很慢。通常情况下25ms就ok
  if cv2.waitKey(25)&0xFF==ord('q'):
     cv2.destroyAllWindows()
     break

print("Mission Down")
```

## loading a picture and moving with progress bar

First, loading the picture
```python
Picture = "/home/ken/Pictures/pokeball.png"
img = cv2.imread(Picture,1)
img = cv2.resize(img, (10,10), interpolation = cv2.INTER_AREA)
```

Then, picture clean:
Details about threads and mask: [假小牙 2017](https://blog.csdn.net/sinat_21258931/article/details/61418681)

Origing by: [万能的小黑Alex 2020](https://www.jb51.net/article/183923.htm)
==Transparent Background==
```python
def CV_mask(img1, img2, rows1, rows2, cols1, cols2):
    # 把logo放在左上角，所以我们只关心这一块区域
    roi = img1[rows1:rows2, cols1:cols2]

    # 创建掩膜
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    print(img2gray[0])
    ret, mask = cv2.threshold(img2gray, 56, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # 保留除logo外的背景
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    dst = cv2.add(img1_bg, img2) # 进行融合
    img1[rows1:rows2, cols1:cols2] = dst # 融合后放在原图上

    return img1
```
or

Origing  by: [红薯爱帅 2017](https://www.jianshu.com/p/7caac6b500e3)
==Clear Background==
```python
def img_deal(img_target, img_logo, row1, row2, col1, col2):
    # 1，对logo进行缩放，按照20%进行
    # cv2.imshow("img_logo", img_logo)
    # 2，对logo做清洗，白色区域是255，其他区域置为黑色0
    img_logo_gray = cv2.cvtColor(img_logo, cv2.COLOR_BGR2GRAY)
    print(img_logo_gray[0])
    ret, img_logo_mask = cv2.threshold(img_logo_gray, 46, 255, cv2.THRESH_BINARY)  # 二值化函数
    img_logo_mask1 = cv2.bitwise_not(img_logo_mask)
    # cv2.imshow("img_logo_gray", img_logo_gray)
    # cv2.imshow("img_logo_mask", img_logo_mask)

    # 3，提取目标图片的ROI
    img_roi = img_target[col1:col2, row1:row2].copy()
    #cv2.imshow("img_roi", img_roi)

    # 4，ROI和Logo图像融合
    img_res0 = cv2.bitwise_and(img_roi, img_roi, mask=img_logo_mask)
    img_res1 = cv2.bitwise_and(img_logo, img_logo, mask=img_logo_mask1)
    img_res2 = cv2.add(img_res0, img_res1)
    # img_res2 = img_res0 + img_res1
    img_target[col1:col2, row1:row2] = img_res2[:, :]

    return img_target
```

Finally, adding picture to frames

```python
import cv2 as cv2
import numpy as np

# Vdieo source
Video = "/run/media/ken/Data/Vlog/Tank_rasbbery/test.avi"
Picture = "/home/ken/Pictures/16048269.png"

# OUTPUT size of the video
Width_out = int(1920*.9)
Height_out = int(1080*.9)
PB_h_r = 1- 0.5
# Resize image
PB_img_wr = .025
img = cv2.imread(Picture,1)
#img = cv2.resize(img, (200, 300), interpolation = cv2.INTER_AREA)

# progress bar
point_color = (0, 0, 255) # BGR
lineType = 8
thickness_r = 0.005

cap=cv2.VideoCapture(Video)
# config
PB_H = int(Height_out*PB_h_r)
Video_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_total = cap.get(cv2.CAP_PROP_FRAME_COUNT)
Num = 0
## img_position in frame
PB_img_hr = (img.shape[0]/ img.shape[1] )* PB_img_wr
PB_img_w = int(PB_img_wr * Height_out)
PB_img_h = int(PB_img_hr * Height_out)
if PB_img_h%2 == 1:
    PB_img_h += 1
frame_img_h1 = PB_H -int(PB_img_h/2)
frame_img_h2 = PB_H +int(PB_img_h/2)
img = cv2.resize(img, (PB_img_w,PB_img_h), interpolation = cv2.INTER_AREA)
## Thickness of Progress bar
thickness = int(thickness_r * Height_out)

def img_deal(img_target, img_logo, row1, row2, col1, col2):
    # 1，对logo进行缩放，按照20%进行
    # cv2.imshow("img_logo", img_logo)
    # 2，对logo做清洗，白色区域是255，其他区域置为黑色0
    img_logo_gray = cv2.cvtColor(img_logo, cv2.COLOR_BGR2GRAY)
    print(img_logo_gray[0])
    ret, img_logo_mask = cv2.threshold(img_logo_gray, 46, 255, cv2.THRESH_BINARY)  # 二值化函数
    img_logo_mask1 = cv2.bitwise_not(img_logo_mask)
    # cv2.imshow("img_logo_gray", img_logo_gray)
    # cv2.imshow("img_logo_mask", img_logo_mask)

    # 3，提取目标图片的ROI
    img_roi = img_target[col1:col2, row1:row2].copy()
    #cv2.imshow("img_roi", img_roi)

    # 4，ROI和Logo图像融合
    img_res0 = cv2.bitwise_and(img_roi, img_roi, mask=img_logo_mask)
    img_res1 = cv2.bitwise_and(img_logo, img_logo, mask=img_logo_mask1)
    img_res2 = cv2.add(img_res0, img_res1)
    # img_res2 = img_res0 + img_res1
    img_target[col1:col2, row1:row2] = img_res2[:, :]

    return img_target

def CV_mask(img1, img2, rows1, rows2, cols1, cols2):
    # 把logo放在左上角，所以我们只关心这一块区域
    roi = img1[rows1:rows2, cols1:cols2]

    # 创建掩膜
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    print(img2gray[0])
    ret, mask = cv2.threshold(img2gray, 46, 255, cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask)

    # 保留除logo外的背景
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    dst = cv2.add(img1_bg, img2) # 进行融合
    img1[rows1:rows2, cols1:cols2] = dst # 融合后放在原图上

    return img1

while Num <= frame_total-1:
  # caculate the current frame
  # The width of the progress bar = (current frame /Total frame) * Width of the frame
  Width = int((( Num/frame_total)*Width_out))
  Num +=1
  # features for rectangle
  ptLeftTop = (0, PB_H)
  print(Num, frame_total, Width, PB_H, print(img[0][0]))
  ptRightBottom = (Width, PB_H)
  # frame
  ret,frame=cap.read()
  frame = cv2.resize(frame, (Width_out,Height_out), interpolation = cv2.INTER_AREA)
  frame = cv2.rectangle(frame, ptLeftTop, ptRightBottom, point_color, thickness, lineType)
  # Adding png for progress bar
  Width_png = int((( Num/frame_total)*(Width_out-PB_img_w)))
  # 保留除logo外的背景
  #frame =
  CV_mask(frame, img, frame_img_h1, frame_img_h2, 0+Width_png, PB_img_w+Width_png)
  #frame = img_deal(frame, img, 0+Width_png, PB_img_w+Width_png, frame_img_h1, frame_img_h2)
  #frame[frame_img_h1:frame_img_h2 ,0+Width_png:PB_img_w+Width_png] = img
  # frame show
  cv2.imshow("video",frame)
  # 在播放每一帧时，使用cv2.waitKey()设置适当的持续时间。如果设置的太低视频就会播放的非常快，如果设置的太高就会播放的很慢。通常情况下25ms就ok
  if cv2.waitKey(25)&0xFF==ord('q'):
     cv2.destroyAllWindows()
     break

print("Mission Down")
```

## Gif progress

Loading gif

```python
import time, cv2
from PIL import Image
import numpy as np

file = "/home/ken/Pictures/pikachu_run.gif"

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

All codes

```python
import cv2 as cv2
import numpy as np
from PIL import Image

# Vdieo source
Video = "/run/media/ken/Data/Vlog/Tank_rasbbery/test.avi"
Picture = "/home/ken/Pictures/test.gif"

# OUTPUT size of the video
Width_out = int(1920*.9)
Height_out = int(1080*.9)
PB_h_r = 1- 0.05
# Resize image
PB_img_wr = .1
img = cv2.imread(Picture,1)
#img = cv2.resize(img, (200, 300), interpolation = cv2.INTER_AREA)

# progress bar
point_color = (0, 0, 255) # BGR
lineType = 8
thickness_r = 0.005

cap=cv2.VideoCapture(Video)
# config
PB_H = int(Height_out*PB_h_r)
Video_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_total = cap.get(cv2.CAP_PROP_FRAME_COUNT)
Num = 0
## img_position in frame
#PB_img_hr = (img.shape[0]/ img.shape[1] )* PB_img_wr
#PB_img_w = int(PB_img_wr * Height_out)
#PB_img_h = int(PB_img_hr * Height_out)
#if PB_img_h%2 == 1:
#    PB_img_h += 1
#frame_img_h1 = PB_H -int(PB_img_h/2)
#frame_img_h2 = PB_H +int(PB_img_h/2)
#img = cv2.resize(img, (PB_img_w,PB_img_h), interpolation = cv2.INTER_AREA)
## Thickness of Progress bar
thickness = int(thickness_r * Height_out)

def img_deal(img_target, img_logo, row1, row2, col1, col2, THRE):
    # 1，对logo进行缩放，按照20%进行
    # cv2.imshow("img_logo", img_logo)
    # 2，对logo做清洗，白色区域是255，其他区域置为黑色0
    img_logo_gray = cv2.cvtColor(img_logo, cv2.COLOR_BGR2GRAY)
    print(img_logo_gray[0])
    ret, img_logo_mask = cv2.threshold(img_logo_gray, THRE, 255, cv2.THRESH_BINARY)  # 二值化函数
    img_logo_mask1 = cv2.bitwise_not(img_logo_mask)
    # cv2.imshow("img_logo_gray", img_logo_gray)
    # cv2.imshow("img_logo_mask", img_logo_mask)

    # 3，提取目标图片的ROI
    img_roi = img_target[col1:col2, row1:row2].copy()
    #cv2.imshow("img_roi", img_roi)

    # 4，ROI和Logo图像融合
    img_res0 = cv2.bitwise_and(img_roi, img_roi, mask=img_logo_mask)
    img_res1 = cv2.bitwise_and(img_logo, img_logo, mask=img_logo_mask1)
    img_res2 = cv2.add(img_res0, img_res1)
    # img_res2 = img_res0 + img_res1
    img_target[col1:col2, row1:row2] = img_res2[:, :]

    return img_target

# reading GIF file
List = []
im = Image.open(Picture)
im.seek(1)#skip to the second frame
try:
    while 1:
        img = cv2.cvtColor(np.asarray(im.convert()),cv2.COLOR_RGB2BGR)
        PB_img_hr = (img.shape[0]/ img.shape[1] )* PB_img_wr
        PB_img_w = int(PB_img_wr * Height_out)
        PB_img_h = int(PB_img_hr * Height_out)
        if PB_img_h%2 == 1:
            PB_img_h += 1
        frame_img_h1 = PB_H -int(PB_img_h/2)
        frame_img_h2 = PB_H +int(PB_img_h/2)

        List += [cv2.resize(img, (PB_img_w,PB_img_h), interpolation = cv2.INTER_AREA)]
        im.seek(im.tell()+1)
except EOFError:#the sequence ends
    pass

def CV_mask(img1, img2, rows1, rows2, cols1, cols2, THRE):
    # 把logo放在左上角，所以我们只关心这一块区域
    roi = img1[rows1:rows2, cols1:cols2]

    # 创建掩膜
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    print(img2gray[0])
    ret, mask = cv2.threshold(img2gray, THRE, 255, cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask)

    # 保留除logo外的背景
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    dst = cv2.add(img1_bg, img2) # 进行融合
    img1[rows1:rows2, cols1:cols2] = dst # 融合后放在原图上

    return img1

while Num <= frame_total-1:
  # caculate the current frame
  # The width of the progress bar = (current frame /Total frame) * Width of the frame
  Width = int((( Num/frame_total)*(Width_out-PB_img_w))) + int(PB_img_w*.5)
  Num +=1
  # features for rectangle
  ptLeftTop = (0, PB_H)
  img = List[int(Num%len(List))]
  img = cv2.flip(img,1 )
  print(Num, frame_total, Width, PB_H, print(img[0][0]))
  ptRightBottom = (Width, PB_H)
  # frame
  ret,frame=cap.read()
  frame = cv2.resize(frame, (Width_out,Height_out), interpolation = cv2.INTER_AREA)
  frame = cv2.rectangle(frame, ptLeftTop, ptRightBottom, point_color, thickness, lineType)
  # Adding png for progress bar
  Width_png = int((( Num/frame_total)*(Width_out-PB_img_w)))
  # 保留除logo外的背景
  #frame =
  #CV_mask(frame, img, frame_img_h1, frame_img_h2, 0+Width_png, PB_img_w+Width_png, 207)
  frame = img_deal(frame, img, 0+Width_png, PB_img_w+Width_png, frame_img_h1, frame_img_h2, 207)
  #frame[frame_img_h1:frame_img_h2 ,0+Width_png:PB_img_w+Width_png] = img
  # frame show
  cv2.imshow("video",frame)
  # 在播放每一帧时，使用cv2.waitKey()设置适当的持续时间。如果设置的太低视频就会播放的非常快，如果设置的太高就会播放的很慢。通常情况下25ms就ok
  if cv2.waitKey(25)&0xFF==ord('q'):
     cv2.destroyAllWindows()
     break

print("Mission Down")
```
