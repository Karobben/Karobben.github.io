---
title: "geom_tufteboxplot"
description: "geom_tufteboxplot"
url: geom_tufteboxplot2
---

# geom_tufteboxplot

![123](https://i.loli.net/2020/06/19/knlNazKxvZshMPq.png)
# Quick Start
```r
library(ggplot2)
library(patchwork)
p <- ggplot(mtcars, aes(factor(cyl), mpg))
## with a point for the median and lines for whiskers
P1 <- p + geom_tufteboxplot() + theme_light()+ ggtitle('P1')+
	theme(plot.title = element_text(hjust = 0.5))
## with a line for the interquartile range and points for whiskers
P2 <- p + geom_tufteboxplot(median.type = "line", whisker.type = "point", hoffset = 0)+
	theme_light()+ ggtitle('P2')+theme(plot.title = element_text(hjust = 0.5))
## with a wide line for the interquartile range and lines for whiskers
P3 <- p + geom_tufteboxplot(median.type = "line", hoffset = 0, width = 3) +
	theme_light()+ ggtitle('P3')+theme(plot.title = element_text(hjust = 0.5))
## with an offset line for the interquartile range and lines for whiskers
P4 <- p + geom_tufteboxplot(median.type = "line") + theme_light()+ ggtitle('P4')+
	theme(plot.title = element_text(hjust = 0.5))
P5 <- p + geom_point() + theme_light() + ggtitle('Scatter')+
	theme(plot.title = element_text(hjust = 0.5))
P6 <- p + geom_boxplot()+ theme_light()+ ggtitle('Boxplot')+
	theme(plot.title = element_text(hjust = 0.5))

(P1|P2|P3)/(P5|P4|P6)
```


<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)




---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
