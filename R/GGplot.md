---
url: ggplot
---

# GGplot

大量带图介绍: [https://yutannihilation.github.io/allYourFigureAreBelongToUs/ggthemes/](https://yutannihilation.github.io/allYourFigureAreBelongToUs/ggthemes/)<br />扩展包介绍: [http://www.ggplot2-exts.org](http://www.ggplot2-exts.org)

图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580277957693-b789a2a5-a7af-4f8b-a194-56d3e4e6e9a9.png#align=left&display=inline&height=939&name=image.png&originHeight=939&originWidth=1897&size=880722&status=done&style=none&width=1897)

<a name="BMcZ4"></a>
## 0. ggsave
<a name="HGrYC"></a>
## <br />
```r
ggsave(filename, plot = last_plot(), device = NULL, path = NULL, scale = 1, width = NA, height = NA, units = c("in", "cm", "mm"), dpi = 300, limitsize = TRUE, ...)
# 当pdf字体有问题时：
ggsave('test.pdf', width=7,height=3, device = cairo_pdf, family = "Song")
```

<a name="ud7Yr"></a>
## 1. Dot plot
<a name="LpqMc"></a>
### 1.1 geom_point
```r
ggplot(mpg) +geom_point(mapping =aes( x =displ, y =hwy, color =class))
ggplot(mpg) +geom_point(mapping =aes( x =V1, y =V2, color =V3, shape =V4, size=V5))
```

<a name="YVt3R"></a>
### 1.2 geom_dotplot

```r
ggplot(mtcars, aes(x = mpg)) + geom_dotplot() + theme_light()
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580024050023-b950da3e-7c40-4b50-8f59-4514e84205be.png#align=left&display=inline&height=174&name=image.png&originHeight=199&originWidth=852&size=23228&status=done&style=none&width=746)<br />

<a name="I007a"></a>
### 1.3 geom_jitter

```r
ggplot(mpg, aes(cyl, hwy))+ geom_point() +geom_jitter(aes(colour = class))+ theme_light()
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580026132819-7f9232dd-97ca-4edf-9ce3-5db4e341ed76.png#align=left&display=inline&height=391&name=image.png&originHeight=520&originWidth=606&size=48393&status=done&style=none&width=456)
<a name="poSDp"></a>
## 2. Line
<a name="FPW7c"></a>
### 2.1 geom_line & geom_path

```r
library(ggplot2)
library(patchwork)

TB = data.frame(X=c(1,23,4,2,3,4,1,1,2,3,4,1,1,5,2,3),Y=c(1:16))

p1 <- ggplot(TB) + geom_line(aes(X,Y)) + labs(title='geom_line()')+ theme_light()
p2 <- ggplot(TB) + geom_path(aes(X,Y)) + labs(title='geom_patch()')+ theme_light()


```

![path.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579536964721-98f1bb2d-df20-4eb5-8821-76a88b141494.png#align=left&display=inline&height=247&name=path.png&originHeight=973&originWidth=2097&size=72039&status=done&style=none&width=533)
<a name="JxYYM"></a>
### 2.2 geom_smooth

```r
ggplot(data = mpg) + geom_point(mapping = aes(x = V1, y = V2)) + geom_smooth(mapping= aes(x=V1, y=V2))
#####
# sting
ggplot(mpg , aes(x = displ, y = hwy)) + geom_point() +
  geom_smooth(method = "lm")

++geom_smooth(data=Growth_p,aes(x=ID,y=log(value+20)/3,group=ALL,color='OD Curve'),se = FALSE,span=0.75)
```

<a name="izF68"></a>
### 2.3 

```r
library(patchwork)

p1 <- ggplot(mtcars,aes(mpg)) + geom_histogram() + theme_light() + ggtitle('histogram')
p2 <- ggplot(mtcars,aes(mpg)) + geom_freqpoly() + theme_light()  + ggtitle('freqpoly')

p2/p1
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580024415512-f1b4c1e4-5c56-4edf-a230-bee17cec80bf.png#align=left&display=inline&height=321&name=image.png&originHeight=321&originWidth=734&size=29404&status=done&style=none&width=734)
<a name="vFIpv"></a>
## 3. geom_boxplot

```r
ggplot(box,aes(x=box$variable,y=box$value)) +geom_boxplot()
```


<a name="njlYT"></a>
## 4. Bar
<a name="ZAoAI"></a>
### geom_bar

```r
+ geom_bar(stat= 'identity')
## the number of the point
+ geom_bar(aes(fill=group),stat="identity")
## the mean of all point (stack togather)
+ geom_bar(aes(fill=group),stat="summary",fun.y="mean",position = 'stack')
## dont stact
+ geom_bar(aes(fill=group),stat="summary",fun.y="mean",position = 'dodge')
```

<a name="CymbV"></a>
### geom_col
#an easier way to draw bar plot
```r
df <- data.frame(trt = c("a", "b", "c"), outcome = c(2.3, 1.9, 3.2))
ggplot(df, aes(trt, outcome)) + geom_col() + geom_point(color='red')
```

Position for bar
```r
## Position 
position = 'fill'
position = 'identity'
position = 'stack'
position = 'dodge'
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580014667073-672cf132-7f6b-48e3-8e7e-86c36de08459.png#align=left&display=inline&height=240&name=image.png&originHeight=240&originWidth=212&size=5541&status=done&style=none&width=212)

<a name="ly8EC"></a>
## 5. Heatmap

```r
ggplot(A, aes(x=Diet,y=A$Time)) + xlab("samples") + ylab(NULL) +
	theme_bw()+theme(panel.grid.major = element_blank()) +
	theme(legend.key=element_blank())+geom_tile(aes(fill=weight)) +
	scale_fill_gradient2(low="steelblue2",mid="white",high="red",midpoint =150)+
	scale_fill_gradient(low = "white", high = "red")

ggplot(A, aes(x=Diet,y=A$Time)) + xlab("samples") + ylab(NULL) +
	theme_bw()+
	theme(panel.grid.major = element_blank()) +
	theme(legend.key=element_blank())+
	geom_tile(aes(fill=weight)) +
	scale_fill_gradient2(low="steelblue2",mid="white",high="red",midpoint =150)+
	scale_fill_gradient(low = "white", high = "red")
```

<a name="489Tu"></a>
### 5.1 Best theme for heatmap

```r
# Best color for heatmap
library(RColorBrewer)
colorRampPalette(rev(brewer.pal(n = 7,name = "RdYlBu"))) -> cc
simplot(d) + scale_fill_gradientn(colors=cc(100)) + theme()
```

<a name="sNAxM"></a>
## 6. Fan plot

```r
ggplot() + geom_bar() + coord_polar(theta = 'y')
# removing background
+theme(panel.grid=element_blank(),panel.border=element_blank(),axis.ticks=element_blank(),axis.text=element_blank(),axis.title=element_blank(),, panel.background = element_blank())
# or

library(ggthemes)
+theme_map()
```


<a name="W8uIK"></a>
## 7. geom_errorbar

```r
 + geom_errorbar(aes(ymin=len-sd, ymax=len+sd), 
	width=.2， position=position_dodge(.9))
```

<a name="8i31l"></a>
## 8. Extra Line

```r
aux2 <- data.frame(cyl = c(4,6,8), x = c(2,3,4),y = c(10,10,10), 
                   xend = c(2,3,4), yend = c(35,35,35),
                   x2 = c(3,4,5), xend2= c(3,4,5))
ggplot(mtcars, aes(x = drat)) + 
  geom_line(aes(y = mpg, colour = "mpg")) + 
  geom_line(aes(y = qsec, colour = "qsec")) +
  geom_segment(aes(x = x, y = y, xend = xend, yend = yend, colour = "xiaopang"),data= aux2, lty = 2) +
  geom_segment(aes(x = x2, y = y, xend = xend2, yend = yend, colour = "xiaomei"),data= aux2, lty = 2)
```

<a name="9vymr"></a>
# Themes
<br />
<a name="OlI1o"></a>
## 1. Axis
<br />
<a name="Pzlwo"></a>
### 1.1 Switch Coordination

```r
#switch X and Y
+ coord_flip()
```


<a name="T7Izn"></a>
### 1.2 Axis Limits

```r
+ coord_cartesian(ylim = c(100,200), expand = F) # moving the panel
+ coord_fixed(ratio =2) #ratio = axis.y/axis.x
+ expand_limits(y=c(-12,18)) # similar like cartesian
```


<a name="VIwTX"></a>
### 1.3 Polar Axis

```r
+ coord_polar(theta ="x", start = pi/3)
+ coord_polar(theta ="y", start = pi/3)
```


<a name="BknYx"></a>
## 1.4 Scale Axis

```r
# https://www.cnblogs.com/wkslearner/p/5635184.html
+scale_x_date(breaks=as.Date(c("2016-06-06","2016-06-13","2016-06-20","2016-06-27")), 
              labels=c("06-06","06-13","06-20","06-27"),date_labels="%y/%m/%d")
```

<a name="unROd"></a>
## 2. Background
<a name="7InUF"></a>
### 2.1 remove
```r
+ theme(panel.grid.major =element_blank(), 						#栅格线1
        panel.grid.minor = element_blank(), 					#栅格线2
				panel.background = element_blank(),						#滑板底层
        axis.line = element_line(colour = "black"),		#轴线
				axis.ticks=element_blank(),										#轴上点
        axis.text.y=element_blank(), 									#y文字
        axis.title.x =elemet_blank(),									#y标题 
				legend.position='none')												#删标注
```

<a name="Kt9wJ"></a>
### 2.2 background color
```r
panel.background = element_rect(fill = "lightblue",
	colour = "lightblue",
	size = 0.5, linetype = "solid"),
```

<a name="Zakzg"></a>
## 3. Texts

<a name="W3uCv"></a>
### 3.1 labs
<br />
```r
+ labs(title="MPO", x="Basket", y="U/g")
+ theme(plot.title = element_text(hjust = 0.5))
```

<br />
<a name="sKvXX"></a>
### 3.2 geom_text & geom_labels
```r
library(ggrepel)
+geom_text_repel(aes(label=variable))
+geom_text(data=A,aes(x=V1,y=valuable,
	label=row.names(A4), colour =row.names(A4)),nudge_x = 0.5)

```

<a name="uD0IC"></a>
### 3.3 Annotate

```r
annotate(geom, x = NULL, y = NULL, xmin = NULL, xmax = NULL,
  ymin = NULL, ymax = NULL, xend = NULL, yend = NULL, ...,
  na.rm = FALSE)
geom="text" |"rect"| "segment" | "pointrange"
 + annotate("segment", x = 2, xend = 4, y = 15, yend = 25, colour = "pink", size=3, alpha=0.6, arrow=arrow())
```

<a name="z7oYB"></a>
### 3.4 ggtitle

```r
ggtitle("AAA")
theme(plot.title = element_text(hjust = 0.5))
```


3.5 Switch x labels (text.x)

```r
# add the limits first and substitu...
+ scale_x_discrete(name ="Dose (mg)", limits=c(1:119),labels=as.character(A$X1))
```


4. Facet

```r
+ facet_grid(Group ~ .)
# for GO enrichment
+ facet_grid(. ~ Cate,scales = "free_x",space = "free")
+ facet_wrap(~ V3, nrow = NULL, ncol = NULL, scales = "free")
```


<a name="JEEuu"></a>
## 5. Levels
<br />
```r
table$X=factor(table$X, levels=table[[1]])
```


<a name="TWMrw"></a>
## 
6. theme()<br />

```r
+ theme(plot.title = element_text(hjust = 0.5),axis.text.x = element_text(angle = 45, hjust=1))
```


<a name="cElq7"></a>
### 6.1 legend

```r
#rm legend
+theme(legend.position='none')
#("none", "left", "right", "bottom", "top", or two-element numeric vect)
```
<a name="KETyn"></a>
## 
<a name="OUsTS"></a>
### 7. Color patern

```r
#Example
scale_fill_manual(values=c("#FB882C","#5B88A0"))
scale_fill_brewer + (..., type = "seq", palette = 1, direction = 1, aesthetics = "colour")
'''
Palettes:
Diverging
BrBG, PiYG, PRGn, PuOr, RdBu, RdGy, RdYlBu, RdYlGn, Spectral
Qualitative
Accent, Dark2, Paired, Pastel1, Pastel2, Set1, Set2, Set3
Sequential
Blues, BuGn, BuPu, GnBu, Greens, Greys, Oranges, OrRd, PuBu, PuBuGn, PuRd, Purples, RdPu, Reds, YlGn, YlGnBu, YlOrBr, YlOrRd
'''

library("ggthemes")
library("RColorBrewer")
# Gradient
scale_fill_gradient() 允许分配一组双色连续渐变，low="white",high="red"
scale_fill_gradient2() 允许分配一组三色连续渐变，low="blue",mid="white",high="red"
# sed a group of colour
scale_fill_manual(values=c("Linen","Peru","PeachPuff","SandyBrown","Chocolate"))
# apply the Set on ggthemes
+ scale_colour_XXX()  # Tab to see more
```


<a name="W6HoY"></a>
# More for plot
<a name="ZovW4"></a>
## 1. Cow plot

```r
library(cowplot)
+ draw_plot(p1,0,0.5,0.5,0.5)+draw_plot(p2,0.5,0.5,0.5)
+draw_plot(pheat,0.5,0,0.5,0.5)
+draw_plot_label(c("A", "B"), c(0,0.5), c(1, 1), size = 20)
'''
Xl,Xr,Yt,Yzoom
draw_plot(p1,Xl,Yb,Xzoom,Yzoom,Pzoom)
'''
```


<a name="LWW1q"></a>
## 2. Patch Work

```r
library(patchwork)
p1 <- ggplot() + ...
p2 <- ggplot() + ...
p1|p2

p1/p2

(p1|p2)|p2
```


<a name="sopow"></a>
## 3. Map

```r
library(pacman)

rladies <- read_csv(url("https://raw.githubusercontent.com/d4tagirl/R-Ladies-growth-maps/master/rladies.csv"))%>% select(-1)

p_load(tidyverse, gganimate, maps, ggthemes)

ggplot()+borders("world", color="black", fill="steelblue4") +
	geom_point(data = rladies, aes(lon, lat, size=followers), color="firebrick3", 
		alpha=0.6)+scale_size_continuous(range = c(2,8), 
		breaks = c(250, 500, 750, 1000)) +
		labs(size="Followers", title="The development of R-Ladies'Twitter accounts",
		x=NULL,y=NULL)+theme(text = element_text(family = "Times New Roman", 
		color = "deeppink"),plot.title = element_text(size=40,color = "#f9ba00"),
		plot.subtitle = element_text(size=14),axis.ticks = element_blank(),
		axis.text = element_blank(),panel.grid = element_blank(),
		panel.background = element_rect(fill="skyblue"),
		plot.background = element_rect(fill = "#333333"),
		legend.position = c(0.18,0.36),legend.background = element_blank(),
		legend.key = element_blank(),legend.text = element_text(size = 24),
		legend.title = element_text(size=28, color = "orangered3"))
```
More for maps, please go to see: [GGplot Map](https://www.yuque.com/liuwenkan/bni63i/bu4wnw)

<a name="fuDYo"></a>
# Extra

<a name="ZY13A"></a>
## Details for theme
```r
##########################
## Parameter of theme
##########################
line  #all line elements (element_line)
rect  #all rectangular elements (element_rect)
text  #all text elements (element_text)
title #all title elements: plot, axes, legends (element_text; inherits from text)
aspect.ratio  #aspect ratio of the panel
axis.title  #label of axes (element_text; inherits from text)
axis.title.x  #x axis label (element_text; inherits from axis.title)
axis.title.y  #y axis label (element_text; inherits from axis.title)
axis.tex  #tick labels along axes (element_text; inherits from text)
axis.text.x #x axis tick labels (element_text; inherits from axis.text)
axis.text.y #y axis tick labels (element_text; inherits from axis.text)
axis.ticks  #tick marks along axes (element_line; inherits from line)
axis.ticks.x  #x axis tick marks (element_line; inherits from axis.ticks)
axis.ticks.y  #y axis tick marks (element_line; inherits from axis.ticks)
axis.ticks.length #length of tick marks (unit)
axis.line #lines along axes (element_line; inherits from line)
axis.line.x #line along x axis (element_line; inherits from axis.line)
axis.line.y #line along y axis (element_line; inherits from axis.line)
legend.background #background of legend (element_rect; inherits from rect)
legend.margin #extra space added around legend (unit)
legend.key  #background underneath legend keys (element_rect; inherits from rect)
legend.key.size #size of legend keys (unit; inherits from legend.key.size)
legend.key.height #key background height (unit; inherits from legend.key.size)
legend.key.width  #key background width (unit; inherits from legend.key.size)
legend.text #legend item labels (element_text; inherits from text)
legend.text.align #alignment of legend labels (number from 0 (left) to 1 (right))
legend.title  #title of legend (element_text; inherits from title)
legend.title.align  #alignment of legend title (number from 0 (left) to 1 (right))
legend.position #the position of legends ("none", "left", "right", "bottom", "top", or two-element numeric vector)
legend.direction  #layout of items in legends ("horizontal" or "vertical")
legend.justification  #anchor point for positioning legend inside plot ("center" or two-element numeric vector)
legend.box  #arrangement of multiple legends ("horizontal" or "vertical")
legend.box.just #justification of each legend within the overall bounding box, when there are multiple legends ("top", "bottom", "left", or "right")
panel.background  #background of plotting area, drawn underneath plot (element_rect; inherits from rect)
panel.border  #border around plotting area, drawn on top of plot so that it covers tick marks and grid lines. This should be used with fill=NA(element_rect; inherits from rect)
panel.margin  #margin around facet panels (unit)
panel.margin.x  #horizontal margin around facet panels (unit; inherits from panel.margin)
panel.margin.y  #vertical margin around facet panels (unit; inherits from panel.margin)
panel.grid  #grid lines (element_line; inherits from line)
panel.grid.major  #major grid lines (element_line; inherits from panel.grid)
panel.grid.minor  #minor grid lines (element_line; inherits from panel.grid)
panel.grid.major.x  #vertical major grid lines (element_line; inherits from panel.grid.major)
panel.grid.major.y  #horizontal major grid lines (element_line; inherits from panel.grid.major)
panel.grid.minor.x  #vertical minor grid lines (element_line; inherits from panel.grid.minor)
panel.grid.minor.y  #horizontal minor grid lines (element_line; inherits from panel.grid.minor)
panel.ontop #option to place the panel (background, gridlines) over the data layers. Usually used with a transparent or blankpanel.background. (logical)
plot.background #background of the entire plot (element_rect; inherits from rect)
plot.title  #plot title (text appearance) (element_text; inherits from title)
plot.margin #margin around entire plot (unit with the sizes of the top, right, bottom, and left margins)
strip.background  #background of facet labels (element_rect; inherits from rect)
strip.text  #facet labels (element_text; inherits from text)
strip.text.x  #facet labels along horizontal direction (element_text; inherits from strip.text)
strip.text.y  #facet labels along vertical direction (element_text; inherits from strip.text)
strip.switch.pad.grid #space between strips and axes when strips are switched (unit)
strip.switch.pad.wrap #space between strips and axes when strips are switched (unit)
```


<a name="G1713"></a>
## Details for element

```r
margin(t = 0, r = 0, b = 0, l = 0, unit = "pt")
element_blank()
element_rect(fill = NULL, colour = NULL, size = NULL,
  linetype = NULL, color = NULL, inherit.blank = FALSE)
element_line(colour = NULL, size = NULL, linetype = NULL,
  lineend = NULL, color = NULL, arrow = NULL,
  inherit.blank = FALSE)
element_text(family = NULL, face = NULL, colour = NULL,
  size = NULL, hjust = NULL, vjust = NULL, angle = NULL,
  lineheight = NULL, color = NULL, margin = NULL, debug = NULL,
  inherit.blank = FALSE)
rel(x)
```




--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
