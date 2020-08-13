---
title: "geom Extra Lines"
description: "geom Extra Lines"
url: extra_lines2
---

# geom Extra Lines

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
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)


---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
