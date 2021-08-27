---
title: "Common Library for R"
description: "Common Library for R"
url: library
date: 2020/02/14
toc: true
excerpt: "This is a note for recording all library I am using frequently"
tags: [R, R packages]
category: [R, libraries]
cover: 'https://s1.ax1x.com/2020/08/15/dk0Jwn.png'
thumbnail: 'https://s1.ax1x.com/2020/08/15/dk0Jwn.png'
priority: 10000
---

## Common Library for R

## Packages from Cran

```r
install.packages('dplyr')
install.packages('ellipse')
install.packages('fastcluster')
install.packages("reshape2")
install.packages("htmlwidgets")
install.packages("gapminder")
install.packages("httr")
install.packages("igraph")
install.packages("jiebaR")
install.packages("jpeg")
install.packages("htmlwidgets")
install.packages("jsonlite")
install.packages("magick")
install.packages("modelr")
install.packages("pacman")
install.packages("psych")
install.packages("randomForest")
install.packages("rayrender")
install.packages("readxl")
install.packages("rpart")
install.packages("Rwordseg")
install.packages("SnowballC")

# Map data
# relied libs: https://www.liujason.com/article/570.html
# sudo apt-get install libgdal-dev libproj-dev gdal-bin -y
install.packages("sf") # map data

install.packages("swirl")
install.packages("tidyr")
install.packages("tidyverse")
install.packages("tm")
install.packages("WGCNA")
install.packages("xgboost")
install.packages("fmsb")
install.packages('rcmdcheck')
install.packages('devtools')
install.packages("rgl")
install.packages("forecast") # Math calculation:  fourier ; pacman -S gcc-fortran
# Plot
install.packages("patchwork")
install.packages("networkD3")
install.packages("ggplot2")
install.packages("maps")
install.packages("ggalluvial")
install.packages('circlize')
install.packages('cowplot')
install.packages("pheatmap")
install.packages("GGally")
install.packages('ggplotify')
install.packages("ggthemes")
install.packages("ggdendro")
install.packages("ggrepel")
install.packages('ggalt') # Map data
install.packages("showtext") # Fonts
install.packages("wordcloud2")
install.packages("ggupset") # devtools::install_github("const-ae/ggupset")
install.packages("plotly")
install.packages("plotrix")
```
## Packages for Biology

```r
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("Biobase")
BiocManager::install("edgeR")
BiocManager::install("Biostrings")
BiocManager::install("clusterProfiler")
BiocManager::install("ggtree")
BiocManager::install("org.Hs.eg.db")
BiocManager::install("pathview")
BiocManager::install("limma")
BiocManager::install("qvalue")
# Plot
BiocManager::install("clue") # for "ComplexHeatmap"
BiocManager::install("ComplexHeatmap") # old version. New version can be found in Github
```

## Packages from github


```r
install.packages('remotes')
remotes::install_github("tylermorganwall/coronaobj")
remotes::install_github("jennybc/gapminder")
remotes::install_github('pzhaonet/ncovr')
# Plot GGplot
remotes::install_github("hrbrmstr/ggalt")
remotes::install_github("AckerDWM/gg3D")
remotes::install_github("jayjacobs/ggcal")
remotes::install_github('ricardo-bion/ggradar')
remotes::install_github("tylermorganwall/rayshader") # 3D plot for ggplot

# Plot Others
remotes::install_github("jokergoo/ComplexHeatmap")
```
