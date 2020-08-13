---
title: "Python|OpenCV| Images to Video"
description: "Connecting the images to the video"
url: py_cv_img2video
---

# Python| OpenCV: Video Speed up

Before starting:
You can find some fundamental codes of Opencv at: [My Blog](https://karobben.github.io/Python/OpenCV.html)
You can find the latest release at: [GitHub: Karobben](https://github.com/Karobben/Karobben-Work-Station/blob/master/img2video.py)


```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/08/03
# @Author  : Karobben
# @Site    : China
# @File    : VideoSlice.py
# @Software: Atom

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '-I', '--input', nargs='+',
                    help='Input Video file')     #输入文件
parser.add_argument('-o', '-U', '--output',
                    default = "out_test.avi",
                    help='Output Video file, default as "out_test.avi"')     #输出文件
parser.add_argument('-f','-F','--fps', default = 0,
                    type = int,
                    help='Speed up by ratio, "default = 24"')     #帧率

#获取参数
args = parser.parse_args()
File = args.input
OUTPUT = args.output
fps = args.fps

import cv2, os

List = os.popen('ls '+File).read().split('\n')[:-1]
img = cv2.imread(File +"/"+List[0])

size = (len(img[0]),len(img))
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
videowriter = cv2.VideoWriter(OUTPUT,fourcc,fps,size)

for i in List:
    img = cv2.imread(File +"/"+i)
    videowriter.write(img)

videowriter.release()
```


---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
BiliBili：[史上最不正經的生物狗](https://space.bilibili.com/393056819)
