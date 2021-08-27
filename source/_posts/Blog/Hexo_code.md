---
title: "Hexo: Personalize Code Block"
url: hexo_code
date: 2020/07/01
description: "hexo 個性化代碼塊; Mac-style Code Block"
toc: true
excerpt: "Hexo: Personalize Code Block in landscape-theme"
tags: [Hexo, HTML]
category: [others, Blog, Hexo]
cover: 'https://s1.ax1x.com/2020/06/26/Nrvy7D.png'
thumbnail: "https://blog.kritner.com/2019/03/19/Hexo-local-configuration/hexo-logo-avatar.png"
priority: 10000
covercopy: '© Karobben'
---
## Hexo: Personalize Code Block

Date: 1 July 2020

## Find the source code

css for code block is in `themes/landscape/source/css/_partial/highlight.styl`
So, you can personalize your code block by rewrite it.

For me, I want to create **deepin-terminal** style **cold block**

![Nrvy7D.png](https://s1.ax1x.com/2020/06/26/Nrvy7D.png)

By checking the source code, we can know that the code block is in a `<table>`
![N7YVxg.png](https://s1.ax1x.com/2020/07/01/N7YVxg.png)

So, if I want to add a guider bar as picture above, I need add an element before the tag `figure`.

Here is my example:
[source](https://karobben.github.io/2020/01/22/Blog/Html)

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

## Mac style Code Block

Reference: [马猴小站](https://violetwsh.com/2020/05/01/MacPanel/)

I tried to following with this tutorial from the link above and found it didn't work. So, I gave it up to recording the changes I made.

But soon, I found that it works only on the new pages I created.

So, I deleted all `md` posts after bake up and copied them to the `source` directory. After I ran `hexo g`, it worked, all pages got new style cold-blocks. But the problem is I totally forgot which changes I made. = =


This is the part of change I can remember:

**CSS file**:
```css
.highlight-wrap[data-rel] {
  position: relative;
  overflow: hidden;
  border-radius: 5px;
/*box-shadow: 0 10px 30px 0px rgba(0, 0, 0, 0.4);*/
  -webkit-box-shadow: 18px 18px 15px 0px rgba(0,0,0,0.4);
  /*Shadow of the code block*/
  box-shadow: 5px 5px 15px 0px rgba(0,0,0,0.4);
  margin: 35px 0;
  margin-top: 10px;
  margin-bottom: 25px;
}
.highlight-wrap[data-rel] ::-webkit-scrollbar {
  height: 10px;
}
.highlight-wrap[data-rel] ::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
  border-radius: 10px;
}
.highlight-wrap[data-rel] ::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.5);
}
.highlight-wrap[data-rel]::before {
  content: attr(data-rel);
  height: 38px;
  line-height: 38px;
  background: #21252b;
/*background: #108414de;*/
  color: #fff;
  font-size: 16px;
/*position: absolute;*/
  top: 0;
  left: 0;
  width: 100%;
/*font-family: 'Source Sans Pro', sans-serif;*/
  font-weight: bold;
  padding: 0px 80px;
  text-indent: 15px;
  float: left;
}
.highlight-wrap[data-rel]::after {
  content: ' ';
  position: absolute;
  -webkit-border-radius: 50%;
  border-radius: 50%;
  background: #fc625d;
  width: 12px;
  height: 12px;
  top: 0;
  left: 20px;
  margin-top: 13px;
  -webkit-box-shadow: 20px 0px #fdbc40, 40px 0px #35cd4b;
  -webkit-box-shadow: 20px 0px #fdbc40, 40px 0px #35cd4b;
  box-shadow: 20px 0px #fdbc40, 40px 0px #35cd4b;
  z-index: 3;
}
```
