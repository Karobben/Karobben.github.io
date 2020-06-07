---
url: geom_rug
---

# geom_rug

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580039021389-e96593e6-5169-4ec7-bf95-d06dfeac7496.png#align=left&display=inline&height=369&name=image.png&originHeight=369&originWidth=646&size=19153&status=done&style=none&width=646)
<a name="fm1kg"></a>
# Quick Inst
```r
library(ggplot2)
library(patchworks)

ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") +
	geom_rug() + theme_light()
```

<a name="njg2Q"></a>
# arguments

<a name="wBLEt"></a>
## outside

```r
 ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
geom_rug( outside = TRUE)+ coord_cartesian(clip = "off")
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580039900077-62d22fab-73a5-4ed8-b67c-8aead0ee3f69.png#align=left&display=inline&height=316&name=image.png&originHeight=316&originWidth=517&size=16809&status=done&style=none&width=517)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580039249545-acf1c65c-0a60-45b2-bae8-bf02266e843e.png#align=left&display=inline&height=357&name=image.png&originHeight=357&originWidth=557&size=16764&status=done&style=none&width=557)
<a name="eA81n"></a>
## side

```r
library(patchwork)
P1 <- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
		geom_rug( sides='t', color='red') + ggtitle('t') +theme(plot.title = element_text(hjust = 0.5))
P2 <- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
		geom_rug( sides='r', color='red') + ggtitle('r') +theme(plot.title = element_text(hjust = 0.5))
P3 <- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
		geom_rug( sides='b', color='red') + ggtitle('b') +theme(plot.title = element_text(hjust = 0.5))
P4 <- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
		geom_rug( sides='l', color='red') + ggtitle('l') +theme(plot.title = element_text(hjust = 0.5))

(P1|P2)/(P3|P4)
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580039687805-ae50d0c9-c47b-4cb7-adbc-f74f42c1575e.png#align=left&display=inline&height=590&name=image.png&originHeight=590&originWidth=874&size=49479&status=done&style=none&width=874)<br />

<a name="154js"></a>
## length


```r
P1<- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
    geom_rug()+ ggtitle('NA') + theme(plot.title = element_text(hjust = 0.5))
P2<- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
    geom_rug( length = unit(0.5, "npc"))+ ggtitle('0.5') + theme(plot.title = element_text(hjust = 0.5))
P3<- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
    geom_rug( length = unit(1, "npc"))+ ggtitle('1') + theme(plot.title = element_text(hjust = 0.5))

P1/(P2|P3)
```

<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580040194659-63ba2800-b949-4772-9010-2ecdf203d715.png#align=left&display=inline&height=410&name=image.png&originHeight=410&originWidth=869&size=57238&status=done&style=none&width=869)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580039626553-b498916d-144b-4728-a661-1ca937713781.png#align=left&display=inline&height=590&name=image.png&originHeight=590&originWidth=869&size=49637&status=done&style=none&width=869)


---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
