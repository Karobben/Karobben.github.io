---
toc: true
url: compouse_keys
covercopy: <a href="https://duncanlock.net/blog/2013/05/03/how-to-set-your-compose-key-on-xfce-xubuntu-lxde-linux/">© Duncan Lock</a>
priority: 10000
date: 2021-10-02 16:57:27
title: "Compose keys in Linux"
ytitle: "Manjaro 的 Compouse Manjaro"
description: "Compose keys in Linux"
excerpt: "Compose keys are a feature in Linux and other operating systems that allows users to input special characters and symbols by typing a specific combination of keystrokes. This is useful for typing characters that may not be available on a standard keyboard, such as accents or diacritical marks. <a title='GhatGPT'>Who said this?</a>"
tags: [Linux, System]
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


## Customize Compouse key

In default profile, the Greek alphabet is like `<dead_greek> <a>`. But normally, we do not have this thing in our keyboard.

As a result, I changed it to `g+g+a`

This is how I change all `<dead_greek>`
```bash
sudo cp /usr/share/X11/locale/en_US.UTF-8/Compose /usr/share/X11/locale/en_US.UTF-8/Compose_bk
sudo sed -i 's/<dead_greek>/<Multi_key> <g> <g>/' /usr/share/X11/locale/en_US.UTF-8/Compose

sudo reboot
```  



## Costumize Compose Key

```bash
sudo vim /usr/share/X11/locale/en_US.UTF-8/Compose
```

```
<Multi_key> <bar> <asciicircum>                     : "↑"
<Multi_key> <asciicircum> <bar>                     : "↑"
<Multi_key> <bar> <v>                     : "↓"
<Multi_key> <bar> <V>                     : "↓"
<Multi_key> <v> <bar>                     : "↓"
<Multi_key> <V> <bar>                     : "↓"
<Multi_key> <asciitilde> <equal>          : "≈"
```

==Reboot/Relogo to reload==
