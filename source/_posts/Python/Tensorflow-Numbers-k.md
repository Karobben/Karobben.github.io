---
title: "Tensorflow-Numbers-k"
description: "Tensorflow-Numbers-k"
url: tf_n2
date: 2020/01/22
toc: true
excerpt: "Machine learning"
tags: [Python, Machine Learning, Tensorflow]
category: [Python, Data, Machine Learning]
cover: 'https://camo.githubusercontent.com/c04e16c05de80dadbdc990884672fc941fdcbbfbb02b31dd48c248d010861426/68747470733a2f2f7777772e74656e736f72666c6f772e6f72672f696d616765732f74665f6c6f676f5f736f6369616c2e706e67'
thumbnail: 'https://camo.githubusercontent.com/c04e16c05de80dadbdc990884672fc941fdcbbfbb02b31dd48c248d010861426/68747470733a2f2f7777772e74656e736f72666c6f772e6f72672f696d616765732f74665f6c6f676f5f736f6369616c2e706e67'
priority: 10000
---

## Tensorflow-Numbers-k

我也不记得这是啥了= = 
```python
##!/usr/local/bin/python3.6
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.python import keras
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Flatten, Conv2D, Dropout

a=pd.read_csv("train.csv")
a.drop('label', axis=1)

img_rows, img_cols = 28, 28
num_classes = 10

def data_prep(raw):
    out_y = keras.utils.to_categorical(raw.label, num_classes)
    num_images = raw.shape[0]
    x_as_array = raw.values[:,1:]
    x_shaped_array = x_as_array.reshape(num_images, img_rows, img_cols, 1)
    out_x = x_shaped_array / 255
    return out_x, out_y

train_size = 30000
train_file = "train.csv"
raw_data = pd.read_csv(train_file)

x, y = data_prep(raw_data)

model = Sequential()
model.add(Conv2D(30, kernel_size=(3, 3),
                 strides=2,
                 activation='relu',
                 input_shape=(img_rows, img_cols, 1)))
Dropout(0.5)
model.add(Conv2D(30, kernel_size=(3, 3), strides=2, activation='relu'))
Dropout(0.5)
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer='adam',
              metrics=['accuracy'])
model.fit(x, y,
          batch_size=128,
          epochs=2,
          validation_split = 0.2)

```
