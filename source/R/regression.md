---
title: "Regression in R"
description: "Calculating regression function by R|R 语言回归曲线"
date: 2020/08/21
url: regression
---

# Regression in R

# linear equation with one unknown
test data: `mpg`

Quick look:
![dYHWbF.png](https://s1.ax1x.com/2020/08/21/dYHWbF.png)
## Quick start
```r
# calculating the model
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

## Plot

```r
Formula <- function(x){
  -3.531*x+35.698
}

x=c(0:10)

# Origiaml point
ggplot() + geom_point(data=mpg, aes(x=displ, y=hwy),color='salmon') +
  theme_light()+  
  # regression model
  geom_line(aes(x=x,y=Formula(x)))
```
![dYHWbF.png](https://s1.ax1x.com/2020/08/21/dYHWbF.png)

# Quadratic Equation

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
