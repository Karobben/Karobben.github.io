---
title: "Deepin 15.11 Bug 汇集"
description: "Deepin 15.11 Bug 汇集"
url: deepin15_bugs
date: 2020/06/26
toc: true
excerpt: "Some bugs of deepin 15.11 I found"
tags: [Linux, bug]
category: [Linux, others]
cover: 'https://s1.ax1x.com/2020/06/26/NrTT7n.png'
thumbnail: 'https://s1.ax1x.com/2020/06/26/NrTT7n.png'
priority: 10000
---

## Deepin 15.11 Bug 汇集

## 任务栏消失
![NsZ1wd.png](https://s1.ax1x.com/2020/06/26/NsZ1wd.png)

解决办法:
1. 山野莽夫, 2019: `https://www.shanyemangfu.com/deepin-dock.html` (链接已失效)
进入任务管理器, 关闭 dock.
2. [livefun, 2020](https://bbs.deepin.org/forum.php?mod=viewthread&tid=188014)
删除配置文件并重启
`rm -rf ~/.config/dconf; reboot`
3. [widon1104, 2020](https://bbs.deepin.org/forum.php?mod=viewthread&tid=188014)
手动启动: `dde-dock & `

## 录屏bug
**deepin screen recorder**:
![NrTtFx.png](https://s1.ax1x.com/2020/06/26/NrTtFx.png)

<a name="rwhNt"></a>
## 窗口冻结在原处
![NrTJT1.jpg](https://s1.ax1x.com/2020/06/26/NrTJT1.jpg)
