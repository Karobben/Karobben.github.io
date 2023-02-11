---
toc: true
url: yolov5
covercopy: <a href="https://github.com/ultralytics/yolov5">© glenn-jocher</a>
priority: 10000
date: 2021-11-06 20:41:59
title: "yolov5"
ytitle: "yolov5"
description: "Yolo5"
excerpt: "Yolo5"
tags: [Python, Machine Learning]
category: []
cover: "https://github.com/ultralytics/yolov5/releases/download/v1.0/splash.jpg"
thumbnail: "https://github.com/ultralytics/yolov5/releases/download/v1.0/splash.jpg"
---


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>

Blogs:
- [Difference Between a Batch and an Epoch in a Neural Network](https://machinelearningmastery.com/difference-between-a-batch-and-an-epoch/)
- [YOLOv5模型训练, 2020](https://xugaoxiang.com/2020/07/02/yolov5-training/#%E4%BD%BF%E7%94%A8COCO%E6%95%B0%E6%8D%AE%E9%9B%86)

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

Blog with data set:
- [YOLOv5模型训练, 2020](https://xugaoxiang.com/2020/07/02/yolov5-training/#%E4%BD%BF%E7%94%A8COCO%E6%95%B0%E6%8D%AE%E9%9B%86)

## My experience

### Train a small group of data set

Some blogs suggest that we should avoid to label one thing multiple times. I want to know how really it affects. I found a small set of data which has only 105 imgas in trainning set. They labeled two classes as mask-on and mask-off. For testing, I'll repeat all labeles as class 3 which stands for face. After trainning with the same arguments, both model would be used to detect the test dataset and results would be recorded.

Aruguments for training with two GPU
```bash
python -m torch.distributed.launch --nproc_per_node 2 train.py --img 640  --batch-size 16 --epochs 500 --data ../png_DB/mask/data.yaml --weights yolov5s.pt  --device 0,1
```

Script for repeat the labels.
PS:
There is a very important features for yolov5: ==if the location of two labels are identical, one of the class would be deleted.==
At the first time, I just simpliy duplicate all boxs and change the class into a new one. After training, results shows that there are no single labeled face in the training set. So, I have tried to add 0.0001 into each location for make the class '2' different from the origin one.

```bash
rm -rf mask2
cp -r mask mask2
cd mask2
cat  */labels/*|wc -l
for i in $(ls */labels/*)
do echo "" >> $i
paste <(awk '$1=2;{print}' $i| uniq| awk '{print $1}') <(awk '$1=2;{print $2+0.00001" "$3+0.00001" "$4+0.00001" "$5+0.00001" "}' $i| grep -v "^2 ") --delimiters=" " >> $i
done
cat  */labels/*|wc -l
cd test
cp labels/* images
cp ../../classes.txt images
```

<pre>
805
1743
</pre>
As you can see, before the repeat, there are 805 targets. After repeat the labels, we'll update the label information in `data.yaml`

```bash
vim data.yaml
```
<pre>
nc: 3
names: ['mask', 'no-mask', 'face']
</pre>

Detacte and result extrect
```bash
python3 detect.py --weight runs/train/mask/weights/best.pt  --source ../png_DB/mask/train/images --save-txt

cat runs/detect/exp2/labels/*| awk '{print $1}'| sort| uniq -c| sed 's/^ *//'
```

The result:

| Class | Model1     | Model2|Truth|
| :-| :------ |:-|:-
| mask|595       |570| 573|
| no_mask|131|110| 123|
| face| 0 | 646| 687|

As you can see, from the result 1

![](https://s1.ax1x.com/2022/07/03/j3Tqvq.png)


### Advice for Best Training Results

First, please read the [Tips for Best Training Results](https://github.com/ultralytics/yolov5)

1. First thing frist: Label the target well! This is the key step for all work.

2. Large batch as you can!

3. Chech the result, try to increasing the epecho as yor "val/obj_loss" didn't increase
