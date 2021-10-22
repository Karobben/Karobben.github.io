---
toc: true
url: compouse_keys
covercopy: <a href="https://duncanlock.net/blog/2013/05/03/how-to-set-your-compose-key-on-xfce-xubuntu-lxde-linux/">© Duncan Lock</a>
priority: 10000
date: 2021-10-02 16:57:27
title: "Compose keys in Manjaro"
ytitle: "Manjaro 的 Compouse Manjaro"
description: ""
excerpt: "Frequent used Compose Key"
tags: [Blog, Manjaro]
category: [Linux, others]
cover: "https://duncanlock.net/images/posts/how-to-set-your-compose-key-on-xfce-xubuntu-linux/compose-key-diagram.png"
thumbnail: ""
---

## Show all keys

Show all able compose keys with command.
```bash
cat "/usr/share/X11/locale/$(grep --max-count=1 "${LANG%.*}.UTF-8\$" /usr/share/X11/locale/locale.dir | cut --delimiter=/ --fields 1)/Compose"
```

 ⫰
## Math

| keys | Result    |
| :------------- | :------------- |
| o o      | °       |
| o A | Å |
| > = | ≥ |
| < = | ≤ |
| x x | ×|
| > > | »|
| < < | «»|



## Direction
| keys | Result    |
| :- | :-- |
|< -| ←|
|\| ^| ↑|
|\| v| ↓|


# Others
| keys | Result    |
| :- | :-- |
| o c | © |
| o r | ® |
| = Y | ¥ |
| = E | € |


## Meme
| keys | Result    |
| :- | :-- |
| < 3       | ♥     |
