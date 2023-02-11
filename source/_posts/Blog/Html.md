---
title: "Html 杂记"
description: "Html 杂记"
date: 2020/01/22
url: fzzq2h
toc: true
excerpt: 'Basic grammars for HTML'
tags: [HTML]
category: [others, Blog, HTML]
cover: 'https://www.tutorialrepublic.com/lib/images/html-illustration.png'
thumbnail: 'https://s1.ax1x.com/2020/06/26/NrjbS1.png'
priority: 10000
---

## 1. 文字
```html
<!-- 颜色 -->
<p style="color:black;">文字</p>
<!-- 大小 -->
<p style="font-size:100px;">文字</p>
<!-- 加粗 400: normal, 700:bold-->
<p style="font-weight:700;">文字</p>
<!-- 行间距 -->
<p style="line-height:20px;">文字</p>
<!-- 换行 -->
<br>
<!-- 加粗 -->
<strong></strong>
<b></b>
<!-- 傾斜 -->
<i></i>
<!-- 下划线 -->
<u></u>
<!-- 右上角 -->
<sup></sup>
<!-- 右下角 -->
<sub></sub>
<!-- 穿越横线 -->
<s></s>
<strike></strike>
<!-- 强制不换行 -->
<nobr></nobr>
```

<a name="Iqend"></a>
### 1.1 标签横向排列

```html
<style>
##nav  li{ float:right; list-style: none;
   margin:10px; /*左右间隔*/
   padding"0; /*上下*/
  }
</style>

<ul id="nav-top";>
  <li>1</li> <li>2</li>
</ul>
```

<a name="C5HpP"></a>
## 2.图片
在img标签里面只设置宽，不设置高，图片就会等比例缩放。
```html
<!-- 等比例缩放 -->
<img src="/i/mouse.jpg" height="200">
<!-- 拉伸 -->
<img style="width:100%; height:100%;" src="2.jpg">
<!-- 旋转 -->
<img style="transform: rotate(90deg);" src="2.jpg">
```
复杂模块
<a name="fhYVv"></a>
### 2.1 图片点击放大
HTML 点击悬屏放大, 再点击退出。鼠标悬停有提示
```html
<div class="col-lg-4 col-md-6 col-xs-12 mix development print">
  <div class="portfolio-item">
    <div class="shot-item">
    <img src="Linkercare/Clients/总览/crop3.png" alt="" />  
    <div class="single-content">
      <div class="fancy-table">
        <div class="table-cell">
          <div class="zoom-icon">
          <a class="lightbox" href="Linkercare/Clients/总览/crop3.png"><i class="lni-zoom-in item-icon"></i></a>
          </div>
        <a href="#">View Project</a>
        </div>
      </div>
    </div>
  </div>               
</div>
```
JS 点击原地放大，并挤压其他图片/文字空间造成重排，再次点击恢复原来打小。鼠标悬停无提示
```html
<html>
    <head>
        <meta charset="utf-8" />
        <script type="text/javascript" src='jquery-1.8.0.js'></script>
    </head>
    <body>
        <img id="img1" src="11.jpg" style="width:100px;height:150px" alt="" />
    </body>
    <script type="text/javascript">
            $(function(){
                $("#img1").click(function(){
                    var width = $(this).width();
                    if(width==100)
                    {
                        $(this).width(200);
                        $(this).height(300);
                    }
                    else
                    {
                        $(this).width(100);
                        $(this).height(150);
                    }
                });
            });
    </script>
</html>
```

<a name="GdPN0"></a>
### 2.2 图片圆角
```html
<img style="border-radius:1000px;" src="Linkercare/Clients/总览/crop3.png" alt="" />
```
<a name="qE5dH"></a>
### 2.3 图片边框

```html
<img style="border:solid;">
```

<a name="rhYz5"></a>
## 3.超链接

```html
<!-- 页面内超链接 -->
<a href="#tips">Text</a>
<h1 id="h1anchor">标题一</h1>

<!--在新的标签打开本链接-->
<a href='test.html' target="_blank" >链接文字</a>
```

<a name="nEqgY"></a>
## 4.插入别的页面

```html
<iframe name="myiframe" id="myrame" src="test.html"  width="1100" height="600"></iframe>
<!-- 额外参数 -->
<iframe frameborder="0" align="left" width="200" height="200" scrolling="no">


```


<a name="cXPrD"></a>
## 5.Table
```html
<table>
  <tr><th>title1</th><th>title2</th><tr>
  <tr><td><img src=test1.jpg border=0></td><td><img src=test2.jpg border=0></td></tr></table>
<!-- table可以并列很多东西 -->

<!--加背景色-->
<table bgcolor=#rrggbb></table>

<tr height='100px'></tr>

/*边框:http://blog.sina.com.cn/s/blog_6721f25c0101e0l8.html */
<table lign="center" frame=below rules=rows border="1"
       cellpadding="2" cellspacing="0">



```

<a name="MbaiS"></a>
## 6 菜单
<a name="QZjbF"></a>
### 6.1 下拉菜单
<a name="7qpeO"></a>
#### a. JS
```html
<!--来源:https://zhidao.baidu.com/question/1110427647137965899.html -->
<html>
  <head>
     <style>*{margin:0;padding:0;} ul,li
       { list-style-type:none; padding:0; margin:0; } #nav li a
       { display:block; width:40px; text-align:center; text-decoration:none; color:#ffffff; background-color:#3ee27d; } #nav li
      { position:relative; margin-bottom:2px;float:left;margin-right:0px; } #nav li ul
      { position:absolute; left:10px; top:30px; display:none;width:100px; } #nav li:hover ul
      { display:block; }
     </style>
</head>
<body>
 <ul id="nav">
   <li>
    <a href="#">首页</a>
   </li>
   <li>
    <a href="#">关于我们</a>
    <ul>
      <li>我们的故事</li>
      <li>我们的团队</li>
    </ul>
   </li>
   <li>
    <a href="#">我们的服务</a>
    <ul>
      <li>网页设计</li>
      <li>页面制作</li>
      <li>程序开发</li>
    </ul>
   </li>
   <li>
    <a href="#">联系我们</a>
    <ul>
      <li>团队主力</li>
      <li>团队成员</li>
    </ul>
   </li>
   </ul>
</body>
</html>
```

效果：
![Nrv2hd.gif](https://s1.ax1x.com/2020/06/26/Nrv2hd.gif)







<a name="nOJaB"></a>
#### b. HTML

```html
<!--来源:https://www.php.cn/div-tutorial-412558.html-->
<!DOCTYPE html>

<html>

<head>

<style>

.dropbtn {

    background-color: black;

    color: white;

    padding: #px;

    font-size: #px;

    border: none;

}

.dropdown {

    position: relative;

    display: inline-block;

}

.dropdown-content {

    display: none;

    position: absolute;

    background-color: lightgrey;

    min-width: #px;

    z-index: 1;

}

.dropdown-content a {

    color: black;

    padding: #px #px;

    text-decoration: none;

    display: block;

}

.dropdown-content a:hover {background-color: white;}

.dropdown:hover .dropdown-content {display: block;}

.dropdown:hover .dropbtn {background-color: grey;}

</style>

</head>

<body>

<div class="dropdown">

<button class="dropbtn">Name</button>

<div class="dropdown-content">

<a href="http://www.php.cn/">Name</a>

<a href="http://www.php.cn/">Name</a>

<a href="http://www.php.cn/">Name</a>

</div>

</div>

</body>

</html>
```

效果：
![NrvcAe.gif](https://s1.ax1x.com/2020/06/26/NrvcAe.gif)
<a name="6iPpw"></a>
## 7.杂记
<a name="S01tI"></a>
### 7.1 align

```html
<img align="left" src="/i/mouse.jpg" height="200">
```

| **值** | **描述** |
| --- | --- |
| left | 左对齐内容。 |
| right | 右对齐内容。 |
| center | 居中对齐内容。 |
| justify | 对行进行伸展，这样每行都可以有相等的长度（就像在报纸和杂志中）。 |


<a name="PtUiR"></a>
### 7.2 Span
```html
<div style="position: relative; width: 170px; height: 89px;">
<img src="loading.gif" width="170" height="89" alt="">
<span style="position: absolute; top: 0; left: 0;">添加文字...添加文字...添加文字...</span>
</div>
```

<a name="iGIa1"></a>
### 7.3 Coding Bar
source:[https://www.bootcdn.cn/highlight.js/](https://www.bootcdn.cn/highlight.js/)
```html
<link href="https://cdn.bootcss.com/highlight.js/9.15.10/styles/a11y-dark.min.css" rel="stylesheet">  
<script async src="https://cdn.bootcss.com/highlight.js/9.15.10/highlight.min.js"></script>  
<script  >hljs.initHighlightingOnLoad();</script>  

<code class="lang-javascript">
for(ii in 1:ncol(a)){
a[,ii][which(a[,ii]>0)] <- log(a[,ii][which(a[,ii]>0)],10)/log(max(a[,ii]),10)
a[,ii][which(a[,ii]<0)] <- log(a[,ii][which(a[,ii]<0)](-1),10)(-1)/log(mean(a[,ii]) *(-1))
}
</code>
```

效果:
![Nrvs0O.png](https://s1.ax1x.com/2020/06/26/Nrvs0O.png)


<a name="l9BRm"></a>
#### 7.32 Terminal
```css
.Terminal{
  max-width: 900px;
  background-color: black;
  color: #ffffff;
  padding-left: 10px;
  font-size: large;
  font-size: 20px;
  font-family: monospace;
  border-radius: 5px 5px 0px 0px;
}

.code{
  max-width:  900px;
  background-color: rgb(65, 65, 65);
  color: rgb(0, 205, 0);
  padding-left: 20px;
  font-family: monospace;
  font-size: 18px;
  border-radius: 0px 0px 10px 10px;
}
```

```html
<div class="Terminal">
  <img src="../Home/img/Terminal.png" height="30px">
  Terminal
  <img src="../Home/img/Terminal2.png" height="30px" align='right' img src="../Home/img/Terminal2.png" height="30px" align='right' style="padding-right:5px;">
</div>
<pre class='code'>
<code class="lang-javascript">
### Generated by deepin-installer
deb [by-hash=force] http://ftp.sjtu.edu.cn/deepin panda main contrib non-free
##deb-src http://ftp.sjtu.edu.cn/deepin panda main contrib non-free
</code>
</pre>
```

效果：
![Nrvy7D.png](https://s1.ax1x.com/2020/06/26/Nrvy7D.png)

图片元素:![NrvW9A.png](https://s1.ax1x.com/2020/06/26/NrvW9A.png) ![NrxYKP.png](https://s1.ax1x.com/2020/06/26/NrxYKP.png)


<a name="JtSw6"></a>
### 7.4 鼠标悬停显示文字

```html
<a href="javascript;" title="悬停的文字">将鼠标移到这个标签上，就会显示"悬停的文字"</a>
```

![NrvgtH.gif](https://s1.ax1x.com/2020/06/26/NrvgtH.gif)

<a name="AxwZt"></a>
### 7.5 每秒刷新一次

```html
<head>
  <meta http-equiv="refresh" content="1">
</head>
```

方便排版的时候预览界面

<a name="iG0aK"></a>
### 7.6 实时预览
VS 插件： Live Server[^TianXinCoord_2018]
亲测有效

[^TianXinCoord_2018]: TianXinCoord; 2018; CSDN; VSCode设置网页代码实时预览.[link](https://blog.csdn.net/sinat_34104446/article/details/83051052)

### 7.7 统计访问量
不蒜子：[http://busuanzi.ibruce.info/](http://busuanzi.ibruce.info/)

```html
<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>
<span id="busuanzi_container_site_pv">本站总访问量<span id="busuanzi_value_site_pv"></span>次</span>
```

<a name="sxLdt"></a>
### 7.8 免除loft影响, 重开一行

```html
div style="clear:both;"></div>
```
### 隐藏内容
```html
<details>
  <summary><span style="font-size:20px"> 请点击我!!</span> </summary>
  我就在这里!!!
</details>
```
<details>
  <summary><span style="font-size:20px"> 请点击我!!</span> </summary>
  我就在这里!!!
</details>
