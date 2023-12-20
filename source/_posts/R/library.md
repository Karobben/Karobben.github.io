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

## library prepare



```bash
# for unit and sf
# cite: https://stackoverflow.com/questions/61733376/r-rgdal-install-fails-on-ubuntu-20-04-with-error-double-red-or-corruption-prev
sudo apt install libudunits2-dev libspatialite-dev 
```

## Packages from Cran


```r
'dplyr', 'ellipse', 'fastcluster', "reshape2",
"htmlwidgets", "gapminder", "httr", "igraph",
"jiebaR", "jpeg", "htmlwidgets", "jsonlite",
"magick", "modelr", "pacman", "psych",
"randomForest", "rayrender", "readxl",
"rpart", "Rwordseg", "SnowballC", "remotes", "overlap", "overlaping"

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
"ggthemes" ,"ggdendro" ,"ggrepel", "ggnewscale", "ggridges", "ggvenn", "svglite", "showtext", "remotes", "venneuler",
"wordcloud2" ,"ggupset" ,"plotly" ,"plotrix" ,'ggalt'

# devtools::install_github("const-ae/ggupset")
# Fonts showtext
# Map data: ggalt

## Biology
"BiocManager", "seurat"

## Mathmatics
"deSolve", "SciViews"
```


### Install with for loop

- config for rJAVA: `sudo R CMD javareconf` [Jim Chen, 2018](https://stackoverflow.com/questions/3311940/r-rjava-package-install-failing)

- proj4: `sudo apt-get install libproj-dev` [DirtStats, 2020](https://stackoverflow.com/questions/56304632/cant-install-proj4-package-because-libproj-and-or-proj-api-h-not-found-in-sta)
- sf: `sudo apt install libgdal-dev` [Gayan Kavirathne, 2018](https://stackoverflow.com/questions/12141422/error-gdal-config-not-found-while-installing-r-dependent-packages-whereas-gdal)
- magick:
    - `sudo add-apt-repository -y ppa:cran/imagemagick`
    - `sudo apt-get update`
    - `sudo apt-get install -y libmagick++-dev`
- textshaping : `sudo apt install libharfbuzz-dev libfribidi-dev`
```r
List <- c('dplyr', 'ellipse', 'fastcluster', "reshape2",
          "htmlwidgets", "gapminder", "httr", "igraph",
          "jiebaR", "jpeg", "htmlwidgets", "jsonlite",
          "magick", "modelr", "pacman", "psych",
          "randomForest", "rayrender", "readxl",
          "rpart", "Rwordseg", "SnowballC", "remotes",
          "sf", "swirl", "tidyr", "tidyverse",
          "tm", "WGCNA", "xgboost", "fmsb", "venneuler",
          'rcmdcheck', 'devtools', "rgl", "forecast",
          "patchwork" ,"networkD3" ,"ggplot2" ,"maps" ,"ggalluvial",
          'circlize' ,'cowplot' ,"pheatmap" ,"GGally" ,'ggplotify',
          "ggthemes" ,"ggdendro" ,"ggrepel", "ggnewscale", "ggridges",
          "ggvenn", "svglite", "showtext", "remotes",
          "wordcloud2" ,"ggupset" ,"plotly" ,"plotrix" ,'ggalt',
          "BiocManager", "deSolve", "SciViews", "overlap")

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
"Biostrings", "BSgenome",

# Annotation and Enrichment
"clusterProfiler", "pathview",
"org.Hs.eg.db", "org.Dr.eg.db", "org.Dm.eg.db", "ReactomePA", "meshes",

# Plot
"ggtree", "clue", "ComplexHeatmap", 'ggtheme',
# clue: for "ComplexHeatmap"
# ComplexHeatmap: old version. New version can be found in Github

# other NGS
"WGCNA",

# Others
"Biobase", "BiocManager"
```


**Prerequisite**:
- Rcurl: `sudo apt-get install -y libcurl4-openssl-dev` [Mike Smith, 2016](https://support.bioconductor.org/p/129866/)
- ggforce: `sudo apt -y install libfontconfig1-dev`[johnbester, 2020](https://github.com/r-lib/systemfonts/issues/35)
- XML: `sudo apt-get install libxml2-dev`
- ggtree: `remotes::install_github("YuLab-SMU/ggtree")`

```r
List <- c("Biobase", "edgeR", "Biostrings", "BSgenome", "clusterProfiler", "ggtree",
          "meshes", "pathview", "limma", "qvalue", "org.Hs.eg.db", "org.Dr.eg.db",
          "org.Dm.eg.db","clue", "ComplexHeatmap", "GEOquery", "WGCNA", "ReactomePA",
          'ggtheme', "TCGAbiolinks")

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
"mattflor/chorddiag", "gaospecial/ggVennDiagram"
# 3D plot : gg3D, rayshader

# Plot Others
"jokergoo/ComplexHeatmap"

# ggplot, regression function
```

```r
List <- c("tylermorganwall/coronaobj", "jennybc/gapminder", 'pzhaonet/ncovr',
          "hrbrmstr/ggalt", "AckerDWM/gg3D", "jayjacobs/ggcal",
          'ricardo-bion/ggradar', "tylermorganwall/rayshader",
          "mattflor/chorddiag", "gaospecial/ggVennDiagram", "jokergoo/ComplexHeatmap", "Laurae2/Laurae")


library(stringr)
for(LIB in List){
  if (!requireNamespace(str_split(LIB, '/')[[1]][2], quietly = TRUE))
      remotes::install_github(LIB)
}
```


## package with troubles

[Gayan Kavirathne](https://stackoverflow.com/questions/12141422/error-gdal-config-not-found-while-installing-r-dependent-packages-whereas-gdal)
```bash
sudo apt install libgdal-dev
```
```r
install.packages("AICcmodavg")
```
