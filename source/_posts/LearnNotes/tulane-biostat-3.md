---
toc: true
url: tulane_biostat_3
priority: 10000
date: 2022-04-02 08:23:38
title: "BioStatistics with R/Python: Block 3"
ytitle: "用R做生统"
description: "Make BioStatistics easy with R or Python"
excerpt: "Make BioStatistics easy with R or Python"
tags: [Classes, BioStatistics, Tulane Classes]
category: [Notes, Class, Tulane, BioStatistics]
covercopy: <a href="https://spauldinggrp.com/using-the-stats-worksheet-to-calculate-tracking-error/statistics-word-cloud/">© John D. Simpson, CIPM</a>
cover: "https://spauldinggrp.com/wp-content/uploads/2015/09/statistics-word-cloud.jpg"
thumbnail: "https://spauldinggrp.com/wp-content/uploads/2015/09/statistics-word-cloud.jpg"
---

## Biomedical Statistics and Data Analysis: Block 3

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>


For more codes and example, please go to view [this page](https://karobben.github.io/2020/08/21/R/regression/)

## Anova

### In python

```python
from bioinfokit.analys import stat
# perform multiple pairwise comparison (Tukey's HSD)
# unequal sample size data, tukey_hsd uses Tukey-Kramer test
for i in ['Nst_dist', 'length', 'B_angle',
       'M_angle', 'Move', 'mm_s', 'Motion', 'Sing', 'Grooming', 'Chasing',
       'Hold', ]:
    res = stat()
    res.tukey_hsd(df=Sample, res_var=i, xfac_var='Group', anova_model=i+' ~ C(Group)')
    print(i)
    print(res.tukey_summary)
```

### In R

All detailed for codes including one-way, two-way, or repeated ANOVA test with examples and citation links could be see: [Karobben, ANOVA in R, 2022](https://karobben.github.io/2022/02/04/R/anova-r/)

### summary table example

Reference: [anova_summary: Create Nice Summary Tables of ANOVA Results](https://rdrr.io/cran/rstatix/man/anova_summary.html)
```r
library(rstatix)
anova_summary()
```

## Lecture 16: Biomedical Statistics and Data Analysis

Linear regression is a technique to find the best line that passes through an X-Y data set. The criteria for “best” linear fit is the line that gives the minimum sum of errors squared:

$$
SSE = \sum{(Y_ i - Pred_ i)^ 2}
$$
Where Y~i~ is the y-value of the X~i~,Y~i~ pair and Pred~i~ is the predicted value of the line at X~i~.

### Linear Regression I

In Linear Regression, you assume that there is a Independent variable (X) that you control, or select and a Dependent variable that you measures. They are related by the equation=mX +b where m is the slope of the line and b is the y-intercept at (X=0)

You assume that all of the uncertainty (scatter) is in Y (not X).

**Types of Uncertainties**:
1) Equal uncertainties (assumed by most programs)
2) Proportional uncertainties
3) Counted uncertainties
4) Individual uncertainties
5) Uncertainties in Y and X


- Linear regression is based on a Chi-squared calculation that finds the “best fit” line which minimizes the sum of the squared differences between the observed and expected values of Y for each value of X.
- Because the expected differences depend on the uncertainties in Y, we must first define the uncertainties (or weighting factors) si for each Y

***There are several possibilities:***

1) Uncertainties in Y are all equal. This is the default assumption of most linear regression calculators,websites etc. Generally valid if each point is a single measurement using a technique that gives a constant absolute uncertainty. In this case, you can estimate s and use it as the weighting factor, or get it from the regression analysis. In the case of equal uncertainties, the important results of the linear regression analysis will not change if you enter the actual values. So you can ignore the actual uncertainties if they are equal.

2) Uncertainties are a constant proportion of the Y-value. In this case multiply Y by the relative uncertainty to get uncertainty in Y.

3) Y is a counted variable or a proportion of counted variables
  - Count: $σ=\sqrt{x}$
    - x = number of events
  - Proportion: $σ=\sqrt{np(1-p)}$
    - $n=total\ event$
    - $p=\frac{x}{n}$

4) Uncertainties in Y are unique for each value. Each Y may be an average with a mean and uncertainty of its own. Or different measurement methods may have been used for different sets of points. In this case use the appropriate uncertainty for each point.

**If your uncertainties are not constant, you must use curve fitting (non-linear regression) to fit an equation for a line to your data. When using curve-fitting you can weight each point by its SD.**

### Linear Regression Function

$$
Y = mX +b
$$

$slop=\frac{\sum{\frac{x_ i^ 2}{σ_ i^ 2}} \sum{\frac{y_ i}{σ_ i^ 2}} -
            \sum{\frac{x_ i}{σ_ i^ 2}} \sum{\frac{y_ i x_ i}{σ_ i^ 2}} }{
						\sum{\frac{x_ i^ 2}{σ_ i^ 2}} \sum{\frac{1}{σ_ i^ 2}} -
						(\sum{\frac{x_ i}{σ_ i^ 2}})^ 2
							}$

$intercept=\frac{\sum{\frac{1}{σ_ i^ 2}} \sum{\frac{y_ i x_ i}{σ_ i^ 2}} -
            \sum{\frac{x_ i}{σ_ i^ 2}} \sum{\frac{y_ i}{σ_ i^ 2}}
            }{
						\sum{\frac{x_ i^ 2}{σ_ i^ 2}} \sum{\frac{1}{σ_ i^ 2}} -
						(\sum{\frac{x_ i}{σ_ i^ 2}})^ 2
							}$

### Calculating p-values from Linear Regression
The Null hypothesis for Linear Regression is that X and Y are not correlated.
In other words:
1) A change in X will not produce a predictable change in Y.
2) The observed changes in Y are due to random error.

p-values are calculated using the **Chi Squared test**.
“Observed” is the measured value of Y at a particular X
“Expected” is the value of the line at a particular X

$$
χ^ 2 = \sum{\frac{expected - observed}{σ^ 2}}^ 2
$$

$$
df = N - 2
$$

Also individual p-values for the slope and intercept (compared to a null hypothesis, usually zero) can be calculated using a one sample t-test with the value of the slope or intercept and its standard error. Use N-2 as the degrees of freedom.

Once we have the χ^2^, we can have the p-value by `pchisq(x, df=2, lower.tail=FALSE)`, which x is the χ^2^.


### What else can you say about a linear regression analysis?

#### Errors

If your estimate of the uncertainties is too large, and you use them to do Linear Regression then the χ^2^ will be too small and the p-value will be close to 1.0. The calculated S value will be smaller that your estimates of SD in the data points.

Correct uncertainties will follow the Z-distribution around the line. In other words roughly 67% of the ± 1 SD error bars on each Y value will include the best fit line, 33% will not include the line. This is because 1 SD is essentially a 67% Confidence interval.

#### Residuals

The distribution of residual errors is an indication of the goodness of fit. They should be randomly distributed.

#### Correlation Coefficient

$$
r^ 2 = \frac{total\ variance\ in\ Y - variance\ in\ Y\ from\ regression }{ total\ variance }
$$

$$
r^ 2 = \frac{\sum{(y_ i - y_ {mean})^ 2} - \sum{(y_ i - y_ {expected})^ 2} }{ \sum{(y_ i - y_ {mean})^ 2} }
$$

r^2^ = 1 means perfect correlation. r^2^ = 0 mean there is no correlation.
Note that some programs give r (not r^2^) which can range from –1 to +1

#### Extrapolation

You can use regression parameters to calculate a new value of Y for any value of X. But beyond the range of the actual data, the calculated values can become very uncertain. Below: 95% confidence interval from Instat.

### Assumptions of linear regression

Linear regression assumes that the X and Y numbers are independent measurements. Y can depend on X, but it can not contain the same data as X.

If the values of X and Y are both used to calculate one or the other, then the observed correlation will be false.

In the example above blood pressure in patients before and after a treatment are plotted. These are independent measurements, until you decide to see if there is a correlation between the change in blood pressure and the value before treatment. The change is really X – Y, so the Y axis values on the right are calculated using X.

Since the numerical value of X is part of the Y axis AND the X axis, you can get a false correlation between X and Y.


## L17: Biomedical Statistics and Data Analysis

### Runs test

The Wald–Wolfowitz runs test (or simply runs test), named after statisticians Abraham Wald and Jacob Wolfowitz is a non-parametric statistical test that checks a randomness hypothesis for a two-valued data sequence. More precisely, it can be used to test the hypothesis that the elements of the sequence are mutually independent. [wikipedia](https://en.wikipedia.org/wiki/Wald%E2%80%93Wolfowitz_runs_test)


Reference: [Runs-test](http://dwoll.de/rexrepos/posts/npRuns.html)

The runs test made by Prism is it assign the elements into two groups and calculate only the "lesser" part of the result.

There are three packages we can do runs test: `DescTools`, `snpar`, and `randtests`. Only the `DescTools` has the same result like Prism by code below. `TMP` is the vector which contain the re-assign result as we talked above. For this package, you can assign the different group either to number or Character. More detailed codes you can find at: [Karobben: Linear Regression in R](https://karobben.github.io/2020/08/21/R/regression/)

PS: `alternative="less"` cannot be ignored.
```r
library(DescTools)
TMP = c("H","H","H","T","T","H","H","T","T","H","H","T")
RunsTest(TMP, alternative = "less")
```

<pre>
Runs Test for Randomness

data:  TMP
runs = 6, m = 7, n = 5, p-value = 0.4242
alternative hypothesis: true number of runs is less than expected
</pre>


### Rejection of data in linear regression
