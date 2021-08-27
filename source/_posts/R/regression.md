---
title: "Linear Regression"
description: "Calculating regression function by R|R 语言回归曲线"
date: 2020/08/21
url: regression
toc: true
excerpt: "Calculating regression function by R"
tags: [R, Regression]
category: [R, Data, Statistic, Regression]
cover: 'https://s3.ax1x.com/2021/02/24/yXdAOS.png'
thumbnail: 'https://s1.ax1x.com/2020/08/21/dYHWbF.png'
priority: 10000
---

## Regression in R

## linear equation with one unknown
test data: `mpg`

### Quick start
```r
## calculating the model
model_mpg <- lm(formula = hwy ~ displ, data = mpg)

print(model_mpg)
```
<pre>
Call:
lm(formula = hwy ~ displ, data = mpg)

Coefficients:
(Intercept)        displ  
     35.698       -3.531
</pre>

As we can see above, the function is

$$
y = -3.531x+35.698
$$

### Plot

```r
Formula <- function(x){
  -3.531*x+35.698
}

x=c(0:10)

## Origiaml point
ggplot() + geom_point(data=mpg, aes(x=displ, y=hwy),color='salmon') +
  theme_light()+  
  # regression model
  geom_line(aes(x=x,y=Formula(x)))
```
![dYHWbF.png](https://s1.ax1x.com/2020/08/21/dYHWbF.png)

## Quadratic Equation

Standard Equation:
$$
y=ax^2+bx+c
$$
<br>
```r
model_mpg1 <- lm(formula = hwy ~ I(displ^2), data = mpg)
model_mpg2 <- lm(formula = hwy ~ I(displ^2) + displ, data = mpg)
```

`model_mpg1`:
<pre>
Call:
lm(formula = hwy ~ I(displ^2), data = mpg)

Coefficients:
(Intercept)   I(displ^2)  
     29.324       -0.429  

</pre>       

`model_mpg2`:
<pre>
Call:
lm(formula = hwy ~ I(displ^2) + displ, data = mpg)

Coefficients:
(Intercept)   I(displ^2)        displ  
     49.245        1.095      -11.760  
</pre>

plot
```r
Formula1 <- function(x){
  model_mpg1$coefficients[2]*x^2 + model_mpg1$coefficients[1]
}

Formula2 <- function(x){
  model_mpg2$coefficients[2]*x^2 + model_mpg2$coefficients[3]*x +model_mpg2$coefficients[1]
}

ggplot() + geom_point(data=mpg, aes(x=displ, y=hwy),color='salmon') +
  theme_light()+  
  # regression model
  geom_line(aes(x=x,y=Formula1(x)))

ggsave('')
ggplot() + geom_point(data=mpg, aes(x=displ, y=hwy),color='salmon') +
  theme_light()+  
  # regression model
  geom_line(aes(x=x,y=Formula2(x)))

```
||model_mpg1|model_mpg2|
|--|:-:|:-:|
|Formula| $$y=-0.429x^{2}+29.324$$ | $$y=1.095x^{2} -11.760x + 49.245$$ |
|Plot|![dYXPYQ.png](https://s1.ax1x.com/2020/08/21/dYXPYQ.png)|![dYXCFg.png](https://s1.ax1x.com/2020/08/21/dYXCFg.png)|



[cor](https://baike.baidu.com/item/%E7%9B%B8%E5%85%B3%E7%B3%BB%E6%95%B0)
```r
cor()
```
## **R^2^**
[谦瑞数据 2019](https://zhuanlan.zhihu.com/p/77052937)

```r
mylr = function(x,y){
  x_mean = mean(x)
  y_mean = mean(y)
  xy_mean = mean(x*y)
  xx_mean = mean(x*x)
  yy_mean = mean(y*y)

  m = (x_mean*y_mean - xy_mean)/(x_mean^2 - xx_mean)
  b = y_mean - m*x_mean

  f = m*x+b# 线性回归方程
  sst = sum((y-y_mean)^2)
  sse = sum((y-f)^2)
  ssr = sum((f-y_mean)^2)
  result = c(m,b,sst,sse,ssr)
  names(result) = c('m','b','sst','sse','ssr')
  result['ssr']/result['sst']
}



x = c(60,34,12,34,71,28,96,34,42,37)

y = c(301,169,47,178,365,126,491,157,202,184)
```


## 一元多次回归方程自动扫描

T test and P value: [数据挖掘运爷](https://blog.csdn.net/chen790646223/article/details/45448717)

Functions:
<details>
  <summary>Click to see</summary>

  ```r
  mylr = function(x,y){
    x_mean = mean(x)
    y_mean = mean(y)
    xy_mean = mean(x*y)
    xx_mean = mean(x*x)
    yy_mean = mean(y*y)

    m = (x_mean*y_mean - xy_mean)/(x_mean^2 - xx_mean)
    b = y_mean - m*x_mean

    f = m*x+b# 线性回归方程
    sst = sum((y-y_mean)^2)
    sse = sum((y-f)^2)
    ssr = sum((f-y_mean)^2)
    result = c(m,b,sst,sse,ssr)
    names(result) = c('m','b','sst','sse','ssr')
    result['ssr']/result['sst']
  }

  F_equation <- function(X,Formula){
    eval(parse(text = Formula))
  }

  LMEE <- function(TB,Times){
    colnames(TB)=c("X","Y")

    Group_X = "X"
    for(i in c(2:Times)){
      X_i = paste("I(X^",i,")",sep="")
      Group_X = paste(Group_X,X_i,sep=" + ")
    }
    str_lm = paste("lm(Y ~",Group_X, ', data=TB)', sep=' ')
    model = eval(parse(text = str_lm))

    Formula = model$coefficients[1]
    for(i in c(Times:1)){
      X_tmp = paste(model$coefficients[i+1], " * X^", i, sep="")
      Formula = paste(Formula,X_tmp,sep="+")
    }
    # T value
    tstats <- coef(model) / sqrt(diag(vcov(model)))
    Tvalue = matrix(tstats)[2]
    # P value
    pvalue <- 2 * pt(abs(tstats), df = df.residual(fit), lower.tail = FALSE)
    Pvalue <- matrix(pvalue)[2]

    R2 = mylr(TB$Y,F_equation(TB$X,Formula))

    result = c()
    result$R2      = R2[[1]]
    result$model   = model
    result$Tvalue  = Tvalue
    result$Pvalue  = Pvalue
    result$Formula =Formula

    return(result)
  }


  MEES <- function(TB, Times){
    colnames(TB)=c("X","Y")
    Result_TB = data.frame()
    for(i in c(1:Times)){
        Result_LMEE = LMEE(TB,i)
        Result_tmp = data.frame(Exp= i, P_value = Result_LMEE$Pvalue, R2= Result_LMEE$R2, F = Result_LMEE$Formula)
        Result_TB = rbind(Result_TB, Result_tmp)
    }

    return(Result_TB)
  }

  MEES_plot <- function(TB,TB_input,header="test"){
    colnames(TB)=c("X","Y")
    TB_Nna = na.omit(TB_input)
    for(i in c(1:nrow(TB_Nna))){
      ggplot()+geom_point(data=TB,aes(x=X,y=Y))+
               geom_line(aes(x=TB$X, y=F_equation(TB$X,as.character(TB_Nna$F[i]))))
      ggsave(paste(header,i,".png",sep=""))
    }
  }


  ```
</details>

Usage:


```r
##Test Data
TB <- head(ChickWeight)[c(2,1)]

MEES(TB,4)
MEES_plot(TB,MEES(TB,4))
```

||Exp|P_value|R2|F|
|--|--|--|--|--:|
|ssr|1|5.100486e-02|0.9641461| $40.2380952380953 + 4.78571428571428 * X$
|1|2|5.100486e-02|0.9865977|43.5714285714286+0.250000000000001 * X^2+2.28571428571428 * X^1|
|11|3|1.550240e-08|0.9986254|41.904761904762+0.069444444444444 * X^3+-0.791666666666658 * X^2+6.0912698412698 * X^1|
|12|4|3.012296e-02|0.9986254|41.904761904762+2.01944464079605e-16 * X^4+0.0694444444444399 * X^3+-0.791666666666634 * X^2+6.09126984126975 * X^1|
|13|5|NaN|1.0000000|41.9999999999999+-0.00625000000000004 * X^5+0.156250000000001 * X^4+-1.29166666666667 * X^3+3.99999999999998 * X^2+0.516666666666805 * X^1|
