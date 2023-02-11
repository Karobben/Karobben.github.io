---
title: "Hexo Weather Widget"
url: hexo_weather
date: "2020-06-20"
description: "Weather Widget for Hexo"
toc: true
excerpt: "Weather Widget for Hexo"
tags: [Hexo, Hexo Plugin, HTML]
category: [others, Blog, Hexo]
cover: 'https://i.loli.net/2020/06/20/iV6W8P31bIDCYqv.png'
thumbnail: "https://blog.kritner.com/2019/03/19/Hexo-local-configuration/hexo-logo-avatar.png"
priority: 10000
covercopy: © Karobben
---
## 1min Hexo 博客添加天氣插件

Date: 20 June 2020
Reference: [cungudafa](https://blog.csdn.net/cungudafa/article/details/104312892)

## 代碼獲取

進入[中國天氣官網](https://cj.weather.com.cn)，免費登錄後就可以直接獲取代碼,(可用微信，QQ等三方登錄): `https://cj.weather.com.cn/plugin/pc`
頁面如下，支持半個性化定製:
![DeepinScreenshot_select-area_20200620184308](https://i.loli.net/2020/06/20/lzYDUXoNb1erqRB.png)

## 代碼插入

我的是默認landscape主題，我選擇自己寫個小文件，然後導入。

複製代碼後， 寫入了 `themes/landscape/layout/_partial/Weather.ejs`文件。
之後在`themes/landscape/layout/layout.ejs`文件中，插入位置如下。
```html
<% if (theme.sidebar && theme.sidebar !== 'bottom'){ %>
  <%- partial('_partial/sidebar', null, {cache: !config.relative_link}) %>
  <!-- Weather Plug-->
  <%- partial('_partial/Weather', null, {cache: !config.relative_link}) %>
<% } %>
```
小調一下位置， 最終顯示結果：
![DeepinScreenshot_select-area_20200620185110](https://i.loli.net/2020/06/20/iV6W8P31bIDCYqv.png)
