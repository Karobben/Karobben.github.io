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
cover: "https://imgur.com/25I7oBF.png"
thumbnail: "https://imgur.com/25I7oBF.png"
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
    - If *X* is a **discrete random variable**, then *P(X)* is its **probability mass function (pmf)**.
    - A probability mass is just a probability. *P(X=x) = Pr(X=x)* is the just the probability of the outcome *X = x* Thus:
    - $0 \leqslant P(X=x)$
    - $ 1 = \sum _x{P(X=x)}$
- **Probability Density Function** (pdf):
    - If *X* is a **density random variable**, then *P(x)* is its **probability density function (pdf)**.
    - A probability density is NOT a probability. Instead, we define it as a density $P(X=x) = \frac{d}{dx} Pr(X \leqslant x)$
    - $0 \leqslant P(X=x)$
    - $ 1 = \int_{-\infty}^\infty {P (X=x)dx}$

### Jointly Random Variables

- Two or three random variables are "jointly random" if they are both outcomes of the same experiment.
- For example, here are the temperature (Y, in °C), and precipitation (X, symbolic) for six days in Urbana:

| Date       | X=Temperature (°C) | Y=Precipitation |
|------------|---------------------|-----------------|
| January 11 | 4                   | cloud           |
| January 12 | 1                   | cloud           |
| January 13 | -2                  | snow            |
| January 14 | -3                  | cloud           |
| January 15 | -3                  | clear           |
| January 16 | 4                   | rain            |

For this table, we could have joint random variables *P(X=x, Y=y)*:

| P(X=x,Y=y) | snow | rain | cloud | clear |
|------------|------|------|-------|-------|
| -3         | 0    | 0    | 1/6   | 1/6   |
| -2         | 1/6  | 0    | 0     | 0     |
| 1          | 0    | 0    | 1/6   | 0     |
| 4          | 0    | 1/6  | 1/6   | 0     |

#### Notation: Vectors and Matrices

- A normal-font capital letter (*X*) is a random variable, which is a function mapping from the outcome of an experiment to a measurement
- A normal-font small letter (*x*) is a scalar instance
- A boldface small letter (***x***) is a vector instance
- A boldface capital letter (***X***) is a matrix instance

*P(X=**x**)* is the probability that random variable *X* takes the value of the vector ***x***. This is just a shorthand for the joint distribution of *x~1~, x~2~, .., x~n~*

|![vector ***x***](https://imgur.com/FRHL0fI.png)|
|:-:|

|![](https://imgur.com/ihgeuXc.png)|
|:-:|
|When ***X*** is a random matrix|

### Marginal Distributions

Suppose we know the joint distribution *P(X,Y)*. We want to find the two **marginal distributions** *P(X)*:
- If the unwanted variable is discrete, we marginalize by adding:
    - $P(X) = \sum_ y P(X,Y=y)$
- If the unwanted variable is continuous, we marginalize by integrating:
    - $P(X) = \int P(X,Y=y)$

Backing the table above, we could know that the marginal distributions of:
- *P(X)* = 1/6 + 1/6 = 1/3; 1/6; 1/6; 1/6 + 1/6 = 1/3
- *P(Y)* = 1/6; 1/6; 1/6 + 1/6 + 1/6 = 1/2; 1/6

PS: Some place also write *P(X)* as *P~X~(X)* or *P~X~(i)* and *P(Y)* as *P~Y~(Y)* or *P~Y~(j)*.

### Joint and Conditional distributions

With the joint possibility and marginal possibility, we could now calculating the Joint and Conditional distributions, which is *P(Y|X)*
- *P(Y|X)* is the probability (or pdf) that *Y = y* happens, given that *X = x* happens, over all *x* and *y*. This is called the **conditional distribution** of *Y* given *X*.
- *P(X|Y)* is the conditional probability distribution of outcomes *P(X=x|Y=y)*
- The conditional is the joint divided by the marginal:
    - $P(X=x|Y=y) = \frac{P(X = x, Y = y)}{P(Y= y)}$ 


!!! Note Exp of Joint and Conditional Distribution *P(X|Y = cloud)*
    $P(X|Y=could) = \frac{P(X, Y = y)}{P(Y = cloud)}$
    
    $=\frac{\frac{1}{6}\ \ 0\ \ \frac{1}{6}\ \ \frac{1}{6}}{\frac{1}{2}}$
    
    So, the result is a vector = {1/3, 0, 1/3, 1/3}

According to the example, we could know that: ==Joint = Conditional×Marginal==; which is:
$$
P(X,Y) = P(X|Y)P(Y)
$$


### Independent Random Variables 

- Two random variables are said to be independent, which means *P(X|Y) = P(X)*
    In other words, knowing the value of *Y* tells you nothing about the value of *X*.
- According to this, we can also know:
    - $\because$ *P(X,Y) = P(X|Y)P(Y)*
    - $\therefore$ *P(X,Y) = P(X)P(Y)*
- *Pr(A⋀B) = Pr(A)Pr(B)*


### Expectation

The expected value of a function is its weighted average, weighted by its pmf or pdf.

- For discrete X and Y:
    $ E[f(X, Y)] = \sum_{x,y} f(x, y)P(X = x, Y = y) $
- If X is continuous:
    $ E[f(X, Y)] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y)P(X = x, Y = y) \,dx\,dy $


### Covariance

The covariance of two random variables is the expected product of their deviations:

**Covar(X,Y) = E[(X- E[X])(Y-E[Y])]**

Covariance Matrix:
Suppose *X = [X~1~, … , X~n~]* is a random vector. Its matrix of variances and covariances (a.k.a. covariance matrix) is

|![Covariance Matrix](https://imgur.com/AHw4vkP.png)|
|:-:|

## Decision Theory

- Suppose we have an experiment with two random variables, X and Y.
    - X is something we can observe, like the words in an email.
    - Y is something we can’t observe, but we want to know. For example, Y=1 means the email is spam (junk mail), Y=0 means it’s ham (desirable mail).
- Can we train an AI to read the email, and determine whether it’s spam or not?

In this case, we have:

- *Y* = the correct label
    - *Y* = the correct label as a random variable (“in general”)
    - *y* = the label observed in a particular experiment (“in particular”)
- *f(X)* = the decision that we make, after observing the datum, *X*.
    - *f(X)* = the function applied to random variable *X* (“in general”)
    - *f(x)* = the function applied to a particular value of *x* (“in particular”)

### Deciding how to Decide: Loss and Risk
 

- Suppose that deciding $f(x)$, when the correct label is $Y = y$, costs us a certain amount of money (or prestige, or safety, or points, or whatever) – call that the loss, $L(f(x), y)$

- In general, we would like to lose as few points as possible (negative losses are good...)

- Define the risk, $R(f)$, to be the expected loss incurred by using the decision rule $f(X)$:

$$ R(f) = E[L(f(X), Y)] = \sum_y \sum_x L(f(x), y)P(X = x, Y = y) $$

### Minimum-Risk Decisions

- If we want to the smallest average loss (the smallest risk), then our
decision rule should be
 ***f = argmin R(f)***
- In other words, for each possible *x*, we find the value of *f(x)* that minimizes our expected loss given that *x*, and that is the *f(x)* that our algorithm should produce.

#### Zero-One Loss


Suppose that $f(x)$ is an estimate of the correct label, and
- We lose one point if $f(x) \neq y$
- We lose zero points if $f(x) = y$

Then the loss function $L(f(x), y)$ is defined as:

|![Zero-One Loss](https://imgur.com/y5yAXn9.png)|
|:-:|

Then the risk is

$$ R(f) = E[L(f(X), Y)] = Pr(f(X) \neq Y) $$

#### Minimum Probability of Error 

We can minimize the probability of error by designing ***f(x)*** so that ***f(x) = 1*** when ***Y= 1*** is more probable, and ***f(x) = 0*** when ***Y= 0*** is more probable.

|![Minimum Probability of Error](https://imgur.com/qFXNGic.png)|
|:-:|

### The Bayesian Scenario

|![Bayes](https://upload.wikimedia.org/wikipedia/commons/d/d4/Thomas_Bayes.gif)|
|:-:|
|[© wikipedia]|

- Let’s use ***x~X*** to mean that ***x*** is an instance of random variable ***X***, and similarly ***y~Y***.
- In order to minimize the probability of error, we just need to know ***P(Y = y|X = x)*** for every pair of values ***x~X*** and
***y~Y***. Then we choose $f(x) = \underset{y}{argmaxP}(Y = y|X = x)$.

#### Example: spam detection 

!!! question  how can we estimate the P(Y=y|X=x)?
    - The prior probability of spam might be obvious. If 80% of all email on the internet is spam, that means that
    ***P(Y=1)=0.8, P(Y=0)=0.2***<br>
    - The probability of X given Y is also easy. Suppose we have a database full of sample emails, some known to be spam, some known to be ham. We count how often any word occurs in spam vs. ham emails, and estimate:<br>
    1. ***P(X=x|Y=1)=*** frequency of the words ***x*** in emails known to be spam<br>
    2. ***P(X=x|Y=0)=*** frequency of the words ***x*** in emails known to be ham<br>
    - Now we have ***P( X=x|Y=y)*** and ***P(Y=y)*** . How do we get ***P(Y=y|X=x)***<br>
    For solve this problem, Bayes come with an idea: **Bayes' Rule**<br>
    $P(Y=y|X=x) = \frac{P(X=x, Y=y)}{P(X=x)}$<br>
    $\frac{P(X=x|Y=y)P(Y=y)}{P(X=x)}$

### The four Bayesian probabilities

$$
P(Y=y|X=x) =\frac{P(X=x|Y=y)P(Y=y)}{P(X=x)}
$$

This equation shows the relationship among four probabilities. This equation has become so world-famous, since 1763, that these four probabilities have standard universally recognized names that you need to know:
- ***P(Y=y|X=x)*** is the a **posteriori** (after-the-fact) probability, or **posterior**
- ***P(Y=y)*** is the **a priori** (before-the-fact) probability, or **prior**
- ***P(X=x|Y=y)*** is the **likelihood**
- ***P(X=x)*** is the **evidence**
Bayes' rule: the posterior equals the prior times the likelihood over the evidence.


#### MPE = MAP

- The "minimum probability of error" (MPE) decision rule is the rule that chooses ***f(X)*** in order to minimize the probability of error:
    - ***f(x) = argmin P(Error|X = x)***
- The “maximum a posteriori” (MAP) decision rule is the rule that chooses ***f(x)*** in order to maximize the posteriori probability:
    - ***f(x) = argmin P(Y = f(x)|X = x)***
- Those two decision rules are the same: **MPE = MAP**

Using Bayes' Rule:
- MPE = MAP: to minimize the probability of error, design f(X) so that:
    $f(x) = \underset{y}{argmaxP}(Y = y|X = x)$
- Bayes' Rule 
    $P(Y=y|X=x) =\frac{P(X=x|Y=y)P(Y=y)}{P(X=x)}$
- Putting the two together:
    $f(x) = \underset{y}{argmaxP}\frac{P(X=x|Y=y)P(Y=y)}{P(X=x)}$
    $\ \ \ =\underset{y}{argmaxP}(X=x|Y=y)P(Y=y)$


- Accuracy
    When we train a classifier, the metric that we usually report is "accuracy"
    $Accuracy = \frac{n tokens\ correctly\ classified}{n\ tokens\ total}$
- Error Rate
    Equivalently, we could report error rate, which is just 1-accuracy:
    $Error Rate = \frac{n\ tokens\ incorrectly\ classified}{n\ tokens\ total}$
- Bayes Error Rate
    The "Bayes Error Rate" is the smallest possible error rate of any classifier with labels "y" and features "x":
    $Error Rate = \sum_x P(X=x)\underset{y}{min} P(Y \neq y |x=x)$
    It’s called the “Bayes error rate” because it’s the error rate of the Bayesian classifier 

## The problem with accuracy

- In most real-world problems, there is one class label that is much more frequent than all others.
    - Words: most words are nouns
    - Animals: most animals are insects
- Disease: most people are healthy
- It is therefore easy to get a very high accuracy. All you need to do is write a program that completely ignores its input, and always guesses the majority class. The accuracy of this classifier is called the "chance accuracy."
- It is sometimes very hard to beat the chance accuracy. If chance=90%, and your classifier gets 89% accuracy, is that good, or bad?

The solution: ==Confusion Matrix==:
Confusion Matrix =
• ***(m, n)^th^*** element is the number of tokens of the ***m^th^*** class that were labeled, by the classifier, as belonging to the ***n^th^*** class.

|![](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/04/Basic-Confusion-matrix.png)|
|:-:|
|[© Aniruddha Bhandari](https://www.analyticsvidhya.com/blog/2020/04/confusion-matrix-machine-learning/)|

!!! note Confusion matrix for a binary classifier
    - Suppose that the correct label is either 0 or 1. Then the confusion matrix is just 2x2.<br>
    - For example, in this box, you would write the # tokens of class 1 that were misclassified as class 0<br>
    - Than, you got TP (True Positives), FN (False Negatives), FP (False Positives), and TN (True Negative)<br>
    - The binary confusion matrix is standard in many fields, but different fields summarize its content in different ways.<br>
    - In medicine, it is summarized using Sensitivity and Specificity.
    - In information retrieval (IR) and AI, we usually summarize it using Recall and Precision.

#### Specificity and Sensitivity

- Specificity = True Negative Rate (TNR):
    - $TNR = P(f(X) =0|Y=0) = \frac{TN}{TN+FP}$
- Sensitivity = True Positive Rate (TPR):
    - $TRP = P(f(X) =1|Y=1) = \frac{TP}{TP+FN}$
- Precision:
    - $P=P(Y =1|f(x)=1)=\frac{TP}{TP+FP}$
- Recall:
    - Recall = Sensitivity = TPR:
    - $R = TRP = P(f(X) =1|Y=1) = \frac{TP}{TP+FN}$


#### Training Corpora

- Training vs. Test Corpora
    **Training Corpus**: a set of data that you use in order to optimize the parameters of your classifier (for example, optimize which features you measure, how you use those features to make decisions, and so on).
    **Test Corpus**: a set of data that is non-overlapping with the training set (none of the test tokens are also in the training dataset) that you can use to measure the accuracy.
    - Measuring the training corpus accuracy is useful for debugging: if your training algorithm is working, then training corpus accuracy should always go up.
    - Measuring the test corpus accuracy is the only way to estimate how your classifier will work on new data (data that you’ve never yet seen).

!!! note Accuracy on which corpus?
    - Large Scale Visual Recognition Challenge 2015: Each competing institution was allowed to test up to 2 different fully-trained classifiers per week.<br>
    - One institution used 30 different e-mail addresses so that they could test a lot more classifiers (200, total). One of their systems achieved <46% error rate – the competition’s best, at that time.<br>
    - Is it correct to say that that institution’s algorithm was the best?

- Training vs. development test vs. evaluation test corpora
    - **Training Corpus**: a set of data that you use in order to optimize the parameters of your classifier (for example, optimize which features you measure, what are the weights of those features, what are the thresholds, and so on). 
    - **Development Test (DevTest or Validation) Corpus**: a dataset, separate from the training dataset, on which you test 200 different fully-trained classifiers (trained, e.g., using different training algorithms, or different features) to find the best.
    - **Evaluation Test Corpus**: a dataset that is used only to test the ONE classifier that does best on DevTest. From this corpus, you learn how well your classifier will perform in the real world.


### Summary

1. Bayes Error Rate:
$$
Error Rate = \sum_x P(X=x)\underset{y}{min} P(Y \neq y |x=x)
$$

2. Confusion Matrix, Precision & Recall (Sensitivity)
$$P=P(Y =1|f(x)=1)=\frac{TP}{TP+FP}$$
$$R = TRP = P(f(X) =1|Y=1) = \frac{TP}{TP+FN}$$


#### Training Corpora



<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
