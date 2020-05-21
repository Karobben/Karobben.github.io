---
url: obs2
---

# 如何在Deepin上安装稳定的OBS

系统： Deepin 15.11<br />apt， Deepin 商店， 以及 OBS 官方教程都试过了， 折腾了好久， 安装都很简单，也能打开。<br />但是一开始录屏或这推流， 软件就开始闪退， 非常头疼，<br />最后终于找到了这个[帖子](https://hacpai.com/article/1563091378708)<br />
<br />记录一下，做个备份
```bash
# 安装 flatpak 软件管理器
apt install flatpak
apt install gnome-software-plugin-flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
# 这里官方建议安装完flatpak以后重启一下系统。不过我好像没有重启，也没有关系的样子


# 安装 OBS
flatpak install flathub com.obsproject.Studio

# 运行 OBS
flatpak run com.obsproject.Studio
```

<br />安装以后，在主菜单也可以找到了，也可以在开始菜单里面，点击运行<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580981771681-de490709-77ec-4002-b821-4b347ff0c840.png#align=left&display=inline&height=405&name=image.png&originHeight=518&originWidth=555&size=69951&status=done&style=none&width=434)<br />
