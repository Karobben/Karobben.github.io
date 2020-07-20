---
title: "Hexo: Personalize Code Block"
url: hexo_code
date: "2020-07-1"
description: "hexo 個性化代碼塊; Mac-style Code Block"
toc: true
---
# Hexo: Personalize Code Block

Date: 1 July 2020

# Find the source code

css for code block is in `themes/landscape/source/css/_partial/highlight.styl`
So, you can personalize your code block by rewrite it.

For me, I want to create **deepin-terminal** style **cold block**

![Nrvy7D.png](https://s1.ax1x.com/2020/06/26/Nrvy7D.png)

By checking the source code, we can know that the code block is in a `<table>`
![N7YVxg.png](https://s1.ax1x.com/2020/07/01/N7YVxg.png)

So, if I want to add a guider bar as picture above, I need add an element before the tag `figure`.

Here is my example:
[source](https://karobben.github.io/Blog/Html.html)
```css
$code-block
  background: rgb(65, 65, 65)
  margin: 0 article-padding * -1
  padding: 15px article-padding
  border-style: solid
  border-color: color-border
  border-width: 1px 0
  overflow: auto
  color: highlight-foreground
  line-height: font-size * line-height
  font-family: monospace;
  font-size: 18px;
  border-radius: 0px 0px 0px 0px;
```

ummmm... I cant remember exactly what am I done, but I made it... Cheers!!!


---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
