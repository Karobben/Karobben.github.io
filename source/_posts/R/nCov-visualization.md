---
title: "nCov visualization"
description: "nCov visualization"
url: vxunsh2
date: 2020/06/10
toc: true
excerpt: "rayrender is an awesome 3D model visualizing library. But it takes lot's of calculating as all other similar tools. Prepare for cooling-fan for your laptop before try this"
tags: [R, 3D, Plot]
category: [R, Plot, VisuaProtocol]
cover: 'https://i.loli.net/2020/06/20/LBFDxuv3UniCAo2.jpg'
thumbnail: 'https://i.loli.net/2020/06/20/LBFDxuv3UniCAo2.jpg'
priority: 10000
---

## nCov visualization


<br />Github project: [tylermorganwall](https://github.com/tylermorganwall)/**[coronaobj](https://github.com/tylermorganwall/coronaobj)**<br />

<a name="2WjTv"></a>
## Packages Install
<a name="ZEugX"></a>
### Install through remotes
```r
remotes::install_github("tylermorganwall/rayrender")
remotes::install_github("tylermorganwall/coronaobj")
```
(An extral data with  91.2MB is in [inst/extdata](https://github.com/tylermorganwall/coronaobj/tree/master/inst/extdata). So, it may take a while to installing it)<br />

<a name="94An8"></a>
### Install from local
```bash
git clone https://github.com/tylermorganwall/rayrender.git
git clone https://github.com/tylermorganwall/coronaobj.git
```
```r
install.packages("/home/ken/test/rayrender/",repos = NULL)
install.packages("/home/ken/test/coronaobj/",repos = NULL)
```


<a name="oDJ9Y"></a>
## Start with coronaobj
```r
library(coronaobj)
library(rayrender)

write_corona_obj("defaults.obj")	 # write the obj file to local

obj_model("defaults.obj", vertex_colors = TRUE) %>%
  add_object(sphere(y=10,z=10,x=10, material=light(intensity=100))) %>%
  add_object(sphere(y=10,z=10,x=-10, material=light(intensity=100))) %>%
  render_scene(parallel=TRUE, samples = 1000, fov = 7, min_variance=0, focal_distance = 9.6,
               width=800,height=800)
```
It takes me about 30min...<br />
![1586932705100-52454ad9-bdec-498e-bb87-8bb61554de89](https://i.loli.net/2020/06/20/LwcMThRQurxa23f.jpg)


```r
## above right
obj_model("defaults.obj", vertex_colors = TRUE) %>%
  add_object(sphere(y=10,z=10,x=10, material=light(color="lightblue",intensity=160))) %>%
  add_object(sphere(y=10,z=10,x=-10, material=light(color="orange",intensity=160))) %>%
  add_object(sphere(y=-10,z=-5,material=light(color="purple", intensity = 160))) %>%
  render_scene(parallel=TRUE, samples = 1000, fov = 7, min_variance=0, focal_distance = 9.6,
               aperture=0.5, width=800,height=800)
```
![1586932810859-46f7ae3b-37b7-4161-8373-c6c0a16d1c9e](https://i.loli.net/2020/06/20/LBFDxuv3UniCAo2.jpg)
