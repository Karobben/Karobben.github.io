---
url: geom_qq2
---

# geom_qq

<a name="aydhZ"></a>
## QQ plot
```r
ggplot(mtcars,aes(sample=mpg)) + geom_qq(aes(color='qq')) + geom_point(aes(mpg,cyl,color='point'))+
	geom_qq_line(aes(color='qqline'))+ theme_light()
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580028319239-dbb6922b-8501-41cd-8ff3-bace95bdae7b.png#align=left&display=inline&height=485&name=image.png&originHeight=485&originWidth=537&size=25709&status=done&style=none&width=537)<br />我也没有搞懂是啥意思- -线马上,下次再来看


<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)


<br />**<br />**<br />**--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
