---
title: "geom_step | ggplot examples"
ytitle: "geom_step | ggplot 分段圖　(生存曲線)"
description: "geom_step | ggplot 分段圖　(生存曲線)"
url: geom_step2
date: 2020/06/19
toc: true
excerpt: "R: ggplot, ggplot, for step plot"
tags: [R, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: 'https://s1.ax1x.com/2020/06/19/Nuwmi4.png'
thumbnail: 'https://s1.ax1x.com/2020/06/19/Nuwmi4.png'
priority: 10000
---
## Quick Start

```r
library(ggplot2)

d=data.frame(x=c(1,2,4,5,7,8,9), y=c(1,2,3,5,6,7,9))

ggplot() + theme_light()+ geom_step(data=d, mapping=aes(x=x, y=y)) +
geom_step(data=d, mapping=aes(x=x, y=y), direction="vh", linetype=3) +
geom_point(data=d, mapping=aes(x=x, y=y), color="red")
```
![Nuwmi4.png](https://s1.ax1x.com/2020/06/19/Nuwmi4.png)

<a name="FG8Ad"></a>
## More
