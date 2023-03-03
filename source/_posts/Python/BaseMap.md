---
title: "Basmap"
description: "Basmap"
url: basemap
date: 2020/01/22
toc: true
excerpt: "Basemap is a Python library that provides a set of map projections and tools for plotting data on maps. It allows you to create maps with various cartographic projections, add features like coastlines and rivers, and plot data points on top of the map. Basemap can be used to create static maps or embedded in interactive web applications. <a title='GhatGPT'>Who said this?</a>"
tags: [Python, Matplotlib, Plot]
category: [Python, Plot]
cover: 'https://miro.medium.com/v2/resize:fit:720/format:webp/1*PIpjPTlcrDyXLl2fDv34bA.png'
covercopy: '<a href="https://towardsdatascience.com/python-libraries-for-natural-language-processing-be0e5a35dd64">© Claire D. Costa</a>'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## Basmap

## 0. Install
教程推薦:
1. [官方文檔](https://matplotlib.org/basemap/users/installing.html)
2. [moxigandashu 2017](https://blog.csdn.net/moxigandashu/article/details/68945845)
3. 往下看我的(系統:Deepin 15.11)

### 1. Dependency:
- python
- pip install:
  - Matplotlib
  - NumPy
  - GeobricksProj4ToEPSG
  - pyproj
  - pyshp
- geos
  `sudo apt install libgeos-3.6.2`
  `sudo apt install libgeos-dev`

### Install from the source
Release：[WeatherGod](https://github.com/matplotlib/basemap/releases/)
[百度網盤](https://pan.baidu.com/s/1q75hbCA0NHj6Bxfl_IDr7Q): 2tue

```bash
mkdir Basemap
cd Basmap
wget -c https://github.com/matplotlib/basemap/archive/v1.1.0.tar.gz
## ummmmm... 126m， 我下載的時候... 有點大， 優點慢， 自己想辦法把
## 給個百度雲鏈接把，我。 100kb，總比50kb的瀏覽器速度要好把
tar -zxvf basemap-1.1.0.tar.gz
cd basemap-1.1.0
cd geos-3.3.3
export GEOS_DIR=$(pwd)
./configure --prefix=$GEOS_DIR
make; make install
```

### 報錯
```
../../../include/geos/geom/Coordinate.inl:39:10: error: 'ISNAN' was not declared in this scope
  return (ISNAN(x) && ISNAN(y) && ISNAN(z));
```
解決： [VeRo](https://askubuntu.com/questions/465550/can-not-compile-without-isnan-function-or-macro-when-trying-to-compile-geos-on)
找到`platform.h`
把24行的`/* #undef HAVE_ISNAN */`
替換成： `#define HAVE_ISNAN 1` ("#"號不能丟)
我直接用sed替換了:
```bash
sed -i 's=/\* #undef HAVE_ISNAN \*/=#define HAVE_ISNAN 1=' ./include/geos/platform.h
```
`make` 要蠻久， 慢慢等把

`sudo make install` 以後， 退到上一級目錄
```bash
python setup.py install
```
又報錯：
```
src/_geoslib.c:5552:21: error: ‘PyThreadState {aka struct _ts}’ has no member named ‘exc_type’; did you mean ‘curexc_type’?
```
`sudo pip3.7  install cpython`

更具jonathanunderwood在[github帖子](https://github.com/mcfletch/pyopengl/issues/11)中的解釋， 是應爲python3.7不適配的原因。
我直接用python2.7安裝成功了。 不過，後面在導入包的時候，又有function問題- -我放棄了 嘿嘿嘿

還是用leaft把
