---
toc: true
url: yolov5
covercopy: © Karobben
priority: 10000
date: 2021-11-06 20:41:59
title: "yolov5"
ytitle: "yolov5"
description: "Yolo5"
excerpt: "Yolo5"
tags: [Python, Machine Learning]
category: []
cover: ""
thumbnail: ""
---

Blogs:
- [Difference Between a Batch and an Epoch in a Neural Network](https://machinelearningmastery.com/difference-between-a-batch-and-an-epoch/)

## Batch
Video:
- [deeplizard, 2017](https://www.youtube.com/watch?v=U4WB9p6ODjM)[^deeplizard]
- [Apeer_micro, 2021](https://www.youtube.com/watch?v=OSY7hWADMZk)[^Apeer_micro]

[^deeplizard]:  Deeplizard; Batch Size in a Neural Network explained; 2017; Youtube.
[^Apeer_micro]: Apeer_micro; Tutorial 97 - Deep Learning terminology explained - Batch size, iterations and epochs; 2021; Youtube

The number of the samples in a group been trained.
As a result, the training speed was largely improved by a large batch. But at the same time, the performance of the model might decreased.

- small batch → Less accurate
- large batch → computer time and over fit the dataset
- batch size of 32 or 64 is a good starting point

## Epochs
The times of back-forward

Exp:
Sampel: 3000
BatcCh 32
epochs: 500
- 32 samples will be taken at a time to train the network
- To go through all 300 samples it takes 3000/32 = 94 iterations → 1 epoch.
- This process continues 500 times (epochs).


## Practice

Youtube:
- [ Roboflow: How to Train YOLO v5 on a Custom Dataset; 2020](https://www.youtube.com/watch?v=MdF6x6ZmLAY&t=1212s)
