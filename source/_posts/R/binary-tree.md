---
toc: true
url: binary_tree
covercopy: © Karobben
priority: 10000
date: 2021-04-20 10:05:06
title: "Develop a Binary Tree in R"
ytitle: "在R语言中计算二叉树的延伸和衍生"
description: "Build a visualize a binary tree in R by using for loop and igraph"
excerpt: "A binary tree is a type of tree data structure in which each node has at most two child nodes, typically referred to as the left child and right child. The nodes in a binary tree are arranged in a hierarchical order, with the topmost node called the root node. <a title='GhatGPT'>Who said this?</a>"
tags: [R, Network]
category: [R, Plot, Blog, Algorithm]
cover: "https://z3.ax1x.com/2021/04/20/c7vKXt.png"
thumbnail: "https://z3.ax1x.com/2021/04/20/c7vKXt.png"
---

## Plot a network

![igraph networkplot](https://s1.ax1x.com/2020/06/20/Nlbi2F.png)


```r R
library(igraph)

##Create data
set.seed(1)
data=matrix(sample(0:1, 100, replace=TRUE, prob=c(0.8,0.2)), nc=10)
network=graph_from_adjacency_matrix(data , mode='undirected', diag=F )

##Default network
par(mar=c(0,0,0,0))
plot(network)

head(data)
```
This is the data structure we'd like to have

<pre>
[,1] [,2] [,3] [,4] [,5] [,6] [,7] [,8] [,9] [,10]
[1,]    0    0    1    0    1    0    1    0    0     0
[2,]    0    0    0    0    0    1    0    1    0     0
[3,]    0    0    0    0    0    0    0    0    0     0
[4,]    1    0    0    0    0    0    0    0    0     1
[5,]    0    0    0    1    0    0    0    0    0     0
[6,]    1    0    0    0    0    0    0    1    0     0
</pre>


## From List to Network-Data Matrix

Let's say, a list of data `1, 2, 3, 4` means the relationship of ` 1-> 2 -> 3 -> 4`.

```r R
List <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
List2DF <- function(List){
  tmp = c(List[-1],NA)
  TB = data.frame("A"=List, "B" = tmp, V = 0)
  colnames(TB) = c("A", "B", "V")
  return(na.omit(TB))
}

DF2Net <- function(TB){
  AA = reshape( TB, timevar='A',idvar='B', direction='wide')
  colnames(AA) <- c(matrix(t(data.frame(strsplit(colnames(AA),"[.]")))[,2]))

  row.names(AA) = AA[,1]

  AA = AA[,-1]
  AA = AA+1
  Element = unique(c(colnames(AA), rownames(AA)))
  AA = AA[match(Element, rownames(AA)),]
  rownames(AA) = Element
  AA = t(AA)
  AA = AA[match(Element, rownames(AA)),]
  rownames(AA) = Element

  AA[is.na(AA)]=0
  return(AA)
}

print(DF2Net(List2DF(List)))
```

<pre>
1 2 3 4 5 6 7 8 9 10
1  0 1 0 0 0 0 0 0 0  0
2  0 0 1 0 0 0 0 0 0  0
3  0 0 0 1 0 0 0 0 0  0
4  0 0 0 0 1 0 0 0 0  0
5  0 0 0 0 0 1 0 0 0  0
6  0 0 0 0 0 0 1 0 0  0
7  0 0 0 0 0 0 0 1 0  0
8  0 0 0 0 0 0 0 0 1  0
9  0 0 0 0 0 0 0 0 0  1
10 0 0 0 0 0 0 0 0 0  0
</pre>

```r R
network=graph_from_adjacency_matrix(data.matrix(AA), mode='undirected')


l <- layout_components(network)
png(paste("network.png",sep=""), width = 400, height =  400)

plot(network,layout=l,
        vertex.size=1,
        vertex.label.cex=0.7,
        vertex.label ="",
        vertex.frame.color="transparent"
        )
dev.off()

```

|![Network plot](https://z3.ax1x.com/2021/04/20/c7ExmQ.png)|
|:-:|
|(c) Karobben|

## For loop to build a list

```r
Tree_grwoth <- function(Growth_Turn = 10, Period = 2){
  for (f in c(2:Growth_Turn)){
    Main = c("A")
    Result = list("main" = Main)
    Turns = f
    for(t in c(1:Turns)){
      for(branch in names(Result)){
        branch_tmp = c( Result[[branch]], paste( Result[[branch]][1],t, sep="-"))
        Result[[branch]] <- branch_tmp
        # New branch
        if(length(branch_tmp) %% Period == 0){
          print("New Branch")
          Result[branch_tmp[length(branch_tmp)]] =  c(branch_tmp[length(branch_tmp)])
        }
      }
    }
  }
  return(Result)
}
Result <- Tree_grwoth(20, 5)
head(summary(Result))
```
<pre>
Length Class  Mode     
main     21     -none- character
A-4      17     -none- character
A-4-8    13     -none- character
A-9      12     -none- character
A-4-8-12  9     -none- character
A-4-13    8     -none- character
</pre>

```r R
head(Result, 3)
```
<pre>
$main
$main
 [1] "A"    "A-1"  "A-2"  "A-3"  "A-4"  "A-5"  "A-6"  "A-7"  "A-8"  "A-9"  "A-10" "A-11" "A-12" "A-13" "A-14" "A-15"
[17] "A-16" "A-17" "A-18" "A-19" "A-20"
$`A-4`
 [1] "A-4"    "A-4-5"  "A-4-6"  "A-4-7"  "A-4-8"  "A-4-9"  "A-4-10" "A-4-11" "A-4-12" "A-4-13" "A-4-14" "A-4-15"
[13] "A-4-16" "A-4-17" "A-4-18" "A-4-19" "A-4-20"
$`A-4-8`
 [1] "A-4-8"    "A-4-8-9"  "A-4-8-10" "A-4-8-11" "A-4-8-12" "A-4-8-13" "A-4-8-14" "A-4-8-15" "A-4-8-16" "A-4-8-17"
[11] "A-4-8-18" "A-4-8-19" "A-4-8-20"
</pre>


## Whole Pipeline

```r
Result <- Tree_grwoth(100, 10)
'''
STATE　<- data.frame(summary(Result))
STAT <- STATE[STATE$Var2 == "Length",]
sum(as.numeric(str_remove_all(as.character(STAT$Freq)," ")) -1)

'''
TB <- data.frame()
for(List in Result){
  TB_tmp <- List2DF(List)
  TB <- rbind(TB, TB_tmp)
}
AA <- DF2Net(TB)

network=graph_from_adjacency_matrix(data.matrix(AA), mode='undirected')
l <- layout_components(network)
plot(network,layout=l,
        vertex.size=1,
        vertex.label.cex=0.7,
        vertex.label ="",
        vertex.frame.color="transparent"
        )
```

When I try `Result <- Tree_grwoth(135, 10)`:
|![Dataframe out of memory](https://z3.ax1x.com/2021/04/20/c7lYB6.png)|
|:-:|

```r
V(network)$color ="steelblue"

for(i in c(1:100)){
  png(paste(i,".png",sep=""), width = 1920, height =  1080)
  plot(network,layout=head(l, i),
          vertex.size=1 / tanh(0.004 * i),
          vertex.label.cex=0.7,
          vertex.label ="",
          vertex.frame.color="transparent"
          )
  dev.off()
}
```

![binary tree igraph](https://z3.ax1x.com/2021/04/20/c7vKXt.png)
