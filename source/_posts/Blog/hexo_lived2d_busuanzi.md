---
title: "Hexo: Busuanzi doesn't work"
description: "<span id='busuanzi_container_site_uv' style='display: none;'>"
date: "2021-02-21"
url: hexo_live2d_busuanzi
toc: true
excerpt: "Sometimes, the busuanzi works, but sometimes it doesn't work. By checking the code, we can find that the script runs well but it was hidden for some reason."
tags: [Hexo, HTML]
category: [others, Blog, Hexo]
cover: 'https://s1.ax1x.com/2020/07/30/amxSmQ.png'
thumbnail: 'https://s1.ax1x.com/2020/07/30/amxSmQ.png'
priority: 10000
covercopy: '© Karobben'
---
## Hexo: Busuanzi doesn't work

[Github Issue](https://github.com/theme-next/hexo-theme-next/pull/1233#issuecomment-585576298)

Sometimes, the busuanzi works, but sometimes it doesn't work. By checking the code, we can find that the script runs well but it was hidden for some reason.
`<span id="busuanzi_container_site_uv" style="display: none;">`

BoyInTheSun gived a solution in [his blog](https://boyinthesun.cn/post/error-live2d-busuanzi/#!)
It works fine. So, I recorded it specifically for theme-icarus.

### Create a js file

For me, I created the script here: `themes/icarus/source/js/busuanzi.pure.js`

### Copy the script
Then, copy the code from [his blog](https://boyinthesun.cn/post/error-live2d-busuanzi/#!)
```js busuanzi.pure.js
var bszCaller,bszTag;!function(){var c,d,e,a=!1,b=[];ready=function(c){return a||"interactive"===document.readyState||"complete"===document.readyState?c.call(document):b.push(function(){return c.call(this)}),this},d=function(){for(var a=0,c=b.length;c>a;a++)b[a].apply(document);b=[]},e=function(){a||(a=!0,d.call(window),document.removeEventListener?document.removeEventListener("DOMContentLoaded",e,!1):document.attachEvent&&(document.detachEvent("onreadystatechange",e),window==window.top&&(clearInterval(c),c=null)))},document.addEventListener?document.addEventListener("DOMContentLoaded",e,!1):document.attachEvent&&(document.attachEvent("onreadystatechange",function(){/loaded|complete/.test(document.readyState)&&e()}),window==window.top&&(c=setInterval(function(){try{a||document.documentElement.doScroll("left")}catch(b){return}e()},5)))}(),bszCaller={fetch:function(a,b){var c="BusuanziCallback_"+Math.floor(1099511627776*Math.random());window[c]=this.evalCall(b),a=a.replace("=BusuanziCallback","="+c),scriptTag=document.createElement("SCRIPT"),scriptTag.type="text/javascript",scriptTag.defer=!0,scriptTag.src=a,document.getElementsByTagName("HEAD")[0].appendChild(scriptTag)},evalCall:function(a){return function(b){ready(function(){try{a(b),scriptTag.parentElement.removeChild(scriptTag)}catch(c){bszTag.hides()}})}}},bszCaller.fetch("//busuanzi.ibruce.info/busuanzi?jsonpCallback=BusuanziCallback",function(a){bszTag.texts(a),bszTag.shows()}),bszTag={bszs:["site_pv","page_pv","site_uv"],texts:function(a){this.bszs.map(function(b){var c=document.getElementById("busuanzi_value_"+b);c&&(c.innerHTML=a[b])})},hides:function(){this.bszs.map(function(a){var b=document.getElementById("busuanzi_container_"+a);b&&(b.style.display="")})},shows:function(){this.bszs.map(function(a){var b=document.getElementById("busuanzi_container_"+a);b&&(b.style.display="inline")})}};
```

### Finally, apply it in your theme

Before doing so, please make sure that you have ==disabled the busuanzi plugin== in your `_congig.icarus.yml`.

And then, insert the scripts appropriately.

For me, I inserted my codes by following [another post](https://karobben.github.io/2021/02/11/Blog/hexo_icarus/).

Now, find your code and replace the source from:
`<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>`
to:
`<script async src="/js/busuanzi.pure.js"></script>`

Now, everything is done!
Enjoy~
