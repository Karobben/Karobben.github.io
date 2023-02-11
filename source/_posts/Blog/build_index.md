---
title: "How to build index in one line codes"
description: "How to build index in one line codes"
thumbnail: https://cdn.jsdelivr.net/gh/removeif/blog_image/img/2019/20190919221611.png
priority: 10000
cover: https://cdn.jsdelivr.net/gh/removeif/blog_image/img/2019/20190919221611.png
url: build_index
date: 2020/07/28
toc: true
excerpt: "就請忽略這個帖子把- -"
---

## How to build index in one line codes

```bash
ls | awk '{print "["$1"]("$i")"}'| sed 's/\.md]/]/;s/\.md)/\.html)/;/yuque.yml/d;/(summary.html)/d'  > Blog_index.md
```
