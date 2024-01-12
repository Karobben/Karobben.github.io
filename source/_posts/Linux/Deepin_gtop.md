---
title: "如何在Deepin上安装gtop"
description: "如何在Deepin上安装gtop"
url: gtop2
date: 2020/06/23
toc: true
excerpt: "gotop is a terminal-based (TUI) system monitor for Linux and macOS. The software is inspired by gtop and vtop, but while these 2 utilities use Node.js, gotop is written in Go. The command line tool supports mouse clicking and scrolling, comes with vi-keys, and it displays the CPU, memory and network usage history using colored graphs, while also displaying their current values."
tags: [Deepin, System, Linux, Scripting, bash, CLI Tools]
category: [Linux, 'Monitor: top\Conky']
cover: 'https://s1.ax1x.com/2020/06/26/NsElcD.gif'
thumbnail: 'https://s1.ax1x.com/2020/06/26/NsElcD.gif'
priority: 10000
---

## 如何在Deepin上安装gtop

参考：[https://github.com/aksakalli/gtop](https://github.com/aksakalli/gtop)

<a name="Py7DW"></a>
## npm Install
```bash
apt-get -y install git curl

npm install gtop --registry https://registry.npm.taobao.org

gtop

'''
You can sort the process table by pressing

p: Process Id
c: CPU usage
m: Memory usage
'''
```


![NsElcD.gif](https://s1.ax1x.com/2020/06/26/NsElcD.gif)
