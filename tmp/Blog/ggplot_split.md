---
title: "ggplot畫斷層圖"
description: "ggplot畫斷層圖"
url: ggplot_splitbar
---

# ggplot畫斷層圖

```r
library(ggplot2)
library(patchwork)

data(cars)
cars[1,2] =100000

p <- ggplot(cars,aes(x=speed,y=dist)) + geom_bar(stat='identity')
```
通過patchwork， 拼接得到想要的圖
```r

p1 <- p + coord_cartesian(ylim = c(0,400))
p2 <- p + coord_cartesian(ylim = c(99998,100020))+ theme(axis.text.x = element_blank(), axis.title = element_blank(), axis.ticks.x = element_blank())
layout <- 'A\nB\nB\nB'
p2/p1 + plot_layout(design = layout)
```
|原圖|拼接圖|
|---|---|
|[![tbJxSI.png](https://s1.ax1x.com/2020/06/11/tbJxSI.png)](https://imgchr.com/i/tbJxSI)|![2](https://i.loli.net/2020/06/11/bHMgopUWjXSDNAh.png)|

# 函數封裝
```r
SplitBar <-  function(p, Y1,Y2,Y3, Y0=0,R=c(1,1)){
  Lay = c(rep("A",R[1]),rep("B",R[2]))
  layout=""
  for( i in Lay){
    layout=paste(layout,i,sep="\n")
  }
  p1 <- p +  coord_cartesian(ylim = c(Y2,Y3))+
    theme(axis.text.x = element_blank(),
    axis.title = element_blank(), axis.ticks.x = element_blank(),
    legend.position =   'none')
  p2 <- p +  coord_cartesian(ylim = c(Y0,Y1))+ theme(title = element_blank(), plot.title = element_blank())
  p1/p2 + plot_layout(design = layout)
}

SplitBar(p,450,99998,100011,0,c(1,10))
```


```r
p <- ggplot(cars,aes(x=speed,y=dist)) + geom_bar(,fill=cars$speed,stat='identity') +
  theme_light()+ ggtitle('哈哈哈哈') + theme( plot.title  = element_text(hjust = 0.5))

SplitBar(p,450,99998,100021,0,c(1,5))
```
|原圖|拼接圖|
|---|---|
|[![tbUS61.md.png](https://s1.ax1x.com/2020/06/11/tbUS61.md.png)](https://imgchr.com/i/tbUS61)|[![tbUCm6.md.png](https://s1.ax1x.com/2020/06/11/tbUCm6.md.png)](https://imgchr.com/i/tbUCm6)|

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
