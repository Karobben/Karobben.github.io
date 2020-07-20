---
title: "How to build index in one line codes"
description: "How to build index in one line codes"
url: Build_index
---

# How to build index in one line codes

```bash
ls | awk '{print "["$1"]("$i")"}'| sed 's/\.md]/]/;s/\.md)/\.html)/;/yuque.yml/d;/(summary.html)/d'  > Blog_index.md
```

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
