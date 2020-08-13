---
title: "NetWorkPlot"
description: "NetWorkPlot"
url: networkplot2
---

# NetWorkPlot

# Igraph

```r
library(htmlwidgets)
saveWidget(P,"_bar.html", selfcontained = F)

library(igraph)

#Create data
set.seed(1)
data=matrix(sample(0:1, 100, replace=TRUE, prob=c(0.8,0.2)), nc=10)
network=graph_from_adjacency_matrix(data , mode='undirected', diag=F )

#Default network
par(mar=c(0,0,0,0))
plot(network)
```

[![Nlbi2F.png](https://s1.ax1x.com/2020/06/20/Nlbi2F.png)](https://imgchr.com/i/Nlbi2F)
```r
plot(network,
vertex.color = rgb(0.8,0.2,0.2,0.9),           # Node color
vertex.frame.color = "Forestgreen",            # Node border color
vertex.shape=c("circle","square"),             # One of “none”, “circle”, “square”, “csquare”, “rectangle” “crectangle”, “vrectangle”, “pie”, “raster”, or “sphere”
vertex.size=c(15:24),                          # Size of the node (default is 15)
vertex.size2=NA,                               # The second size of the node (e.g. for a rectangle)
edge.curved=0.8
)
```
[![NlbRiV.png](https://s1.ax1x.com/2020/06/20/NlbRiV.png)](https://imgchr.com/i/NlbRiV)
```r
# color palette
library(RColorBrewer)
coul = brewer.pal(nlevels(as.factor(mtcars$cyl)), "Set2")
# Map the color to cylinders
my_color=coul[as.numeric(as.factor(mtcars$cyl))]

# plot
par(bg="grey13", mar=c(0,0,0,0))
set.seed(4)
plot(network,
    vertex.size=12,
    vertex.color=my_color,
    vertex.label.cex=0.7,
    vertex.label.color="white",
    vertex.frame.color="transparent"
    )
text(0,0,"The network chart of the mtcars dataset",col="white")
text(0.2,-0.1," - by the R graph gallery",col="white")
legend(x=-0.6, y=-0.12, legend=paste( levels(as.factor(mtcars$cyl)), " cylinders", sep=""), col = coul , bty = "n", pch=20 , pt.cex = 2, cex = 1, text.col="white" , horiz = T)


```

[![NlbSU0.png](https://s1.ax1x.com/2020/06/20/NlbSU0.png)](https://imgchr.com/i/NlbSU0)

# NetworkD3
```r
library(networkD3)

# Load data
data(MisLinks)
data(MisNodes)
forceNetwork(Links=MisLinks, #读入基因之间的关系列表，基因以数字为编号，从0开始；value可用来设置基因间连线的宽度
    Nodes=MisNodes, #基因信息，以对应编号的大小排序
    Source="source", #指定Links文件中的源节点
    Target="target", #指定Links文件中的靶节点
    Value="value", #设定基因间连线的宽度
    NodeID="name", #指定节点显示的标签
    fontSize=20, #设定节点标签的字号，单位为像素
    Group="group", #对节点进行分组，这里可根据基因的功能进行分组，配置不同颜色
    opacity=0.8, #指定图像的不透明度
    zoom=TRUE, #是否允许图像缩放
    arrows=TRUE, #连线是否添加箭头，显示方向
    opacityNoHover=0.7, #鼠标悬停前，节点标签的不透明度
    legend=TRUE, #是否显示图例
    height=600, #设置图像高度
    width=600 #设置图像宽度
    #Nodesize = "Freq_l"
    #radiusCalculation = "d.nodesize"          
)
```
![123](https://s1.ax1x.com/2020/08/13/dS6sCF.gif)

<a name="iGebE"></a>
Those Code Doesn't Works without the data set
```r
forceNetwork(Links=genelinks, #读入基因之间的关系列表，基因以数字为编号，从0开始；value可用来设置基因间连线的宽度
    Nodes=genenodes, #基因信息，以对应编号的大小排序
    Source="source", #指定Links文件中的源节点
    Target="target", #指定Links文件中的靶节点
    linkColour=genelinks$col, #指定连线的颜色，默认为单一颜色，这里用红、绿色分别表示某一基因对靶基因的正、负调控关系
    Value="value", #设定基因间连线的宽度
    NodeID="name", #指定节点显示的标签
    fontSize=20, #设定节点标签的字号，单位为像素
    Group="group", #对节点进行分组，这里可根据基因的功能进行分组，配置不同颜色
    opacity=0.8, #指定图像的不透明度
    zoom=TRUE, #是否允许图像缩放
    arrows=TRUE, #连线是否添加箭头，显示方向
    opacityNoHover=0.7, #鼠标悬停前，节点标签的不透明度
    legend=TRUE, #是否显示图例
    height=600, #设置图像高度
    width=600 #设置图像宽度
    #Nodesize = "Freq_l"
    #radiusCalculation = "d.nodesize"
    )

MyClickScript <- 'r = confirm(d.name+"\\n\\nIf you\'d like to know more about "+d.name+", Please Click \'OK\'");
                  if (r == true){
                    window.open("https://www.uniprot.org/uniprot/"+d.name+"_HUMAN");};'

forceNetwork(
  Links=GeneLinks,
  Nodes=GeneNodes,
  Source="source",
  Target="target",
  linkColour="#99FFCC",
  Value="value",
  NodeID="name",
  Nodesize = "Freq_l",
  fontSize=20,
  Group="group",
  opacity=0.98,
  zoom=TRUE,
  arrows=F,
  opacityNoHover=0.7,
  legend=TRUE,
  clickAction = MyClickScript)
```


<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)




---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
