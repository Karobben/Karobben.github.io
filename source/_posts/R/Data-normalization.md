---
title: "Data normalization"
url: normalization
date: 2020/05/01
toc: true
excerpt: "Few ways to normalizing your date, reducing batch effect..."
tags: [R, Statistic]
category: [R ]
cover: 'https://www.r-project.org/Rlogo.png'
thumbnail: 'https://www.r-project.org/Rlogo.png'
priority: 10000
---

## Data normalization

<a name="Y4znF"></a>
## Normalization

<a name="CMtTL"></a>
### 1 Max-Min
```r
for(ii in 1:ncol(a))
{a[,ii] <- (a[,ii]-min(a[,ii]))/(max(a[,ii])-min(a[,ii]))}
```


<a name="G1R41"></a>
### 2 z-score
```r
for(ii in 1:ncol(a))
{a[,ii] <- (a[,ii]-mean(a[,ii]))/sd(a[,ii])}
```


<a name="S4tTs"></a>
### 3 Soft-max_Normalization
```r
for(ii in 1:ncol(a))
{a[,ii] <- pnorm((a[,ii]-mean(a[,ii]))/sd(a[,ii]))}
```


<a name="zb92d"></a>
### 4 Logistic/Softmax
```r
for(ii in 1:ncol(a))
{a[,ii] <- 1/(1+ exp(-a[,ii]))
```


<a name="l6OhA"></a>
### 5 模糊量化模式
```r
for(ii in 1:ncol(a))
{x<- a[,ii]
a[,ii] <- x <- 1/2 +1/2sin(pi/(max(x)-mean(x))(x-max(x)-mean(x)/2)) *x}
```


<a name="SbqDp"></a>
### 6 log
```r
for(ii in 1:ncol(a))
{
a[,ii][which(a[,ii]>0)] <- log(a[,ii][which(a[,ii]>0)],10)/log(max(a[,ii]),10)
a[,ii][which(a[,ii]<0)] <- log(a[,ii][which(a[,ii]<0)](-1),10)(-1)/log(mean(a[,ii]) *(-1))}
```


<a name="uEmOn"></a>
### 7 atan
```r
for(ii in 1:ncol(a))
{
a[,ii][which(a[,ii]>0)] <- atan(a[,ii][which(a[,ii]>0)])*2/pi
a[,ii][which(a[,ii]<0)] <- atan(a[,ii][which(a[,ii]<0)])2/pi (-1)}
```


<a name="Ih7Gy"></a>
### 8 Logistic/Softmax
```r
## Something wrong with this 1/2+ 1/2sim(pi/max())
```
