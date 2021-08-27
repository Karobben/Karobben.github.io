---
title: "GGmap: geom_map | ggplot for maps"
ytitle: "geom_map | 用ggplot畫地圖"
description: "GGmap: geom_map"
url: geom_map2
date: 2020/08/13
toc: true
excerpt: "map function from ggplot"
tags: [R, Plot, ggplot, map]
category: [R, Plot, GGPLOT]
cover: 'https://s1.ax1x.com/2020/08/13/dSDpoF.png'
thumbnail: 'https://s1.ax1x.com/2020/08/13/dSDpoF.png'
priority: 10000
---


## Install

```r
install.packages('ggalt')  
```

文件下载: CLIWOC15.csv
`https://raw.githubusercontent.com/ljtyduyu/DataWarehouse/master/File/CLIWOC15.csv` (也许需要科学上网)

```r
library(ggplot2)  #需安装最新的2.0.0版本
library(dplyr)  #你也可以用内置的subset函数来代替filter函数
library(ggalt) #安装方法: devtools::install_github("hrbrmstr/ggalt")。需安装加载devtools包
library(ggthemes)

world <- map_data("world")
world <- world[world$region != "Antarctica",] # 剔除南极洲


dat <- read.csv("CLIWOC15.csv")
dat <- filter(dat, Nation != "Sweden")

ggplot()+ geom_map(data=world, map=world,
  aes(x=long, y=lat, map_id=region), fill="#00518E",
  color="white", fill="#7f7f7f", size=0.05, alpha=1/4)+
  geom_point(data=dat,aes(x=Lon3, y=Lat3, color=Nation),size=0.15, alpha=1/100)+
  scale_color_tableau()+ coord_proj("+proj=wintri")+ facet_wrap(~Nation)+
  theme_map()+ theme(strip.background=element_blank())+ theme(legend.position="none")
ggsave('map.png',w=500,h=450)
## graph shows as in head
```
![1](https://s1.ax1x.com/2020/08/13/dSDpoF.png)

<a name="b0FAh"></a>
## library(map)

```r
library(ggplot2)
library(maps)

data(us.cities)
big_citi <- subset(us.cities,pop > 500000)  ##人口大于50万的城市


##Quick plot (left)
qplot(long,lat,data=big_citi) + borders("state",size=0.5)
##ggsave('map2.png',w=4,h=2.6)

##Quick plot (right)
library(ggthemes)
library(ggrepel)
qplot(long,lat,data=big_citi) + borders("state",size=0.5)  +theme_map()+
  geom_label_repel(data=big_citi,aes(x=long,y=lat,label=name))
##ggsave('map3.png',w=8,h=5.2)
```

|![dSsgG4.jpg](https://s1.ax1x.com/2020/08/13/dSsgG4.jpg)|![dSsciF.jpg](https://s1.ax1x.com/2020/08/13/dSsciF.jpg)|
|:--:|:--:|
|map2.png|map3.png|
<a name="FG8Ad"></a>
## More
