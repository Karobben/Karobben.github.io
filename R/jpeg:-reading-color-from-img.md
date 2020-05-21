---
url: jpeg2
---

# jpeg: reading color from img

<a name="bYAmA"></a>
# 配色难题
#Reading color from the image

```r
library(jpeg);library(reshape2)
picture <- readJPEG("~/Pictures/test.jpg")
longImage <- melt(picture)
rgbImage <- reshape(longImage, timevar='Var3',idvar=c('Var1','Var2'), direction='wide')
colorColumns<- rgbImage[, substr(colnames(rgbImage), 1, 5)== "value"]
Color_B  = data.frame(sort(table(rgb(colorColumns)),decreasing=T))[[1]]
```
