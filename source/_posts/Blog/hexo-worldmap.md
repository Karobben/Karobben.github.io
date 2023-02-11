---
toc: true
url: hexo_worldmap
covercopy: © Revolvermaps
priority: 10000
date: 2021-03-22 10:26:50
title: "Hexo: Visitor traffic map|Revolvermaps, clustrmaps, maploco| Static Blog"
description: "A real-time visitor statistic map widget or visitor traffic map widget is a script that could show the visitor records on the maps."
excerpt: "A real-time visitor statistic map widget or visitor traffic map widget is a script that could show the visitor records on the maps. It is fun to see that you remain a trace on the site or notice that someone is visiting this site with you at the same time. For the owner, it could greatly gain a sense of achievement by watching this map and promoting their motivation to update. For static web-pages/blogs, there are few but awesome free-services we can use to decorate our pages."
tags: [Hexo, Hexo Plugin]
category: [others, Blog, Hexo]
cover: "http://rf.revolvermaps.com/h/m/a/3/ff0000/256/0/5obi4wthjqz.png"
thumbnail: "http://rf.revolvermaps.com/h/m/a/3/ff0000/60/0/5oxb03w3827.png"
---

A real-time visitor statistic map widget or visitor traffic map widget is a script that could show the visitor records on the maps. It is fun to see that you remain a trace on the site or notice that someone is visiting this site with you at the same time. For the owner, it could greatly gain a sense of achievement by watching this map and promoting their motivation to update. For static web-pages/blogs, there are few but awesome free-services we can use to decorate our pages.

Please visit JNingWei[^JNingWei_2017] to see more!

[^JNingWei_2017]: [JNingWei, 2017: 利用 visitor map (访客地图) 统计网站访客](https://blog.csdn.net/JNingWei/article/details/78897441))

## [clustrmaps](https://clustrmaps.com/)

Where to git the widget: [links](https://clustrmaps.com/add)
- [x] Customize

It is highly customizable and beautiful. But it runs a little bit slower than I expected.

Effects:

`<script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=-i1RAbH-h9aHEmWoLwPcQ5wyiILjE5GhqB9gLn_MTlQ&cl=ffffff&w=a"></script>`

2D map:
<a href="https://clustrmaps.com/site/1bgwc"  title="Visit tracker"><img src="//www.clustrmaps.com/map_v2.png?d=-i1RAbH-h9aHEmWoLwPcQ5wyiILjE5GhqB9gLn_MTlQ&cl=ffffff" /></a>

3D Globe:

<script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=-i1RAbH-h9aHEmWoLwPcQ5wyiILjE5GhqB9gLn_MTlQ"></script>

## [maploco](https://www.maploco.com/)

This is the easiest one to create. But it seems you can't customize it
<a href="https://m.maploco.com/details/29a60k8d"><img style="border:0px;" src="https://www.maploco.com/vmap/10103917.png" alt="Locations of Site Visitors" title="Locations of Site Visitors"/></a>

## [Revolvermaps](https://www.revolvermaps.com/)
- [x] Customize

Revolvermaps is one of the most popular visitor traffic maps among them since I saw them so frequently.

It can not only show 2D maps but also a 3D globe is supportable.

<script type="text/javascript" src="//rf.revolvermaps.com/0/0/6.js?i=5obi4wthjqz&amp;m=7&amp;c=e63100&amp;cr1=ffffff&amp;f=arial&amp;l=0&amp;bv=90&amp;lx=-420&amp;ly=420&amp;hi=20&amp;he=7&amp;hc=a8ddff&amp;rs=80" async="async"></script>



<script type="text/javascript" src="//rf.revolvermaps.com/0/0/7.js?i=5obi4wthjqz&amp;m=0c&amp;c=f03b11&amp;cr1=ffffff&amp;sx=0&amp;cw=ffffff&amp;cb=3472cd" async="async"></script>

One thing that **bothered** me a lot was that I **failed to customize** it when I inserted it below my profile widget. I thought it was the fault of the revolvermaps. But I find that it works fine when it is present in the post. That means the JS in the profile widget doesn't work appropriately. By comparing the source of the JS between profile and widget:

There are slight differences between them

**Source in Profile**:
`//rf.revolvermaps.com/w/7/a/a2.php?i=5obi4wthjqz&amp;m=0c&amp;c=f03b11&amp;cr1=ffffff&amp;sx=0&amp;cw=ffffff&amp;cb=3472cd`
**Source in Posrt**:
`//rf.revolvermaps.com/w/7/a/a2.php?i=5obi4wthjqz&m=0c&c=f03b11&cr1=ffffff&sx=0&cw=ffffff&cb=3472cd`

**The raw source is** `//rf.revolvermaps.com/0/0/7.js?i=5obi4wthjqz&amp;m=0c&amp;c=f03b11&amp;cr1=ffffff&amp;sx=0&amp;cw=ffffff&amp;cb=3472cd`

So, I **altered** it as `//rf.revolvermaps.com/0/0/7.js?i=5obi4wthjqz&m=0c&c=f03b11&cr1=ffffff&sx=0&cw=ffffff&cb=3472cd`

And them, boon!! It works fine, now! Enjoy~
