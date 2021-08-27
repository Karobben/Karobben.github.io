---
title: "nCov(新冠状病毒数据获取与可视化)"
description: "nCov(新冠状病毒数据获取与可视化)"
url: ncov2
date: 2020/06/20
toc: true
excerpt: "This script is based on an GitHub project which stopped to updating. So, I'm sure you can find a better one"
tags: [R, Plot, map]
category: [R, Plot, VisuaProtocol]
cover: 'https://s1.ax1x.com/2020/06/20/NlHt9U.png'
thumbnail: 'https://s1.ax1x.com/2020/06/20/NlHt9U.png'
priority: 10000
---

## nCov(新冠状病毒数据获取与可视化)


<a name="sYvc9"></a>
## 1 Loading Packages
```r
library("httr")
library("jsonlite")
```

<a name="54cF1"></a>
## 2 Data acquiring

```r
base <- 'https://lab.isaaclin.cn/nCoV/api/' # api 网址
port <- 'area' #接口
get_raw <- GET(paste0(base, port)) # 获取链接
get_text <- content(get_raw, "text") # 获取数据
ncov_area <- fromJSON(get_text) #提取数据
```
![Nl73WD.png](https://s1.ax1x.com/2020/06/20/Nl73WD.png)

## 3 Data
```r
remotes::install_github('pzhaonet/ncovr')
library("ncovr")
ncov <- get_ncov()         # Downloading the Date... It takes me about 10min

```

這一步可能會因爲網絡問題而下載數據失敗. 可以直接用瀏覽器下載RDS, 然後本地讀取<br />下載地址: https://github.com/pzhaonet/ncov/raw/master/static/data-download/ncov.RDS<br />讀取方式:

```r
ncov <- readRDS("ncov.RDS")
```

讀取數據了, 就是喜聞樂見的, 清洗和可視化了
```r
## area data
TB = ncov$area
## China
中国  = TB[TB$countryName == "中国",]
中国$日期 = as.Date.POSIXct(中国$updateTime/1000)
湖北 =中国[中国$provinceShortName=='湖北',]
```

这里的时间困惑了我很久. 表格里的时间, 举例: 1583295001876, 通过as.Date.POSIXct 转化以后,成了"52142-08-15". 通过删除后面3位数, 876, 及可获得正确时间"2020-03-04". 我也不知道为什么

```r
library(ggplot2)
ggplot(湖北)+
  geom_point(aes(x=日期,y=confirmedCount)) + #Dot plot
  geom_smooth(aes(x=日期,y=confirmedCount,color = continentName)) + # Smooth line
  theme_light()
```
![Nl7awt.png](https://s1.ax1x.com/2020/06/20/Nl7awt.png)
<br />加上几个别的数据
```r
ggplot(湖北)+  
        geom_smooth(aes(x=日期,y=confirmedCount))+
        geom_smooth(aes(x=日期,y=deadCount))+
        geom_smooth(aes(x=日期,y=curedCount))+
        geom_point(aes(x=日期, y=confirmedCount, color='confirmed'))+  
        geom_point(aes(x=日期, y=deadCount, color='dead'))+  
        geom_point(aes(x=日期, y=curedCount,color= 'cured'))+
        theme_light()   
```
![Nl7dTP.png](https://s1.ax1x.com/2020/06/20/Nl7dTP.png)
<br />同样的方法看看别的省:

```r
ggplot(中国[中国$provinceShortName=='湖南',])+  
        geom_smooth(aes(x=日期,y=confirmedCount))+
        geom_smooth(aes(x=日期,y=deadCount))+
        geom_smooth(aes(x=日期,y=curedCount))+
        geom_point(aes(x=日期, y=confirmedCount, color='confirmed'))+  
        geom_point(aes(x=日期, y=deadCount, color='dead'))+  
        geom_point(aes(x=日期, y=curedCount,color= 'cured'))+
        theme_light()   
```

![Nl7BY8.png](https://s1.ax1x.com/2020/06/20/Nl7BY8.png)
All Provinces
```r
ggplot(中国)+   
    geom_smooth(aes(x=日期,y=confirmedCount))+  
    geom_smooth(aes(x=日期,y=deadCount))+  
    geom_smooth(aes(x=日期,y=curedCount))+  
    geom_point(aes(x=日期, y=confirmedCount, color='confirmed'))+   
    geom_point(aes(x=日期, y=deadCount, color='dead'))+   
    geom_point(aes(x=日期, y=curedCount,color= 'cured'))+  
    theme_light() +facet_wrap(provinceShortName ~., scales =  'free')             
```


![Nl7JQH.jpg](https://s1.ax1x.com/2020/06/20/Nl7JQH.jpg)

<a name="Up7pb"></a>
## 4 map
<a name="SK6ny"></a>
### China city
cn_city_map.rds is required:<br />Specific Date is comming from [GuangchuangYu](https://guangchuangyu.github.io)<br />location: [https://github.com/GuangchuangYu/map_data](https://github.com/GuangchuangYu/map_data)<br />But as you know, downloading Data from Github is preaty slow.
```r
data <- readRDS("cn_city_map.rds")
```
Take 湖北 as an example:

```r
湖北地图 <- data[ data$ADMINCODE  %in% 湖北$cities[[1]]$locationId,]
ggplot(湖北地图) + geom_sf(aes(fill = OBJECTID))+ theme_light()
```
![Nl7UeI.png](https://s1.ax1x.com/2020/06/20/Nl7UeI.png)

Adding nCov information

```r
## sort
湖北地图 = 湖北地图[match(湖北$cities[[1]]$locationId,湖北地图$ADMINCODE),]

## Graph Left
ggplot(湖北地图) +
       geom_sf(aes(fill = 湖北$cities[[1]]$currentConfirmedCount))+
       theme_light()

## Log the count before fill
ggplot(湖北地图) +
       geom_sf(aes(fill = log(湖北$cities[[1]]$currentConfirmedCount)))+
       theme_light()
```

|![Nl70Ff.png](https://s1.ax1x.com/2020/06/20/Nl70Ff.png)|![NlHt9U.png](https://s1.ax1x.com/2020/06/20/NlHt9U.png)|
| --- | --- |


<a name="qcz6i"></a>
### China Province
Data is shared by : [skyme](https://www.cnblogs.com/skyme/p/5182149.html)<br />Download locaktion: [Click Here!](http://cos.name/wp-content/uploads/2009/07/chinaprovinceborderdata_tar_gz.zip)
```r
China <-  sf::st_read('bou2_4p.shp')
```

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

```r
library(ggrepel)
Today = 中国[中国$日期=="2020-03-04",]
Cities = data.frame()
for( i in Today$cities){
  Cities = rbind(Cities,i)
}

AAA = Cities[Cities$cityName %in% City_loc$城市,]                                                        
AAA2 = City_loc[match(AAA$cityName, City_loc$城市),]     
## now, Map data is in AAA, location of cites are in AAA2

ggplot(China) + geom_sf(color='white')+
       geom_text_repel(data=AAA2,aes(x=jd,y=wd,label=城市))+
       geom_point(data=AAA2,aes(x=jd,y=wd,
       color=log(AAA$confirmedCount),
       size=AAA$confirmedCount),alpha=0.8)+
       theme_light()+scale_color_gradient(low = "white",high = "red")
```
![Nl7Yyd.png](https://s1.ax1x.com/2020/06/20/Nl7Yyd.png)


<a name="QLhCR"></a>
## 5 世界

```r
TB$日期 = as.Date.POSIXct(TB$updateTime/1000)
ggplot(TB)+
    geom_smooth(aes(x=日期,y=confirmedCount))+   
    geom_smooth(aes(x=日期,y=deadCount))+   
    geom_smooth(aes(x=日期,y=curedCount))+   
    geom_point(aes(x=日期, y=confirmedCount, color='confirmed'))+    
    geom_point(aes(x=日期, y=deadCount, color='dead'))+    
    geom_point(aes(x=日期, y=curedCount,color= 'cured'))+   
    theme_light() +facet_wrap(countryName ~., scales =  'free')   
```

Keep the countries which aboves 1000 confiremed cases.
```r
TB2 <- TB[TB$countryName %in% unique(TB$countryName[which(TB$confirmedCount>1000)]),]

ggplot(TB2)+
    geom_smooth(aes(x=日期,y=confirmedCount))+   
    geom_smooth(aes(x=日期,y=deadCount))+   
    geom_smooth(aes(x=日期,y=curedCount))+   
    geom_point(aes(x=日期, y=confirmedCount, color='confirmed'))+    
    geom_point(aes(x=日期, y=deadCount, color='dead'))+    
    geom_point(aes(x=日期, y=curedCount,color= 'cured'))+   
    theme_light() +facet_wrap(countryName ~., scales =  'free')   
```

![Nl7GSe.jpg](https://s1.ax1x.com/2020/06/20/Nl7GSe.jpg)
