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
'dplyr', 'ellipse', 'fastcluster', "reshape2",
"htmlwidgets", "gapminder", "httr", "igraph",
"jiebaR", "jpeg", "htmlwidgets", "jsonlite",
"magick", "modelr", "pacman", "psych",
"randomForest", "rayrender", "readxl",
"rpart", "Rwordseg", "SnowballC", "remotes"

# Map data
# relied libs: https://www.liujason.com/article/570.html
# sudo apt-get install libgdal-dev libproj-dev gdal-bin -y

"sf", "swirl", "tidyr", "tidyverse",
"tm", "WGCNA", "xgboost", "fmsb",
'rcmdcheck', 'devtools', "rgl", "forecast",

# Math calculation:  fourier ; pacman -S gcc-fortran

# Plot
"patchwork" ,"networkD3" ,"ggplot2" ,"maps" ,"ggalluvial",
'circlize' ,'cowplot' ,"pheatmap" ,"GGally" ,'ggplotify',
"ggthemes" ,"ggdendro" ,"ggrepel" ,"showtext", "remotes",
"wordcloud2" ,"ggupset" ,"plotly" ,"plotrix" ,'ggalt',

# devtools::install_github("const-ae/ggupset")
# Fonts showtext
# Map data: ggalt
```


### Install with for loop
```r
List <- c('dplyr', 'ellipse', 'fastcluster', "reshape2",
          "htmlwidgets", "gapminder", "httr", "igraph",
          "jiebaR", "jpeg", "htmlwidgets", "jsonlite",
          "magick", "modelr", "pacman", "psych",
          "randomForest", "rayrender", "readxl",
          "rpart", "Rwordseg", "SnowballC", "remotes",
          "sf", "swirl", "tidyr", "tidyverse",
          "tm", "WGCNA", "xgboost", "fmsb",
          'rcmdcheck', 'devtools', "rgl", "forecast",
          "patchwork" ,"networkD3" ,"ggplot2" ,"maps" ,"ggalluvial",
          'circlize' ,'cowplot' ,"pheatmap" ,"GGally" ,'ggplotify',
          "ggthemes" ,"ggdendro" ,"ggrepel" ,"showtext", "remotes",
          "wordcloud2" ,"ggupset" ,"plotly" ,"plotrix" ,'ggalt')

for(LIB in List){
  if (!requireNamespace(LIB, quietly = TRUE))
      install.packages(LIB)
}
```

#### sf

udunits is required for `sf` (udunits)
for manjaro install

```bash
wget  	https://mirrors.tuna.tsinghua.edu.cn/arch4edu/x86_64/udunits-2.2.28-2-x86_64.pkg.tar.zst
pacman -U udunits-2.2.28-2-x86_64.pkg.tar.zst
```

`gdal-config not found or not executable`

```bash
sudo pacman -S gdal
```

## Packages for Biology

```r
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

# For calculation
"edgeR", "limma", "qvalue", "DESeq2",

# Microarray
"GEOquery",

# Seq data
"Biostrings",

# Annotation and Enrichment
"clusterProfiler", "pathview",
"org.Hs.eg.db", "org.Dr.eg.db", "org.Dm.eg.db",

# Plot
"ggtree", "clue", "ComplexHeatmap",
# clue: for "ComplexHeatmap"
# ComplexHeatmap: old version. New version can be found in Github

# other NGS
"WGCNA",

# Others
"Biobase"
```

```r
List <- c("Biobase", "edgeR", "Biostrings", "clusterProfiler", "ggtree",
          "pathview", "limma", "qvalue", "org.Hs.eg.db", "org.Dr.eg.db",
          "org.Dm.eg.db","clue", "ComplexHeatmap", "GEOquery", "WGCNA")

for(LIB in List){
  if (!requireNamespace(LIB, quietly = TRUE))
      BiocManager::install(LIB)
}
```

## Packages from github


```r

"tylermorganwall/coronaobj", "jennybc/gapminder", 'pzhaonet/ncovr',

# Plot GGplot
"hrbrmstr/ggalt", "AckerDWM/gg3D", "jayjacobs/ggcal",
'ricardo-bion/ggradar', "tylermorganwall/rayshader",

# 3D plot : gg3D, rayshader

# Plot Others
"jokergoo/ComplexHeatmap"
```

```r
List <- c("tylermorganwall/coronaobj", "jennybc/gapminder", 'pzhaonet/ncovr',
          "hrbrmstr/ggalt", "AckerDWM/gg3D", "jayjacobs/ggcal",
          'ricardo-bion/ggradar', "tylermorganwall/rayshader",
          "jokergoo/ComplexHeatmap")


for(LIB in List){
  if (!requireNamespace(LIB, quietly = TRUE))
      remotes::install_github(LIB)
}
```
