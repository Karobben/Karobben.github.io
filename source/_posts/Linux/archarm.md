---
toc: true
url: archarm
covercopy: © Karobben
priority: 10000
date: 2023-06-15 12:17:02
title: "Arch linux in Android (aarch64)/No root (proot)"
ytitle: "Arch linux in Android (aarch64)/No root (proot)"
description: "Arch linux in Android (aarch64)/No root (proot)"
excerpt: "Arch linux in Android (aarch64)/No root (proot)"
tags: [Linux, Android]
category: [Linux, Arch]
cover: "https://s1.ax1x.com/2023/06/16/pCMPusP.png"
thumbnail: "https://s1.ax1x.com/2023/06/16/pCMPusP.png"
---

## Arch linux in Android phon

Test host: Samsung Galaxy ultra S23

## How to install: Tmoe

Tmoe link: [majianwei_private](https://gitee.com/mr_ma_technology/linux)



## After start with VNC

1. install a packages: 
  ```bash
  sudo pacman -S cmatrix
  ```
2. remove the package:
  ```bash
  sudo pacman -R cmatrix
  ```
3. get the information of the package:
  ```bash
  pacman -Qi cmatrix
  ```

<pre>
Name            : cmatrix
Version         : 2.0-2
Description     : A curses-based scrolling 'Matrix'-like screen
Architecture    : aarch64
URL             : https://www.asty.org/cmatrix/
Licenses        : GPL3
Groups          : None
Provides        : None
Depends On      : ncurses
Optional Deps   : kbd: cmatrix-tty custom font [installed]
                  xterm: cmatrix-tty custom font
Required By     : None
Optional For    : None
Conflicts With  : None
Replaces        : None
Installed Size  : 94.74 KiB
Packager        : Arch Linux ARM Build System <builder+n1@archlinuxarm.org>
Build Date      : Mon 29 Jun 2020 02:47:20 PM CDT
Install Date    : Thu 15 Jun 2023 12:26:30 PM CDT
Install Reason  : Explicitly installed
Install Script  : No
Validated By    : Signature
</pre>



## setup yay

```bash
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/yay-git.git
cd yay-git/
makepkg -si
```

<pre>
==> Making package: yay-git 12.0.5.r0.g9641d2a-1 (Thu 15 Jun 2023 12:34:49 PM CDT)
==> Checking runtime dependencies...
==> Checking buildtime dependencies...
==> Installing missing dependencies...
resolving dependencies...
looking for conflicting packages...

Packages (1) go-2:1.20.4-1

Total Download Size:    35.71 MiB
Total Installed Size:  192.95 MiB

:: Proceed with installation? [Y/n]
</pre>

Just type `y` and `enter`

## some software you may like

- firefox: `pacman -S firefox`



























































<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
