---
url: ggradar
---

# GGradar

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579751569701-4e466d81-7a2d-408e-8215-f4f91611fbfe.png#align=left&display=inline&height=353&name=image.png&originHeight=619&originWidth=980&size=96199&status=done&style=none&width=559)

<a name="sCsRw"></a>
# Quick Start

```r
library(ggplot2)
library(ggradar)

mydata<-matrix(runif(40,0,1),5,8)
rownames(mydata) <- LETTERS[1:5]
colnames(mydata) <- c("Apple","Google","Facebook","Amozon","Tencent","Alibaba","Baidu","Twitter")
mynewdata<-data.frame(mydata)
Name<-c("USA","CHN","UK","RUS","JP")
mynewdata<-data.frame(Name,mynewdata)
ggradar(mynewdata)

ggradar(mynewdata) + theme(legend.position = 'none') 
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580053884743-7d678f2f-7913-4000-96df-c444acdd3b45.png#align=left&display=inline&height=527&name=image.png&originHeight=527&originWidth=705&size=86207&status=done&style=none&width=705)
```r
#Data structure
'''
Name     Apple    Google  Facebook    Amozon    Tencent    Alibaba     Baidu
A  USA 0.6028703 0.9975856 0.4771023 0.8630967 0.21543389 0.78643566 0.7611366
B  CHN 0.3853622 0.7067794 0.4991334 0.8006687 0.47394478 0.68875340 0.1547279
C   UK 0.2634778 0.3165925 0.8032880 0.5479650 0.87007110 0.01701491 0.3585789
D  RUS 0.9749844 0.6391640 0.0542372 0.2777984 0.04970435 0.38795458 0.4374871
E   JP 0.3928207 0.5548013 0.5891342 0.5367423 0.69436110 0.48937538 0.1104125
'''
```
<a name="TLyND"></a>
# Arguments

```r
ggradar(data,axis.label.size = 4,
grid.label.size =7,
group.line.width = 1,
group.point.size = 3,
plot.title = '这啥？')
```

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)




--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
