---
toc: true
url: ai_linear
covercopy: © Karobben
priority: 10000
date: 2024-02-05 12:26:13
title: "Linear Regression"
ytitle: "Linear Regression"
description: "Linear Regression"
excerpt: "Linear Regression"
tags: []
category: []
cover: ""
thumbnail: ""
---

## Linear Regression

### Vectors and Matrix

In numpy, the dot product can be written np.dot(w,x) or w@x.
Vectors will always be column vectors. Thus:

|![](https://imgur.com/Zq0RMO8.png)|![](https://imgur.com/TF5NMbz.png)|
|:-:|:-:|
|Vectors are lowercase bold letters|Matrices are uppercase bold letters|

Vector and Matrix Gradients
The gradient of a scalar function with respect to a vector or matrix is:
The symbol $\frac{\sigma f}{\sigma x_ 1}$ means "partial derivative of f with respect to *x~1~*"

|![](https://imgur.com/2b5hSHK.png)|
|:-:|

|![](https://www.researchgate.net/profile/Vladimir-Nasteski/publication/328146111/figure/fig4/AS:702757891751937@1544561946700/Visual-representation-of-the-linear-regression-22.ppm)|
|:-:|
|[© Vladimir Nasteski](https://www.researchgate.net/publication/328146111_An_overview_of_the_supervised_machine_learning_methods?_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6Il9kaXJlY3QiLCJwYWdlIjoiX2RpcmVjdCJ9fQ)|

$$ f(x) = w^ T x + b = \sum_{j=0} ^{D-1} w_ j x_ j + b $$
- $f(x) = y$
- Generally, we want to choose the weights and bias, *w* and *b*, in order to minimize the errors.
- The errors are the vertical green bars in the figure at right, *&epsilon; = f(x) − y*.
- Some of them are positive, some are negative. What does it mean to "minimize" them?
    - $ f(x) = w^ T x + b = \sum_{j=0} ^{D-1} w_ j x_ j + b $
- Training token errors Using that notation, we can define a signed error term for every training token: *&epsilon; = f(x~i~) - y~i~*
- The error term is positive for some tokens, negative for other tokens. What does it mean to minimize it?

### Mean-squared error

Squared: tends to notice the big values and trying ignor small values.  

One useful criterion (not the only useful criterion, but perhaps the most common) of “minimizing the error” is to minimize the mean squared error:
$$  \mathcal{L} = \frac{1}{2n} \sum_{i=1}^ {n} \varepsilon_i^ 2 = \frac{1}{2n} \sum_{i=1}^ {n} (f(x_ i) - y_ i)^ 2  $$
The factor $\frac{1}{2}$ is included so that, so that when you differentiate ℒ , the 2 and the $\frac{1}{2}$ can cancel each other.

!!! note MSE = Parabola 
    Notice that MSE is a non -negative quadratic function of *f(**x**~i~) = **w**^T^ x~i~ + b*, therefore it’s a non negative quadratic function of ***w*** . Since it’s a non -negative quadratic function of ***w***, it has a unique minimum that you can compute in closed form! We won’t do that today. 
$\mathcal{L} = \frac{1}{2n} \sum_{i=1}^ {n} (f(x_ i) - y_ i)^ 2$

**The iterative solution to linear regression** (gradient descent):
- Instead of minimizing MSE in closed form, we’re going to use an iterative algorithm called gradient descent. It works like this:
    -  Start: random initial ***w*** and *b* (at *t=0*)
    - Adjust ***w*** and *b* to reduce MSE (*t=1*)
    - Repeat until you reach the optimum (*t = ∞*).

$ w \leftarrow w - \eta \frac{\partial \mathcal{L}}{\partial w} $
$ b \leftarrow b - \eta \frac{\partial \mathcal{L}}{\partial b} $


### Finding the gradient

The loss function \( \mathcal{L} \) is defined as:

\[ \mathcal{L} = \frac{1}{2n} \sum_{i=1}^{n} L_i, \quad L_i = \varepsilon_i^2, \quad \varepsilon_i = w^T x_i + b - y_i \]

To find the gradient, we use the chain rule of calculus:

\[ \frac{\partial \mathcal{L}}{\partial w} = \frac{1}{2n} \sum_{i=1}^{n} \frac{\partial L_i}{\partial w}, \quad \frac{\partial L_i}{\partial w} = 2\varepsilon_i \frac{\partial \varepsilon_i}{\partial w}, \quad \frac{\partial \varepsilon_i}{\partial w} = x_i \]

Putting it all together,

\[ \frac{\partial \mathcal{L}}{\partial w} = \frac{1}{n} \sum_{i=1}^{n} \varepsilon_i x_i \]

### The iterative solution to linear regression
• Start from random initial values of
� and � (at � = 0).
• Adjust � and � according to:

\[ w \leftarrow w - \frac{\eta}{n} \sum_{i=1}^{n} \varepsilon_i x_i \]
\[ b \leftarrow b - \frac{\eta}{n} \sum_{i=1}^{n} \varepsilon_i \]

- Intuition:
- Notice the sign:
\[ w \leftarrow w - \frac{\eta}{n} \sum_{i=1}^{n} \varepsilon_i x_i \]
- If \( \varepsilon_i \) is positive (\( f(x_i) > y_i \)), then we want to *reduce* \( f(x_i) \), so we make \( w \) less like \( x_i \)
- If \( \varepsilon_i \) is negative (\( f(x_i) < y_i \)), then we want to *increase* \( f(x_i) \), so we make \( w \) more like \( x_i \)











<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
