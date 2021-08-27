---
title: "geom Extra Lines| Adding a line in ggplot"
ytitle: "geom Extra Lines| 在 ggplot 裏面加一條線"
description: "geom Extra Lines"
url: extra_lines2
date: 2020/06/19
toc: true
excerpt: "R: ggplot, ggplot, adding extral lines in ggolot"
tags: [R, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: 'https://s1.ax1x.com/2020/06/19/Nu06nx.png'
thumbnail: 'https://s1.ax1x.com/2020/06/19/Nu06nx.png'
priority: 10000
---


geom_vline()<br />geom_hline()<br />geom_abline()

```r
library(ggplot2)
library(patchwork)

P1 <- ggplot(mtcars)+ geom_point(aes(mpg, cyl)) +
  geom_vline( xintercept = 20) + ggtitle('vline') +theme_light()
P2 <- ggplot(mtcars)+ geom_point(aes(mpg, cyl)) +
geom_hline( yintercept = 7) + ggtitle('hline') +theme_light()
P3 <- ggplot(mtcars, aes(wt, mpg)) + geom_point() + geom_abline(intercept = 25, slope = -1) +
  ggtitle("abline")+theme_light()

P3|(P1/P2)
```

![Nu06nx.png](https://s1.ax1x.com/2020/06/19/Nu06nx.png)

<a name="FG8Ad"></a>
## More
