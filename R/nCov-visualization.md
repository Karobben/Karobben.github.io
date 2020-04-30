---
url: vxunsh
---

# nCov visualization


<br />Github project: [tylermorganwall](https://github.com/tylermorganwall)/**[coronaobj](https://github.com/tylermorganwall/coronaobj)**<br />

<a name="2WjTv"></a>
# Packages Install
<a name="ZEugX"></a>
## Install through remotes
```r
remotes::install_github("tylermorganwall/rayrender")
remotes::install_github("tylermorganwall/coronaobj")
```
(An extral data with  91.2MB is in [inst/extdata](https://github.com/tylermorganwall/coronaobj/tree/master/inst/extdata). So, it may take a while to installing it)<br />

<a name="94An8"></a>
## Install from local
```bash
git clone https://github.com/tylermorganwall/rayrender.git
git clone https://github.com/tylermorganwall/coronaobj.git
```
```r
install.packages("/home/ken/test/rayrender/",repos = NULL)
install.packages("/home/ken/test/coronaobj/",repos = NULL)
```


<a name="oDJ9Y"></a>
# Start with coronaobj
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
It takes me about 30min...<br />![123.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/691897/1586932705100-52454ad9-bdec-498e-bb87-8bb61554de89.jpeg#align=left&display=inline&height=509&margin=%5Bobject%20Object%5D&name=123.jpg&originHeight=546&originWidth=800&size=50508&status=done&style=none&width=746)

![123.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/691897/1586932810859-46f7ae3b-37b7-4161-8373-c6c0a16d1c9e.jpeg#align=left&display=inline&height=331&margin=%5Bobject%20Object%5D&name=123.jpg&originHeight=378&originWidth=400&size=24253&status=done&style=none&width=350)![124.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/691897/1586932811370-89ee3eb1-4b6d-4555-ad3e-c92a49144ab3.jpeg#align=left&display=inline&height=331&margin=%5Bobject%20Object%5D&name=124.jpg&originHeight=372&originWidth=400&size=19672&status=done&style=none&width=356)
```r
# above right
obj_model("defaults.obj", vertex_colors = TRUE) %>%
  add_object(sphere(y=10,z=10,x=10, material=light(color="lightblue",intensity=160))) %>%
  add_object(sphere(y=10,z=10,x=-10, material=light(color="orange",intensity=160))) %>%
  add_object(sphere(y=-10,z=-5,material=light(color="purple", intensity = 160))) %>%
  render_scene(parallel=TRUE, samples = 1000, fov = 7, min_variance=0, focal_distance = 9.6,
               aperture=0.5, width=800,height=800)
```
