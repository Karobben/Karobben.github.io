---
url: geom_polygon2
---

# GGmap: geom_polygon

主要参考: [https://blog.csdn.net/kMD8d5R/article/details/86582019](https://blog.csdn.net/kMD8d5R/article/details/86582019)

![map.gif](https://cdn.nlark.com/yuque/0/2020/gif/691897/1579462256784-925aa6e5-8695-4125-8cee-566de006fa60.gif#align=left&display=inline&height=2720&name=map.gif&originHeight=2720&originWidth=5823&size=6701944&status=done&style=none&width=5823)
```r
install.packages('mapproj')
```

<a name="xNsgR"></a>
# 快速上手
```r
library(ggplot2)
library(ggthemes)

# 世界地图，比较好的配色
world <- map_data("world")
worldmap <- ggplot(world, aes(x = long, y = lat, group = group)) +
    geom_polygon(fill = "#00518E",color = "#317DA4") +
    scale_y_continuous(breaks = (-2:2) * 30) +
    scale_x_continuous(breaks = (-4:4) * 45)

# 正射投影
worldmap + coord_map("ortho") # 默认北极为中心点。  
# 南极为中心点
worldmap + coord_map("ortho", orientation = c(30, 100, 0))# 中国 中心
worldmap + coord_map("ortho", orientation = c(-90, 0, 30)) # 顺时针旋转30度
worldmap + coord_map("ortho", orientation = c(41, -74, 0)) # 随便取一点

#下图
worldmap + coord_map("ortho", orientation = c(30, 100, 0))+ theme_map()
```

![test.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579462068577-fa059bc6-99df-49a9-ad1a-a9841bd9a438.png#align=left&display=inline&height=1025&name=test.png&originHeight=1025&originWidth=1101&size=228048&status=done&style=none&width=1101)
<a name="D48Ow"></a>
# 原理

```r
x=c(0,0,6,6)
y=c(0,7,0,8)
TB=data.frame(X=x,Y=y)

gplot(TB,aes(X,Y)) + geom_polygon(aes(fill='red')) + geom_point() + theme_light()  
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580027438008-ec9f63ab-91c7-4080-8b6c-f94129e214da.png#align=left&display=inline&height=255&name=image.png&originHeight=255&originWidth=303&size=8312&status=done&style=none&width=303)

<a name="eGbgH"></a>
# 动画
<a name="uJRTA"></a>
## 1. gganimate
gganimate 只能画平面图的动画，不能画球状以后的动画<br />[gps.txt](https://www.yuque.com/attachments/yuque/0/2020/txt/691897/1579462446201-e55a4ce9-d9e4-4d71-873a-c30c3128159e.txt?_lake_card=%7B%22uid%22%3A%221579462446095-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Ftxt%2F691897%2F1579462446201-e55a4ce9-d9e4-4d71-873a-c30c3128159e.txt%22%2C%22name%22%3A%22gps.txt%22%2C%22size%22%3A391%2C%22type%22%3A%22text%2Fplain%22%2C%22ext%22%3A%22txt%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22n4KRD%22%2C%22card%22%3A%22file%22%7D)<br />随便测试一下
```r
library(gganimate)

City = read.table('gps.txt')
City$Group=1
Num=nrow(City)
for(i in c(2:10)){
  tmp = City[1:Num,1:3]
  tmp$Group=i
  tmp[[3]]=tmp[[3]]+i-1
  City =rbind(City,tmp)}

ggplot(head(City,30))+
	geom_polygon(data=world,aes(x = long, y = lat, group = group),
		fill = "#00518E",color = "#317DA4")+
	geom_point(data=City,aes(x=V2,y=V3)) +  
	geom_text(data=head(City,Num),aes(x=V2,y=V3,label=V1))+
	coord_cartesian(xlim=c(70,150),ylim = c(10,65))+
	transition_time(City$Group) + theme_map()

# 简单示范
```

![123.gif](https://cdn.nlark.com/yuque/0/2020/gif/691897/1579463358762-15102158-f3f8-416d-8e9c-13892b527733.gif#align=left&display=inline&height=480&name=123.gif&originHeight=480&originWidth=480&size=2327788&status=done&style=none&width=480)
<a name="R4vCh"></a>
## 2.多 png 转 gif
先画出一系列的png，在叠加成gif
```r
#旋转
library(ggrepel)
p <- ggplot(head(City,15))+ geom_polygon(data=world,aes(x = long, y = lat, group = group),fill = "#00518E",color = "#317DA4")+
         geom_point(data=City,aes(x=V2,y=V3))  + coord_map("ortho")+
         geom_text(data=head(City,Num),aes(x=V2,y=V3,label=V1))+ theme_map()
for(i in c(1:5)){
  p = p + coord_map("ortho", orientation = c(30, 50+i*20, 0))
  ggsave(paste(i,'_map.png',sep=''))
  }

＃bash 下完成
＃convert $(ls  *_map.png| sort -n) map.gif
```
<a name="n6MZ4"></a>
# 各种杂耍
<a name="DJlJs"></a>
## 加上经纬线
\[经纬线函数链接](https://www.yuque.com/liuwenkan/bni63i/bwkcrz#rlfqy)/
```r
#杂技函数
经纬线() +geom_polygon(data=world, aes(x = long, y = lat, group = group),
    		fill = "#00518E",color = "#317DA4") +
    scale_y_continuous(breaks = (-2:2) * 30) +
		coord_map("ortho", orientation = c(30, 100, 0)) +
    scale_x_continuous(breaks = (-4:4) * 45)+ theme_map()+


```
![123.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579465902517-0cd86c41-84f1-4840-8255-bd53afaa944d.png#align=left&display=inline&height=2628&name=123.png&originHeight=2628&originWidth=3080&size=1109016&status=done&style=none&width=3080)
<a name="8v0r9"></a>
## 链接两点
这里用到Connet函数，详见“[曲线链接两点](https://www.yuque.com/liuwenkan/bni63i/bwkcrz#1aCF2)” <br />创建地点
```bash
echo "巴黎	2.294694	48.856958
墨尔本	144.958832	-37.812164
马德里	-3.677528	40.390197
SD	-117.071944	32.775554
马塞卢	27.512883	-29.363468
罗萨里奥	-60.62623	-32.949375
东京	139.752725	35.68461" > 20City
```

```r
北京= c(116.4167, 39.91667)                                                                                                   

City2=read.table('20City')  

建立链接
Num=0
Result=data.frame()
for(i in c(1:nrow(City2))){
    Num=Num+1
    tmp = Connet(北京,c(City2[i,][[2]],City2[i,][[3]]),Space=pi/10)
    tmp$Group=Num
    Result = rbind(Result,tmp)
}

经纬线() +
    geom_polygon(data=world, aes(x = long, y = lat, group = group), fill = "#00518E",color = "white",size=1.2)+
    coord_map("ortho", orientation = c(30, 100, 0)) +theme_map()+
    geom_polygon(data=world, aes(x = long, y = lat, group = group), fill = "#00518E",color = "#317DA4",alpha=0.25,size=0.5,linetype=6) +
    geom_point(data=Result,aes(x=X,y=Y))

```
![123.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579467409861-69c39961-828a-4085-ae25-6610b623072c.png#align=left&display=inline&height=3321&name=123.png&originHeight=3321&originWidth=6129&size=2243896&status=done&style=none&width=6129)

<iframe src="https://player.bilibili.com/player.html?aid=84247400" frameborder="no" allowfullscreen="true"></iframe>


<a name="FG8Ad"></a>
# More

<a name="5TVWU"></a>
## [**GGmap: geom_map**](https://www.yuque.com/liuwenkan/rr/geom_map)
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1583310614338-770a0479-b095-46da-b5b4-5feb555295da.png#align=left&display=inline&height=221&name=image.png&originHeight=221&originWidth=315&size=60738&status=done&style=none&width=315)

<a name="eXInz"></a>
## [**geom_sf**](https://www.yuque.com/liuwenkan/rr/geom_sf)



![123.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/691897/1583310796813-5db8905d-65bd-462d-ae2f-a4f468835263.jpeg#align=left&display=inline&height=184&name=123.jpg&originHeight=184&originWidth=200&size=5774&status=done&style=none&width=200)

图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
