---
toc: true
url: AI1
covercopy: © Karobben
priority: 10000
date: 2024-01-26 01:22:21
title: "Artificial Intelligent 1"
ytitle: "Artificial Intelligent 1"
description: "Artificial Intelligent"
excerpt: "Artificial Intelligent"
tags: []
category: []
cover: ""
thumbnail: ""
---

## Random Variable

Probability:
- Exp1: $Pr(A) > 0$ which means that A has non-negative probability.
- Exp2: $Pr(A) = 1$ means when event A occurs, the probability is 1.
- Exp3: $Pr(A \cap B) = Pr(A) × Pr(B)$ when events A and B are independent.

!!! Question What is <b>Random Variable</b>?
    - We use <b>capital letters</b> to denote the random variable
    - We use a small letter to denote a particular outcome of the experiment

$P(X=x)$ means the probability of the occurs for value x. Here $P(X=x)$ is a ==number==, the $P(X)$ is a distribution.

!!! note Example 
    Event = [Cloud, Cloud, Rain]
    In this Weather event P(X), it the probability of:
        - Cloud: $P(X=Cloud) = \frac{2}{3}$.
        - Rain: $P(X=Rain) = \frac{1}{3}$
        - Sun:  $P(X=sun) = 0$

The random variable we used in the example above is ==Discrete== random variable, but sometimes we have to use continues random variable. For example: $X \in R$ (the set of all positive real numbers)

Because we have two types of random variable, the function for calculating the sun of all possible variables are different:
- **Probability Mass Function** (pmf): For discrete random variable
    - $0 \leqslant P(X=x)$
    - $ 1 = \sum _x{P(X=x)}$
- **Probability Density Function** (pdf):
    - $0 \leqslant P(X=x)$
    - $ 1 = \int_{-\infty}^\infty {P (X=x)dx}$



<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
