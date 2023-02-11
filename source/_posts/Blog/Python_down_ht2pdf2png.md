---
title: "Python 下载html 为PDF, 再转成PNG"
description: "Python 下载html 为PDF, 再转成PNG"
url: gcxpz7
date: 2020/07/17
toc: true
excerpt: "用python爬蟲下載高中人教版教材"
tags: [Python, Crawler]
category: [Python, Crawler]
cover: 'https://s1.ax1x.com/2020/07/17/Uy4W4g.png'
thumbnail: 'https://s1.ax1x.com/2020/07/17/Uy4W4g.png'
priority: 10000
---

## Python 下载html 为PDF, 再转成PNG

html ot PDF: [https://www.jb51.net/article/160638.htm](https://www.jb51.net/article/160638.htm)<br />PDF to PNG: [https://cloud.tencent.com/developer/article/1481641](https://cloud.tencent.com/developer/article/1481641)
```python
##!/usr/bin/env python3

import pdfkit, sys
import sys, fitz
import os
import datetime


PATH = sys.path[0]
print(PATH)
pdfkit.from_url('https://www.nature.com/subjects/biological-sciences', PATH+'/out.pdf')



def pyMuPDF2_fitz(pdfPath, imagePath):
    pdfDoc = fitz.open(pdfPath) # open document
    for pg in range(pdfDoc.pageCount): # iterate through the pages
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333 #(1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate) # 缩放系数1.3在每个维度  .preRotate(rotate)是执行一个旋转
        rect = page.rect                         # 页面大小
        mp = rect.tl + (rect.bl - (0,1224/zoom_x)) # 矩形区域    56=75/1.3333
        clip = fitz.Rect(mp, rect.br)            # 想要截取的区域
        pix = page.getPixmap(matrix=mat, alpha=False, clip=clip) # 将页面转换为图像
        if not os.path.exists(imagePath):
            os.makedirs(imagePath)
        pix.writePNG(imagePath+'/'+'psReport_%s.png' % pg)# store image as a PNG

if __name__ == "__main__":
    pdfPath = PATH+'/out.pdf'
    imagePath = PATH+'/../Nature'
    #pyMuPDF_fitz(pdfPath, imagePath)#只是转换图片
    pyMuPDF2_fitz(pdfPath, imagePath)#指定想要的区域转换成图片
```
