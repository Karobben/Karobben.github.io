---
url: geom_bin2d2
---
# geom_bin2d


![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580013586134-cebe2794-338c-446f-b2fd-fee3e5e0f0de.png#align=left&display=inline&height=669&name=image.png&originHeight=669&originWidth=1060&size=19196&status=done&style=none&width=1060)

<a name="4wGpq"></a>
# Quick Start
```r
library(ggplot2)
library(ggthemes)

world <- map_data("world")
ggplot(world, aes( long, lat)) +geom_bin2d()  + theme_map()
```

<a name="vmNgc"></a>
# Arguments
<a name="N6aE2"></a>
## bins
x=y=bins+1
```r
library(patchwork)

P1 <- ggplot(world, aes( long, lat)) +geom_bin2d(bins = 10)  + theme_map() +
			ggtitle('bins=10')+ theme(plot.title = element_text(hjust=0.5,size=20))
P2 <- ggplot(world, aes( long, lat)) +geom_bin2d(bins = 100)  + theme_map() +
			ggtitle('bins=100')+ theme(plot.title = element_text(hjust=0.5,size=20))

P1/P2
```


![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580013945709-8a623246-3b31-4aed-a74d-883a55c929e6.png#align=left&display=inline&height=639&name=image.png&originHeight=639&originWidth=630&size=33173&status=done&style=none&width=630)<br />

<a name="pMKRk"></a>
## binwidth
```r
library(RColorBrewer)
colorRampPalette(rev(brewer.pal(n = 7,name = "RdYlBu"))) -> cc

P1 <- ggplot(world, aes( long, lat)) +geom_bin2d(binwidth = c(0.1, 0.1))+
		theme_map() +ggtitle('0.1 0.1')+ theme(plot.title = element_text(hjust=0.5,size=20))+
		scale_fill_gradientn(colors=cc(100))
P2 <- ggplot(world, aes( long, lat)) +geom_bin2d(binwidth = c(0.1, 10))+
		theme_map() +ggtitle('0.1 10')+ theme(plot.title = element_text(hjust=0.5,size=20))+
		scale_fill_gradientn(colors=cc(100))
P3 <- ggplot(world, aes( long, lat)) +geom_bin2d(binwidth = c(10, 0.1))+
		theme_map() +ggtitle('10 0.1')+ theme(plot.title = element_text(hjust=0.5,size=20))+
		scale_fill_gradientn(colors=cc(100))
P4 <- ggplot(world, aes( long, lat)) +geom_bin2d(binwidth = c(10, 10))+
		theme_map() +ggtitle('10 10')+ theme(plot.title = element_text(hjust=0.5,size=20))+
		scale_fill_gradientn(colors=cc(100))

(P1|P2)/(P4|P3)
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580052808856-8356b6dc-4e6c-47ef-80d2-48ea064af220.png#align=left&display=inline&height=549&name=image.png&originHeight=549&originWidth=770&size=43351&status=done&style=none&width=770)

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)




--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
