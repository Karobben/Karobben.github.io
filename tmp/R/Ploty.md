---
title: "Ploty"
description: "Ploty"
url: ploty2
---

# Ploty

[![NlqCdI.gif](https://s1.ax1x.com/2020/06/20/NlqCdI.gif)](https://imgchr.com/i/NlqCdI)

<a name="HvQTq"></a>
# Quick Start
```r
install.packages("plotly")

library(plotly)
library(ggplot2)
p <- ggplot(df) + geom_point(ase(x=X,y=Y))
P <- ggplotly(p)
```
 
[![NlbVbR.gif](https://s1.ax1x.com/2020/06/20/NlbVbR.gif)](https://imgchr.com/i/NlbVbR)
<a name="JvQCa"></a>
# Save

```r
library(htmlwidgets)
saveWidget(P,"1.html",selfcontained = F)
```

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
