---
title: "geom_bar"
description: "geom_bar"
url: geom_bar
---
# geom_bar

Here, we use `mtcars` as an example
# Quick Start
```r
library(ggplot2)

ggplot(mtcars) +
	geom_bar(aes(cyl, disp,fill=drat), stat='identity') +
	theme_light()
#ggsave('bar1.png')
ggplot(mtcars) +
	geom_bar(aes(cyl, disp,fill=drat), stat='summary') +
	theme_light()
#ggsave('bar2.png')
```
|identity|summary|
|---|---|
|![bar1](https://i.loli.net/2020/06/18/B9KoShVUCnZMcsr.png)|![bar2](https://i.loli.net/2020/06/18/rpTbdUltRaOnuWB.png)|


# State = identity
```r
ggplot(mtcars) +
	geom_bar(aes(cyl, disp,fill=drat), stat='identity', position = 'fill') +
  theme_light()
ggsave('bar3.png')

ggplot(mtcars) +
  geom_bar(aes(cyl, disp,fill=drat), stat='identity', position = 'identity') +
  theme_light()
ggsave('bar4.png')

ggplot(mtcars) +
  geom_bar(aes(cyl, disp,fill=drat), stat='identity', position = 'stack') +
  theme_light()
ggsave('bar5.png')

ggplot(mtcars) +
  geom_bar(aes(cyl, disp,fill=drat), stat='identity', position = 'dodge') +
  theme_light()
ggsave('bar6.png')
```
|fill|identity/dodge|stack/default|
|:---:|:---:|:---:|
|![bar3](https://i.loli.net/2020/06/18/ehObZzq1oUsXiVQ.png)|![bar4](https://i.loli.net/2020/06/18/j6gP4KY5ehuUyt8.png)|![bar5](https://i.loli.net/2020/06/18/KFvImt4r3UpJOLP.png)|


# State = count
```r
ggplot(mtcars) +
	geom_bar(aes(cyl, fill='salmon')) +
	theme_light()

ggplot(mtcars) +
  geom_bar(aes(cyl, fill='salmon'), stat='count') +
  theme_light()
```
![bar_counts](https://i.loli.net/2020/06/18/BIN1SHnEyfmOo9b.png)

# position
Reference: [Dwzb](https://zhuanlan.zhihu.com/p/27093478)
```r
library(patchwork)
p1 <- ggplot(mpg,aes(x=class)) +
			geom_bar(aes(fill=factor(cyl)),position="stack")+
			ggtitle(label='Stack') # position默认，堆叠
p2 <- ggplot(mpg,aes(x=class)) +
			geom_bar(aes(fill=factor(cyl)),position="stack")+
			ggtitle(label='Stack') + coord_flip()
p3 <- ggplot(mpg,aes(x=class)) +
			geom_bar(aes(fill=factor(cyl)),position="dodge")+
			ggtitle(label='Dodge') # 并排放置
p4 <- ggplot(mpg,aes(x=class)) +
			geom_bar(aes(fill=factor(cyl)),position="fill")+
			ggtitle(label='Fill') # 填充显示比例
(p1|p2)/(p3|p4)
```
![bar_4](https://i.loli.net/2020/06/18/f5C31RSnaJdG7Ub.png)


# polar axis

```r
p1 <- ggplot(mpg,aes(x=class)) +
    geom_bar(aes(fill=factor(cyl)),position="stack")+
    ggtitle(label='X_Stack') + coord_polar('x') + theme_map()+
    theme(plot.title = element_text(hjust = 0.5))

p2 <- ggplot(mpg,aes(x=class)) +
    geom_bar(aes(fill=factor(cyl)),position="dodge")+
    ggtitle(label='X_Dodge') + coord_polar('x') + theme_map()+
    theme(plot.title = element_text(hjust = 0.5))

p3 <- ggplot(mpg,aes(x=class)) +
    geom_bar(aes(fill=factor(cyl)),position="fill")+
    ggtitle(label='X_Fill') + coord_polar('x') + theme_map()+
    theme(plot.title = element_text(hjust = 0.5))

p11 <- ggplot(mpg,aes(x=class)) +
    geom_bar(aes(fill=factor(cyl)),position="stack")+
    ggtitle(label='Y_Stack') + coord_polar('y') + theme_map()+
    theme(plot.title = element_text(hjust = 0.5))

p22 <- ggplot(mpg,aes(x=class)) +
    geom_bar(aes(fill=factor(cyl)),position="dodge")+
    ggtitle(label='Y_Dodge') + coord_polar('y') + theme_map()+
    theme(plot.title = element_text(hjust = 0.5))

p33 <- ggplot(mpg,aes(x=class)) +
    geom_bar(aes(fill=factor(cyl)),position="fill")+
    ggtitle(label='Y_Fill') + coord_polar('y') + theme_map()+
    theme(plot.title = element_text(hjust = 0.5))

(p1|p11)/(p2|p22)/(p3|p33)
ggsave('bar_polar.png')
```
![bar_polar](https://i.loli.net/2020/06/18/KUyTX1tkcfGxRov.png)

# Pie plot
![pie1](https://i.loli.net/2020/06/18/y1drCS3bYxRnZEK.png)
More for pei plot: More for pie: [GitIO](https://karobben.github.io/R/geom_pie.html)/[语雀](https://www.yuque.com/liuwenkan/rr/geom_pie)



# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
