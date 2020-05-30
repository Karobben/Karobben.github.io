---
url: riverplot2
---

# R-riverplot

brary(riverplot)

#1. 画一个6级能量流动图/桑基图

<a name="e17be30c"></a>
# 构造连接节点(边)的数据框，采用runif生成模拟数据

<a name="23d3dfda"></a>
# 实验中每个节点间的连续情况是己知的

<a name="79043749"></a>
# 生成一个组1-5与组2-6对应的值数据框

edges = data.frame(N1 = paste0(rep(LETTERS[1:4], each = 4), rep(1:5, each = 16)),<br />
N2 = paste0(rep(LETTERS[1:4], 4), rep(2:6, each = 16)),<br />
Value = runif(80, min = 2, max = 5) * rep(c(1, 0.8, 0.6, 0.4, 0.3), each = 16),<br />
stringsAsFactors = F)

<a name="12cddf0c"></a>
# 筛选80%的记录，以免每个点都对应到4个点(可选)

edges = edges[sample(c(TRUE, FALSE), nrow(edges), replace = TRUE, prob = c(0.8, 0.2)),]<br />
head(edges)

<a name="4ee9736e"></a>
# 获得非冗余结点nodes

nodes = data.frame(ID = unique(c(edges![](https://g.yuque.com/gr/latex?N1%2C%20edges#card=math&code=N1%2C%20edges&height=18&width=71)N2)), stringsAsFactors = FALSE)

<a name="2baacf63"></a>
# 添加x: X为组编号，即列位置

nodes![](https://g.yuque.com/gr/latex?x%20%3D%20as.integer(substr(nodes#card=math&code=x%20%3D%20as.integer%28substr%28nodes&height=20&width=211)ID, 2, 2))

<a name="2324ee62"></a>
# Y为组类型字符，转换为ASCII编号，减65，即为A/B/C/D转换为0/1/2/3数值，即行位置

nodes![](https://g.yuque.com/gr/latex?y%20%3D%20as.integer(sapply(substr(nodes#card=math&code=y%20%3D%20as.integer%28sapply%28substr%28nodes&height=20&width=264)ID, 1, 1), charToRaw)) - 65

<a name="2faf48ca"></a>
# 添加行名

rownames(nodes) = nodes$ID<br />
head(nodes)

<a name="95e9696b"></a>
# 添加颜色

library(RColorBrewer)

<a name="a3620cd2"></a>
# brewer.pal生成柔合色，后面加调淡颜色

palette = paste0(brewer.pal(4, "Set1"), "60")

<a name="db6266fa"></a>
# 对每个节点生成相应的列表格式，颜色col，线条类型lty，文字颜色textcol

styles = lapply(nodes![](https://g.yuque.com/gr/latex?y%2C%20function(n)%20%7B%20%20%0A%20%20list(col%20%3D%20palette%5Bn%2B1%5D%2C%20lty%20%3D%200%2C%20textcol%20%3D%20%22black%22)%20%20%0A%7D)%20%20%0Anames(styles)%20%3D%20nodes#card=math&code=y%2C%20function%28n%29%20%7B%20%20%0A%20%20list%28col%20%3D%20palette%5Bn%2B1%5D%2C%20lty%20%3D%200%2C%20textcol%20%3D%20%22black%22%29%20%20%0A%7D%29%20%20%0Anames%28styles%29%20%3D%20nodes&height=20&width=658)ID

<a name="c93c874d"></a>
# 将点、单和样式合并为List，构建riverplot对象

rp <- list(nodes = nodes, edges = edges, styles = styles)

<a name="ae03b881"></a>
# 添加对你属性包括riverplot

class(rp) <- c(class(rp), "riverplot")

<a name="09f44fc8"></a>
# 绘制桑基图，plot_area设置绘图面积，yscale设置Y轴方向缩放

plot(rp, plot_area = 0.95, yscale=0.06)




---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
