---
title: "VedioSlice.py"
description: "VedioSlice.py"
url: vedioslice
date: 2020/06/23
toc: true
excerpt: "Reversing play video by using OpenCV"
tags: [Python, OpenCV]
category: [Python, OpenCV]
cover: 'https://opencv.org/wp-content/uploads/2021/01/OpenCV-logo.png'
thumbnail: 'https://opencv.org/wp-content/uploads/2021/01/OpenCV-logo.png'
priority: 10000
---

## `VedioSlice.py`

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
parser.add_argument('-s','-S','--Start', type = int, default = 0,
                    help='Start from X second. default from 0')     #输入文件
parser.add_argument('-e','-E','--End', type = int, default = 1,
                    help='End at X second, defalt at 1s')     #输入文件

##获取参数
args = parser.parse_args()
INPUT = args.input
OUTPUT = args.output
Slice_S = args.Start
Slice_E = args.End

import cv2
import numpy as np

##INPUT = 'bug.avi'
cap = cv2.VideoCapture(INPUT)
fps_c = cap.get(cv2.CAP_PROP_FPS)
Vedio_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
Vedio_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print("Current fps:",fps_c)

Slice_S = Slice_S* fps_c
Slice_E = Slice_E* fps_c
##OUTPUT = "out_test.avi"
fps_o = fps_c
Out_size = (int(Vedio_w),int(Vedio_h))
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
videowriter = cv2.VideoWriter(OUTPUT,fourcc,fps_o,Out_size)

Num = 0
while (True):
   Num += 1
   ret,frame=cap.read()
   if Num >= Slice_S and Num <= Slice_E:
       videowriter.write(frame)
   if Num >= Slice_E:
       break

videowriter.release()
```
<a name="9thCi"></a>
## How to use it
```bash
## print the vedio from 0s to 1s to out_test.avi
Vedio_slice.py -i bug.avi

## print the vedio from 10s to 20s to sliced.avi file
Vedio_slice.py -i bug.avi -s 10 -e 20 -o sliced.avi
```
