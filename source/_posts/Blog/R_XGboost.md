---
title: "XGboost With R"
url: r_xgboost
date: 2020/09/20
description: "Machine Learning With R|XGboost"
toc: true
excerpt: "XGBoost (Extreme Gradient Boosting) is a popular open-source machine learning library used for classification and regression tasks. It is designed to improve upon the performance of traditional gradient boosting algorithms by adding additional regularization and optimizing the gradient descent algorithm. It is widely used in industry and has won several machine learning competitions. <a title='GhatGPT'>Who said this?</a>"
tags: [R, Machine Learning]
category: [R, Data, Machine Learning]
cover: 'https://s1.ax1x.com/2020/06/26/NskWaq.png'
thumbnail: 'https://s1.ax1x.com/2020/06/26/NskWaq.png'
priority: 10000
---

## XGboost With R

**Documentation**: [Tutorial](https://xgboost.readthedocs.io/en/latest/R-package/xgboostPresentation.html)

## Brief Introduction:
Xgboost (e**X**treme **G**radient **Boost**ing)

- linear model ;
- tree learning algorithm.

it supports various objective functions, including **regression**, **classification** and **ranking**.


## Install

```r
install.packages("drat")
install.packages("xgboost")
```

## Quick Start
### Test Data
Just as all Machine algorithms, we need the training data set and testing data set.
In real world, `caret` can help to split the training and testing data set.
```r
library("drat")
library("xgboost")


data(agaricus.train, package='xgboost')
data(agaricus.test, package='xgboost')
train <- agaricus.train
test <- agaricus.test
```

```r
## Have a quick Look
str(train)
```
<pre>
List of 2
 $ data :Formal class 'dgCMatrix' [package "Matrix"] with 6 slots
  .. ..@ i       : int [1:143286] 2 6 8 11 18 20 21 24 28 32 ...
  .. ..@ p       : int [1:127] 0 369 372 3306 5845 6489 6513 8380 8384 10991 ...
  .. ..@ Dim     : int [1:2] 6513 126
  .. ..@ Dimnames:List of 2
  .. .. ..$ : NULL
  .. .. ..$ : chr [1:126] "cap-shape=bell" "cap-shape=conical" "cap-shape=convex" "cap-shape=flat" ...
  .. ..@ x       : num [1:143286] 1 1 1 1 1 1 1 1 1 1 ...
  .. ..@ factors : list()
 $ label: num [1:6513] 1 0 0 1 0 0 0 1 0 0 ...
</pre>

Here in our data set `train`, `label` is the outcome of what we'd like to predict.

```r
class(train$data)
```
<pre>
[1] "dgCMatrix"
attr(,"package")
[1] "Matrix"
</pre>

As seen below, the data are stored in a `dgCMatrix` which is a **sparse matrix** and label vector is a **numeric vector** ({0,1}):

### Quick Model
```r
bstSparse <- xgboost(data = train$data, label = train$label, max.depth = 2, eta = 1, nthread = 2, nrounds = 2, objective = "binary:logistic")
```
<pre>
[1]	train-error:0.046522
[2]	train-error:0.022263
</pre>

- objective = "binary:logistic": we will train a binary classification model ;
- max.depth = 2: the trees won’t be deep, because our case is very simple ;
- nthread = 2: the number of cpu threads we are going to use;
- nrounds = 2: there will be two passes on the data, the second one will enhance the model by further reducing the difference between ground truth and prediction.

### Preparing Your Data Set
We can preparing our data by turn `matrix` or `attr` matrix to `xgb.Dmatrix`
```r
dtrain <- xgb.DMatrix(data = train$data, label = train$label)
bstDMatrix <- xgboost(data = dtrain, max.depth = 2, eta = 1, nthread = 2, nrounds = 2, objective = "binary:logistic")
```

### Predict
Now, Let's so the utmost goal,
**Perform the prediction**
```r
pred <- predict(bstDMatrix, test$data)
## Check The result
print(data.frame(Pre=round(head(pred,10),4),Rel=head(test$label,10)))
```

<pre >
   Pre      Rel
1  0.2858   0
2  0.9239   1
3  0.2858   0
4  0.2858   0
5  0.0517   0
6  0.9239   0
7  0.9239   1
8  0.2858   0
9  0.9239   1
10 0.0107   0
</pre>

As we can see, most of results are acceptable (except row 6~th~).

### Save your model
```r
## save the trained model
xgb.DMatrix.save(dtrain, "dtrain.buffer")

## to load it in, simply call xgb.DMatrix
dtrain2 <- xgb.DMatrix("dtrain.buffer")
```


### feature importance

```r
xgb.importance(colnames(agaricus.train$data), model = bstDMatrix)
```
<pre>
Feature       Gain     Cover Frequency
1:               odor=none 0.67615469 0.4978746       0.4
2:         stalk-root=club 0.17135376 0.1920543       0.2
3:       stalk-root=rooted 0.12317237 0.1638750       0.2
4: spore-print-color=green 0.02931918 0.1461960       0.2
</pre>





<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
