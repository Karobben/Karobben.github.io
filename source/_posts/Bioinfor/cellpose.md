---
toc: true
url: cellpose
covercopy: <a href="https://cellpose.readthedocs.io/en/latest/outputs.html">© CellPose</a>
priority: 10000
date: 2022-12-21 17:55:36
title: "Cellpose"
ytitle: "Cellpose"
description: "A quick note of how to use the cellpose to do cell segmentation"
excerpt: "Cellpose is a deep learning-based software that automates cell segmentation and classification from fluorescence microscopy images. It provides a user-friendly interface and can process a large number of images in a short time, making it a valuable tool for biologists and biomedical researchers studying cell morphology and behavior. <a title='ChatGPT'>Who sad this?</a>"
tags: [Bioinformatics, Image, Machine Learning]
category: [Biology, Bioinformatics, Software]
cover: "https://cellpose.readthedocs.io/en/latest/_images/ex_seg.png"
thumbnail: "https://cellpose.readthedocs.io/en/latest/_images/ex_seg.png"
---


## CellPose

CellPose is an awesome machine learning-based tool that could segment cells very easily. The pre-trained model could suit multiple scenarios and fit the basic usages. And it can do more than cell segmentation (Though the cell pose looks fancy, I still didn't know who to work with the results.) To learn more, please read the [documentation](https://cellpose.readthedocs.io/en/latest/index.html)



```python
from cellpose import models
from cellpose.io import imread

# model_type='cyto' or model_type='nuclei'
model = models.Cellpose(gpu=False, model_type='cyto')

files = ['img0.tif', 'img1.tif']
imgs = [imread(f) for f in files]
masks, flows, styles, diams = model.eval(imgs, diameter=None, channels=[0,1],
                                         flow_threshold=0.4, do_3D=False)



```





























<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
