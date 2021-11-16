---
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
flatpak update
sudo reboot now
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

## hexo

Reference: [hexo.io](https://hexo.io/docs/)
```bash
sudo apt upgrade node
sudo apt install npm
sudo npm install -g hexo-cli
```

## waque

```bash
npm i -g waque
```

## Scrcyp

the best app for cast your cell on linux
```bash
sudo apt install meson ninja
```

### Install Atom plugs

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

```bash
sudo apt install python3-pip
```



## others

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

# Gnome-tweaks
sudo apt install gnome-tweak-tool

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
sudp apt install flameshot
flameshot gui

##Multimedia Codecs
#Install and compile multimedia codecs:
sudo apt install -y libavcodec-extra libdvd-pkg; sudo dpkg-reconfigure libdvd-pkg

#OBS
sudo apt install -y obs-studio

# xmind
snap install xmind

# gotop
snap install  cowsay

sudo apt install imagemagick-6.q16 # convert function

sudo apt install ffmpeg
sudo apt install kdenlive


## gtt-cli
pip install python3-gtts

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
sudo apt install blast2 clustalw bowtie bowtie2 muscle rsem t-coffee pymol ncbi-entrez-direct samtools
```

## auto mount D

[Quetza, 2019](https://askubuntu.com/questions/520992/what-causes-high-cpu-usage-by-mount-ntfs)
```bash
sudo echo "/dev/sda2   /media/$USER/Data/   ntfs    defaults,nls=utf-8,umask=007,gid=46   0   0" >> /etc/fstab

```
