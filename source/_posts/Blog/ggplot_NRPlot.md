---
title: "Nutrition Data Sheet Visualization"
description: "ggplot| Complicate nutrition date sheet"
date: 2020/07/28
url: r_nutrplot
toc: true
excerpt: "Plot Nutrition Data Matrix in ggplot"
tags: [Plot, ggplot, R, Nutrition matrix]
category: [R, Plot, GGPLOT]
cover: 'https://s3.ax1x.com/2020/12/27/r55Fje.md.png'
thumbnail: 'https://s3.ax1x.com/2020/12/27/r55Fje.md.png'
priority: 10000
---

## Complicate Nutrition Data Sheet Visualization

**Example Data**
`A <- read.table("Digestive_Enzymes.csv",sep=',',header=T)`
In this matrix, we have unique `colname` and `rowname`.
There are `±` and `abc` followed with the numbers.
Data Matrix online: [Github](https://github.com/Karobben/Test_Data_Set/blob/master/Data_vidulization/nutrition_data_set.csv)
```
Gastric_Pepsin Gastric_Amylase Gastric_Lipase Intestinal_Pepsin
G1    17.23±0.03f       0.68±0.00    18.08±0.12f        1.54±0.01d
G2    18.48±0.02e       0.71±0.00    19.11±0.11e        1.62±0.01c
G3    20.67±0.04d       0.77±0.00    20.0±0.14ad       1.68±0.01bc
G4    22.32±0.10c       0.80±0.00   20.71±0.21ab       1.76±0.02ab
G5   24.21±0.04ab       0.84±0.00    21.18±0.25a       1.78±0.01ab
G6   17.38±0.02de       0.70±0.00    17.63±0.15f       1.57±0.02cd
```


## Data Clean
```r
NutriSplit <- function(A){
  A1 <- c()
  A2 <- c()
  # Split the Avr and Disparity
  for(i in A){
    tmp1 = sapply(strsplit(as.character(i),'±'),"[",1)
    tmp2 = sapply(strsplit(as.character(i),'±'),"[",2)
    A1 <- c(A1,tmp1)
    A2 <- c(A2,tmp2)
  }
  A1 <- as.numeric(A1)
  # split the Dist and Significant
  A2_1 <- gsub("[^0-9.]", "", A2)
  A2_2 <- gsub("[^a-z]", "", A2)
  # Matrix
  A1 <- matrix(A1,nrow = nrow(A))
  A2_1 <- matrix(as.numeric(A2_1),nrow = nrow(A))
  A2_2 <- matrix(A2_2,nrow = nrow(A))
  colnames(A1) = colnames(A2_1) = colnames(A2_2) = colnames(A)
  rownames(A1) = rownames(A2_1) = rownames(A2_2) = rownames(A)
  A1 <- data.frame(A1)
  A2_1 <- data.frame(A2_1)
  A2_2 <- data.frame(A2_2)
  Result = c()
  Result$Avr <- A1
  Result$Dit <- A2_1
  Result$Sig <- A2_2
  return(Result)
}
```

## Plot

```r
library(ggplot2)
library(reshape2)
library(ggrepel)

TB <- NutriSplit(t(A))

ggplot(melt(as.matrix(TB$Avr)),aes(x=Var2,y=value)) +
  geom_line(aes(group=Var1)) +
  geom_errorbar(aes(ymin=value-melt(as.matrix(TB$Dit))$value, ymax=value+melt(as.matrix(TB$Dit))$value), width=0.2)+
  geom_text_repel(aes(x=Var2,y=value,label= melt(as.matrix(TB$Sig))$value, color= 'blue' ))+ theme_light() +
  facet_wrap(~Var1, scales = 'free')+
  geom_point(aes(color=melt(as.matrix(TB$Sig))$value))+
  theme(axis.text.x=element_text(angle=45, hjust=1))
```

![r55Fje.md.png](https://s3.ax1x.com/2020/12/27/r55Fje.md.png)
