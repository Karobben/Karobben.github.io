---
title: "jpeg: reading color from img"
description: "jpeg: reading color from img"
url: jpeg2
date: 2020/06/19
toc: true
excerpt: "jpeg package is a library for reading image file to R. By doing those, you can read the rgb value from a image and do calculate you like!"
tags: [R, Image]
category: [R, Image]
cover: 'https://www.r-project.org/Rlogo.png'
thumbnail: 'https://www.r-project.org/Rlogo.png'
priority: 10000
---

## jpeg: reading color from img

<a name="bYAmA"></a>
## 配色难题
##Reading color from the image

```r
library(jpeg);library(reshape2)
picture <- readJPEG("~/Pictures/test.jpg")
longImage <- melt(picture)
rgbImage <- reshape(longImage, timevar='Var3',idvar=c('Var1','Var2'), direction='wide')
colorColumns<- rgbImage[, substr(colnames(rgbImage), 1, 5)== "value"]
Color_B  = data.frame(sort(table(rgb(colorColumns)),decreasing=T))[[1]]
```
