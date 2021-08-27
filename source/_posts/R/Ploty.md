---
title: "Ploty"
description: "Ploty"
url: ploty2
date: 2020/06/20
toc: true
excerpt: "heatmap is fun!"
tags: [R, Plot, Interoperable Plot]
category: [R, Plot, others]
cover: 'https://s1.ax1x.com/2020/08/15/dFpkUH.png'
thumbnail: 'https://s1.ax1x.com/2020/08/15/dFpkUH.png'
priority: 10000
---

## Ploty

![NlqCdI.gif](https://s1.ax1x.com/2020/06/20/NlqCdI.gif)

<a name="HvQTq"></a>
## Quick Start
```r
install.packages("plotly")

library(plotly)
library(ggplot2)
p <- ggplot(df) + geom_point(ase(x=X,y=Y))
P <- ggplotly(p)
```

![NlbVbR.gif](https://s1.ax1x.com/2020/06/20/NlbVbR.gif)
<a name="JvQCa"></a>
## Save

```r
library(htmlwidgets)
saveWidget(P,"1.html",selfcontained = F)
```

<a name="FG8Ad"></a>
## More
