---
title: "Python|OpenCV| Images to Video"
ytitle: "Python: OpenCV 图片转视频"
description: "This is a script for connect a serious of images to a video by using python openCV."
url: py_cv_img2video
date: 2020/10/25
toc: true
excerpt: "This is a script for connect a serious of images to a video by using python openCV."
tags: [Python, OpenCV]
category: [Python, OpenCV]
cover: 'https://s1.ax1x.com/2020/05/22/YLZMxf.png'
thumbnail: 'https://s1.ax1x.com/2020/05/22/YLZMxf.png'
priority: 10000
---

This is a script for connect a serious of images to a video by using python openCV.

Before starting:
You can find some fundamental codes of Opencv at: [My Blog](https://karobben.github.io/2020/09/12/Python/OpenCV/)

```bash BASH
python3 img2video.py -i *.png -o output.avi -f 24 -t N
```

`img2video.py`:

```python img2video.py
#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## @Time    : 2020/08/03
## @Author  : Karobben
## @Site    : China
## @File    : img2video.py
## @Software: Atom

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '-I', '--input', nargs='+',
                    help='Input Video file')     #输入文件
parser.add_argument('-o', '-U', '--output',
                    default = "out_test.avi",
                    help='Output Video file, default as "out_test.avi"')     #输出文件
parser.add_argument('-f','-F','--fps', default = 24,
                    type = int,
                    help='Speed up by ratio, "default = 24"')     #帧率

parser.add_argument('-t', '-T', '--title',
                    default ="N",
                    help=
                    '''
                    Add a title;\n
                    Y/N;
                    default = "N"
                    ''')     #输入文件


#获取参数
args = parser.parse_args()
File = args.input
OUTPUT = args.output
fps = args.fps
Title = args.title

import cv2, os

def FD_judge(path):
    result = ""
    if len(path) > 1:
        result = "Files"
    elif os.path.isdir(path[0]):
        result = "Directory"
    elif os.path.isfile(path[0]):
        result = "File"
    else:
        result = "path is incorrect"
    return result


Typ_in = FD_judge(File)

if Typ_in == "Directory":
    List = os.popen('ls '+File).read().split('\n')[:-1]
    img = cv2.imread(File +"/"+List[0])
else:
    List = File
    img = cv2.imread(List[0])

size = (len(img[0]),len(img))
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
videowriter = cv2.VideoWriter(OUTPUT,fourcc,fps,size)

for i in List:
    if Typ_in == "Directory":
        i = File +"/"+i
    # Reading img
    img = cv2.imread(i)
    # Adding title
    if Title == "Y":
        cv2.putText(img, i.split("/")[-1] ,(200, 100), cv2.FONT_HERSHEY_COMPLEX, 2.0, (100, 200, 200), 5)

    videowriter.write(img)

videowriter.release()
```



BiliBili：[史上最不正經的生物狗](https://space.bilibili.com/393056819)
