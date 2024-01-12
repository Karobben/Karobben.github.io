---
toc: true
url: bluetooth
covercopy: © Karobben
priority: 10000
date: 2022-05-27 15:24:06
title: "Linux Bluetooth Trouble Shoot"
ytitle: "Linux 蓝牙问题"
description: "Bluetooth is a bit odd. There are a lot of factors that go into whether Bluetooth devices work together as expected."
excerpt: "Bluetooth is a bit odd. There are a lot of factors that go into whether Bluetooth devices work together as expected."
tags: [Linux, System]
category: [Linux]
cover: "https://s1.ax1x.com/2022/05/28/XnaoSP.png"
thumbnail: "https://s1.ax1x.com/2022/05/28/XnaoSP.png"
---

## Linux Blue tooth Trouble Shoot

Reference: [system 76](https://support.system76.com/articles/bluetooth/)

Except Nvidia driver, bluetooth driver could be an annoying one, too. Link above list lost of possible ways to deal with the bluetooth.

Im my situation, I am using `Pop 20.04 focal` which kernel is `x86_64 Linux 5.16.19-76051619-generic`. Very interesting thing is I can connect my Cellphone with bluetooth but not head buds. After tried a few codes from the blog of  [system 76](https://support.system76.com/articles/bluetooth/), my problem was solved by reset the bluetooth devices profile.

```bash
sudo rm -r /var/lib/bluetooth/
```

|![](https://s1.ax1x.com/2022/05/28/XnaoSP.png)|
|:-:|
