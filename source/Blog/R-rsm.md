---
title: "Response Surface Methodology in R"
description: "Response Surface Methodology in R| R语言做响应面分析，并可视化"
date: 2020/08/02
url: rsm
---

# Response Surface Methodology in R

Response-surface methodology comprises a body of methods for exploring for **optimum operating conditions** through experimental methods.

The rsm package for R (R Development Core Team 2009[^1]) provides several functions to facilitate classical response-surface methods.

[^1]: R Development Core Team (2009). R: A Language and Environment for Statistical Computing. R Foundation for Statistical Computing, Vienna, Austria. ISBN 3-900051-07-0, URL http://www.R-project.org/.

# Install

```r
install.packages('rsm')
```


```r
library("rsm")
ChemReact

CR1 <- coded.data(ChemReact1, x1 ~ (Time - 85)/5, x2 ~ (Temp - 175)/5)

des1 <- ccd (y1 + y2 ~ A + B + C + D,
  generators = E ~ - A * B * C * D, n0 = c(6, 1))

des10 <- ccd( ~ A + B + C + D + E,
  blocks = Blk ~ c(A * B * C, C * D * E), n0 = c(2, 4))

par(mfrow=c(1,2))
varfcn(des10, ~ Blk + SO(A,B,C,D,E), dist = seq(0, 3, by=.1))
varfcn(des10, ~ Blk + SO(A,B,C,D,E), dist = seq(0, 3, by=.1), contour = TRUE)
```

[![aYEgeK.md.png](https://s1.ax1x.com/2020/08/02/aYEgeK.md.png)](https://imgchr.com/i/aYEgeK)

```r
ccd(2, n0 = c(1,1), inscribed=TRUE, randomize=FALSE)
```
```
run.order std.order   x1.as.is   x2.as.is Block
1          1         1 -0.7071068 -0.7071068     1
2          2         2  0.7071068 -0.7071068     1
3          3         3 -0.7071068  0.7071068     1
4          4         4  0.7071068  0.7071068     1
5          5         5  0.0000000  0.0000000     1
6          1         1 -1.0000000  0.0000000     2
7          2         2  1.0000000  0.0000000     2
8          3         3  0.0000000 -1.0000000     2
9          4         4  0.0000000  1.0000000     2
10         5         5  0.0000000  0.0000000     2

Data are stored in coded form using these coding formulas ...
x1 ~ x1.as.is
x2 ~ x2.as.is
```


```r
CR1.rsm <- rsm(Yield ~ FO(x1, x2), data = CR1)
summary(CR1.rsm)
```
