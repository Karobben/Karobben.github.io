---
title: "Start With Raspberry pi"
description: "Start With Raspberry pi"
url: raspi
date: 2020/06/26
toc: true
excerpt: "Packages managers like atp, snap, npm, apm, and flatpak"
tags: [Linux, RasperryPi]
category: [Linux, RasperryPi]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=465&h=180'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=180&h=180'
priority: 10000
---

## Start With Raspberry pi

<a name="zrj6g"></a>
## apt Mirror
reference: [https://mirrors.tuna.tsinghua.edu.cn/help/raspbian/](https://mirrors.tuna.tsinghua.edu.cn/help/raspbian/)<br />

```bash
## 编辑 `/etc/apt/sources.list` 文件，删除原文件所有内容，用以下内容取代：
deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib
deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib

## 编辑 `/etc/apt/sources.list.d/raspi.list` 文件，删除原文件所有内容，用以下内容取代：
deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ buster main ui
```


<a name="7Ngbi"></a>
## Virtual Keyboard
reference:[https://www.cnblogs.com/little-kwy/p/9478961.html](https://www.cnblogs.com/little-kwy/p/9478961.html)
```bash
sudo apt-get install matchbox-keyboard
sudo apt-get install libmatchbox1 -y
```


```bash
sudo nano /usr/bin/toggle-matchbox-keyboard.sh
```


```bash
##!/bin/bash
##This script toggle the virtual keyboard

PID=`pidof matchbox-keyboard`
if [ ! -e $PID ]; then
  killall matchbox-keyboard
else
 matchbox-keyboard&
fi
```


```bash
sudo nano /usr/share/applications/toggle-matchbox-keyboard.desktop
```


```bash
[Desktop Entry]
Name=Toggle Matchbox Keyboard
Comment=Toggle Matchbox Keyboard
Exec=toggle-matchbox-keyboard.sh
Type=Application
Icon=matchbox-keyboard.png
Categories=Panel;Utility;MB
X-MB-INPUT-MECHANSIM=True
```

<br />It's failed and I don't know why. But there is a keyboard for rasberrypi, so...
![Nse24I.png](https://s1.ax1x.com/2020/06/26/Nse24I.png)

## Screen Shot


```bash
sudo apt-get install scrot
scrot test.png

## screen shot for
scrot -s 0 0 100 100
## Screen shot after 10s
scrot -d 10

```


<a name="7c6vp"></a>
## Screen Record


```bash
sudo apt-get install vokoscreen
vokoscreen
```


<a name="UitKE"></a>
## USB Camera
reference: [https://blog.csdn.net/yjp19871013/article/details/80147803](https://blog.csdn.net/yjp19871013/article/details/80147803)
<a name="ehp8l"></a>
### Take a Photo
```bash
sudo apt-get install fswebcam
fswebcam /dev/video0 ~/image.jpg #/dev/vedio0 is the vedio
```


```bash
raspistill -o ugi.jpg -w 2560 -h 1440 -v # -vf
```


<a name="Lutis"></a>
### Stream image
```python
sudo apt-get install luvcview
luvcview -s 400x400
```

<br />I got an error code after a lunached the command. The image poped out and crashed after about 1s.<br />

```bash
luvcview: ../../src/xcb_io.c:165: dequeue_pending_request:
  Assertion `!xcb_xlib_unknown_req_in_deq' failed.
```

<br />But I find that once you launched your camera, you need to keep the camera moving for a while and so, it can run smoothly.<br />

<a name="Z6Lcj"></a>
## 自动免密码登录


```bash
##https://blog.csdn.net/zexzex_/article/details/78490054
sudo raspi-config
选择Boot Options
Desktop / CLT
console Autologin Text console int3 或者 Desktop Autologin Desktop GUI 桌面环境
finish
reboot
```

## 开机任务
参考: [yuanfujie](https://blog.csdn.net/u011720560/article/details/80591460)

進入隱藏文件夾， 然後創建一個文件夾和文件， 做開機啓動腳本

```bash
cd ~/.config
cd /home/pi/.config
mkdir autostart
cd autostart
## 創建自啓腳本
sudo nano myapp.desktop
```
在`nano`後黏貼代碼如下。重點在`Exec=XXX`;
比如，我的需要執行的腳本路徑爲<span style="background:salmon">/home/pi/Blive</span>
```desktop
[Desktop Entry]
Type=Application
Exec=/home/pi/Blive
Icon=ICON_PATH
```
親測有效


Enjoy～
