---
title: "magick (Picture needed)"
description: "magick (Picture needed)"
url: magick2
date: 2020/06/19
toc: true
excerpt: "magick package is a library for reading image file to R. By doing those, you can manipulate each pixl of the image to do some calculating!"
tags: [R, Image]
category: [R, Image]
cover: 'https://www.r-project.org/Rlogo.png'
thumbnail: 'https://www.r-project.org/Rlogo.png'
priority: 10000
---

## magick (Picture needed)


```r
library("magick")
tiger <- image_read_svg('http://jeroen.github.io/images/tiger.svg', width = 400)
print(tiger)
##rewrite
image_write(tiger, path = "tiger.png", format = "png")
##inf
image_info(tiger_png)
##Edit
image_crop(image, "100x150+50"): crop out width:100px and height:150px starting +50px from the left
image_scale(image, "200"): resize proportionally to width: 200px
image_scale(image, "x200"): resize proportionally to height: 200px
image_fill(image, "blue", "+100+200"): flood fill with blue starting at the point at x:100, y:200
image_border(frink, "red", "20x10"): adds a border of 20px left+right and 10px top+bottom
img <- image_resize(logo, "300x300")
img_blurred <- image_convolve(img, kern)
image_append(c(img, img_blurred))
```
