---
title: "Vedio_reverse.py"
description: "Vedio_reverse.py"
url: imtemd
date: 2020/06/23
toc: true
excerpt: "Reversing play video by using OpenCV"
tags: [Python, OpenCV]
category: [Python, OpenCV]
cover: 'https://opencv.org/wp-content/uploads/2021/01/OpenCV-logo.png'
thumbnail: 'https://opencv.org/wp-content/uploads/2021/01/OpenCV-logo.png'
priority: 10000
---

## Vedio_reverse.py

##视频倒放
```python
##!/usr/bin/env python3
## -*- coding: utf-8 -*-
## @Time    : 2020/4/18
## @Author  : Karobben
## @Site    : China
## @File    : VedioSlice.py
## @Software: Atom

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input',
                    help='Input vedio file')     #输入文件
parser.add_argument('-o','-U','--output', default = "out_test.avi",
                    help='Output vedio file, default as "out_test.avi"')     #输入文件

##获取参数
args = parser.parse_args()
INPUT = args.input
OUTPUT = args.output

import cv2
import numpy as np

##INPUT = 'bug.avi'
cap = cv2.VideoCapture(INPUT)
fps_c = cap.get(cv2.CAP_PROP_FPS)
Vedio_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
Vedio_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print("Current fps:",fps_c)


##OUTPUT = "out_test.avi"
fps_o = fps_c
Out_size = (int(Vedio_w),int(Vedio_h))
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
videowriter = cv2.VideoWriter(OUTPUT,fourcc,fps_o,Out_size)

List= []
while True:
    ret,frame=cap.read()
    try:
        frame[0,0,0] != None
        List += [frame]
    except:
        break

for i in List[::-1]:
    videowriter.write(i)

videowriter.release()
```
```bash
Vedio_reverse.py -i caopazi.avi -o test.avi
```
