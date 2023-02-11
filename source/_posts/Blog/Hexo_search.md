---
title: "Hexo: local search"
date: "2020-06-23"
description: "hexo 博客搭建站、安裝內搜索"
url: hexo_saerch
toc: true
excerpt: "hexo 博客搭建站、安裝內搜索"
tags: [Hexo, Hexo Plugin, HTML]
category: [others, Blog, Hexo]
cover: "https://lunarscents.github.io/images/hexo.jpg"
thumbnail: "https://blog.kritner.com/2019/03/19/Hexo-local-configuration/hexo-logo-avatar.png"
priority: 10000
covercopy: © lunarscents
---

## Local search for hexo blog


hexo 配置本地搜索

<span styl='back-ground:salmon'>注意:</span>
Main Tutorial: [梦中程序员
](https://www.jianshu.com/p/436faaf55ae9)

1. 進入博客根目錄， 然後下載插件
```bash
npm isntall hexo-generator-search --save
```

2. 下載配置文件
```bash
git clone https://gitee.com/sjclub/hexo-search-plugin.git
```

3. 部署配置文件
複製`js`腳本到主題的`source/js/`目錄下
```bash
cp hexo-search-plugin/plugin/*.js themes/landscape/source/js/
```
並添加入配置中。 我的例子：
編輯 `themes/landscape/layout/_partial/after-footer.ejs`
在最後行加入
```html
<!-- Searche Module-->
<script src="<%- config.root %>js/search.js"></script>
<script src="<%- config.root %>js/load.js"></script>
```

4. 把`search.styl`放到主题下的source文件夹下的css目录下
```bash
cp hexo-search-plugin/plugin/search.styl themes/landscape/source/css
```
插入`styl`
在`themes/landscape/layout/_partial/head.ejs`文件的`  <%- css('css/style') %>`後面， 加上
```bash
<%- css('css/search') %>
```

5. 插入`search.ejs`

這樣就就能看見了

6. 最後配置 config
6.1 更目錄 `_config.yml`
```bash
search:
    path: search.xml
    field: post
    content: true
```
6.2 主題下的 `_config.yml`
```bash
local_search:
    enable: true  #搜索开关
    location: "right: 50px;top: 30px;" #搜索框位置top/left/bottom/right
    facade: ""  #搜索框样式
```

7. `hexo g` 就可以了看見了
`public` 下多了一個 `search.xml`。 這個就是搜索的文件了。
不過，我在 `hexo s -g`的狀態下， 搜索是無效的。
上傳了以後， 反而可以了。 23333

上一張效果圖, 搜個函數試試～
![NNvrY8.png](https://s1.ax1x.com/2020/06/23/NNvrY8.png)

## **最后**
直接使用的話，移動版網頁是無法使用這個功能的。 猜測應該是， 作者認爲在手小屏幕的情況下彈出這個框太醜了， 所以就關掉了。
如果想要打開這個功能， 只需要在 `load.js`中的21行，
`if ($('.local-search').size() && !isMobile.any()) {`
把`&& !isMobile.any()`刪除， 手機端就也能正常使用了！
