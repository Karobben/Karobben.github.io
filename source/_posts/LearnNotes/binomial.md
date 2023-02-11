---
toc: true
url: binomial
covercopy: <a href="https://www.onlinemathlearning.com/binomial-distribution.html">© onlinemathlearning.com</a>
priority: 10000
date: 2021-04-08 15:58:10
title: "Binomial Distribution | Introduction and examples"
ytitle: "二项式分布 | 介绍和简单例子"
description: "binomial distribution with examples"
excerpt: "What is binomial and binomial distribution. $b(x; n, P) = C_{n}^{x} * P^ x  (1 - P)^{(n - x)}$"
tags: [Statistic, Distribution]
category: [Notes, Statistic, Distribution]
cover: "https://www.onlinemathlearning.com/image-files/binomial-distribution-formula.png"
thumbnail: "https://www.onlinemathlearning.com/image-files/binomial-distribution-formula.png"
---

## What Is Binomial

Video tutorial: [Wrath of Math, 2017, YouTube](https://www.youtube.com/watch?v=KsmcvwDb9iQ)

Binomial is a simplistic polynomial.
It has two terms, which could be numeral, variable, or combined element.
for example:
$3x +4$
$x+5$
$x^2 + 5x$

As you can see, they are all binomials.

## What Is Binomial Experiment

>A binomial experiment is a statistical experiment that has the following properties:
> - The experiment consists of n repeated trials.
> - Each trial can result in just two possible outcomes. We call one of these outcomes a success and the other, a failure.
> - The probability of success, denoted by P, is the same on every trial.
> - The trials are independent; that is, the outcome on one trial does not affect the outcome on other trials.
> Cite: Stat Trek[^Stat_Trek]

[^Stat_Trek]: [Stat_Trek, Binomial Probability Distribution](https://stattrek.com/probability-distributions/binomial.aspx)

For example, the experiment about flipping a coin and counting the probabilities of each side.

## Binomial Distribution

> A binomial random variable is the number of successes x in n repeated trials of a binomial experiment. The probability distribution of a binomial random variable is called a binomial distribution. [^Stat_Trek]

For example, when we flip a coin **two times**,
We can have the results:
|Result| Probability|
|:-|:-|
|Head * 2| 25%|
|Head, Tail| 50%|
|Tail * 2|25%|

$$
b(x; n, P) = C_{n}^{x} * P^ x  (1 - P)^{(n - x)}
$$
$$
C_{n}^{x} = \frac{ n!}{ x! (n - x)! }
$$

The properties of the Binomial Distribution:
> - The mean of the distribution $μx$ is equal to $n \times P$ .
> - The variance $σ2x$ is $nP( 1 - P) $.
> - The standard deviation $σx$ is $\sqrt{nP( 1 - P ) }$.
> AND
>- $x$: The number of successes that result from the binomial experiment.
>- $n$: The number of trials in the binomial experiment.
>- $P$: The probability of success on an individual trial.
>- $Q$: The probability of failure on an individual trial. (This is equal to 1 - P.)
>- $n!$: The factorial of n (also known as n factorial).
>- $b(x; n, P)$: Binomial probability - the probability that an $n$ trial binomial experiment results in exactly $x$ successes, when the probability of success on an individual trial is $P$.
>- $C_n^x$: The number of combinations of $n$ things, taken $x$ at a time.
> Cite: Stat Trek[^Stat_Trek]

## Example 1:
Suppose a die is tossed 5 times. What is the probability of getting exactly 2 fours?[^Stat_Trek]

So, we have 5 times, which means $n = 5$;
We need exactly four * 2, which means $x = 2$;
The probability of a single trial is 1/6, which give $P = 1/6$

According to the function above, we can have:
$b(2; 5, 1/6) = C_{5}^{2} * (1/6)^ 2  (1 - (1/6))^{(5 - 2)}$

In R, we can calculate the binomial with the function `dbinom` as `dbinom(2, 5, 1/6)`.
Now we have the results:
$b(2; 5, 1/6) = 0.160751$

## Example 2:

$b(x; n, P) = \frac{ n!}{ x! (n - x)!} \times P^ x  (1 - P)^{(n - x)}$

Let's back to the coin.
When we flip it once, and the chances of **Head** is obviously 50%.
Which is:

$b(1; 1, 1/2) = \frac{ 1!}{ 1! (1 - 1)!} * 0.5^ 1  (1 - 1)^{(1 - 1)}$
$b(1; 1, 1/2) = 1 * 0.5 * 1$
$b(1; 1, 1/2) = 0.5$

When we flip it twice, we can have 4 results: HH, HT, TH, TT
- the chance we have only one head is `dbinom(1, 2, 1/2)`, which is 50%. (HT, TH)
- the chance we have two heads is `dbinom(2, 2, 1/2)`, which is 25%. (HH)
- the chance we have *heads* from 0 to all is:
  0.25, 0.5, 0.25, which means
  $1: 2:1$
Now, let's try to flip it triple times, so we have 8 results:
<pre>
HHH, HHT, HTH, THH
HTT, THT, TTH, TTT
</pre>
- one head: HTT, THT, TTH: $3/8 = 0.375$
  $b(1; 3, 1/2) = \frac{ 3!}{ 1! (3 - 1)!} \times 0.5^ 1  (1 - 0.5)^{(3 - 1)}$
  $b(1; 3, 1/2) = 3 \times 0.5 \times 0.25$
  $b(1; 3, 1/2) = 0.375$

- two head: HHT, HTH, THH: $3/8 = 0.275$
  $b(2; 3, 1/2) = \frac{ 3!}{ 2! (3 - 2)!} \times 0.5^ 2  (1 - 0.5)^{(3 - 2)}$
  $b(2; 3, 1/2) = 3 \times 0.25 \times 0.5$
  $b(2; 3, 1/2) = 0.375$

- the chance we have *head* from 0 to all is:
  0.125, 0.375, 0.375, 0.125, which means
  $1:3:3:1$

With the increase of the flipping number to 10, for instance, we can have the ratio:
```r
for( n in c(1:10)){
  Result = c()
  for(x in c(0:n)){
    Result = c(Result, dbinom(x, n, 1/2)/ dbinom(0, n, 1/2))
  }
  print(Result)
}
```
<pre>
                 1
                1 1
               1 2 1
             1  3 3  1
            1 4  6  4 1
          1 5  10  10  5 1
        1 6  15  20  15  6 1
      1 7  21  35  35  21  7 1
    1 8  28  56  70  56  28  8 1
  1 9  36  84 126 126  84  36 9 1
1 10 45 120 210 252 210 120 45 10 1
</pre>


{% echarts 400 '85%' %}
option = {
    xAxis: {
        type: 'category',
        name: 'Concentration of the Substrate (S)',
        nameLocation: "middle",
        nameTextStyle: {fontSize: 25,
          padding: [10, 0, 0, 0] ,
            },
        data: [0,1,2,3,4,5,6,7,8,9,10,11]
    },
    yAxis: {
        type: 'value',
        name: "Velacity (V0)",
        max: 330 ,
        nameLocation: "middle",
        nameTextStyle: {fontSize: 25,
            padding: [0, 0, 10, 0] ,
        },
    },
    legend: {
        data: ['n = 10', "n = 7"]
    },

    series: [{
        name: 'n = 10',
        smooth: true,
        areaStyle: {},
        data: [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1],
        type: 'line',
    },
  {
          name: 'n = 7',
          smooth: true,
          areaStyle: {},
          data: [1, 7,  21,  35,  35,  21,  7, 1],
          type: 'line',
  }
      ]
  };
{% endecharts %}


# Poisson theorem[^cai_2016]

[^cai_2016]: [蔡高玉, 2016, 浅谈二项分布及其应用, 《考试周刊》 2016年A5期 期刊](https://www.doc88.com/p-0159698250459.html)

When The $n$ is infinite large, we can have:
$$
\lim_ {n \to \infty} C_ n ^x P^ x  (1 - P)^{(n - x)}, x = 0, 1, 2, ...
$$
Let's say, $nP = \lambda $
When the $n$ is very large and the $P$ is infinite small, we can have:
$$
C_ n ^x P^ x  (1 - P)^{(n - x)} \approx \frac{\lambda ^ x}{x!} e^ {-\lambda}
$$

I have no idea how it works. So, I'm gonna stopping here.
