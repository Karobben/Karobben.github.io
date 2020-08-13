---
title: "geom_qq"
description: "geom_qq"
url: geom_qq2
---

# geom_qq

<a name="aydhZ"></a>
## QQ plot
```r
ggplot(mtcars,aes(sample=mpg)) + geom_qq(aes(color='qq')) + geom_point(aes(mpg,cyl,color='point'))+
  geom_qq_line(aes(color='qqline'))+ theme_light()
```


![qqplot](https://i.loli.net/2020/06/18/QXvEDCrNh7cmza8.png)
我也没有搞懂是啥意思- -线马上,下次再来看



<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)


---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
