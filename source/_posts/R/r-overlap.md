---
toc: true
url: r-overlap
covercopy: © Karobben
priority: 10000
date: 2023-02-14 01:25:30
title: "Overlap calculation in R"
ytitle: "Overlap calculation in R"
description: "Overlap calculation in R with library overlap and kerndwd"
excerpt: "There are several R packages that can help you calculate the overlap between two density distributions. For example, `overlap`, `kerndwd`, `KernSmooth`, and `pracma`"
tags: [Data, R]
category: [Data, Statistic]
cover: "https://s1.ax1x.com/2023/02/14/pSTf79K.png"
thumbnail: "https://s1.ax1x.com/2023/02/14/pSTf79K.png"
---

## overlap

`overlap`: The overlap package provides functions to calculate and visualize the overlap of two or more density distributions. The `overlapEst` function can be used to calculate the overlap of two density distributions, while the `overlapPlot` function can be used to visualize the overlap.

```r
library(overlap)
library(ggplot2)

# Generate two random lists of numbers
set.seed(123)
list1 <- rnorm(100, mean = 5, sd = 1)
list2 <- rnorm(100, mean = 8, sd = 1)

# Calculate overlap density
overlapEst(list1, list2)

ggplot() + geom_density(aes(list1, fill = "list1"), alpha = .5) + 
  geom_density(aes(list2, fill = "list2"), alpha = .5) + theme_bw()

```

<pre>
    Dhat1     Dhat4     Dhat5 
0.2460298        NA        NA 
</pre>

![Density overlapping estimate 1](https://s1.ax1x.com/2023/02/14/pSTf79K.png)




## overlapping



```r
library(overlapping)

# Generate two random lists of numbers
set.seed(123)
list1 <- rnorm(100, mean = 5, sd = 1)
list2 <- rnorm(100, mean = 8, sd = 1)

# Calculate overlap density
overlap(list(list1, list2))
```

<pre>
$OV
[1] 0.1431085
</pre>

I personally believe that this result is more reliable.

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
