---
url: hexo
---

# 如何优雅的白嫖博客服务

Date: 2020/6/14
[Main Tutorial](https://blog.csdn.net/muzilanlan/article/details/81542917)

原博客已经写的很清楚了， 这里我只记录一下我遇到的问题。


# 1. npm error
```bash
npm install -g hexo-cli
```
```bash
npm ERR! code EINTEGRITY
npm ERR! sha512-XlPzRtnsdrUfTSkLJPACQgWByybB56E79H8xIjGWj0GL+J/VqENsgc+GER0ytFwrP/6YKCerXdaUWOYMcv6aiA== integrity checksum failed when using sha512: wanted sha512-XlPzRtnsdrUfTSkLJPACQgWByybB56E79H8xIjGWj0GL+J/VqENsgc+GER0ytFwrP/6YKCerXdaUWOYMcv6aiA== but got sha512-BdyVintFFu5qQX0AtuwgmXxphBU1V+VL9+8GPemcM9Q86MPG+MCTA26bCyEyzUqDPVBm7xF3gjACaOwMBEmAZQ==. (653 bytes)

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/ken/.npm/_logs/2020-06-14T05_36_46_129Z-debug.log
```

**Solution:**
```bash
npm cache verify
npm install -g hexo-cli
```
reference: [天魂_TH](https://www.jianshu.com/p/2899bd2a0a20)

## 2. npm Download

```bash
npm config set registry https://registry.npm.taobao.org
```
reference: [慢读慢写](https://blog.csdn.net/ibmall/article/details/81390639)

## 3. Start the Service:
[![tztLw9.jpg](https://s1.ax1x.com/2020/06/14/tztLw9.jpg)](https://imgchr.com/i/tztLw9)

# 4 Director Structure

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

# New Category:

```bash
hexo new page categories
```
A new directory `categories` would be create in `source`


# Customize your theme
reference: [dxs雪松](https://www.cnblogs.com/d-xs/p/6891647.html)


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
