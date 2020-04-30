# geom_curve

<a name="EsYEd"></a>
# Quick Start

```r
ggplot() + geom_curve( aes(x = 1, y = 1, xend= 6, yend = 6))
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580002378693-66bbef77-0319-482b-899f-42065b8e936c.png#align=left&display=inline&height=309&name=image.png&originHeight=315&originWidth=306&size=9328&status=done&style=none&width=300)<br />‘geom_segment’ draws a straight line between points (x, y) and (xend, yend).<br />‘geom_curve’ draws a curved line. <br />

<a name="Mqwv9"></a>
# Arguments
<a name="fneug"></a>
## ncp

```r
p <- ggplot()
for(i in c(1:10)){
	p <- p+ geom_curve( aes(x = 1, y = 1, xend= 6, yend = 6),ncp = i)
}
p+ theme_light()
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580002841799-69649495-407b-42bf-b191-af6438addd24.png#align=left&display=inline&height=292&name=image.png&originHeight=351&originWidth=361&size=23697&status=done&style=none&width=300)<br />

<a name="NaZpK"></a>
## curvature

```r
p <- ggplot() 
for(i in c(-10:10)){ 
    p <- p+ geom_curve( aes(x = 1, y = 1, xend= 6, yend = 6), curvature = i*0.1) 
}
p+ theme_light()+ expand_limits(x=c(0,10),y=c(0,6))
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580004412550-d04d6262-c4f2-48c9-8e0f-4e483b8a991f.png#align=left&display=inline&height=276&name=image.png&originHeight=276&originWidth=330&size=38725&status=done&style=none&width=330)<br />

<a name="WHHOW"></a>
## angle

```r
p <- ggplot() 
for(i in c(1:9)){ 
    p <- p+ geom_curve( aes(x = 1, y = 1, xend= 6, yend = 6), angle = i*10) 
}
p+ theme_light()+ expand_limits(x=c(0,10),y=c(0,6))
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580003906479-b67a7ba6-db59-4087-8064-2a0ab787cde9.png#align=left&display=inline&height=590&name=image.png&originHeight=590&originWidth=599&size=73291&status=done&style=none&width=599)<br />
<br />

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
