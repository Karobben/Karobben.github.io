---
title: "Python|OpenCV| Video Speedup"
description: "Accelerate/Speed up your video by dropping frames or increasing fps"
url: python_video_speed
date: 2020/10/25
toc: true
excerpt: "Speed up your video by deleting some frames through OpenCV"
tags: [Python, OpenCV]
category: [Python, OpenCV]
cover: 'https://s1.ax1x.com/2020/05/22/YLZMxf.png'
thumbnail: 'https://s1.ax1x.com/2020/05/22/YLZMxf.png'
priority: 10000
---

## Python| OpenCV: Video Speed up

Before starting:
You can find some fundamental codes of Opencv at: [My Blog](https://karobben.github.io/2020/09/12/Python/OpenCV/)
You can find the latest release at: [GitHub: Karobben](https://github.com/Karobben/Karobben-Work-Station/blob/master/Video_speed.py)


```python
##!/usr/bin/env python3
## -*- coding: utf-8 -*-
## @Time    : 2020/08/03
## @Author  : Karobben
## @Site    : China
## @File    : VideoSlice.py
## @Software: Atom

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input',
                    help='Input Video file')     #输入文件
parser.add_argument('-o','-U','--output', default = "out_test.avi",
                    help='Output Video file, default as "out_test.avi"')     #输出文件
parser.add_argument('-r','-R','--ratio', default = 2,
                    type = int,
                    help='Speed up by ratio, "default = 2"')     #加速比率
parser.add_argument('-f','-F','--fps', default = 0,
                    type = int,
                    help='Speed up by ratio, "default = 2"')     #帧率
parser.add_argument('-inf', nargs='?',default=True)

##获取参数
args = parser.parse_args()
INPUT = args.input
OUTPUT = args.output
Ratio = args.ratio
fps_o = args.fps
inf = args.inf


import cv2

##INPUT = 'bug.avi'
cap = cv2.VideoCapture(INPUT)
fps_c = cap.get(cv2.CAP_PROP_FPS)
Video_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
Video_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print("Current fps:",fps_c)


##OUTPUT = "out_test.avi"
if fps_o == 0:
    fps_o = fps_c

def Video_speed(cap, OUTPUT):
    Out_size = (int(Video_w),int(Video_h))
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    videowriter = cv2.VideoWriter(OUTPUT,fourcc,fps_o,Out_size)

    i = 0
    ret = True
    while ret == True:
        i +=1
        ret,frame=cap.read()
        if i % Ratio == 0:
            videowriter.write(frame)

    videowriter.release()

if inf == True:
    Video_speed(cap, OUTPUT)
```



BiliBili：[史上最不正經的生物狗](https://space.bilibili.com/393056819)
