---
title: "Correlation"
description: "Correlation"
url: correlation2
---

# Correlation

[![NguwK1.png](https://s1.ax1x.com/2020/06/28/NguwK1.png)](https://imgchr.com/i/NguwK1)

<a name="2x5Oh"></a>
# CORRELATION ELLIPSES
```r
library(ellipse)
library(RColorBrewer)

data=cor(mtcars)

#Build a Pannel of 100 colors with Rcolor Brewer
my_colors <- brewer.pal(5, "Spectral")
my_colors=colorRampPalette(my_colors)(100)

#Order the correlation matrix
ord <- order(data[1, ])
data_ord = data[ord, ord]
plotcorr(data_ord , col=my_colors[data_ord*50+50] , mar=c(1,1,1,1))
```




<a name="IL1P4"></a>
## BASIC SCATTERPLOT MATRIX

```r
data=mtcars[ , c(1,3:6)]
#Make the plot
plot(data , pch=20 , cex=1.5 , col=rgb(0.5, 0.8, 0.9, 0.7))
```
[![NguU29.png](https://s1.ax1x.com/2020/06/28/NguU29.png)](https://imgchr.com/i/NguU29)
<a name="EjKBE"></a>
## SCATTERPLOT MATRIX – CAR PACKAGE

```r
library(car)
library(RColorBrewer)
#Let's use the car dataset proposed by R

data=mtcars
my_colors <- brewer.pal(nlevels(as.factor(data$cyl)), "Set2")
scatterplotMatrix(~mpg+disp+drat|cyl, data=data , reg.line="" ,
  smoother="", col=my_colors , smoother.args=list(col="grey") ,
  cex=1.5 , pch=c(15,16,17) , main="Scatter plot with Three Cylinder Options")
```

[![NguN8J.png](https://s1.ax1x.com/2020/06/28/NguN8J.png)](https://imgchr.com/i/NguN8J)

```r
library(GGally)

# Create data
sample_data <- data.frame( v1 = 1:100 + rnorm(100,sd=20), v2 = 1:100 + rnorm(100,sd=27), v3 = rep(1, 100) + rnorm(100, sd = 1))
sample_data$v4 = sample_data$v1 ** 2
sample_data$v5 = -(sample_data$v1 ** 2)

# Check correlation between variables
cor(sample_data)
# Check correlations (as scatterplots), distribution and print corrleation coefficient
ggpairs(sample_data)  # image left
ggcorr(sample_data, method = c("everything", "pearson"))  # image right
```

|[![NguavR.png](https://s1.ax1x.com/2020/06/28/NguavR.png)](https://imgchr.com/i/NguavR)|[![NgutC4.png](https://s1.ax1x.com/2020/06/28/NgutC4.png)](https://imgchr.com/i/NgutC4)|
|--|--|



<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)




---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
