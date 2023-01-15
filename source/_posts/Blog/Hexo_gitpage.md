---
title: "Hexo with Github"
date: "2020-06-14"
description: "Start with Hexo"
url: hexo
toc: true
excerpt: "place your hexo in gitpage"
tags: [Hexo, GitPage]
category: [others, Blog, Hexo]
cover: "https://lunarscents.github.io/images/hexo.jpg"
thumbnail: "https://blog.kritner.com/2019/03/19/Hexo-local-configuration/hexo-logo-avatar.png"
priority: 10000
covercopy: © lunarscents
---


## 如何优雅的白嫖博客服务 (hexo + github)

Date: 2020/6/14
[Main Tutorial](https://blog.csdn.net/muzilanlan/article/details/81542917)

原博客已经写的很清楚了， 这里我简单开始创建文件夹, 然后记录一下我遇到的问题。


## Quick to build a hexo folder
Before doing that, make sure the version of nodejs:
```bash
node -v
```
<pre>
v18.8.0
</pre>
If the version is below 16, please upgrade it.
[Brian Boucheron, 2020: Upgrade Node.js](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04)
```bash
wget https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh
bash install.sh
source ~/.bashrc
nvm list-remote
nvm install v18.8.0
```

```bash
sudo apt install npm

hexo init hexo
cd hexo
npm install node
#npm install -g hexo-cli
npm install
```

## npm error
```bash
npm install -g hexo-cli
```
<pre>
npm ERR! code EINTEGRITY
npm ERR! sha512-XlPzRtnsdrUfTSkLJPACQgWByybB56E79H8xIjGWj0GL+J/VqENsgc+GER0ytFwrP/6YKCerXdaUWOYMcv6aiA== integrity checksum failed when using sha512: wanted sha512-XlPzRtnsdrUfTSkLJPACQgWByybB56E79H8xIjGWj0GL+J/VqENsgc+GER0ytFwrP/6YKCerXdaUWOYMcv6aiA== but got sha512-BdyVintFFu5qQX0AtuwgmXxphBU1V+VL9+8GPemcM9Q86MPG+MCTA26bCyEyzUqDPVBm7xF3gjACaOwMBEmAZQ==. (653 bytes)

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/ken/.npm/_logs/2020-06-14T05_36_46_129Z-debug.log
</pre>

**Solution:**
```bash
npm cache verify
npm install -g hexo-cli
```
reference: [天魂_TH 2017](https://www.jianshu.com/p/2899bd2a0a20)

## 2. npm Download

Change the mirror if you in China
```bash
npm config set registry https://registry.npm.taobao.org
```
reference: [慢读慢写 2018](https://blog.csdn.net/ibmall/article/details/81390639)

## 3. Start the Service:
![tztLw9.jpg](https://s1.ax1x.com/2020/06/14/tztLw9.jpg)

## 4. Director Structure

```bash
.
├── 1
├── _config.yml
├── db.json
├── node_modules
├── package.json
├── package-lock.json
├── public
├── scaffolds
├── source
└── themes
```

After you run `hexo g`, all `.md` files in `source` directory would be turned to `html` files and stored at `publish` directory which you can upload to GitHub.

the home page `public/index.html` is stored at `source/_posts/hello-world.md`.

## 5. Plunges

### flow and mermaid support
reference: [慧行说 2018](https://www.liuyude.com/How_to_make_your_HEXO_blog_support_handwriting_flowchart.html)

```bash
npm install --save hexo-filter-flowchart
npm install --save hexo-filter-mermaid-diagrams
npm install --save hexo-filter-sequence
npm install hexo-renderer-pug hexo-renderer-stylus
```
If you have any trouble with **mermaid**, please went to see: [荒野之萍 2019](https://blog.csdn.net/qq_36347375/article/details/90478335)

### RSS feed
reference: [試毅_思伟 2019](https://www.jianshu.com/p/2aaac7a19736)
```bash
npm install hexo-generator-feed
```
`_config.yml`

```bash
## Extensions
plugins:
  hexo-generator-feed
##Feed Atom
feed:
  type: atom
  path: atom.xml
  limit: 20
```

### Word count
reference: [李瑞豪 2018](https://lruihao.cn/posts/hexo-wordcount.html)
```bash
npm i --save hexo-wordcount
```

Other tutorials:[IT自学不成才 2019](https://cloud.tencent.com/developer/article/1381382)

### Comments

utterances: [LitStronger 2020](https://litstronger.github.io/2020/04/03/hexo-fluid%E6%B7%BB%E5%8A%A0utterances%E8%AF%84%E8%AE%BA%E5%8A%9F%E8%83%BD/#)
## 6. New Category:

```bash
hexo new page categories
```
A new directory `categories` would be create in `source`


## Customize your theme
reference: [dxs雪松 2017](https://www.cnblogs.com/d-xs/p/6891647.html)


```bash
~/hexofolder$ tree -L 1 themes/landscape/
```
```
themes/landscape/
├── _config.yml
├── Gruntfile.js
├── languages
├── layout
├── LICENSE
├── package.json
├── README.md
├── scripts
└── source
```

## Adding head index

reference: [锦瑟华年 2015](http://kuangqi.me/tricks/enable-table-of-contents-on-hexo/)

Insert the codes below after `<%- post.content %>` in the file `themes/landscape/layout/_partial/article.ejs`
```html
<!-- Table of Contents -->
<% if (!index){ %>
  <div id="toc" class="toc-article">
    <strong class="toc-title">文章目录</strong>
    <%- toc(post.content) %>
  </div>
<% } %>
```

Adding codes below at `themes/landscape/source/css/_partial/article.styl`
```css
/*toc*/
.toc-article
  z-index:999;
  background: #eee;
  border: 1px solid #bbb;
  border-radius: 10px;
  margin: 1.5em 0 0.3em 1.5em;
  padding: 0em 1em 0 1em;
  max-width: 400px;
  max-height: 500px;
  overflow: auto

.toc-title
  font-size: 120%;

##toc
  line-height: 1em;
  font-size: 0.9em;
  padding-top: 10px;
  float: right
.toc
  padding-top: 10px;
  margin: 1em;
  line-height: 1.8em;
.toc-child
  margin-left: 1em

.title_index li
    list-style-type:none;

##nav
  display:block;
  background: salmon;
  border: 1px solid #bbb;
  border-radius: 100px;
  max-width: 100%;

##nav li a
    display:block;
    max-width: 100%;

##nav li ul
    position: fixed;
    right: 0;
    bottom:5%;
    display:none;
    width:80%;

##nav li:hover ul
    display:block;
```

## final style.css file
```css
/* -2.5 Scroll To Up */
.back-to-top {
  position: fixed;
  bottom: 10px;
  right: 10px;
  border-radius:1000px
}

.back-to-top i {
  display: block;
  width: 36px;
  height: 36px;
  line-height: 36px;
  color: #fff;
  font-size: 14px;
  text-align: center;
  border-radius: 30px;
  background-color: #F97794;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
}

.title_index {
  position: fixed;
  z-index:999;
  bottom: 40px;
  right: -9px;
}

/*toc*/
.toc-article {
  background: #eee;
  border: 1px solid #bbb;
  border-radius: 10px;
  margin: 1.5em 0 0.3em 1.5em;
  padding: 0em 1em 0 1em;
  max-width: 400px;
  max-height: 500px;
  overflow: auto
}
.toc-title {
  font-size: 120%
}

##toc {
  padding-top: 10px;
  line-height: 1em;
  font-size: 0.9em;
  float: right
}
.toc{
  padding-top: 10px;
  margin: 1em;
  line-height: 1.8em;
}
.toc-child {
  margin-left: 1em
}
.title_index li {
    list-style-type:none;
}


##nav {
  display:block;
  z-index: 10;
  background: salmon;
  border: 1px solid #bbb;
  border-radius: 100px;
  max-width: 100%;
}
##nav li a {
    display: block;
    max-width: 100%;
}
##nav li ul {
    position: fixed;
    right: 0;
    bottom:5%;
    display:none;
    width:80%;
}
##nav li:hover ul {
    display:block;
}
```
最终效果:

![NrbUf0.png](https://s1.ax1x.com/2020/06/26/NrbUf0.png)

http://kuangqi.me/tricks/enable-table-of-contents-on-hexo/
