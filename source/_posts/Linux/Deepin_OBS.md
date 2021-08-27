---
title: "如何在Deepin上安装稳定的OBS"
description: "如何在Deepin上安装稳定的OBS"
url: obs2
date: 2020/06/26
toc: true
excerpt: "OBS (Open Broadcaster Software) is free and open source software for video recording and live streaming. Stream to Twitch, YouTube and many other providers or record your own videos with high quality H264 / AAC encoding."
tags: [Linux, Software]
category: [Linux, Software]
cover: 'https://s1.ax1x.com/2020/06/26/NsE8nH.png'
thumbnail: 'https://s1.ax1x.com/2020/06/26/NsE8nH.png'
priority: 10000
---

## 如何在Deepin上安装稳定的OBS

系统： Deepin 15.11<br />apt， Deepin 商店， 以及 OBS 官方教程都试过了， 折腾了好久， 安装都很简单，也能打开。<br />但是一开始录屏或这推流， 软件就开始闪退， 非常头疼，<br />最后终于找到了这个[帖子](https://hacpai.com/article/1563091378708)<br />
<br />记录一下，做个备份
```bash
## 安装 flatpak 软件管理器
apt install flatpak
apt install gnome-software-plugin-flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
## 这里官方建议安装完flatpak以后重启一下系统。不过我好像没有重启，也没有关系的样子


## 安装 OBS
flatpak install flathub com.obsproject.Studio

## 运行 OBS
flatpak run com.obsproject.Studio
```

<br />安装以后，在主菜单也可以找到了，也可以在开始菜单里面，点击运行<br />
![NsE8nH.png](https://s1.ax1x.com/2020/06/26/NsE8nH.png)


