---
url: geom_map2
---

# GGmap: geom_map

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579786627467-be905073-1422-4905-a312-f8a4108449a9.png#align=left&display=inline&height=530&name=image.png&originHeight=696&originWidth=979&size=258040&status=done&style=none&width=746)

```r
install.packages('ggalt')  
```

文件下载:[CLIWOC15.csv](https://raw.githubusercontent.com/ljtyduyu/DataWarehouse/master/File/CLIWOC15.csv)

```r
library(ggplot2)  #需安装最新的2.0.0版本
library(dplyr)  #你也可以用内置的subset函数来代替filter函数
library(ggalt) #安装方法: devtools::install_github("hrbrmstr/ggalt")。需安装加载devtools包
library(ggthemes)

world <- map_data("world")
world <- world[world$region != "Antarctica",] # 剔除南极洲


dat <- read.csv("CLIWOC15.csv")
dat <- filter(dat, Nation != "Sweden")

gg <- ggplot()+ geom_map(data=world, map=world,
	aes(x=long, y=lat, map_id=region), fill="#00518E",
	color="white", fill="#7f7f7f", size=0.05, alpha=1/4)+
	geom_point(data=dat,aes(x=Lon3, y=Lat3, color=Nation),size=0.15, alpha=1/100)+
	scale_color_tableau()+ coord_proj("+proj=wintri")+ facet_wrap(~Nation)+
	theme_map()+ theme(strip.background=element_blank())+ theme(legend.position="none")
gg
# graph shows as in head
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579786619592-4124512b-2264-411b-b4dd-0ff47f4bf536.png#align=left&display=inline&height=696&name=image.png&originHeight=696&originWidth=979&size=258040&status=done&style=none&width=979)

<a name="b0FAh"></a>
# library(map)

```r
library(ggplot2)
library(maps)

data(us.cities)
big_citi <- subset(us.cities,pop > 500000)  ##人口大于50万的城市


#Quick plot (left)
qplot(long,lat,data=big_citi) + borders("state",size=0.5)

#Quick plot (right)
library(themes)
library(ggrepel)
qplot(long,lat,data=big_citi) + borders("state",size=0.5)  +theme_map()+
	geom_label_repel(data=big_citi,aes(x=long,y=lat,label=name))
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579879615029-4b3dd184-7177-40e8-974d-702fe5ccc5b0.png#align=left&display=inline&height=240&name=image.png&originHeight=405&originWidth=586&size=57663&status=done&style=none&width=347)![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579785807568-59258b75-0aca-410b-8228-916dc6ac8659.png#align=left&display=inline&height=240&name=image.png&originHeight=346&originWidth=562&size=82851&status=done&style=none&width=390)


<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)




---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
