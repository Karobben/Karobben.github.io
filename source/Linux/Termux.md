---
title: "Termux"
description: "Termux"
url: termux
---

# Termux

<a name="6MmZq"></a>
# 1. SSH
```bash
pkg install openssh # 安装ssh
passwd # 设置登录密码

ifconfig # 获取ip (手机电脑链接同一路由器/局域网)
whoami # 获取用户名

sshd # 开启 ssh 服务
```


<a name="uZy27"></a>
# 2. Storage


```bash
#建立storage

termux-setup-storage #(手机需要授予权限)

```


<a name="L2AxH"></a>
# 3. Mirror


```bash
vi $PREFIX/etc/apt/sources.list # 注释掉原本该源，并添加清华镜像
```


```bash
# The main termux repository:
#deb https://termux.org/packages/ stable main
deb https://mirrors.tuna.tsinghua.edu.cn/termux stable main
#deb https://its-pointless.github.io/files/ termux extras
#deb [trusted=yes] http://termux.iikira.com stable main

#test
#deb http://httpredir.debian.org/debian stretch main contrib non-free
#deb http://deb.debian.org/debian stretch main contrib non-free
#deb-src http://deb.debian.org/debian stretch main contrib non-free
#deb http://deb.debian.org/debian stable main contrib
#deb-src http://deb.debian.org/debian stable main contrib
#deb http://deb.debian.org/debian testing main contrib
#deb-src http://deb.debian.org/debian testing main contrib
#deb http://deb.debian.org/debian unstable main contrib
#deb-src http://deb.debian.org/debian unstable main contrib
```


```bash
apt update && apt upgrade # 更新并升级 (有些需要y确认)
```

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
