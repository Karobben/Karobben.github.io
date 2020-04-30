---
url: ploty
---

# Ploty

![deepin-screen-recorder_Select area_20200123214833.gif](https://cdn.nlark.com/yuque/0/2020/gif/691897/1579787331214-52d40e96-aadb-4ab9-95e1-d9c9753348a2.gif#align=left&display=inline&height=523&name=deepin-screen-recorder_Select%20area_20200123214833.gif&originHeight=523&originWidth=656&size=108678&status=done&style=none&width=656)
<a name="HvQTq"></a>
# Quick Start
```r
install.packages("plotly")

library(plotly)
library(ggplot2)
p <- ggplot(df) + geom_point(ase(x=X,y=Y))
P <- ggplotly(p)
```

![deepin-screen-recorder_Select area_20200123214724.gif](https://cdn.nlark.com/yuque/0/2020/gif/691897/1579787270007-c502f91a-716e-48c5-9023-0ca2b4b6fa75.gif#align=left&display=inline&height=564&name=deepin-screen-recorder_Select%20area_20200123214724.gif&originHeight=564&originWidth=557&size=171188&status=done&style=none&width=557)
<a name="JvQCa"></a>
# Save

```r
library(htmlwidgets)
saveWidget(P,"1.html",selfcontained = F)
```

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
