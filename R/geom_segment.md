---
url: geom_segment2
---
# geom_segment

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580042754302-e41ae099-9e92-4350-a371-0f7ad7a03ca3.png#align=left&display=inline&height=691&name=image.png&originHeight=691&originWidth=1058&size=183176&status=done&style=none&width=1058)
<a name="1BDiL"></a>
# Quick Start

```r
library(ggplot2)
library(ggtheme)

ggplot(seals, aes(long, lat)) + theme_map()
		geom_segment(aes(xend = long + delta_long, yend = lat + delta_lat),
    arrow = arrow(length = unit(0.1,"cm")))
```


<a name="L96t9"></a>
# length

```r
P1 <- ggplot(seals, aes(long, lat)) + theme_map()+ ggtitle('0.1')+
		geom_segment(aes(xend = long + delta_long, yend = lat + delta_lat),
    arrow = arrow(length = unit(0.1,"cm")))+
		theme(plot.title = element_text(hjust = 0.5))

P2 <- ggplot(seals, aes(long, lat)) + theme_map()+ ggtitle('0.3')+
    geom_segment(aes(xend = long + delta_long, yend = lat + delta_lat),
    arrow = arrow(length = unit(0.3,"cm")))+
		theme(plot.title = element_text(hjust = 0.5))

P1|P2
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580044384121-9cbeb652-a455-4c90-8ded-a1b8aa99fdbb.png#align=left&display=inline&height=442&name=image.png&originHeight=442&originWidth=1122&size=318494&status=done&style=none&width=1122)<br />

<a name="odojW"></a>
# Bar

```r
counts <- as.data.frame(table(x = rpois(100,5)))
counts$x <- as.numeric(as.character(counts$x))

ggplot(counts, aes(x, Freq)) + theme_light()
  geom_segment(aes(xend = x, yend = 0), size = 10, lineend = "butt")
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580044640887-86b58a85-d446-4698-9507-ced2cd19b905.png#align=left&display=inline&height=333&name=image.png&originHeight=333&originWidth=808&size=11855&status=done&style=none&width=808)<br />
<br />

<a name="jVgvF"></a>
# geom_spoke
<br />
```r
df <- expand.grid(x = 1:10, y=1:10)
df$angle <- runif(100, 0, 2*pi)
df$speed <- runif(100, 0, sqrt(0.1 * df$x))

ggplot(df, aes(x, y)) + geom_point() + theme_light()+
  geom_spoke(aes(angle = angle), radius = 0.5)
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580047386218-332a98a1-b393-4edc-a46c-70718c7bd610.png#align=left&display=inline&height=640&name=image.png&originHeight=640&originWidth=1120&size=68400&status=done&style=none&width=1120)<br />

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
