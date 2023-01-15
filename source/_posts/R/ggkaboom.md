---
title: "ggkaboom: minimal codes for ggplot"
description: "ggkaboom: minimal codes for ggplot"
url: ggkaboom
date: 2022/02/28
toc: true
excerpt: "R: ggplot, ggkaboom, barplot"
tags: [R, Plot, ggplot, ggkaboom]
category: [R, Plot, GGPLOT]
cover: 'https://s4.ax1x.com/2022/03/01/bQfC4g.png'
thumbnail: 'https://s4.ax1x.com/2022/03/01/bQgzHU.png'
covercopy: © Karobben
priority: 10000
---

## ggkaboom

ggkaboom is a ggplot extensions which compressed a set of code for statistics and quick graph.

## Install

```r
remotes::install_github("karobben/ggkaboom")
library(ggkaboom)
```


## Kaboom_flow

This is a flow chart which designed for show the dynamic change of the composition from each sample.

```r
Kaboom_flow(TB)
```

![](https://s1.ax1x.com/2022/05/27/XZTJC6.png)

A quick simulation data could be:


```r
A <- c("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M")
B <- c("A", "B", "C", "D", "E", "F", "K", "L", "M", "N")
C <- c("A", "B", "C", "D", "E", "F", "G", "H", "N","O")

TB = data.frame(row.names =  sort(unique(c(A,B,C))))

Num = 0
for(Col in list(A,B,C)){
    Num = Num + 1
    TB[paste("Group",Num, sep="_")] = 0
    TB[paste("Group",Num, sep="_")][row.names(TB) %in% Col,] = 1
}

print(TB)
```

<pre>
Group_1 Group_2 Group_3
A       1       1       1
B       1       1       1
C       1       1       1
D       1       1       1
E       1       1       1
F       1       1       1
G       1       0       1
H       1       0       1
I       1       0       0
J       1       0       0
K       1       1       0
L       1       1       0
M       1       1       0
N       0       1       1
O       0       0       1
</pre>


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>


## Kaboom_break

With this function, you can make as many breaks as you like by given y lims.

```r
remotes::install_github("karobben/ggkaboom")
library(ggkaboom)

data(cars)
cars[1,2] =100000

p <- ggplot(cars,aes(x=speed,y=dist, fill=as.factor(speed))) + geom_bar(stat='identity')
# For tow break
Kaboom_break(p, c(0,  400, 10000, 120000), R=c(1, 4))

# Three breaks
Kaboom_break(p, c(0, 15, 30, 400, 10000, 120000), R=c(1,4, 2))

# Three breaks with changed grid
Kaboom_break(p, c(0, 15, 30, 400, 10000, 120000), R=c(1, 4, 2), panel.grid.scale = 'len', panel.grid.num = 6)
```

|![](https://s1.ax1x.com/2022/09/10/vLfZZD.png)|![](https://s1.ax1x.com/2022/09/10/vLfEqO.png)|
|:-:|:-:|
|Raw Plot| With one break|
|![](https://s1.ax1x.com/2022/09/10/vLfkM6.png)|![](https://s1.ax1x.com/2022/09/10/vLfixx.png)|
|Two breaks with no `panel.grid` parameters| With `panel.grid` parameters|


Other Parameters

<pre>
panel.grid = element_line(colour = 'grey'),
panel.background = element_blank(),
panel.border = element_blank(),
panel.grid.num = 10,
panel.grid.scale = F,
legend.position = 'bottom',
legend.direction = 'vertical'
</pre>

## Kaboom_bar

This main idea of Kaboom bar is using row data to calculate the mean, sd, and sem value for you.

- [x] Mean
- [x] sd
- [x] sem
- [x] Statistics for two set of observes
- [x] facet; fill, inherit the factors from raw data
- [x] color plate
- [x] t-test and anova test

### Quick Examples

```
Kaboom_bar(iris, "Species")
Kaboom_bar(ChickWeight[-3], 'Time', 'Diet', fill = "Diet", Var = "SEM")
Kaboom_bar(midwest[c(1:10,200:210, 300:310), c(3:8,ncol(midwest))], "state", "category", Var = "SEM", Facet_row = 'Variable', space = 'free', scales = 'free')
```

|iris | ChickWeight | midwest|
|:-:|:-:|:-:|
|![ggplot barplot](https://s4.ax1x.com/2022/03/01/bQgzHU.png)|![ggplot barplot](https://s4.ax1x.com/2022/03/01/bQgxBT.png)|![ggplot barplot](https://s4.ax1x.com/2022/03/01/bQ2pEF.png)|


```
Kaboom_bar <- function(data, x,
		 Col= FALSE, Var="SD", fill = FALSE,
		 Pos = "dodge", BarW = .9, BarAl = .6, ErbW = .3,
	   Plate = "Set1",
	   Facet = "wrap", Facet_row = FALSE, scales = "fixed", space="fixed",
	   Vari_level= FALSE, Frow_level = FALSE)
```

```
data: Data frame
x: Variable for X axis. The mean and sd/sem would calculated.
Col: The second variable. The mean and sd/sem would be calculated based on the `x` and `Col`
fill: Colors for the bar. Default is the Variable
BarW: float. Width of the bar
BarAl: 0:1: Alpha of the bar
ErbW: float: Width of the Error bar
Plate: "Set1", "Paired", ... Color Plate. Check all plate by `brewer.pal.info`
Facet: "wrap", "grid": `facet_wrap` if there has `Col`.
Facet_row: facet by a variable in row. No statistics.
scales: as facet_grid(scales=...)
space: as facet_grid(space=...)
```




### How to use different types of data with this function

Due to some unpleasant reasons, the logic of this functions is kind of wired and jumping. Instead of insert more "wired" patches to  confusing myself, I decided not rewrite this function but given more detailed descriptions and examples. Cheers!

Tips 1: ==DO NOT CONTAIN "-" IN YOUR SAMPLE/GROUP NAMES==, it would ruine the Tukey-test function.
Tips 2: Assign all the character variables into factors. It would solve most of unpleasant errors.
Tips 3: Sort your axis into a desire order. The final result would follows the order of the data rather than levels.

### Exp1: Two Columns Data
