---
url: geom_tile2
---
# geom_tile

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580048510936-fec0d7d9-24d7-4354-b0c5-db15365e3d1c.png#align=left&display=inline&height=425&name=image.png&originHeight=425&originWidth=730&size=12048&status=done&style=none&width=730)<br />

<a name="6qOmi"></a>
# Quick Start
```r
library(ggplot2)
df <- data.frame(
  x = rep(c(2, 5, 7, 9, 12), 2),
  y = rep(c(1, 2), each = 5),
  z = factor(rep(1:5, each = 2)),
  w = rep(diff(c(0, 4, 6, 8, 10, 14)), 2)
)

ggplot(df, aes(x, y)) + theme_light()+
	geom_tile(aes(fill = z), colour = "grey50")
```


```r
library(patchwork)

P1 <- ggplot(df, aes(x, y)) + theme_light()+ ggtitle('P1')+
	geom_tile(aes(fill = z), colour = "grey50")+
	theme(plot.title = element_text(hjust = 0.5))

P2 <- ggplot(df, aes(x, y, width = w)) + theme_light()+ ggtitle('P2')+
	theme(plot.title = element_text(hjust = 0.5))+
  geom_tile(aes(fill = z), colour = "grey50")

P3 <- ggplot(df, aes(x, y))+ geom_bar(aes(fill=z),stat='identity')+ theme_light()+
	ggtitle('bar plot')+ theme(plot.title = element_text(hjust = 0.5))

(P1|P2)/P3
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580048826017-b418a814-66b6-49eb-8e0d-fd867865c012.png#align=left&display=inline&height=468&name=image.png&originHeight=468&originWidth=742&size=20573&status=done&style=none&width=742)


<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)




---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
