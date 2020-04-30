# geom_rangeframe


```r
library(ggthemes)
library(patchwork)
library(ggplot2)

P1 <- ggplot(mtcars,aes(wt,mpg))+ ggtitle('Has rangeframe')+
      geom_point()+geom_rangeframe()+theme_tufte()+ theme(plot.title=element_text(hjust=0.5)) 
P2 <- ggplot(mtcars,aes(wt,mpg))+ ggtitle('No rangeframe')+
      geom_point()+theme_tufte()+ theme(plot.title=element_text(hjust=0.5)) 
P1|P2
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580037794666-eea34fd2-1dff-4204-ae1d-c26a12d0d1c3.png#align=left&display=inline&height=367&name=image.png&originHeight=270&originWidth=549&size=17346&status=done&style=none&width=746)<br />
<br />

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
