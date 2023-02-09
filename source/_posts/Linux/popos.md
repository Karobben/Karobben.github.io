---
title: "Pop OS"
description: "Quick Guide of settel your Pop OS!"
date: 2022/01/31
url: pop_os
toc: true
excerpt: "Quick Guide of settel your Pop OS!"
tags: [Linux, System]
category: [Linux]
cover: 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Pop_OS-Logo-nobg.svg/800px-Pop_OS-Logo-nobg.svg.png?20200519213455'
thumbnail: 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Pop_OS-Logo-nobg.svg/800px-Pop_OS-Logo-nobg.svg.png?20200519213455'
priority: 10000
covercopy: ''
---

## Pop os

- [x] Atom
- [x] R
- [x] python
- [x] latex
- [x] Apps from stores

### update

```bash
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade
sudo apt autoremove
sudo apt autoclean
sudo fwupdmgr get-devices
sudo fwupdmgr get-updates
sudo fwupdmgr update
sudo apt install flatpak
flatpak update
sudo reboot now


sudo apt  install curl vim
```

install aps from store shop:

atom; obs

## wechat

Reference: [Kumar, 2020](https://itsfoss.com/install-wechat-desktop-client-in-ubuntu/)
Use web app throuhg Rambox
```bash
sudo snap install ramboxpro
```

```bash
sudo snap install electronic-wechat
```

Wine based wechat: [白菜林; 2022](https://3ae.cn/article/2022/ubuntu_wechat-install/)
App source from: [Ukylin](https://www.ubuntukylin.com/applications/106-cn.html)

```bash
wget  -O weixin.deb "http://archive.ubuntukylin.com/software/pool/partner/weixin_2.1.1_amd64.deb"
sudo dpkg -i weixin.deb
```

## hexo

Reference: [hexo.io](https://hexo.io/docs/)

```bash
sudo apt install nodejs

sudo apt upgrade node
sudo apt install npm
sudo npm install -g hexo-cli
```

## waque

```bash
npm i -g waque
```



### Install Atom plugs

==Atom is died==

More: [Karobben 2020](https://karobben.github.io/2020/06/26/Linux/Atom/)
- markdown-preview-enhanced
- language-r (R 语言语法高亮)
- minimap (VS 一样小图预览)
- atom-beautify (高亮美化)
- emmet (emmet是HTML,CSS快速编写的神器,具体的使用可以参看emmet官网。)
- autocomplete-* 系列 (自动补全)
- pigments (显示颜色)

```bash
apm install markdown-preview-enhanced
apm install language-r minimap pigments atom-beautify
```

## R

```bash
sudo apt install r-base-core
```


## python

Python3 was pre-installed
```bash
sudo apt install python3-pip
```

## Go lang

```bash
sudo apt install golang-go
```

## others

### Scrcpy

the best app for cast your cell on linux
[Karobben, 2020](https://karobben.github.io/2020/06/26/Linux/Deepin_scrcpy)

```bash
sudo apt install meson
sudo apt install adb ffmpeg libsdl2-2.0-0 make gcc pkg-config meson ninja-build \
    libavcodec-dev libavformat-dev libavutil-dev libsdl2-dev libusb-1.0-0-dev

wget -c https://github.com/Genymobile/scrcpy/releases/download/v1.11/scrcpy-server-v1.11
wget -c https://github.com/Genymobile/scrcpy/archive/v1.11.tar.gz

mv scrcpy-server-v1.11 scrcpy-server-v1.11.jar
tar -zxvf v1.11.tar.gz
sudo install scrcpy-server-v1.11.jar /usr/local/bin/scrcpy-server.jar
cd scrcpy-1.11
meson build --buildtype release --strip -Db_lto=true  -Dprebuilt_server=../scrcpy-server-v1.11.jar

cd build
ninja

sudo ninja install
scrcpy
```

### Gotop

Github: 
- [cjbassi/gotop](https://github.com/cjbassi/gotop)
- [Release](https://github.com/cjbassi/gotop/releases)

```bash
wget https://github.com/cjbassi/gotop/releases/download/3.0.0/gotop_3.0.0_linux_amd64.deb
sudo dpkg -i gotop_3.0.0_linux_amd64.deb
rm gotop_3.0.0_linux_amd64.deb
```

```bash
snap install gotop-cjbassi
snap connect gotop-cjbassi:hardware-observe
snap connect gotop-cjbassi:mount-observe
snap connect gotop-cjbassi:system-observe

gotop-cjbassi
```

### else
```bash
## Set a hostname
hostnamectl set-hostname karobben

## install screenfetch
sudo apt install screenfetch
sudo apt install lolcat


## SSH keys
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

## Fish - A Friendly Interactive Shell  (doesn't work for me)
sudo apt install -y fish util-linux-user
chsh -s /usr/bin/fish
mkdir -p /home/$USER/.local/bin
set -Ua fish_user_paths /home/$USER/.local/bin


# Snap
## Enable snap support
sudo apt install snapd

# nautilus-admin
## Right-click context menu in nautilus for admin
sudo apt install -y nautilus-admin


#Virtual machines: Quickemu and other stuff
# git clone https://github.com/wmutschl/quickemu ~/quickemu
#sudo apt install snapd bsdgames wget
#sudo snap install qemu-virgil
#sudo snap connect qemu-virgil:kvm
#sudo snap connect qemu-virgil:raw-usb
#sudo snap connect qemu-virgil:removable-media
#sudo snap connect qemu-virgil:audio-record
#sudo ln -s ~/quickemu/quickemu /home/$USER/.local/bin/quickemu

## Open-ssh
sudo apt install openssh-server



# git
sudo apt install -y git git-lfs
git-lfs install
flatpak install -y gitkraken

# latex
sudo apt install -y texlive texlive-font-utils texlive-pstricks-doc texlive-base texlive-formats-extra texlive-lang-german texlive-metapost texlive-publishers texlive-bibtex-extra texlive-latex-base texlive-metapost-doc texlive-publishers-doc texlive-binaries texlive-latex-base-doc texlive-science texlive-extra-utils texlive-latex-extra texlive-science-doc texlive-fonts-extra texlive-latex-extra-doc texlive-pictures texlive-xetex texlive-fonts-extra-doc texlive-latex-recommended texlive-pictures-doc texlive-fonts-recommended texlive-humanities texlive-lang-english texlive-latex-recommended-doc texlive-fonts-recommended-doc texlive-humanities-doc texlive-luatex texlive-pstricks perl-tk


## zoom
flatpak install -y zoom

## Flameshort
sudo apt install flameshot
flameshot gui

##Multimedia Codecs
#Install and compile multimedia codecs:
sudo apt install -y libavcodec-extra libdvd-pkg; sudo dpkg-reconfigure libdvd-pkg

#OBS
sudo apt install -y obs-studio

# xmind
snap install xmind

# cowsay
snap install  cowsay

sudo apt install imagemagick-6.q16 # convert function

sudo apt install ffmpeg
sudo apt install kdenlive


## gtt-cli
sudo apt install python3-gtts

## play
sudo apt install sox
sudo apt install mplayer

# PDF reader
sudo apt-get install okular
```

## fingerprint authority

```bash
sudo pam-auth-update
```

## python

### OpenCV

```bash
pip3 install --upgrade setuptools
pip3 install numpy Matplotlib
pip3 install opencv-python
```

## Chinese input

download the deb: [link](http://packages.deepin.com/deepin/pool/non-free/i/iflyime/)


reference:
- [@kuang-da , github](https://gist.github.com/kuang-da/3e77389965cd24e726db545c690a4c1d)
- [woq 2021](https://0xffff.one/d/902-pop-os-20-04-lts-zhi-nan)
- [Lei Mao](https://leimao.github.io/blog/Ubuntu-Gaming-Chinese-Input/) (==This post shell be solve your question==)

```bash
sudo apt install fcitx

sudo apt install  fcitx5-chinese-addons fcitx5

curl -sL 'https://keyserver.ubuntu.com/pks/lookup?&op=get&search=0x73BC8FBCF5DE40C6ADFCFFFA9C949F2093F565FF' | sudo apt-key add
sudo apt-add-repository 'deb http://archive.ubuntukylin.com/ukui focal main'
sudo apt upgrade
```

### imput themes/skin for fcitx

Source: [@BrandonCardoso; 2021-github](https://github.com/BrandonCardoso/fcitx-dracula)
```bash
https://github.com/BrandonCardoso/fcitx-dracula
```

![fcitx skin](https://z3.ax1x.com/2021/11/04/IVg8Ig.png)

### 拼音词库

Reference: [CodeAlex; 2019](https://alessandrochen.github.io/2019/04/27/Fcitx%E6%B7%BB%E5%8A%A0%E8%AF%8D%E5%BA%93/)
```bash
sudo apt install fcitx-tools
mkdir /home/$USER/.config/fcitx/pinyin/

git clone https://github.com/AlessandroChen/fcitx-pinyin-lexicon.git
cd fcitx-pinyin-lexicon


```

## Apps from stores

atom
Xmind 8
TigerVNC Viewer

## software for biologist

```bash
sudo apt install clustalw bowtie bowtie2 muscle rsem t-coffee pymol ncbi-entrez-direct samtools

sudo apt install ncbi-blast+ # some system is blast2 
```

## auto mount D

[Quetza, 2019](https://askubuntu.com/questions/520992/what-causes-high-cpu-usage-by-mount-ntfs)
```bash
sudo echo "/dev/sda2   /media/$USER/Data/   ntfs    defaults,nls=utf-8,umask=007,gid=46   0   0" >> /etc/fstab

```

## Themes

Reference:[Abhishek Prakash, 2021, It's FOSS](https://itsfoss.com/install-switch-themes-gnome-shell/)

Select a theme from [Website](https://itsfoss.com/best-gtk-themes/)

install `ocs-url` from [here](https://www.opendesktop.org/p/1136805/)
After download, an example code for installation could be:
```bash
sudo dpkg -i ocs-url_3.1.0-0ubuntu1_amd64.deb
```

Then, open Tweaks → Apearance → Applications → Theme you download


${theme.zip} is the theme zip file you download

```bash
mkdir ~/.themes
sudo apt install gnome-shell-extensions
cd ~/.themes
mv ~/Download/${theme.zip} .
unzip ${theme.zip}
```

Other themes for Gnome:
[gnome-look.org](https://www.gnome-look.org/browse?ord=rating)

Exp:
[Win11 style](https://www.gnome-look.org/p/1596196)


### Gnome-tweaks

```bash
sudo apt install gnome-tweaks 
sudo apt install gnome-tweak-tool
sudo apt install gnome-shell-extensions
sudo apt install $(apt search gnome-shell-extension | grep ^gnome | cut -d / -f1)

gnome-tweaks
```

> apps for configuring Ubuntu, removes GNOME Shell Extensions support by releasing version 40. You need to launch extensions idependently [Karim Buzdar,2020](https://ubuntuhandbook.org/index.php/2021/05/gnome-tweaks-40-no-longer-manage-extensions/)

After start the `Extesion`, choose `User themes` → `Settings` → select it


### video wall paper

[komorebi](https://github.com/cheesecakeufo/komorebi)

## Zsh

A similar zsh environment from Manjaro.
zsh theme: [source](https://juejin.cn/post/6985123210782212132)

!!! info Fonts for powerlevel10k
    Download fonts: [MesloLGS NF; from Github](https://github.com/romkatv/powerlevel10k#manual-font-installation)

```bash
# Install zsh
sudo apt install zsh
chsh -s /bin/zsh
# Install oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# Zsh Theme: powerlevel10k
git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k
# Install the font for powerlevel10k
apt-get install fonts-powerline

# add lines below to ~/.zshrc
#ZSH_THEME="powerlevel10k/powerlevel10k"
#POWERLEVEL9K_MODE="awesome-patched"

# Set the theme
source ~/.zshrc
# configure the theme again if you wanna a change
p10k configure

# plugins
git clone https://github.com/zsh-users/zsh-autosuggestions.git  $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting

# add lines below to ~/.zshrc
#plugins=(zsh-autosuggestions zsh-syntax-highlighting git)

source ~/.zshrc
```

You should change `~/.zshrc` as below listed.
```diff
- ZSH_THEME="..."
+ ZSH_THEME="powerlevel10k/powerlevel10k"
- plugins=(git)
+ plugins=(git
+   zsh-autosuggestions
+   zsh-syntax-highlighting)
```

zsh didn't load automatically: [skepticNeophyte](https://stackoverflow.com/questions/15682456/oh-my-zsh-config-file-not-loading/15882090#15882090)
We need to reload oh-my-zsh.sh and config again
<pre>
source $ZSH/oh-my-zsh.sh
</pre>

command Autosuggestion:

Thansk for [Kumar Abhirup](https://dev.to/kumareth/a-beginner-s-guide-for-setting-up-autocomplete-on-ohmyzsh-hyper-with-plugins-themes-47f2)'s post, I finally get my favorate zsh environment.

zsh plunges:

[Varun Kumar Manik: How to Install Zsh/ zsh-autosuggestions/ oh-my-zsh in Linux](https://varunmanik1.medium.com/how-to-install-zsh-zsh-autosuggestions-oh-my-zsh-in-linux-65fa01cc038d)

## Kivy

I Strongly recommend that build the kivy in an virtualenv. You can use either `conda` or `python virtualenv`

### python virtualenv
```bash
python3.7 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --user --upgrade pip wheel setuptools virtualenv
cd ~
python3.7 -m virtualenv kivyven
source kivyven/bin/activate
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple kivy   
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple cython
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple buildozer
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  https://github.com/kivymd/KivyMD/archive/master.zip
```


### Conda

```bash
conda create -n kivy python==3.8.10
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple kivy   
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple cython
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple buildozer
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple  https://github.com/kivymd/KivyMD/archive/master.zip

```
