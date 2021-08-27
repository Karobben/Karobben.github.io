---
title: "Tensorflow"
description: "Tensorflow"
url: tf2
date: 2020/01/22
toc: true
excerpt: "Machine learning"
tags: [Python, Machine Learning, Tensorflow]
category: [Python, Data, Machine Learning]
cover: 'https://camo.githubusercontent.com/c04e16c05de80dadbdc990884672fc941fdcbbfbb02b31dd48c248d010861426/68747470733a2f2f7777772e74656e736f72666c6f772e6f72672f696d616765732f74665f6c6f676f5f736f6369616c2e706e67'
thumbnail: 'https://camo.githubusercontent.com/c04e16c05de80dadbdc990884672fc941fdcbbfbb02b31dd48c248d010861426/68747470733a2f2f7777772e74656e736f72666c6f772e6f72672f696d616765732f74665f6c6f676f5f736f6369616c2e706e67'
priority: 10000
---

## Tensorflow


```python
##!/usr/locol/bin/python3.6

import tensorflow as tf
import numpy as np

## creat data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3


#### creat tnsorflow structure start
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weightess =tf.Session()
*x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)

train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

###create tensorflow structure end ###
sess =tf.Session()
sess.run(init)

for step in range(201):
 sess.run(train)
 if step % 20 == 0:
  print(step, sess.run(Weights),sess.run(biases))





#### add a laier###

def add_layer(inputs, in_size, out_size, activation_function=None):
  Weights = tf.Variable(tf.random_normal([in_size, out_size]))
  biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
  Wx_plus_b = tf.matmul(inputs, Weights) + biases
  if activation_function is None:
     outputs = Wx_plus_b
  else:
     outputs = activation_function(Wx_plus_b)
  return outputs






##################
###From  https://tensorflow.google.cn/get_started/premade_estimators##
#############

```
