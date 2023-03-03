---
title: "NetWorkPlot"
description: "NetWorkPlot"
url: networkplot2
date: 2020/08/13
toc: true
excerpt: "There are few libraries for draw the network Plot. JS library networkD3 is diffidently my favorite one!"
tags: [R, Network, Plot]
category: [R, Plot, others]
cover: 'https://s1.ax1x.com/2020/08/13/dS6sCF.gif'
thumbnail: 'https://s1.ax1x.com/2020/08/13/dS6sCF.gif'
priority: 10000
---

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>

## NetWorkPlot


## Igraph

[Document](https://igraph.org/r/doc/)

```r
library(igraph)

##Create data
set.seed(1)
data=matrix(sample(0:1, 100, replace=TRUE, prob=c(0.8,0.2)), nc=10)
network=graph_from_adjacency_matrix(data , mode='undirected', diag=F )

##Default network
par(mar=c(0,0,0,0))
plot(network)
```

![igraph networkplot](https://s1.ax1x.com/2020/06/20/Nlbi2F.png)

### Tricks for Igraph

#### nodes-distance; name of the nodes

The trickiest way to achieve this goal is decreasing the size of nodes.
```r
library(igraph)

##Create data
set.seed(1)
data=matrix(sample(0:1, 100, replace=TRUE, prob=c(0.8,0.2)), nc=10)
network=graph_from_adjacency_matrix(data , mode='undirected', diag=F )

V(network)$name <- paste("dot", c(1:10))

##Default network
par(mar=c(0,0,0,0))
plot(network, vertex.size = 5)
```

|![](https://s1.ax1x.com/2023/02/06/pScSzh6.png)|![](https://s1.ax1x.com/2023/02/06/pScpFnH.png)|
|:-:|:-:|


### More examples
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
![igraph networkplot](https://s1.ax1x.com/2020/06/20/NlbRiV.png)

### node shape

```r
names(igraph:::.igraph.shapes)
```
<pre>
[1] "circle"     "square"     "csquare"    "rectangle"  "crectangle"
[6] "vrectangle" "none"
</pre>

```r
## color palette
library(RColorBrewer)
coul = brewer.pal(nlevels(as.factor(mtcars$cyl)), "Set2")
## Map the color to cylinders
my_color=coul[as.numeric(as.factor(mtcars$cyl))]

## plot
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

![NlbSU0.png](https://s1.ax1x.com/2020/06/20/NlbSU0.png)

More instructions:
- [Katherine Ognyanova, 2016](https://kateto.net/netscix2016.html)
- [Group-1, Åsa Björklund; ](https://nbisweden.github.io/workshop-archive/workshop-scRNAseq/2019-02-04/labs/igraph)
- [Group-2, Antoine; 2015](https://stackoverflow.com/questions/16390221/how-to-make-grouped-layout-in-igraph)


## NetworkD3

### dave it as html

```r
library(htmlwidgets)
saveWidget(P,"_bar.html", selfcontained = F)
```

```r
library(networkD3)

# options(browser = 'firefox')

## Load data
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
    Source="source", #library(RColorBrewer)
coul = brewer.pal(nlevels(as.factor(mtcars$cyl)), "Set2")
指定Links文件中的源节点
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


## matrix to network data

Data: X and Y don't share the items in `raw_tb`
<pre>
屋 沃 烛 觉
歌  0  0  0  0
戈  2  0  0  0
豪 12  6  0  3
肴  2  0  0 18
</pre>

```r
MT_Network <- function(raw_tb, direction="wide"){
  if(direction=="wide"){
      raw_tb$ID = row.names(raw_tb)
      raw_tb <- melt(raw_tb)
  }
  if(direction=="long"){
      colnames(raw_tb) <- c("ID", "variable", "value")
  }
  ID = unique(c(raw_tb$ID, as.character(raw_tb$variable)))
  ID = data.frame(ID, NO=c(1:length(ID)))

  MisLinks = raw_tb
  MisLinks$ID =  ID$NO[match(raw_tb$ID, ID$ID)]-1
  MisLinks$variable =  ID$NO[match(raw_tb$variable, ID$ID)]-1
  colnames(MisLinks) = c("source", "target", "value")
  MisLinks = MisLinks[which(MisLinks$value!=0),]
  MisLinks = MisLinks[order(MisLinks$source),]

  MisNodes = ID
  colnames(MisNodes) = c("name", "group")
  MisNodes$size = 1
  return(list(MisLinks,MisNodes))
}
```

```r
TB <- data.frame(A=c(0,2,1), B= c(0,0,1), C=c(1,0,5))
row.names(TB) = c("A", "C", "D")
print(TB)
Result <- MT_Network(TB)
Links <- Result[[1]]
Nodes <- Result[[2]]

forceNetwork(
  Links=Links, Nodes=Nodes,
  Source="source", Target="target",
  linkColour="#99FFCC", Value="value",
  NodeID="name", fontSize=20,
  Group="group", opacity=0.98,
  zoom=TRUE, arrows=T,
  opacityNoHover=0.7, legend=TRUE
)
```
<pre>
  A B C
A 0 0 1
C 2 0 0
D 1 1 5
</pre>

|![](https://s1.ax1x.com/2022/06/15/Xo352n.png)|
|:-:|


## Sankey Diagram

```r
library(networkD3)

# Load energy projection data
URL <- "https://cdn.rawgit.com/christophergandrud/networkD3/master/JSONdata/energy.json"

Energy <- jsonlite::fromJSON(URL)
head(Energy$links)
head(Energy$nodes)

# Thus we can plot it
p <- sankeyNetwork(Links = Energy$links, Nodes = Energy$nodes,
        Source = "source", Target = "target", Value = "value",
        NodeID = "name", units = "TWh", fontSize = 12, nodeWidth = 30)
p
```

<pre>
source target   value
1      0      1 124.729
2      1      2   0.597
3      1      3  26.862
4      1      4 280.322
5      1      5  81.144
6      6      2  35.000
                name
1 Agricultural 'waste'
2       Bio-conversion
3               Liquid
4               Losses
5                Solid
6                  Gas
</pre>

<iframe src="https://r-graph-gallery.com/HtmlWidget/sankeyEnergy.html" style="border:none;" width="100%" height="640">
</iframe>

![](https://s1.ax1x.com/2022/05/22/Ovg6qf.png)
