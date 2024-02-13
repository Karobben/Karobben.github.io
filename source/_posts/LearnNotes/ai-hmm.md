---
toc: true
url: ai_hmm
covercopy: © Karobben
priority: 10000
date: 2024-02-12 00:59:06
title: "Hidden Markov Model"
ytitle: "Hidden Markov Model"
description: "Hidden Markov Model"
excerpt: "Hidden Markov Model"
tags: []
category: []
cover: "https://artint.info/3e/html/x83.png"
thumbnail: "https://artint.info/3e/html/x83.png"
---

![](https://imgur.com/oMmL1Ln.png)

A Hidden Markov Model is a Bayes Network with these assumptions:
• *Y~t~* depends only on *Y~t-1~*
• *X~t~* depends only on *Y~t~*

The belief network conveys the independence assumption: 
$$
for\ all\ i \geq 0, P(S_{i+1}|S_i) = P (S_1|S_0)
$$

$$
P(S_i = s) = \sum_{s'} P(S_{i+1} = s \mid S_i = s') * P(S_i = s')
$$

In the context of the equation you're referring to, \( s \) and \( s' \) represent states in a Markov chain. Typically, \( s \) is used to denote the current state, while \( s' \) (read as "s prime") denotes a subsequent or different state that the system can transition into from the current state \( s \). 

The summation over \( s' \) in the equation indicates that you're summing over all possible subsequent states that the system can transition to from the current state \( s \). This is part of the definition of a stationary distribution for a Markov chain, where the probability of being in any given state \( s \) is equal to the sum of the probabilities of transitioning to state \( s \) from all possible previous states \( s' \), weighted by the probability of being in state \( s' \) at the previous time step.

background-color:#38393d;
<style>
pre {
  color: #5fd381;
}
</style>
