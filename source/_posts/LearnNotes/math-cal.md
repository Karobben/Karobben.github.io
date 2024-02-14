---
toc: true
url: math_cal
covercopy: <a href="https://www.discovermagazine.com/the-sciences/5-obscure-formulas-that-rule-the-world">© Marina Sun</a>
priority: 10000
date: 2024-02-11 22:58:46
title: "Basic Mathematics Calculating"
ytitle: "Basic Mathematics Calculating"
description: "Basic Mathematics Calculating"
excerpt: "Basic Mathematics Calculating"
tags: []
category: []
cover: "https://images.ctfassets.net/cnu0m8re1exe/6FXIifvsqgc4djOGE4klDa/d08c250a062604e29226a8572727c5aa/shutterstock_376537891-_1_.jpg_mw_900_mh_600"
thumbnail: "https://images.ctfassets.net/cnu0m8re1exe/6FXIifvsqgc4djOGE4klDa/d08c250a062604e29226a8572727c5aa/shutterstock_376537891-_1_.jpg_mw_900_mh_600"
---

## Sum

The sum symbol, represented by the Greek letter sigma (Σ), is widely used in mathematics to denote the summation of a sequence of numbers or expressions. When you see this symbol, it means you should add up a series of numbers according to the specified rule. Here's a breakdown of how it's typically used:

### Basic Structure

The summation symbol is written as:

$$
\sum_{i=a}^{b} f(i)
$$

where:
- $i$ is the index of summation, which takes on each integer value from $a$ to $b$, inclusive.
- $a$ is the lower limit of summation, the starting value of $i$.
- $b$ is the upper limit of summation, the ending value of $i$.
- $f(i)$ is the function of $i$ to be summed over the range from $a$ to $b$.

### Examples

1. **Sum of the first 5 natural numbers**:
   $$
   \sum_{i=1}^{5} i = 1 + 2 + 3 + 4 + 5 = 15
   $$
   Here, $f(i) = i$, and you sum the values of $i$ from 1 to 5.

2. **Sum of the squares of the first 3 positive integers**:
   $$
   \sum_{i=1}^{3} i^2 = 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
   $$
   In this example, $f(i) = i^2$, so you square each $i$ from 1 to 3 and then add them together.

3. **Sum of a constant over a range**:
   Suppose you want to add the number 4, five times. The expression would be:
   $$
   \sum_{i=1}^{5} 4 = 4 + 4 + 4 + 4 + 4 = 20
   $$

   Here, $f(i) = 4$, which doesn't depend on $i$. You're essentially multiplying 4 by the number of terms (5 in this case).

4. **Two sums**
    $$
    \sum_{i=1}^ {5}\sum_{j=2}^ {6} ij
    $$
    For this, you sum over $j$ from 2 to 6 for each value of $i$ from 1 to 5, and then sum those results. It's like computing a series within another series. The operation proceeds as follows:
    1. First, fix $i$ at its starting value, 1.
    2. Then, for $i = 1$, sum over $j$ from 2 to 6, calculating $1 \cdot j$ for each $j$ and adding them together.
    3. Repeat this process for each value of $i$ up to 5.
    4. Finally, sum all the results from the inner summations together.

    Let's compute this step-by-step to see the result.
    The result of the double summation $\sum_{i=1}^ {5}\sum_{j=2}^ {6} ij$ is 300. This means that when you sum the product of $i$ and $j$ for each $i$ from 1 to 5 and each $j$ from 2 to 6, the total sum is 300.
    PS: in python:

    ```python
    N= 0
    for i in range(1,6):
        for j in range(2,7):
            N += i*j
    ```

### How to Use

- **Identify the sequence** you need to sum. This could be a series of numbers, functions of an index, or even a constant value repeated several times.
- **Determine the starting and ending indices** ($a$ and $b$, respectively) for your summation.
- **Write down the function or value** to be summed as $f(i)$ for each $i$ in the range from $a$ to $b$.
- **Compute each term** in the series and **add them together** to find the total sum.

Summation notation is a powerful tool in mathematics, especially for dealing with sequences and series, and it's widely used in various fields such as statistics, physics, and finance.

## Product Notation

Similarly, we have ==product notation==, too. The product symbol is represented by the Greek letter pi (Π), not to be confused with the mathematical constant $\pi$ (pi) used for the ratio of a circle's circumference to its diameter. The product symbol is used to denote the multiplication of a sequence of numbers or expressions, just like the sum symbol is used for addition.

$$
\prod_{i=a}^{b} f(i)
$$

where:
- $i$ is the index of multiplication, taking on each integer value from $a$ to $b$, inclusive.
- $a$ is the lower limit of the product, the starting value of $i$.
- $b$ is the upper limit of the product, the ending value of $i$.
- $f(i)$ is the function of $i$ to be multiplied over the range from $a$ to $b$.

### Examples

1. **Product of the first 5 natural numbers** (also known as $5!$, factorial of 5):

   $$
   \prod_{i=1}^{5} i = 1 \times 2 \times 3 \times 4 \times 5 = 120
   $$

   This multiplies the values of $i$ from 1 to 5.

In mathematics and particularly in machine learning, besides the summation (Σ) and product (Π) notations, another frequently used notation is the integral symbol (∫). While the summation and product notations deal with discrete sequences, the integral symbol is used for continuous functions and is fundamental in calculus. Integrals play a crucial role in various aspects of machine learning, especially in optimization, probability distributions, and understanding the area under curves (such as ROC curves).

## Integral Notation

The basic structure of an integral is:

$$
\int_{a}^{b} f(x) \, dx
$$

where:
- $a$ and $b$ are the lower and upper limits of integration, respectively, defining the interval over which the function $f(x)$ is integrated.
- $f(x)$ is the function to be integrated over $x$.
- $dx$ represents an infinitesimally small increment of $x$, indicating that the integration is performed with respect to $x$.

### Importance in Machine Learning

1. **Optimization**: Many machine learning models involve optimization problems where the goal is to minimize or maximize some function (e.g., a loss function in neural networks or a cost function in logistic regression). Integrals are essential in solving continuous optimization problems, especially when calculating gradients or understanding the behavior of functions over continuous intervals.

2. **Probability Distributions**: In the context of probabilistic models and statistics, integrals are used to calculate probabilities, expected values, and variances of continuous random variables. For example, the area under the probability density function (PDF) of a continuous random variable over an interval gives the probability of the variable falling within that interval.

3. **Feature Extraction and Signal Processing**: In machine learning applications involving signal processing or feature extraction from continuous data, integrals are used to calculate various features and transform signals into more useful forms.

4. **Kernel Methods**: In machine learning, kernel methods (e.g., support vector machines) utilize integrals in the formulation of kernel functions, which are essential in mapping input data into higher-dimensional spaces for classification or regression tasks.

5. **Deep Learning**: In the training of deep neural networks, integrals may not be explicitly visible but are conceptually present in the form of continuous optimization and in the calculation of gradients during backpropagation.

### Example

Consider the problem of finding the area under a curve, which is a fundamental concept in machine learning for evaluating model performance (e.g., calculating the area under the ROC curve (AUC) for classification problems). If $f(x)$ represents the curve, the area under $f(x)$ from $a$ to $b$ can be computed by the integral:

$$
\text{Area} = \int_{a}^{b} f(x) \, dx
$$

## Other Frequently Used Notations

This integral computes the total area under $f(x)$ between $a$ and $b$, providing a measure of the model's performance over that interval.

Integrals, along with summation and product notations, form the backbone of many mathematical operations in machine learning, from theoretical underpinnings to practical applications in data analysis, model evaluation, and optimization strategies.

Beyond summation (Σ), product (Π), and integral (∫) notations, there are several other mathematical symbols and concepts that are frequently used in machine learning and statistics. These include:

### Gradient (∇)

The gradient is a vector operation that represents the direction and rate of the fastest increase of a scalar function. In machine learning, the gradient is crucial for optimization algorithms like gradient descent, which is used to minimize loss functions. The gradient of a function $f(x_1, x_2, \ldots, x_n)$ with respect to its variables is denoted by:

$$
\nabla f = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n} \right)
$$

### Partial Derivative (∂)

The partial derivative represents the rate of change of a function of multiple variables with respect to one of those variables, keeping the others constant. It's denoted by the symbol ∂. Partial derivatives are essential in the calculation of gradients and in the optimization of machine learning models.

### Expectation (E)

The expectation or expected value of a random variable is a fundamental concept in probability and statistics, denoted by $E[X]$ for a random variable $X$. It represents the average or mean value that $X$ takes over its probability distribution and is crucial in understanding the behavior of models, especially in probabilistic settings.

### Variance (Var) and Standard Deviation (σ)

Variance measures the spread of a random variable's values and is denoted by $Var(X)$ or $\sigma^2$ for a random variable $X$. The standard deviation, $\sigma$, is the square root of the variance and provides a measure of the dispersion of data points around their mean value. These concepts are vital in assessing the reliability and performance of models.

### Covariance and Correlation

Covariance and correlation measure the relationship between two random variables. Covariance indicates the direction of the linear relationship between variables, while correlation measures both the strength and direction of this linear relationship. Understanding these relationships is essential in features selection and in modeling the interactions between variables.

### Big O Notation (O)

Big O notation is used to describe the computational complexity of algorithms, which is crucial in machine learning for understanding the scalability and efficiency of models and algorithms. For example, an algorithm with a complexity of $O(n^2)$ means its execution time or space requirements increase quadratically as the input size $n$ increases.

### Matrix Notations and Operations

Matrices and vectors are fundamental in machine learning for representing and manipulating data. Operations such as matrix multiplication, transpose, and inversion are essential for linear algebra, which underpins many machine learning algorithms, including neural networks, PCA (Principal Component Analysis), and SVMs (Support Vector Machines).

Each of these mathematical concepts plays a crucial role in the formulation, analysis, and implementation of machine learning algorithms. They provide the theoretical foundation for understanding model behavior, optimizing performance, and evaluating outcomes in a wide range of applications.

## Matrix Calculating

Matrix multiplication is a fundamental operation in linear algebra with extensive applications in mathematics, physics, engineering, computer science, and particularly in machine learning and data analysis. The way matrix multiplication is defined—by taking the dot product of rows and columns—might seem arbitrary at first, but it's designed to capture several important mathematical and practical concepts.

Understanding how to perform basic operations with matrices—addition, subtraction, multiplication, and division (in a sense)—is crucial in linear algebra, which is foundational for many areas of mathematics, physics, engineering, and especially machine learning. Here's a brief overview of each operation:

$$
\begin{pmatrix}  
  a_{11} & \cdots & a_{1j} \\\\
  \vdots & \ddots & \vdots \\\\  
  a_{i1} & \cdots & a_{ij}  
\end{pmatrix}
$$

Each element within the matrix is a pair $(i,j)$, where $i$ is the row index and $j$ is the column index.

### Matrix Addition and Subtraction

Matrix addition and subtraction are straightforward operations that are performed element-wise. This means you add or subtract the corresponding elements of the matrices. For these operations to be defined, the matrices must be of the same dimensions.

- **Addition**: If $A$ and $B$ are matrices of the same size, their sum $C = A + B$ is a matrix where each element $c_{ij}$ is the sum of $a_{ij} + b_{ij}$.

- **Subtraction**: Similarly, the difference $C = A - B$ is a matrix where each element $c_{ij}$ is the difference $a_{ij} - b_{ij}$.

#### Example:

If $A = \begin{pmatrix} 1 & 2 \\\\ 3 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 5 & 6 \\\\ 7 & 8 \end{pmatrix}$, then

- $A + B = \begin{pmatrix} 1+5 & 2+6 \\\\ 3+7 & 4+8 \end{pmatrix} = \begin{pmatrix} 6 & 8 \\\\ 10 & 12 \end{pmatrix}$
- $A - B = \begin{pmatrix} 1-5 & 2-6 \\\\ 3-7 & 4-8 \end{pmatrix} = \begin{pmatrix} -4 & -4 \\\\ -4 & -4 \end{pmatrix}$

### Matrix Multiplication

Matrix multiplication is more complex and involves a dot product of rows and columns. For two matrices $A$ and $B$ to be multiplied, the number of columns in $A$ must equal the number of rows in $B$. If $A$ is an $m \times n$ matrix and $B$ is an $n \times p$ matrix, the resulting matrix $C = AB$ will be an $m \times p$ matrix where each element $c_{ij}$ is computed as the dot product of the $i$th row of $A$ and the $j$th column of $B$.

#### Example:

If $A = \begin{pmatrix} 1 & 2 \\\\ 3 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 5 & 6 \\\\ 7 & 8 \end{pmatrix}$, then

- $AB = \begin{pmatrix} (1× 5 + 2× 7) & (1× 6 + 2× 8) \\\\ (3× 5 + 4× 7) & (3× 6 + 4× 8) \end{pmatrix} = \begin{pmatrix} 19 & 22 \\\\ 43 & 50 \end{pmatrix}$

### Matrix Division

Matrix division as such doesn't exist in the way we think of division for real numbers. Instead, we talk about the inverse of a matrix. For matrix $A$ to "divide" another matrix $B$, you would multiply $B$ by the inverse of $A$, denoted as $A^{-1}$. This operation is only defined for square matrices (same number of rows and columns), and not all square matrices have an inverse.

- **Multiplying by the Inverse**: If you want to solve for $X$ in $AX = B$, you can multiply both sides by $A^{-1}$, assuming $A^{-1}$ exists, to get $X = A^{-1}B$.

#### Example:

If $A = \begin{pmatrix} 1 & 2 \\\\ 3 & 4 \end{pmatrix}$, and its inverse $A^{-1} = \begin{pmatrix} -2 & 1 \\\\ 1.5 & -0.5 \end{pmatrix}$, and you want to "divide" $B = \begin{pmatrix} 5 & 6 \\\\ 7 & 8 \end{pmatrix}$ by $A$, you would compute $A^{-1}B$.

### Key Points

- **Addition/Subtraction**: Element-wise operation requiring matrices of the same dimensions.
- **Multiplication**: Involves the dot product of rows and columns, requiring the number of columns in the first matrix to equal the number of rows in the second.
- **Division**: Not directly defined, but involves multiplying by the inverse of a matrix.


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
