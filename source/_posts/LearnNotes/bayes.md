---
toc: true
url: bayes
covercopy: <a href="https://www.analyticsvidhya.com/blog/2022/10/frequently-asked-interview-questions-on-naive-bayes-classifier/">© Aman Preet Gulati</a>
priority: 10000
date: 2024-02-01 23:20:50
title: "Naive Bayes and Bayes NetWork"
ytitle:  "Naive Bayes and Bayes NetWork"
description: "Naive Bayes and Bayes NetWork"
excerpt: "Naive Bayes and Bayes NetWork"
tags: []
category: []
cover: "https://editor.analyticsvidhya.com/uploads/839681.png"
thumbnail: "https://editor.analyticsvidhya.com/uploads/839681.png"
---

## Naïve Bayes

!!! note The problem with likelihood: Too many words
    What does it mean to say that the words, x, have a particular probability?<br>
    Suppose our training corpus contains two sample emails:<br>
    - Email1: Y = spam, X ="Hi there man – feel the vitality! Nice meeting you…"<br>
    - Email2: Y = ham, X ="This needs to be in production by early afternoon…"<br>
    
    Our test corpus is just one email:<br>
    - Email1: X="Hi! You can receive within days an approved prescription for increased vitality and stamina"<br>
    How can we estimate P(X="Hi! You can receive within days an approved prescription for increased vitality and stamina"|Y = spam)?<br>

One thing we could do is:


1. $P(W = \text{"hi"} | Y = \text{spam}), P(W = \text{"hi"} | Y = \text{ham})$
2. $P(W = \text{"vitality"} | Y = \text{spam}), P(W = \text{"vitality"} | Y = \text{ham})$
3. $P(W = \text{"production"} | Y = \text{spam}), P(W = \text{"production"} | Y = \text{ham})$

Then the approximation formula for $P(X | Y)$ is given by:

$$ P(X = x | Y = y) \approx \prod_{i=1}^{n} P(W = w_i | Y = y) $$

In this context, $W$ represents a word in a document, $X$ represents the document itself, $Y$ represents the class (spam or ham), $w_i$ represents the $i$-th word in the document, and $n$ is the total number of words in the document. The product is taken over all words in the document, assuming that the words are conditionally independent of each other given the class label $Y$.

!!! question Why naïve Bayes is "naïve"?
    We call this model "naïve Bayes" because the words aren't really conditionally independent given the label. For example, the sequence "for you" is more common in spam emails than it would be if the words "for" and "you" were conditionally independent.<br>
    **True Statement**:<br>
        - ***P(X = for you|Y= Spam > P( W = for |Y = Spam)(P = you |= Spam)***<br>
    The naïve Bayes approximation simply says: estimating the likelihood of every word sequence is too hard, so for computational reasons, we'll pretend that sequence probability doesn't matter.<br>
    
    **Naïve Bayes Approximation**:<br>
        - ***P(X = for you |Y = Spam) ≈ P(W = for |Y = Spam)P( W= you |Y= Spam)***<br>
    We use naïve Bayes a lot because, even though we know it's wrong, it gives us computationally efficient algorithms that work remarkably well in practice. 


- Floating-point underflow
    That equation has a computational issue. Suppose that the probability of any given word is roughly ***P(W = W~i~|Y = y) ≈ 10^-3^***, and suppose that there are 103 words in an email. Then ***∏^n^~i=1~ P(W = W~i~|Y = y) = 10^-309^***,which gets rounded off to zero. This phenomenon is called "floating-point underflow".
- Solution
    $f(x) = \underset{y}{\mathrm{argmax}} \left( \ln P(Y = y) + \sum^n_{i=1} \ln P(W = w_i | Y = y) \right)$

### Reducing the naivety of naïve Bayes
Remember that the bag-of-words model is unable to represent this fact: 
- **True Statement**:
    - ***P(X = for you|Y= Spam > P( W = for |Y = Spam)(P = you |= Spam)***
    Though the bag-of-words model can’t represent that fact, we can represent it using a slightly more sophisticated naïve Bayes model, called a "bigram" model.

- N-Grams:
    - Unigram: a unigram (1-gram) is an isolated word, e.g., “you”
    - Bigram: a bigram (2-gram) is a pair of words, e.g., “for you”
    - Trigram: a trigram (3-gram) is a triplet of words, e.g., “prescription for you”
    - 4-gram: a 4-gram is a 4-tuple of words, e.g., “approved prescription for you”

!!! note Bigram naïve Bayes
    A bigram naïve Bayes model approximates the bigrams as conditionally independent, instead of the unigrams. For example,<br>
    ***P(X = “approved prescription for you” | Y= Spam) ≈***<br>
    ***P(B = “approved prescription” |Y = Spam) ×***<br>
    ***P(B = “prescription for” | Y= Spam) ×***<br>
    ***P(B = “for you” |Y = Spam)***


- The naïve Bayes model has two types of parameters:
    - The a priori parameters: ***P(Y = y)***
    - The likelihood parameters: ***P(W = w~i~| Y = y)***
- In order to create a naïve Bayes classifiers, we must somehow estimate the numerical values of those parameters.
- Model parameters: feature likelihoods ***P(Word | Class)*** and priors ***P(Class)***

### Parameter estimation: Prior

The prior, ***P(x)***, is usually estimated in one of two ways.
- If we believe that the test corpus is like the training corpus, then we just use frequencies in the training corpus:
$$
P(Y = Spam) = \frac{Docs(Y=Spam)}{Docs(Y=Spam) + Docs(Y \neq Spam)}
$$
where ***Docs(Y=Spam)*** means the number of documents in the training corpus that have the label Y=Spam.
- If we believe that the test corpus is different from the training corpus, then we set ***P(Y = Spam)*** = the frequency with which we believe spam will occur in the test corpus.

### Parameter estimation: Likelihood

The likelihood, ***P(W = w~i~|Y = y), is also estimated by counting. The “maximum likelihood estimate of the likelihood parameter” is the most intuitively obvious estimate:
$$
P(W=w_i| Y = Spam) = \frac{Count(W=w_i, Y = Spam)}{Count(Y = Spam)}
$$
where ***Count(W=w~i~, Y = Spam)*** means the number of times that the word ***w~i~*** occurs in the Spam portion of the training corpus, and ***Count(Y = Spam)*** is the total number of words in the Spam portion.

### Laplace Smoothing for Naïve Bayes

One of the biggest challenge for Bayes is it can't handle unobserved situation.

- The basic idea: add $k$ “unobserved observations” to the count of every unigram
  - If a word occurs 2000 times in the training data, Count = 2000+k
  - If a word occur once in training data, Count = 1+k
  - If a word never occurs in the training data, then it gets a pseudo-Count of $k$

- Estimated probability of a word that occurred Count(w) times in the training data:
  $$ P(W = w) = \frac{k + \text{Count}(W = w)}{k + \sum_v (k + \text{Count}(W = v))} $$

- Estimated probability of a word that never occurred in the training data (an “out of vocabulary” or OOV word):
  $$ P(W = \text{OOV}) = \frac{k}{k + \sum_v (k + \text{Count}(W = v))} $$

- Notice that
  $$ P(W = \text{OOV}) + \sum_w P(W = w) = 1 $$



## Bayesian Networks































<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
