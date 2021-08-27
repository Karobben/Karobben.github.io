---
title: "geom_pie | ggfan |ggplot examples"
ytitle: "geom_pie | ggplot 餅圖| ggfan包"
description: "geom_pie"
url: geom_pie
date: 2020/06/18
toc: true
excerpt: "R: ggplot, ggplot, pie"
tags: [R, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: 'https://i.loli.net/2020/06/18/AP2zfYt5qwcLxk1.png'
thumbnail: 'https://i.loli.net/2020/06/18/AP2zfYt5qwcLxk1.png'
priority: 10000
---


## Install
```r
##install.packages("ggfan") # or
##devtools::install_github("jasonhilton/ggfan")
```

## Quick Start

Reference: []()
```r
library(ggplot2)

df <- data.frame(
  group = c("Male", "Female", "Child"),
  value = c(25, 25, 50)
  )
head(df)
```
```
group value
1   Male    25
2 Female    25
3  Child    50
```

```r
library(ggplot2)
library(ggthemes)

pie <- ggplot(df, aes(x="", y=value, fill=group))+
    geom_bar(width = 1, stat = "identity") + coord_polar("y", start=0) + theme_map()
pie
ggsave("pie.png", w=3.17, h=2.92)
```
![aQ18Wd.md.png](https://s1.ax1x.com/2020/07/31/aQ18Wd.md.png)

```r
pie +  scale_fill_manual(values=c("#999999", "#E69F00", "#56B4E9"))
ggsave('pie2.png', wi=4.6, hei=3.76)
```
![pie2](https://i.loli.net/2020/06/18/DaeIctdAkl1rhxg.png)

```r
pie +  scale_fill_manual(values=c("#999999", "#E69F00", "#56B4E9")) +  geom_text(aes(y = value/3 + c(0, cumsum(value)[-length(value)]),  
                label = paste(value*100/sum(value),"%", sep='')))
```
![pie3](https://i.loli.net/2020/06/18/AP2zfYt5qwcLxk1.png)

## Ring pie

```r
pie +  scale_fill_manual(values=c("#999999", "#E69F00", "#56B4E9")) +
  geom_text(aes(y = value/3 + c(0, cumsum(value)[-length(value)]),  
                label = paste(value*100/sum(value),"%", sep='')))+
  expand_limits(x=c(-1,1))              
```
![pie4](https://i.loli.net/2020/06/18/HE9qSbdfLWV4hK5.png)

## Multi-layer
```r
TB = rbind(df,df)
TB$Sub = c(10,15,15,15,10,35)
TB$Group = c(rep("A",3),rep("B",3))

ggplot(TB) + geom_bar(data=TB[1:3,],aes(x="A",y=value[1:3], fill=group),stat = 'identity') +
    geom_bar(aes(x="B",y =Sub, fill=Group),stat='identity')+
    coord_polar('y')                                 
```

## Rose Plot
Reference: [九茶](https://blog.csdn.net/bone_ace/article/details/47624987)
```r
library(ggplot2)
dt = data.frame(A = c(2, 7, 4, 10, 1), B = c('B','A','C','D','E'))
ggplot(dt, aes(x = B, y = log(1+A), fill = B)) +  
      geom_bar(stat = "identity", alpha = 0.7) +  
      coord_polar() + theme_light()
```

![rose](https://i.loli.net/2020/06/18/MfdJyE93WvchHmK.png)
## pie 3D

For pie3D, you'd like to install `plotrix` first.
```r
install.packages("plotrix")
library("plotrix")

x <-c(10,20,30,40,50)
label <-c("Alabama", "Alaska", "Arizona","Arkansas", "California")
pie3D(x,labels=label,explode=0.1,main="PieChart of Countries ")
```
![pie5](https://i.loli.net/2020/06/18/JyXs8UnQzFV4Np1.png)

## More

### pie

author: [陈娜](http://blog.sciencenet.cn/blog-1468811-939783.html)

|Pie|Pie3D|Fan|
|---|---|---|
|![pie](http://image.sciencenet.cn/album/201511/30/095516j5dqx2de2q19bbqh.png)|![pie3D](http://image.sciencenet.cn/album/201511/30/095608alcdhac773j7l3au.png)|![plotrix](http://image.sciencenet.cn/album/201511/30/095650yu52524f7zf2rb7u.png)|
[© 陈娜 2015](http://blog.sciencenet.cn/blog-1468811-939783.html)

### [SALVAGING THE PIE](https://www.darkhorseanalytics.com/blog/salvaging-the-pie)
![img](https://images.squarespace-cdn.com/content/v1/56713bf4dc5cb41142f28d1f/1450306657208-N3NFCZECC1X5Y7LKZXNS/ke17ZwdGBToddI8pDm48kPmLlvCIXgndBxNq9fzeZb1Zw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZamWLI2zvYWH8K3-s_4yszcp2ryTI0HqTOaaUohrI8PI1ywBQVkPxlWdHWNwmTPkOtpL7dAXKpzabxT18Uiubqc/devourThePie3.gif?format=750w)
