---
toc: true
url: ai_learning
covercopy: <a href="https://www.analyticsvidhya.com/blog/2020/12/understand-machine-learning-and-its-end-to-end-process/">© Shanthababu Pandian</a>
priority: 10000
date: 2024-02-02 12:58:50
title: "Learning Progress"
ytitle: "Learning Progress" 
description: "Learning Progress"
excerpt: "Learning Progress"
tags: [Machine Learning, Data Science]
category: [Notes, Class, UIUC, AI]
cover: "https://editor.analyticsvidhya.com/uploads/52606ML-stage.png"
thumbnail: "https://editor.analyticsvidhya.com/uploads/52606ML-stage.png"
---

## Learning

!!! note Biological inspiration: Long-term potentiation
    1. A synapse is repeatedly stimulated<br>
    2. More dendritic receptors<br>
    3. More neurotransmitters<br>
    4. A stronger link between neurons

- Mathematical Model this Biological Learning Model:
    - ***X*** = input signal; ***f(X)*** = output signal 
    - **Learning** = adjust the parameters of the learning machine so that ***f(x)*** becomes the function we want
- Mathematical Model of Supervised Learning
    - ***D = {(x~1~, y~1~), ..., (x~n~, y~n~)}*** = training dataset containing pairs of (example signal ***x~i~***, desired system output ***y~i~***) 
    - **Supervised Learning** = adjust parameters of the learner to minimize ***E[ℓ(Y, f(X))]***
    - ***ℓ***: loss function

|![loss-function](https://imgur.com/228ikan.png)|
|:-:|

### Decision tree learning: An example

The Titanic sank. You were rescued. You want to know if your friend was also rescued. You can’t find them. Can you use machine learning methods to estimate the probability that your friend survived? (Calculate the possibility of your friend also be rescued)

1. Gather data about as many of the passengers as you can.
    - X = variables that describe the passenger, e.g., age, gender, number of siblings on board.
    - Y = 1 if the person is known to have survived
2. Learn a function, f(X), that matches the known data as well as possible
3. Apply f(x) to your friend’s facts, to estimate their probability of survival

**Decision-tree learning***:
- 1st branch = variable that best distinguishes between groups with higher vs. lower survival rates (e.g., gender)
- 2nd branch = variable that best subdivides the remaining group
- Quit when all people in a group have the same outcome, or when the group is too small to be reliably subdivided.

|![Decision-tree for Titanic](https://upload.wikimedia.org/wikipedia/commons/e/eb/Decision_Tree.jpg)|
|:-:|
|[© wikipedia](https://en.m.wikipedia.org/wiki/File:Decision_Tree.jpg)|

In each leaf node of this tree:
- Number on the left = probability of survival
- Number on the right = percentage of all known cases that are explained by this node


- A decision tree is an example of a parametric learner
- The function ***f(x)*** is determined by some learned parameters
- In this case, the parameters are:
- Should this node split, or not?
- If so, which tokens go to the right-hand child?
- If not, what is ***f(x)*** at the current node?
- Titanic shipwreck example:
    - &Theta; = [Y, female, Y, age ≤ 9.5, N, f(x) = 0.73, …]


!!! Note A mathematical definition of learning
    - Environment: there are two random variables, X and Y, that are jointly distributed according to
        - ***P(X,Y)***
    - Data: ***P(X, Y)*** is unknown, but we have a sample of training data
        - ***D = {(x~1~, y~1~), ..., (x~n~, y~n~)}*** 
    - Objective: We would like a function � that minimizes the expected value of some loss function, ***ℓ(Y , f(x))*** :
        - ***ℛ = E[ℓ(Y, f(x))]***
    - Definition of learning: Learning is the task of estimating the function ***f***, given knowledge of ***D***.

### Training vs. Test Corpora

- **Training Corpus** = a set of data that you use in order to optimize the parameters of your classifier (for example, optimize which features you measure, how you use those features to make decisions, and so on).
    - Measuring the training corpus accuracy is important for debugging: if your training algorithm is working, then training corpus error rate should always go down.
- **Test Corpus** = a set of data that is non-overlapping with the training set (none of the test tokens are also in the training dataset) that you can use to measure the error rate.
    - Measuring the test corpus error rate is the only way to estimate how your classifier will work on new data (data that you’ve never yet seen)
- **Training error** is sometimes called "optimization error". It happens because you haven’t finished optimizing your parameters.
- **Test error** = ==optimization error + generalization error==
- **Evaluation Test Corpus** = a dataset that is used only to test the ONE classifier that does best on DevTest. From this corpus, you learn how well your classifier will perform in the real world.

### Early stopping

- **Learning**: Given $\mathcal{D} = \{(x_1, y_1), \ldots, (x_n, y_n)\}$, find the function $f(X)$ that minimizes some measure of risk.
- **Empirical risk**: a.k.a. training corpus error:
    - $R_{\text{emp}} = \frac{1}{n} \sum_{i=1}^{n} \ell(y_i, f(x_i))$
- **True risk**, a.k.a. expected test corpus error:
    - $R = \mathbb{E}[\ell(Y, f(X))] = R_{\text{emp}} + R_{\text{generalization}}$

- Usually, minimum test error and minimum dev error don’t occur at the same time
- … but early stopping based on the test set is cheating,
- … so early stopping based on the dev set is the best we can do w/o cheating.





## Summary
- **Biological inspiration**: Neurons that fire together wire together. Given enough training examples ***(x~i~, y~i~)***, can we learn a desired function so that ***f(x) ≈ y***?
- **Classification tree**: Learn a sequence of if-then statements that computes ***f(x) ≈ y***
- **Mathematical definition of supervised learning**: Given a training dataset, ***D = {(x~1~, y~1~), ..., (x~n~, y~n~)}*** , find a function ***f*** that minimizes the risk, ***ℛ = E[ℓ(Y, f(x))]***.
- **Overtraining**: $ℛ_ {emp} = \frac{1}{n} \sum^n_{i=1} ℓ*y_i, f(x_i))$ reaches zero if you train long enough.
- **Early Stopping**: Stop when error rate on the dev set reaches a minimum



<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
