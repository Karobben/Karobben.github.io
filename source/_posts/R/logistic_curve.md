---
title: "logistic regression in R"
description: "Calculating logistic function with R| logistic regression| 逻辑斯蒂曲线"
date: 2020/08/21
url: logistic
toc: true
excerpt: "Calculating logistic function with R| logistic regression| 逻辑斯蒂曲线"
tags: [R, Regression, Logistic]
category: [R, Data, Statistic, Regression]
cover: 'https://s3.ax1x.com/2021/02/24/yXaRMT.png'
thumbnail: 'https://s1.ax1x.com/2020/08/21/dYctdf.png'
priority: 5
---

## Logistic regression in R

## Standard Logistic function

$$
P(m)= \frac{KP_{0}e^{rm}}{K + P_0(e^{rm} - 1)}
$$

## Test Data

reference: [PriscillaBai 2018](https://www.jianshu.com/p/ed4167c8a5e9)[^1]

[^1]: PriscillaBai; R语言绘制逻辑斯蒂(logistic)生长曲线; 简书; 2018; [Link](https://www.jianshu.com/p/ed4167c8a5e9)
```r
## Test Date set
n<-c(0.15,0.15,0.20,0.28,0.35,0.4,0.44,0.47,0.49,0.51,0.53,0.56,0.56,0.57,0.6,0.58,0.6,0.61,0.6, 0.58,0.54, 0.58)
m = c(1:length(n))
df<-as.data.frame(cbind(m,n))

## Regression
```

## Regression

```r
library(deSolve)

### 估计参数初始值| estimate
SS <- getInitial(n ~ SSlogis(m, alpha, xmid, scale), data = df)
K_start <- SS["alpha"]
R_start <- 1/SS["scale"]
P0_start <- SS["alpha"]/(exp(SS["xmid"]/SS["scale"])+1)

### 拟合函数方程
log_formula <- formula(n ~ K*P0*exp(R*m)/(K + P0*(exp(R*m) - 1)))
formu<-nls(log_formula, start = list(K = K_start, R = R_start, P0 = P0_start))

## Visualization
library(ggplot2)
ggplot() + geom_line(data=df,aes(m,predict(formu)))+
  geom_point(aes(x=m,y=n))+
  theme_bw()
```

![logistic1](https://s1.ax1x.com/2020/08/21/dYctdf.png)


### plot more

We can check more information by:
```r
formu
```
<pre>
Nonlinear regression model
  model: n ~ K * P0 * exp(R * m)/(K + P0 * (exp(R * m) - 1))
   data: parent.frame()
 K.alpha  R.scale P0.alpha
 0.58610  0.38294  0.09482
 residual sum-of-squares: 0.006648

Number of iterations to convergence: 0
Achieved convergence tolerance: 1.708e-06
</pre>

As a result, we can have the formula:

$$
P(m)= \frac{0.58610 * 0.09482 * e^{0.38294 * m}}{0.58610 + 0.09482(e^{0.38294 * m} - 1)}
$$


```r
K <- SS["alpha"] # K = 0.58610
R <- 1/SS["scale"] # R = 0.38294
P0 <- SS["alpha"]/(exp(SS["xmid"]/SS["scale"])+1) # P0 = 0.09482

Log_r <- function(m){
   K * P0 * exp(R * m)/(K + P0 * (exp(R * m) - 1))
}

x=c(-20:40)
ggplot() + geom_line(data=df,aes(m,predict(formu)))+
  geom_point(aes(x=m,y=n))+
  theme_bw()+ geom_line(aes(x=x,y=Log_r(x)))
```

|![logistic1](https://s1.ax1x.com/2020/08/21/dYctdf.png)|![logistic2](https://s1.ax1x.com/2020/08/21/dYcYeP.png)|
|:-:|:-:|
