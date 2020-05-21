---
url: circlize2
---

# circlize

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579796012787-eef9e5f8-3856-4999-a405-5fb82872b44c.png#align=left&display=inline&height=652&name=image.png&originHeight=652&originWidth=655&size=103227&status=done&style=none&width=655)
<a name="1poi9"></a>
# Quick Start

```r
install.packages('circlize')
library(circlize)

#Create data
data = data.frame(
    factor = sample(letters[1:8], 1000, replace = TRUE),
    x = rnorm(1000),
    y = runif(1000)
    )

# Step1: Initialise the chart giving factor and x-axis.
circos.initialize( factors=data$factor, x=data$x )

# Step 2: Build the regions.
circos.trackPlotRegion(factors = data$factor, y = data$y, panel.fun = function(x, y) {
    circos.axis()
    })

# Step 3: Add points
circos.trackPoints(data$factor, data$x, data$y, col = "blue", pch = 16, cex = 0.5)

# Step 4: Add points
circos.trackPoints(data$factor, data$x, data$y, col = rgb(0.1,0.5,0.8,0.3), pch = 20, cex = 2)


```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579791017502-b5c1fb9d-0774-4e3a-b82c-a02341e73683.png#align=left&display=inline&height=631&name=image.png&originHeight=631&originWidth=644&size=194043&status=done&style=none&width=644)
```r

library(circlize)

# Create data
data = data.frame(
    factor = sample(letters[1:8], 1000, replace = TRUE),
    x = rnorm(1000),
    y = runif(1000)
    )

# General parameters
circos.par("track.height" = 0.4)


```

<a name="zhv19"></a>
## 1: scatter plot
```r
# Initialize chart
circos.initialize(factors = data$factor, x = data$x )
circos.trackPlotRegion(factors = data$factor, y=data$y, panel.fun = function(x, y) {
    circos.axis(labels.cex=0.5, labels.font=1, lwd=0.8, h="bottom", direction="inside")
    })
circos.trackPoints(data$factor, data$x, data$y, col = rgb(0.1,0.5,0.8,0.3), pch=20)

```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579794098197-b0480ea8-329c-4f8c-b478-53bd94c1a1e0.png#align=left&display=inline&height=304&name=image.png&originHeight=624&originWidth=626&size=162986&status=done&style=none&width=305)![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579794119131-57cb3921-e5d6-4821-8b94-898e120e23fc.png#align=left&display=inline&height=272&name=image.png&originHeight=607&originWidth=632&size=169945&status=done&style=none&width=283)
<a name="hSSiS"></a>
## 2: lines
```r
# Initialize chart
circos.initialize(factors = data$factor, x = data$x )

# Build the regions.
circos.trackPlotRegion(factors = data$factor, y=data$y, panel.fun = function(x, y) {
    circos.axis(labels.cex=0.5, labels.font=1, lwd=0.8, h="bottom", direction="inside")
    })
circos.trackLines(data$factor, data$x[order(data$x)], data$y[order(data$x)], col = rgb(0.1,0.5,0.8,0.3), lwd=2)

```

<a name="HUdip"></a>
## 3: abline (vertical lines)
```r
# Initialize chart
circos.initialize(factors = data$factor, x = data$x )

# Build the regions.
circos.trackPlotRegion(factors = data$factor, y=data$y, panel.fun = function(x, y) {
    circos.axis(labels.cex=0.5, labels.font=1, lwd=0.8, h="bottom", direction="inside")
    })
circos.trackLines(data$factor, data$x[order(data$x)], data$y[order(data$x)], col = rgb(0.1,0.5,0.8,0.3), lwd=2, type="h")

```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579794149973-0b80dfba-9d2b-4dce-9cad-921a92ead5d3.png#align=left&display=inline&height=334&name=image.png&originHeight=616&originWidth=633&size=233457&status=done&style=none&width=343)![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579794173398-87f26ca6-dac0-4c15-b76b-a44677bbb5df.png#align=left&display=inline&height=329&name=image.png&originHeight=634&originWidth=649&size=199988&status=done&style=none&width=337)
<a name="9jhF8"></a>
## 4: text
```r
# Initialize chart
circos.initialize(factors = data$factor, x = data$x )

# Build the regions.
circos.trackPlotRegion(factors = data$factor, y=data$y, panel.fun = function(x, y) {
    circos.axis(labels.cex=0.5, labels.font=1, lwd=0.8, h="bottom", direction="inside")
    })
circos.trackText(data$factor, data$x[order(data$x)], data$y[order(data$x)], labels=data$factor, col = rgb(0.9,0.2,0.8,0.3), cex=1)



```

<a name="FTGhd"></a>
## 5: histogram
```r
circos.initialize(factors = data$factor, x = data$x )
circos.trackPlotRegion(factors = data$factor, panel.fun = function(x, y) {
    circos.axis(labels.cex=0.5, labels.font=1, lwd=4)
    })
circos.trackHist(data$factor, data$x, bg.col = "grey78", col = rgb(0.1,0.5,0.8,0.3))

```

<a name="5ab91e24"></a>
#

<a name="7B2cF"></a>
## Layer by layer
```r

library(circlize)

#Create data
data = data.frame(
    factor = sample(letters[1:8], 1000, replace = TRUE),
    x = rnorm(1000),
    y = runif(1000)
    )

#Initialize the plot.
par(mar = c(1, 1, 1, 1) )
circos.initialize(factors = data$factor, x = data$x )


# Build the regions of track #1
circos.trackPlotRegion(factors = data$factor, y=data$y, panel.fun = function(x, y) {
    circos.axis(labels.cex=0.5, labels.font=1, lwd=0.8)
    })
# --> Add a scatterplot on it:
circos.trackPoints(data$factor, data$x, data$y, col = rgb(0.1,0.5,0.8,0.3), pch=20)


# Build the regions of track #2:
circos.trackPlotRegion(factors = data$factor, y=data$y, panel.fun = function(x, y) {
    circos.axis(labels=FALSE, major.tick=FALSE)
    })
# --> Add a scatterplot on it
circos.trackPoints(data$factor, data$x, data$y, col = rgb(0.9,0.5,0.8,0.3), pch=20, cex=2)



# Add the couche #3 --> don't forget you can custom the height of tracks!
circos.par("track.height" = 0.4)
circos.trackPlotRegion(factors = data$factor, y=data$y, panel.fun = function(x, y) {
    circos.axis(labels=FALSE, major.tick=FALSE)
    })
circos.trackLines(data$factor, data$x, data$y, col = rgb(0.9,0.5,0.1,0.3), pch=20, cex=2, type="h")
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579795085487-f886e93c-5ad7-4034-8cfb-4d908bb90a01.png#align=left&display=inline&height=586&name=image.png&originHeight=586&originWidth=603&size=209047&status=done&style=none&width=603)<br />

<a name="ai2vy"></a>
## Example 2

Source: [https://www.jianshu.com/p/a87bcc1cb67b](https://www.jianshu.com/p/a87bcc1cb67b)
```r
library(circlize)
# 简单创建一个数据集
set.seed(999)
n <- 1000
a <- data.frame(factors = sample(letters[1:8], n, replace = TRUE), x = rnorm(n), y = runif(n))

#Layer 1
par(mar = c(1, 1, 1, 1), lwd = 0.1, cex = 0.6)
circos.par(track.height = 0.1)
circos.initialize(factors = a$factors, x = a$x) #初始化，factors来控制track数目，初始化里只有x， 没有y。这一步相当于ggplot()
circos.trackPlotRegion(factors = a$factors, y = a$y,
panel.fun = function(x, y) {
circos.axis()})
col <- rep(c("#FF0000", "#00FF00"), 4) #自定义一下颜色# 这里先解释一下，一个track有好几个cell，具体数目由factors决定的，向本数据集中factors有八个，因此绘制一个track，其包含八个cell。含有前缀circos.track的函数会在所有的cel里添加基本元素，而只有前缀circos.的函数可以在特定的track、cell里添加基本元素。具体看下演示。
circos.trackPoints(a$factors, a$x, a$y, col = col, pch = 16, cex = 0.5) #所有的cell里都绘制点图
circos.text(-1, 0.5, "left", sector.index = "a", track.index = 1) #在track 1中的标记为a的cell里添加
circos.clear()
#Layer 2
par(mar = c(1, 1, 1, 1), lwd = 0.1, cex = 0.6)
circos.par(track.height = 0.1)
circos.initialize(factors = a$factors, x = a$x)
circos.trackPlotRegion(factors = a$factors, y = a$y,
panel.fun = function(x, y) {
circos.axis()})
col <- rep(c("#FF0000", "#00FF00"), 4)
circos.trackPoints(a$factors, a$x, a$y, col = col, pch = 16, cex = 0.5)
circos.text(-1, 0.5, "left", sector.index = "a", track.index = 1)
circos.text(1, 0.5, "right", sector.index = "a")
bg.col <- rep(c("#EFEFEF", "#CCCCCC"), 4)
circos.trackHist(a$factors, a$x, bg.col = bg.col, col = NA)
circos.clear()
#Layer 3
par(mar = c(1, 1, 1, 1), lwd = 0.1, cex = 0.6)
circos.par(track.height = 0.1)
circos.initialize(factors = a$factors, x = a$x)
circos.trackPlotRegion(factors = a$factors, y = a$y,
 panel.fun = function(x, y) {
circos.axis()})
col <- rep(c("#FF0000", "#00FF00"), 4)
circos.trackPoints(a$factors, a$x, a$y, col = col, pch = 16, cex = 0.5)
circos.text(-1, 0.5, "left", sector.index = "a", track.index = 1)
circos.text(1, 0.5, "right", sector.index = "a")
bg.col <- rep(c("#EFEFEF", "#CCCCCC"), 4)
circos.trackHist(a$factors, a$x, bg.col = bg.col, col = NA)
circos.trackPlotRegion(factors = a$factors, x = a$x, y = a$y,
panel.fun = function(x, y) {
 grey = c("#FFFFFF", "#CCCCCC", "#999999")
sector.index = get.cell.meta.data("sector.index") #这个是第三个track，因为我们刚刚创建，这里这一步不用也可。
 xlim = get.cell.meta.data("xlim")
 ylim = get.cell.meta.data("ylim")
circos.text(mean(xlim), mean(ylim), sector.index)
circos.points(x[1:10], y[1:10], col = "red", pch = 16, cex = 0.6)
circos.points(x[11:20], y[11:20], col = "blue", cex = 0.6)})
circos.clear()
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579797353044-91154da9-3af0-4bd8-bc07-ae4719eafa31.png#align=left&display=inline&height=642&name=image.png&originHeight=642&originWidth=650&size=91666&status=done&style=none&width=650)

<a name="BpV9z"></a>
## Connection

```r
set.seed(999)
mat = matrix(sample(18, 18), 3, 6)
rownames(mat) = paste0("S", 1:3)
colnames(mat) = paste0("E", 1:6)
df=melt(mat)
df$X1=as.character(df$Var1)
df$X2=as.character(df$Var2)

#作图
chordDiagram(mat)
chordDiagram(df)
circos.clear()

#图形的精修和参数介绍
chordDiagram(df,
  reduce = -1, #如果单个扇叶/整个环 < reduce,则这个扇叶不展示
  grid.col=sample(colors(),length(union(df$X1,df$X2)),replace = F),  #扇叶的颜色，顺序和union(df[[1]],df[[2]])一样
  col=colorRamp2(breaks=c(1,18),colors=c("blue","red")),  #连线的颜色，也可以设置展示df中数值的大小
  order = union(df$X2,df$X1),  #扇叶展示的顺序
  directional = 1, #连线的方向，1=第一列到第二列，2=双方向，-1=第二列到第一列，0=无方向
  direction.type = "arrows", #可以为“diffHeight”，也可以为“arrows”
  diffHeight = rep(convert_height(1,"mm"),length(union(df$X1,df$X2))), #正值代表出处比末尾凸出，负值代表出处比末尾凹进去
 self.link = 1, #自己和自己相连的线，1=形似山 宽度代变数值大小，2=出和入的宽度相同并代表数值的大小
  preAllocateTracks = 1, #预留出多少空的轨道
  link.border = rep('grey',nrow(df)), #连线边界的颜色
  link.lwd = rep(1,nrow(df)), #连线边界的宽度
  link.lty = rep(3,nrow(df)), #设置连线边界的线型
  link.sort = T, # 对连线依据大小排序
  link.decreasing = T, #连线降序排序
  link.arr.width = rep(0.1,nrow(df)), #连线方向用箭头表示时，箭头的宽度
  link.arr.type = "triangle", #箭头类型
  link.arr.col = rep('grey',nrow(df)), #箭头的颜色
  link.arr.lwd = rep(1,nrow(df)), #箭头的尾线宽度
  link.arr.lty = rep(3,nrow(df)), #箭头尾线的线型
  link.visible = c(rep(T,9),rep(F,9)) #连线是否画出
  )
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579797089728-c901085b-ea67-4e2b-82d9-4d70204471b9.png#align=left&display=inline&height=640&name=image.png&originHeight=640&originWidth=604&size=64216&status=done&style=none&width=604)

```r
layout(matrix(1:9, 3, 3))
for (i in 1:9) {
 factors = letters[1:8]
par(mar = c(0.5, 0.5, 0.5, 0.5))
circos.par(cell.padding = c(0, 0, 0, 0))
circos.initialize(factors = factors, xlim = c(0, 1))
circos.trackPlotRegion(ylim = c(0, 1), track.height = 0.05,
bg.col = rand_color(8), bg.border = NA)
# 绘制links
for (i in 1:20) {
se = sample(letters[1:8], 2)
circos.link(se[1], runif(2), se[2], runif(2),
col = rand_color(1, transparency = 0.4), border = NA)
}}
circos.clear()
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579796012787-eef9e5f8-3856-4999-a405-5fb82872b44c.png#align=left&display=inline&height=652&name=image.png&originHeight=652&originWidth=655&size=103227&status=done&style=none&width=655)


```r
set.seed(1234)
data <- matrix(rnorm(100 * 10), nrow = 10, ncol = 100)
col <- colorRamp2(c(-2, 0, 2), c("green", "black", "red"))
factors <- rep(letters[1:2], times = c(30, 70))
data_list <- list(a = data[, factors == "a"], b = data[, factors == "b"])
dend_list <- list(a = as.dendrogram(hclust(dist(t(data_list[["a"]])))),
                  b = as.dendrogram(hclust(dist(t(data_list[["b"]])))))
circos.par(cell.padding = c(0, 0, 0, 0), gap.degree = 5)
circos.initialize(factors = factors, xlim = cbind(c(0, 0), table(factors)))
circos.track(ylim = c(0, 10), bg.border = NA,
panel.fun = function(x, y) {
 sector.index = get.cell.meta.data("sector.index")
d = data_list[[sector.index]]
dend = dend_list[[sector.index]]
d2 = d[, order.dendrogram(dend)]
col_data = col(d2)
nr = nrow(d2)
nc = ncol(d2)
for (i in 1:nr) {
circos.rect(1:nc - 1, rep(nr - i, nc), 1:nc, rep(nr - i + 1, nc),
border = col_data[i, ], col = col_data[i, ]) }})
max_height <- max(sapply(dend_list, function(x) attr(x, "height")))
circos.track(ylim = c(0, max_height),
bg.border = NA, track.height = 0.3,
panel.fun = function(x, y) {
sector.index = get.cell.meta.data("sector.index")
dend = dend_list[[sector.index]]
circos.dendrogram(dend, max_height = max_height)})
circos.clear()
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579796615573-46f12f99-f32d-490e-8212-f481be8eb0b1.png#align=left&display=inline&height=338&name=image.png&originHeight=338&originWidth=335&size=62369&status=done&style=none&width=335)<br />
<br />

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)






--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
