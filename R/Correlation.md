---
url: correlation
---

# Correlation

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579788489000-83635ab7-5935-4c40-afd9-8b42533f0d9d.png#align=left&display=inline&height=577&name=image.png&originHeight=577&originWidth=563&size=153205&status=done&style=none&width=563)
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

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579788592455-3cc633cc-0673-4edb-a63b-26d5e7330ece.png#align=left&display=inline&height=494&name=image.png&originHeight=613&originWidth=666&size=84852&status=done&style=none&width=537)


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
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579788894381-a4deb66d-9faf-4a59-8183-6dc09f189418.png#align=left&display=inline&height=434&name=image.png&originHeight=627&originWidth=674&size=82432&status=done&style=none&width=466)

```r
library(GGally)

# Create data
sample_data <- data.frame( v1 = 1:100 + rnorm(100,sd=20), v2 = 1:100 + rnorm(100,sd=27), v3 = rep(1, 100) + rnorm(100, sd = 1))
sample_data$v4 = sample_data$v1 ** 2
sample_data$v5 = -(sample_data$v1 ** 2)

# Check correlation between variables
cor(sample_data)
# Check correlations (as scatterplots), distribution and print corrleation coefficient
ggpairs(sample_data)	# image left
ggcorr(sample_data, method = c("everything", "pearson"))	# image right
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579788983764-008a9d7c-f414-462a-90b4-8e867c2d6a29.png#align=left&display=inline&height=350&name=image.png&originHeight=678&originWidth=670&size=128790&status=done&style=none&width=346)![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579789041242-48e0b783-d279-4715-9962-63511f1b2c4e.png#align=left&display=inline&height=350&name=image.png&originHeight=539&originWidth=616&size=12660&status=done&style=none&width=400)


<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)




--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
