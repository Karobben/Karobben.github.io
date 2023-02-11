---
title: "leaflet in R"
description: "Leaflet is an Js library which support the R API. You can draw high complicate and interoperable maps with it"
date: 2020/08/15
url: leaflet
toc: true
excerpt: "Leaflet is an Js library which support the R API. You can draw high complicate and interoperable maps with it"
tags: [R, Plot, map]
category: [R, Plot, Maps]
cover: 'https://s1.ax1x.com/2020/08/15/dk0Jwn.png'
thumbnail: 'https://s1.ax1x.com/2020/08/15/dk0Jwn.png'
priority: 10000
---

## leaflet

```r
install.packages("leaflet")
```

## Quick start

```r
library(leaflet)

m <- leaflet()
at <- addTiles(m)
addMarkers(at,lng=116.391, lat=39.912, popup="这里是北京")
```
![dk0Jwn.png](https://s1.ax1x.com/2020/08/15/dk0Jwn.png)

## 中国区使用高德地图

```r
install.packages("leafletCN")
library(leafletCN)


m <- leaflet() %>%   amap()
at <- addTiles(m)
addMarkers(at,lng=116.391, lat=39.912, popup="这里是北京")
```
结果差不多哦的， 但是加了 `amap()` 参数，加载速度， 会快很多。


## two or more marks on the map

We can make it by pipelines

```r
m <- leaflet() %>%   amap()
at <- addTiles(m)
addMarkers(at,lng=116.391, lat=39.912, popup="这里是北京")
addMarkers(at,lng=116.391, lat=38.912, popup="这里是北京")

```
![dk0j1S.png](https://s1.ax1x.com/2020/08/15/dk0j1S.png)

## adding lines



```r
m <- leaflet() %>%   amap()
m<- setView(m,lng=116.38,lat=39.9,zoom=6)
at <- addTiles(m)
addMarkers(at,lng=126.6623854637146, lat=45.73903109525129, popup="学校; 哈九中") %>%
addMarkers(at,lng=126.61242295716093, lat=45.7074338843242, popup="市图书馆") %>%
addMarkers(at,lng=126.47783875465393, lat=45.809739913121916, popup="赛信生物; 待定") %>%
addMarkers(at,lng=126.61695957183838, lat=45.721858584688206, popup="殷氏生物; 中兴街中关村基地一楼; 周二上午10点") %>%
addMarkers(at,lng=126.58702611923218, lat=45.69826679861071, popup="销售，E区 东南门; 哈西万达华宅E3栋1单元2401室; 周三上午9点")




,  

```

---
## Reference:
[大虾卢; R语言在线地图神器：Leaflet for R包（一）; 2016; CNDS](https://blog.csdn.net/allenlu2008/article/details/52816708)
