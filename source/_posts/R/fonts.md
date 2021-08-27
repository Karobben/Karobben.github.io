---
title: "Fonts family in R plot"
date: 2020/09/03
url: fonts
description: "Change Fonts family in R plot| R语言换画图字体"
toc: true
excerpt: "R: Stylize the font in your Chart with library showtext"
tags: [R, Plot]
category: [R, Plot, others]
cover: 'https://upload-images.jianshu.io/upload_images/3884693-8864db1dbb538efc'
thumbnail: 'https://upload-images.jianshu.io/upload_images/3884693-8864db1dbb538efc'
priority: 10000
---


## Switch Fonts in R

![](https://upload-images.jianshu.io/upload_images/3884693-8864db1dbb538efc?imageMogr2)

## library(showtext)
reference: [王诗翔 2018](https://www.jianshu.com/p/9b9c9f4ddf6b)

## Quick Start
```r
library(showtext)

showtext_auto()
```

## Checking local fonts
```r
font.paths()
font.files()
````

<pre>
'fond.paths()' is now renamed to 'font_paths()'
The old version still works, but consider using the new function in future code
 [1] "/home/ken/.fonts"                             "/usr/local/share/fonts"                       "/usr/local/share/fonts/conkycolors"           "/usr/share/fonts"                            
 [5] "/usr/share/fonts/cmap"                        "/usr/share/fonts/cMap"                        "/usr/share/fonts/cmap/adobe-cns1"             "/usr/share/fonts/cmap/adobe-gb1"             
 [9] "/usr/share/fonts/cmap/adobe-japan1"           "/usr/share/fonts/cmap/adobe-japan2"           "/usr/share/fonts/cmap/adobe-korea1"           "/usr/share/fonts/deepin-font-install"        
[13] "/usr/share/fonts/eot"                         "/usr/share/fonts/eot/font-awesome"            "/usr/share/fonts/opentype"                    "/usr/share/fonts/opentype/cantarell
</pre>

<pre>
'font.files()' is now renamed to 'font_files()'
The old version still works, but consider using the new function in future code
                                            path                                      file                        family            face
1                               /home/ken/.fonts                  AvantGarde_LT_Medium.ttf          AvantGarde LT Medium         Regular
2                               /home/ken/.fonts                            GE_Inspira.ttf                    GE Inspira         Regular
3                               /home/ken/.fonts                                Ubuntu.ttf                        Ubuntu         Regular
4             /usr/local/share/fonts/conkycolors                           aClock_Hour.ttf                        aClock           _Hour
5             /usr/local/share/fonts/conkycolors                            aClock_Min.ttf                        aClock            _Min
</pre>

## Plot

```r
library(showtext)
font_add_google("Lobster", "lobster")

showtext_auto()

plot(1, pch = 16, cex = 3)
text(1, 1.1, "A fancy dot", family = "lobster", col = "steelblue", cex = 3)
```

![123.png](https://upload-images.jianshu.io/upload_images/3884693-8864db1dbb538efc)
© 王诗翔 2018
