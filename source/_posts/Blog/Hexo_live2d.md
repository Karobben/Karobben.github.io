---
title: "Hexo: live2d"
description: "hexo live2d|給博客加一個板娘"
date: "2020-07-30"
url: hexo_live2d
toc: true
excerpt: "hexo live2d|給博客加一個板娘"
tags: [Hexo]
category: [others, Blog, Hexo]
cover: 'https://s1.ax1x.com/2020/07/30/amxSmQ.png'
thumbnail: 'https://s1.ax1x.com/2020/07/30/amxSmQ.png'
priority: 10000
covercopy: '© Karobben'
---
## Hexo: live2d


|![amxSmQ.png](https://s1.ax1x.com/2020/07/30/amxSmQ.png)|Project: [github EEEEEEYHN](https://github.com/EYHN/hexo-helper-live2d)<br>Models downloads: [github summerscar](https://github.com/summerscar/live2dDemo)|
|--|--|


## Install
install the widget at the hexo's directory of your blog
```bash
npm install --save hexo-helper-live2d
```

## Models

Make a directory for storing the models at your hexo's directory
```bash
mkdir live2d_models
## Downloads
git clone https://github.com/summerscar/live2dDemo
## Models
mv live2dDemo/assets/shizuku live2d_models/
```
Moving the models you like from `live2dDemo/assets/` (from git clone) to `live2d_models` (in your hexo's directory)
## Config
Add configuration in hexo's `_config.yml` file or theme's `_config.yml`.
(PS: I tried to add configuration at theme's `_config.yml` file first and it **didn't work** for me)

```bash
live2d:
  enable: true
  scriptFrom: local
  pluginRootPath: live2dw/
  pluginJsPath: lib/
  pluginModelPath: assets/
  tagMode: false
  log: false
  model:
    use: shizuku
  display:
    position: right #left
    width: 150
    height: 300
  mobile:
    show: true
  react:
    opacity: 0.7
```

## Final Result

![amxpwj.gif](https://s1.ax1x.com/2020/07/30/amxpwj.gif)
