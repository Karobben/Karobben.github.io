---
title: "To Start With Linux"
description: "To Start With Linux"
url: linux2
date: 2020/06/26
toc: true
excerpt: "Add a user"
tags: [Linux, bash]
category: [Linux, Bash, Beginner]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=465&h=180'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=180&h=180'
priority: 10000
---

## To Start With Linux

<a name="f2cMB"></a>
## 1 Add a user

```bash
useradd ken # add a user 'ken'
passwd ken  # add a password for urser 'ken'
```


<a name="iIARD"></a>
## 2 Add users to sudo group

```bash
vim /etc/sudoers # use root acount or run with sudo
```

Find the line "root    ALL=(ALL)        ALL" and add a line:
```bash
ken  ALL=(ALL)    ALL
```
save and quite


<a name="6nxWN"></a>
## 3 Adding Script to boot list

```bash
sudo vim /etc/rc.local
```
 
```bash
##!/bin/bash
## rc.local config file created by use

##The script you want to run while booting

exit 0

```

```bash
sudo chmod +x /etc/rc.local
```

## Something Else

### System infor

```bash
# print distro
head -n 1 /etc/issue

# Name of the computer
hostname
```

### Hardware infor

```bash
# CPU infor
cat /proc/cpuinfo

# Ram infor
grep MemTotal /proc/meminfo
# Ram infor
free -h
```
### Java
[adopt open jdk](https://adoptopenjdk.net/)
