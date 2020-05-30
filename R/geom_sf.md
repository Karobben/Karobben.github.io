# geom_sf

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580045445306-24183639-fd7b-41c8-bb0d-ba27865da9fc.png#align=left&display=inline&height=398&name=image.png&originHeight=398&originWidth=1155&size=112194&status=done&style=none&width=1155)

<a name="CHCOR"></a>
# Quick Start
```r
library(ggplot2)
nc <- sf::st_read(system.file("shape/nc.shp", package = "sf"), quiet = TRUE)
ggplot(nc) + geom_sf(aes(fill = AREA))+ theme_light()
```

This function needs "shp" data set. Coordinate information was in geometry column<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580045921868-f2a2022b-fc46-4122-95e7-a93706a949be.png#align=left&display=inline&height=139&name=image.png&originHeight=139&originWidth=1239&size=56896&status=done&style=none&width=1239)

```r
ggplot()
nc <- sf::st_read(system.file("shape/nc.shp", package = "sf"), quiet = TRUE)
ggplot(nc) +
  geom_sf(aes(fill = AREA))

world2 <- sf::st_transform(world1,
  "+proj=laea +y_0=0 +lon_0=155 +lat_0=-90 +ellps=WGS84 +no_defs")
 ggplot() + geom_sf(data = world2)+  theme_map()
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580046733865-c88aaa95-7468-4b80-9268-aac8e47b8f3c.png#align=left&display=inline&height=549&name=image.png&originHeight=676&originWidth=663&size=175444&status=done&style=none&width=538)
<a name="NTzPU"></a>
# Arguments list
```r
coord_sf(xlim = NULL, ylim = NULL, expand = TRUE, crs = NULL,
  datum = sf::st_crs(4326), label_graticule = waiver(),
  label_axes = waiver(), ndiscr = 100, default = FALSE,
  clip = "on")

geom_sf(mapping = aes(), data = NULL, stat = "sf",
  position = "identity", na.rm = FALSE, show.legend = NA,
  inherit.aes = TRUE, ...)

geom_sf_label(mapping = aes(), data = NULL, stat = "sf_coordinates",
  position = "identity", ..., parse = FALSE, nudge_x = 0,
  nudge_y = 0, label.padding = unit(0.25, "lines"),
  label.r = unit(0.15, "lines"), label.size = 0.25, na.rm = FALSE,
  show.legend = NA, inherit.aes = TRUE, fun.geometry = NULL)

geom_sf_text(mapping = aes(), data = NULL, stat = "sf_coordinates",
  position = "identity", ..., parse = FALSE, nudge_x = 0,
  nudge_y = 0, check_overlap = FALSE, na.rm = FALSE,
  show.legend = NA, inherit.aes = TRUE, fun.geometry = NULL)

stat_sf(mapping = NULL, data = NULL, geom = "rect",
  position = "identity", na.rm = FALSE, show.legend = NA,
  inherit.aes = TRUE, ...)

```


<a name="2SOp0"></a>
# China City
Specific Date is comming from [GuangchuangYu](https://guangchuangyu.github.io)<br />location: [https://github.com/GuangchuangYu/map_data](https://github.com/GuangchuangYu/map_data)<br />But as you know, downloading Data from Github is preaty slow.

<a name="xaf8Z"></a>
## Quick Start

```r
library(ggplot2)
data <- readRDS("cn_city_map.rds")
ggplot(data) + geom_sf(aes(fill = OBJECTID))+ theme_light()
```

![123.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/691897/1583311312206-a04387f1-aca1-4e5d-b61c-7fc35bcdae35.jpeg#align=left&display=inline&height=461&name=123.jpg&originHeight=461&originWidth=500&size=24318&status=done&style=none&width=500)



Location for main City (Data is from [skyme](https://www.cnblogs.com/skyme/p/5182149.html))
```r
City_loc = read.csv(text = "城市,jd,wd
北京,116.4666667,39.9
上海,121.4833333,31.23333333
天津,117.1833333,39.15
重庆,106.5333333,29.53333333
哈尔滨,126.6833333,45.75
长春,125.3166667,43.86666667
沈阳,123.4,41.83333333
呼和浩特,111.8,40.81666667
石家庄,114.4666667,38.03333333
太原,112.5666667,37.86666667
济南,117,36.63333333
郑州,113.7,34.8
西安,108.9,34.26666667
兰州,103.8166667,36.05
银川,106.2666667,38.33333333
西宁,101.75,36.63333333
乌鲁木齐,87.6,43.8
合肥,117.3,31.85
南京,118.8333333,32.03333333
杭州,120.15,30.23333333
长沙,113,28.18333333
南昌,115.8666667,28.68333333
武汉,114.35,30.61666667
成都,104.0833333,30.65
贵阳,106.7,26.58333333
福州,119.3,26.08333333
台北,121.5166667,25.05
广州,113.25,23.13333333
海口,110.3333333,20.03333333
南宁,108.3333333,22.8
昆明,102.6833333,25
拉萨,91.16666667,29.66666667
香港,114.1666667,22.3
澳门,113.5,22.2")
```

<a name="b2SLf"></a>
## Pinning the cities
```r
library(ggrepel)

ggplot(data) + geom_sf(aes(fill = OBJECTID))+
		geom_point(data=City_loc,aes(x=jd,y=wd))+
		geom_text_repel(data=City_loc,aes(x=jd,y=wd,label=城市))+
		theme_light()
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1583314607739-7c648cd6-6877-4e3a-aa9e-4dd8b50864e7.png#align=left&display=inline&height=544&name=image.png&originHeight=544&originWidth=566&size=142491&status=done&style=none&width=566)
<a name="mOPej"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)






---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
