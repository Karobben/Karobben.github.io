---
title: "Atom"
description: "Atom"
url: atom2
date: 2020/06/26
toc: true
excerpt: "Atom install, packages install. Some awesome packages for atom"
tags: [Linux]
category: [Linux, Software]
cover: 'https://s1.ax1x.com/2020/06/26/NsA2lD.png'
thumbnail: 'https://s1.ax1x.com/2020/06/26/NsA2lD.png'
priority: 10000
---

## Atom

System： Deepin 15.11Atom    : 1.41.0<br />Electron: 4.2.7<br />Chrome  : 69.0.3497.128<br />Node    : 10.11.0

<a name="4LN4y"></a>
## 安装插件

ctrl + ， 打开设置
![NsA2lD.png](https://s1.ax1x.com/2020/06/26/NsA2lD.png)

<a name="rJPAR"></a>
## 1 预览Markdonw


ctrl + shift + m
![NsAgSO.jpg](https://s1.ax1x.com/2020/06/26/NsAgSO.jpg)


效果还是感人的～！！

<a name="jzoHj"></a>
## 2 预览html

下载并安装
```bash
git clone https://github.com/harmsk/atom-html-preview.git

cd atom-html-preview/
apm install
```


Ctrl + Shift + H<br />（我没成功）

<a name="GjTh6"></a>
## 3 自动补全文件路径

```bash
git://www.github.com/atom-community/autocomplete-paths.git

cd autocomplete-paths
##apm install
npm install
## 直接使用 apm install 可能會缺少插件導致， 安裝成功卻無法使用，
## 而 npm Install 會有報錯
```

`npm install` 報錯：
```bash
npm WARN worker-loader@0.8.1 requires a peer of webpack@>=0.9 <2 || ^2.1.0-beta || ^2.2.0 but none is installed. You must install peer dependencies yourself.

audited 53 packages in 1.756s
found 3 vulnerabilities (2 moderate, 1 high)
  run `npm audit fix` to fix them, or `npm audit` for details
```
解決：
```bash
npm install npm WARN worker-loader@0.8.1 requires a peer of webpack@>=0.9 <2 || ^2.1.0-beta || ^2.2.0 but none is installed. You must install peer dependencies yourself.

audited 53 packages in 1.756s
found 3 vulnerabilities (2 moderate, 1 high)
  run `npm audit fix` to fix them, or `npm audit` for details

```
说实话 - -我安装了- -但是没看出什么效果来- -

<a name="ePp9Z"></a>
## 其他
### 插件網頁下載：
https://atom.io/packages
### 更多博客：
Location：https://www.cnblogs.com/GarfieldEr007/p/5594700.html
更多插件:
- language-r (R 语言语法高亮)
- minimap (VS 一样小图预览)
- atom-beautify (高亮美化)
- emmet (emmet是HTML,CSS快速编写的神器,具体的使用可以参看emmet官网。)
- autocomplete-* 系列 (自动补全)
- pigments (显示颜色)
https://blog.csdn.net/qq_32340877/article/details/79095610
- script (run different kinds of scripts in atom)



## high CPU Usage

Reference: 1. [Fantashit](https://fantashit.com/atom-helper-using-100-of-cpu/)
