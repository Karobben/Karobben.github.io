---
url: extra_lines
---

# geom Extra Lines

geom_vline()<br />geom_hline()<br />geom_abline()

```r
library(ggplot2)
library(patchwork)

P1 <- ggplot(mtcars)+ geom_point(aes(mpg, cyl)) +
	geom_vline( xintercept = 20) + ggtitle('vline') +theme_light()
P2 <- ggplot(mtcars)+ geom_point(aes(mpg, cyl)) +
geom_hline( yintercept = 7) + ggtitle('hline') +theme_light()
P3 <- ggplot(mtcars, aes(wt, mpg)) + geom_point() + geom_abline(intercept = 25, slope = -1) + 
	ggtitle("abline")+theme_light()

P3|(P1/P2)
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580026647767-5d1c5819-f954-46c4-9f1f-85036a4cd116.png#align=left&display=inline&height=518&name=image.png&originHeight=518&originWidth=597&size=37134&status=done&style=none&width=597)<br />

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)







--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
