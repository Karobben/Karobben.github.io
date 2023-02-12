---
toc: true
url: venn
covercopy: <a href="https://statisticsglobe.com/ggvenn-r-package">© statisticsglobe</a>
priority: 10000
date: 2022-10-17 10:13:58
title: "Venn Plot in R"
ytitle: "维恩图"
description: "Venn Plot in R"
excerpt: "Venn plot is a visualization tool to display overlapping or unique sets between two or more groups. In R, the 'VennDiagram' package provides an easy-to-use interface to create Venn plots with customizable colors, labels, and shapes. <a title='ChatGPT'>Who sad this?</a>"
tags: [Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: "https://statisticsglobe.com/wp-content/uploads/2021/01/figure-3-plot-ggvenn-r-package-programming-language.png"
thumbnail: "https://statisticsglobe.com/wp-content/uploads/2021/01/figure-3-plot-ggvenn-r-package-programming-language.png"
---

## ggvenn

Reference: [statisticsglobe.com](https://statisticsglobe.com/ggvenn-r-package)


```r
library(ggvenn)

set.seed(654925)                          # Create example list
list_venn <- list(A = sort(sample(1:100, 20)),
                  B = sort(sample(1:100, 20)),
                  C = sort(sample(1:100, 20)),
                  D = sort(sample(1:100, 20)))
list_venn
```

<pre>
list_venn                                                                                         
$A
[1]  1  3  4 11 19 20 22 32 34 36 47 48 58 59 60 64 69 72 97 98
$B
[1]  4 17 18 23 32 33 34 41 45 52 53 56 58 59 66 67 74 78 91 92
$C
[1]  3 10 28 31 34 38 46 47 51 57 58 65 67 70 72 74 80 89 94 97
$D
[1]  8 11 14 15 17 18 19 33 34 47 51 59 66 68 73 77 78 82 86 87
</pre>




|![](https://statisticsglobe.com/wp-content/uploads/2021/01/figure-1-plot-ggvenn-r-package-programming-language.png)|![](https://statisticsglobe.com/wp-content/uploads/2021/01/figure-2-plot-ggvenn-r-package-programming-language.png)|![](https://statisticsglobe.com/wp-content/uploads/2021/01/figure-3-plot-ggvenn-r-package-programming-language.png)|
| :-: | :-:|  :-:|
| `ggvenn(list_venn, c("A", "C"))`    | `ggvenn(list_venn, c("A", "C", "D"))`     | `ggvenn(list_venn)  `|



!!! note Change the fill color
    ```r
    ggvenn(list_venn, c("A", "C")) + scale_fill_brewer( palette = 'Set1')
    ```




Other related Posts:
- [Alboukadel](https://www.datanovia.com/en/blog/venn-diagram-with-r-or-rstudio-a-million-ways/)
    - [![](https://www.datanovia.com/en/wp-content/uploads/dn-tutorials/r-tutorial/figures/venn-diagram-in-r-or-rstudio-ggVennDiagram-1.png)](https://www.datanovia.com/en/blog/venn-diagram-with-r-or-rstudio-a-million-ways/)




































































<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
