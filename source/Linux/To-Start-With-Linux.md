---
title: "To Start With Linux"
description: "To Start With Linux"
url: linux2
---

# To Start With Linux

<a name="f2cMB"></a>
# 1 Add a user

```bash
useradd ken # add a user 'ken'
passwd ken  # add a password for urser 'ken'
```


<a name="iIARD"></a>
# 2 Add users to sudo group

```bash
vim /etc/sudoers # use root acount or run with sudo
```

Find the line "root    ALL=(ALL)        ALL" and add a line:
```bash
ken  ALL=(ALL)    ALL
```
save and quite


<a name="6nxWN"></a>
# 3 Adding Script to boot list

```bash
sudo vim /etc/rc.local
```
 
```bash
#!/bin/bash
# rc.local config file created by use

#The script you want to run while booting

exit 0

```

```bash
sudo chmod +x /etc/rc.local
```

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
