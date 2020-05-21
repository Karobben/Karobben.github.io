---
url: gganimate2
---

# R-gganimate

library(ggplot2)<br />
library(gganimate)

ggplot(mtcars, aes(factor(cyl), mpg)) +<br />
geom_boxplot() +

```r
TB= data.frame(Shrink(world,40),Group=1)
Num=1
for(i in c(1:36)){
  tmp = data.frame(Shrink(world,40),Group=1)
  Num= Num+1
	tmp$lat = tmp$lat +rnorm(nrow(tmp),0,1)
  tmp$Group=Num
  TB = rbind(TB,tmp)
}

ggplot()+ geom_point(data=TB,aes(x=long, y=lat),size=0.3, color="#00518E") +
	theme_map() + coord_map("ortho", orientation = c(30, 100, 0)) +
	transition_time(Group)

anim_save("map.gif")
```
![map.gif](https://cdn.nlark.com/yuque/0/2020/gif/691897/1580010244077-fb1be6ee-b542-4d6d-ba56-e87d4f031998.gif#align=left&display=inline&height=480&name=map.gif&originHeight=480&originWidth=480&size=1502574&status=done&style=none&width=480)
<a name="2fe6d3c7"></a>
# Here comes the gganimate code

transition_states(<br />
gear,<br />
transition_length = 2,<br />
state_length = 1<br />
) +<br />
enter_fade() +<br />
exit_shrink() +<br />
ease_aes('sine-in-out')

<a name="4edfa2d3"></a>
# Animate bar

[https://gganimate.com/](https://gganimate.com/)

library(gapminder)

ggplot(gapminder, aes(gdpPercap, lifeExp, size = pop, colour = country)) +<br />
geom_point(alpha = 0.7, show.legend = FALSE) +<br />
scale_colour_manual(values = country_colors) +<br />
scale_size(range = c(2, 12)) +<br />
scale_x_log10() +<br />
facet_wrap(~continent) +

<a name="67cf702a"></a>
# Here comes the gganimate specific bits

labs(title = 'Year: {frame_time}', x = 'GDP per capita', y = 'life expectancy') +<br />
transition_time(year) +<br />
ease_aes('linear')

<a name="save"></a>
# save

anim_save("test.gif")

d <- trans_3d_2d(Ball[1:3])<br />
d![](https://g.yuque.com/gr/latex?Group%20%3D%20Ball#card=math&code=Group%20%3D%20Ball&height=18&width=101)X4

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)






--------------------------------------------------------------------------------------------------------------------------------------------<br />github: https://github.com/Karobben<br />blog: Karobben.github.io<br />R 语言画图索引: https://karobben.github.io/R/R-index.html
