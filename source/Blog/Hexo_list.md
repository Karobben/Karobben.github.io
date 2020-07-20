---
title: "Hexo 正文部分的編號消失"
url: hexo_list
date: "2020-06-24"
description: "hexo 正文的list編號，標籤，消失問題"
toc: true
---
# Hexo 正文部分列表編號消失

Date: 24 June 2020

在atom本地插件中， 看起來是這樣的， 有序號的話， 看起來比較有條理。

[![NaLp4O.png](https://s1.ax1x.com/2020/06/24/NaLp4O.png)](https://imgchr.com/i/NaLp4O)

hexo 以後， 就不對勁了， 序號都消失了， 問題是還，到處都找不到攻略， 似乎就我一個人有這樣的問題
[![NaLSUK.png](https://s1.ax1x.com/2020/06/24/NaLSUK.png)](https://imgchr.com/i/NaLSUK)

查看控制檯，可以發現， 明明是`<li>`， 但是卻沒有li的**圓點**標誌，所以肯定是css設置了什麼。
最後在`themes/landscape/source/css/_partial/archive.styl`中找到了:

```css
li
    list-style-type:none;
```

刪掉以後，才發現 = =這個代碼， 是我自己加的。。。
當時做title的時候，發現前面有個小點， 就直接加了個全局 - -
在前面加上 title 的標籤後， 就一切正常了。 唉- -哭了

[![NaqzE6.png](https://s1.ax1x.com/2020/06/24/NaqzE6.png)](https://imgchr.com/i/NaqzE6)

```css
.title_index li
    list-style-type:none;
```





---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
