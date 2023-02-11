---
title: "R-gganimate | ggplot examples"
ytitle: "gganimate | 用ggplot做動畫"
description: "R-gganimate | 用ggplot做動畫"
url: gganimate2
date: 2020/06/19
toc: true
excerpt: "animate solution package for ggplot"
tags: [R, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: 'https://i.loli.net/2020/06/19/XLQgcEmJGlsOhC6.gif'
thumbnail: 'https://i.loli.net/2020/06/19/XLQgcEmJGlsOhC6.gif'
priority: 10000
---


```r
library(ggplot2)
library(gganimate)

ggplot(mtcars, aes(factor(cyl), mpg)) +
geom_boxplot()

TB= data.frame(Shrink(world,40),Group=1)
Num=1
for(i in c(1:36)){
  tmp = data.frame(Shrink(world,40),Group=1)
  Num= Num+1
  tmp$lat = tmp$lat +rnorm(nrow(tmp),0,1)
  tmp$Group=Num
  TB = rbind(TB,tmp)
}

## animation::ani.options(ani.width= 1000, ani.height=1000, ani.res = 1000)

ggplot()+ geom_point(data=TB,aes(x=long, y=lat),size=0.3, color="#00518E") +
  theme_map() + coord_map("ortho", orientation = c(30, 100, 0)) +
  transition_time(Group)

anim_save("map.gif")
```
![Earth](https://i.loli.net/2020/06/19/XLQgcEmJGlsOhC6.gif)

## Here comes the gganimate code

```R
transition_states(
  gear,
  transition_length = 2,
  state_length = 1
)
enter_fade()
exit_shrink()
ease_aes('sine-in-out')
```

## Animate bar

[https://gganimate.com/](https://gganimate.com/)

```R
library(gapminder)

ggplot(gapminder, aes(gdpPercap, lifeExp, size = pop, colour = country)) +
  geom_point(alpha = 0.7, show.legend = FALSE) +
  scale_colour_manual(values = country_colors) +
  scale_size(range = c(2, 12)) +
  scale_x_log10() +
  facet_wrap(~continent)
```

## Here comes the gganimate specific bits

```R
labs(title = 'Year: {frame_time}', x = 'GDP per capita', y = 'life expectancy') +
transition_time(year) +
ease_aes('linear')
```

## save

```r
anim_save("test.gif")

d <- trans_3d_2d(Ball[1:3])
```
d![wqe](https://g.yuque.com/gr/latex?Group%20%3D%20Ball#card=math&code=Group%20%3D%20Ball&height=18&width=101)X4
