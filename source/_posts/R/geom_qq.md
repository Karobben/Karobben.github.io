---
title: "geom_qq"
description: "geom_qq"
url: geom_qq2
date: 2020/06/18
toc: true
excerpt: "R: ggplot, ggplot, qq plot"
tags: [R, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: 'https://i.loli.net/2020/06/18/QXvEDCrNh7cmza8.png'
thumbnail: 'https://i.loli.net/2020/06/18/QXvEDCrNh7cmza8.png'
priority: 10000
---

## geom_qq

<a name="aydhZ"></a>
### QQ plot
```r
ggplot(mtcars,aes(sample=mpg)) + geom_qq(aes(color='qq')) + geom_point(aes(mpg,cyl,color='point'))+
  geom_qq_line(aes(color='qqline'))+ theme_light()
```


![qqplot](https://i.loli.net/2020/06/18/QXvEDCrNh7cmza8.png)
我也没有搞懂是啥意思- -线马上,下次再来看



<a name="FG8Ad"></a>
## More



