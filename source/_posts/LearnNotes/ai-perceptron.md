---
toc: true
url: ai_perceptron
covercopy: © Karobben
priority: 10000
date: 2024-02-07 13:03:23
title: 
ytitle:
description:
excerpt:
tags:
category:
cover:
thumbnail:
---

## Perceptron

Perceptron is invented before the loss function 

Linear classifier: Notation
• The observation x^T^ = [x~1~, … , x~n~] is a real-valued vector (d is the number of feature dimensions)
• The class label y ∈ Y is drawn from some finite set of class labels.
• Usually the output vocabulary, Y, is some set of strings. For
convenience, though, we usually map the class labels to a sequence
of integers, Y = [1, … , v} , where � is the vocabulary size

## Linear classifier: Definition

A linear classifier is defined by

$$
f(x) = \text{argmax } Wx + b
$$

where:

![](https://imgur.com/zuycCx8.png)

$w_k, b_k$ are the weight vector and bias corresponding to class $k$, and the argmax function finds the element of the vector $wx$ with the largest value.

There are a total of $v(d + 1)$ trainable parameters: the elements of the matrix $w$.

![](https://imgur.com/undefined.png)

# Example

Notice that in the two-class case, the equation

$$
f(x) = \text{argmax } Wx + b
$$

Simplifies to

![](https://imgur.com/QAGB3Ur.png)

The class boundary is the line whose equation is

$$
(w_2 - w_1)^T x + (b_2 - b_1) = 0
$$

## Gradient descent

# Gradient descent

Suppose we have training tokens $(x_i, y_i)$, and we have some initial class vectors $w_1$ and $w_2$. We want to update them as

$$
w_1 \leftarrow w_1 - \eta \frac{\partial \mathcal{L}}{\partial w_1}
$$

$$
w_2 \leftarrow w_2 - \eta \frac{\partial \mathcal{L}}{\partial w_2}
$$

...where $\mathcal{L}$ is some loss function. What loss function makes sense?

![](https://imgur.com/YaSOBI6.png)

### Zero-one loss function

# Zero-one loss function

The most obvious loss function for a classifier is its classification error rate,

$$
\mathcal{L} = \frac{1}{n} \sum_{i=1}^{n} \ell(f(x_i), y_i)
$$

Where $\ell(\hat{y}, y)$ is the zero-one loss function,

$$
\ell(f(x), y) =
\begin{cases}
0 & \text{if } f(x) = y \\
1 & \text{if } f(x) \neq y
\end{cases}


### Non-differentiable!

The problem with the zero -one loss function is that it’s not differentiable:
![](https://imgur.com/tuIgHI9.png)

### 

Integer vectors: One-hot vectors, A one-hot vector is a binary vector in which all elements are 0 except for a single element that’s equal to 1.








Drive the perceptron



# The perceptron learning algorithm

a mistake happens here (function)










<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
