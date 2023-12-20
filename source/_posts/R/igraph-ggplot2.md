---
toc: true
url: igraph_ggplot2
covercopy: © Karobben
priority: 10000
date: 2023-02-07 12:44:28
title: "From igraph to ggplot2"
ytitle: "From igraph to ggplot2"
description: "Turn igraph result to ggplot2 and more"
excerpt: "ggplot is flexible, integrates well with igraph, and provides a consistent grammar for building plots, making it an ideal tool for creating informative, visually appealing, and reproducible visualizations of your network data. <a title='ChatGPT'>Who sad this?</a>"
tags: [ggplot, Network]
category: [R, Plot, GGPLOT]
cover: "https://s1.ax1x.com/2023/02/08/pS2UVIg.png"
thumbnail: "https://s1.ax1x.com/2023/02/08/pS2UVIg.png"
---


## Turn igraph result to ggplot2 plot

!!! note Why you want to turn igraph network polot to ggplot?
    - Flexibility: ggplot is a very flexible and customizable plotting package that allows you to create high-quality, publication-ready plots with a high degree of control over the visual aesthetics of your plots. You can easily modify various aspects of the plot, such as the color, shape, and size of the nodes and edges, and the placement of the labels.
    - Integration with igraph: ggplot works seamlessly with igraph, making it easy to create complex and informative visualizations of your network data. You can use ggplot to visualize network data in a variety of ways, including heatmaps, scatterplots, and bar charts.
    - Consistency: ggplot provides a consistent grammar for building plots, which makes it easy to create plots with a consistent style and look across different datasets. This can be particularly useful if you are working with multiple datasets and want to create a consistent visual language for your plots.
    - Reproducibility: ggplot produces code that can be easily reproduced, making it easier to share and collaborate on your work. You can also easily modify and update your plots as your data or analysis changes.
    Overall, using ggplot to plot igraph results can help you create informative, visually appealing, and reproducible visualizations of your network data.

Basic idea of this post is from [© Christopher Chizinski, 2014](https://chrischizinski.github.io/rstats/igraph-ggplotll/). It is an old post but all codes work just fine!

## install igraph

```r
install.packages('igraph')
```

- Errors
  <pre>
  libopenblas.so.0: cannot open shared object file: No such file or directory
  </pre>

  ```bash
  sudo apt-get install libopenblas-dev
  ```

## Example data for igraph

```r
library(stringr)
library(reshape2)
library(ggplot2)
library(igraph)
library(RColorBrewer)
library(qgraph)
library(ggthemes)


# data clean
dataUU <- read.table("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/13_AdjacencyUndirectedUnweighted.csv", header=TRUE)
TB <- na.omit(melt(dataUU))
TB$from <- str_replace_all(TB$from, ' ', '.')
# width of the edges
set.seed(3)
TB$value = runif(nrow(TB), min=0, max=10)
# size of pointsd
TB_size <- as.data.frame(table(c(as.matrix(TB[1:2]))))

network=graph_from_data_frame(TB[1:2] )

set.seed(1)
e <- get.edgelist(network,names=FALSE)
l <- qgraph.layout.fruchtermanreingold(e,vcount=vcount(network),  
    area=30*(vcount(network)^2), repulse.rad=(vcount(network)^4))  
plot(network,  
    layout=l, 
    vertex.size=4, vertex.label=NA,  
    edge.arrow.size= 0, 
)
```




```r
## convert the layout to a data.frame
fr.all.df <- as.data.frame(l)
## add in the species codes
fr.all.df$species <- V(network)$name
## add size for each nodes
fr.all.df$size <- TB_size$Freq[match(fr.all.df$species, TB_size$Var1)]

g <- TB[1:2]
colnames(g) <-c('from', 'to')
g$weight = TB[[3]]
g$from.x <- fr.all.df$V1[match(g$from, fr.all.df$species)]  #  match the from locations from the node data.frame we previously connected
g$from.y <- fr.all.df$V2[match(g$from, fr.all.df$species)]
g$to.x <- fr.all.df$V1[match(g$to, fr.all.df$species)]  #  match the to locations from the node data.frame we previously connected
g$to.y <- fr.all.df$V2[match(g$to, fr.all.df$species)]

P <-ggplot() +
        geom_segment(data=g,aes(x=from.x,xend = to.x, y=from.y,yend = to.y, size = weight),colour="black", alpha =.1 ) +
        geom_point(data=fr.all.df,aes(x=V1,y=V2)) +
        geom_text(data=fr.all.df,aes(x=V1,y=V2,label="")) +
        theme_map()   + coord_fixed(ratio = 1) + coord_fixed(ratio = 1)
```

|![](https://s1.ax1x.com/2023/02/08/pS2NQED.png)|![](https://s1.ax1x.com/2023/02/08/pS2N14H.png)|
|:-:|:-:|

## include size of the dots and the weight of edges

```r
ggplot() +
  geom_segment(data=g,aes(x=from.x,xend = to.x, y=from.y,yend = to.y, size = weight), size = log(g$weight + 1)/2, colour="black", alpha =.1 ) +
  geom_point(data=fr.all.df,aes(x=V1,y=V2, size = size, color = size), alpha = .8) +
  geom_text(data=fr.all.df,aes(x=V1,y=V2,label="")) +
  theme_map()   + coord_fixed(ratio = 1) + coord_fixed(ratio = 1) + scale_color_gradient(high = 'red', low = 'steelblue')
```


![](https://s1.ax1x.com/2023/02/08/pS2UVIg.png)


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
