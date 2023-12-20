---
title: "Termux"
description: "Termux"
url: termux
date: 2021/05/19
toc: true
excerpt: "Termux Termux is an Android terminal emulator and Linux environment app that works directly with no rooting or setup required. A minimal base system is installed automatically - additional packages are available using the APT package manager. Read the wiki to learn more..."
tags: [Linux, Android]
category: [Linux, Termux]
cover: 'https://descargarparapc.club/wp-content/uploads/2020/06/termux.jpg'
thumbnail: 'https://descargarparapc.club/wp-content/uploads/2020/06/termux.jpg'
covercopy: <a href="https://descargarparapc.club/termux/">© Descargar Termux para PC</a>
priority: 10000
---

Version:

## Switch to your favorite mirror
```bash
termux-change-repo
```
1. Select all (or whatever you want)
2. Select a mirror
  exp: mirror by Tsinghua University

## SSH
```bash
pkg install openssh # 安装ssh
passwd # 设置登录密码

ifconfig # 获取ip (手机电脑链接同一路由器/局域网)
whoami # 获取用户名

sshd # 开启 ssh 服务
```

Now, you can login your termux through ssh:

```bash
u0_a450@192.168.0.100 -p8022
```

## Cell Phon Storage Access

```bash
##建立storage
termux-setup-storage #(手机需要授予权限)
```
After executed the code, you can see the directory `storage` which can connect to your cell phone directories.

## Install VNC desktop environment

[Document](https://wiki.termux.com/wiki/Graphical_Environment)

```bash
pkg install x11-repo
pkg install tigervnc
# setup server
vncserver -localhost

# kill desktop
vncserver -kill :1
```

## xfce4 desktop

```bash
pkg install xfce4
export DISPLAY=":1"
xfce4-session &
apt install aterm twm
```

==PS:==
Though it seems have a 'perfect' desktop environment, it can't show the result of the plot from R and python  .


### errors
<pre>
E: Failed to fetch https://10.via0.com/ipns/k51qzi5uqu5dg9vawh923wejqffxiu9bhqlze5f508msk0h7ylpac27fdgaskx/pool/main/libs/libsm/libsm_1.2.3-17_aarch64.deb  521  Origin Down [IP: 172.67.212.200 443]
E: Failed to fetch https://10.via0.com/ipns/k51qzi5uqu5dg9vawh923wejqffxiu9bhqlze5f508msk0h7ylpac27fdgaskx/pool/main/libx/libxext/libxext_1.3.4-11_aarch64.deb  521  Origin Down [IP: 172.67.212.200 443]
E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?
</pre>

Connection is unstable, try it few more times.
```bash
apt install tigervnc
```

## Some other packages

```bash
apt install vim vim-gtk vim-python wget
```

## pythonenv

```bash
wget http://python.org/ftp/python/3.7.6/Python-3.7.6.tar.xz
tar xf Python-3.7.6.tar.xz
cd Python-3.7.6
./configure --enable-optimizations
make altinstall
rm -rf ../Python*xz
```

## kivyenv

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple kivy  
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pillow
```
hello world example: [Kivy hello world](https://www.geeksforgeeks.org/hello-world-in-kivy/)


## R
[Conor I. Anderson](https://conr.ca/post/installing-r-on-android-via-termux/)

```bash
pkg install curl gnupg
mkdir -p "$PREFIX/etc/apt/sources.list.d/"
echo "deb https://its-pointless.github.io/files/24 termux extras" > "$PREFIX/etc/apt/sources.list.d/pointless.list"
curl "https://its-pointless.github.io/pointless.gpg" | apt-key add

pkg install r-base
```


## Install linux

### The troditional way (which I faild = =)

[想做个好人 2020](https://blog.csdn.net/qqk808/article/details/104897411)

```bash faild
apt install openssl
pkg install wget proot
wget https://raw.githubusercontent.com/Neo-Oli/termux-ubuntu/master/ubuntu.sh
bash ubuntu.sh
```

### Tmoe-linux

[青菜芋子 2020](https://loafing.cn/posts/Termux-Ubuntu-GUI.html)
[Tmoe-repository](https://gitee.com/mo2/linux)

You just need run one of them three. I failed for execute the first and succesed on the second.

```bash
#bash -c "$(curl -L git.io/linux.sh)"
bash -c "$(curl -L l.tmoe.me)"
#bash -c "$(curl -L https://gitee.com/mo2/linux/raw/2/2)"
```
#### Arch in Tmoe

```bash
# add a user 'ken'
useradd ken
# add a password for urser 'ken'
passwd ken  
# use root acount or run with sudo
vim /etc/sudoers
# siwtch to user ken
su ken
```

Find the line "root    ALL=(ALL)        ALL" and add a line:
```bash
ken  ALL=(ALL)    ALL
```
save and quite


```bash
pacman -S r tk
# tk for matplotlib
pip install radian matplotlib docutils  pygments  pygame
```

Matplotlib doesn't show graph
```python
import matplotlib
matplotlib.use('TkAgg')
```

##### kivy

***Don't install kivy while pip!!!***

```bash
pacman -S python sdl2_image sdl2_mixer sdl2_ttf   python-setuptools  sdl2
pacman -S python-pygame python-kivy
```

##### openCV
```bash
pip install opencv-python
```

##### Some other Softwarw

```bash
sudo pacman -Sy yay python-conda
chmod +777 /usr/bin/conda

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
channel conda config -- remove
conda create --name Bio
source activate
# (base) [user@localhost Desktop]$
conda activate Bio
# (Bio) [user@localhost Desktop]$
sudo pacman -Sy zlib

```

`requests idna chardet urllib3 six`

### Error
<pre>
Unable to establish SSL connection.
</pre>

```bash
apt install openssl
```
## Install R in Jupyter Notebook

```bash
pip3 install notebook
```

```R
install.packages("remotes")
remotes::install_github('IRkernel/IRkernel')

# Connect to Jupyter Notebook
IRkernel::installspec()
# 或者是在系统下安装
IRkernel::installspec(user = FALSE)
```


Enable Jupyter notebook remote (local) computer
[Lup Peng 2017](https://luppeng.wordpress.com/2017/04/18/remote-access-to-jupyter-notebook/)

```bash
jupyter notebook --generate-config
vim ./.jupyter/jupyter_notebook_config.py
```

```diff
  #------------------------------------------------------------------------------
  # NotebookApp(JupyterApp) configuration
  #------------------------------------------------------------------------------
  ...
  ## The IP address the notebook server will listen on.
  #c.NotebookApp.ip = 'localhost'
+ c.NotebookApp.ip = '0.0.0.0'
```

```bash
jupyter notebook password
```

## blast+

```bash
apt install blast2
```

## Trinity-try

### dependency
```bash
apt install cd autoconf
apt install cd automake
```

```bash
# download the trinity. I used the mirror which is more stable in China
wget -c https://github.com.cnpmjs.org/trinityrnaseq/trinityrnaseq/releases/download/v2.12.0/trinityrnaseq-v2.12.0.FULL.tar.gz

tar -zxvf trinityrnaseq-v2.12.0.FULL.tar.gz
cd trinityrnaseq-v2.12.0

make
```

### problem


<pre>
Err:1 https://termux.org/packages stable/main aarch64 m4 aarch64 1.4.18-3
  <span style="color:salmon">OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to termux.org:443</span>
Err:2 https://termux.org/packages stable/main aarch64 autoconf all 2.71
  OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to termux.org:443
Unable to correct missing packages.
E: Failed to fetch https://termux.org/packages/pool/main/m/m4/m4_1.4.18-3_aarch64.deb  OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to termux.org:443
E: Failed to fetch https://termux.org/packages/pool/main/a/autoconf/autoconf_2.71_all.deb  OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to termux.org:443
E: Aborting install.
</pre>

Reason: failed to connect the github
Set a proxy / VPN


**During make**
<pre>
cannot find required auxiliary files: config.guess config.sub
</pre>

```bash
apt install automake
vim /data/data/com.termux/files/home/Biosoft/trinityrnaseq-v2.11.0/trinity-plugins/bamsifter/build_htslib.sh
```

```bash
set -e -v

cd htslib
automake -a
mkdir -p build
autoheader
autoconf
./configure --prefix=`pwd`/build/
make
make install
```

###  error: /bin/sh

<pre>
checking host system type... Invalid configuration `unknown-Linux': machine `unknown' not recognized
configure: error: /bin/sh ./config.sub unknown-Linux failed
</pre>


```bash
sed -i 's=CONFIG_SHELL-/bin/sh=CONFIG_SHELL-/data/data/com.termux/files/usr/bin/sh=' /data/data/com.termux/files/home/Biosoft/trinityrnaseq-v2.11.0/trinity-plugins/bamsifter/htslib/configure | grep "/bin/sh"
```




[Github issue](https://github.com/asdf-vm/asdf-erlang/issues/195)
```bash
curl -O http://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz
tar zxvf autoconf-2.70.tar.gz
cd autoconf-2.70
./configure && make

# add to path
source ~/.bashrc

export PATH=$PATH:/data/data/com.termux/files/home/Softwarw/autoconf-2.70/bin
#:wq! exit

source ~/.bashrc
```

### module Autom4te::ChannelDefs

<pre>
Can't locate Autom4te/ChannelDefs.pm in @INC (you may need to install the Autom4te::ChannelDefs module) (@INC contains: /usr/local/share/autoconf /data/data/com.termux/files/usr/lib/perl5/site_perl/5.30.0/aarch64-android /data/data/com.termux/files/usr/lib/perl5/site_perl/5.30.0 /data/data/com.termux/files/usr/lib/perl5/5.30.0/aarch64-android /data/data/com.termux/files/usr/lib/perl5/5.30.0 .) at /data/data/com.termux/files/home/Softwarw/autoconf-2.69/bin/autoheader line 41.
</pre>

Problem: lack of perl modules

By `perldoc perllocal`

We can find the module was in `/data/data/com.termux/files/usr/lib/perl5/site_perl/5.30.0` directory
<pre>
Wed May 12 15:19:24 2021: "Module" Test::Warnings
  *   "installed into:
      /data/data/com.termux/files/usr/lib/perl5/site_perl/5.30.0"
  *   "LINKTYPE: dynamic"
  *   "VERSION: 0.030"
  *   "EXE_FILES: "
Wed May 12 15:19:26 2021: "Module" File::Slurper
</pre>

So, we can make the soft link
```bash
ln -s  /data/data/com.termux/files/home/Softwarw/autoconf-2.70/lib/Autom4te /data/data/com.termux/files/usr/lib/perl5/site_perl/5.30.0/Autom4te
```

### /usr/local/bin/
<pre>
cd bamsifter && make
make[2]: Entering directory '/data/data/com.termux/files/home/Biosoft/trinityrnaseq-v2.12.0/trinity-plugins/bamsifter'
./build_htslib.sh

cd htslib
mkdir -p build
autoheader
sh: 1: /usr/local/bin/autom4te: not found
autoheader: '/usr/local/bin/autom4te' failed with exit status: 127
make[2]: *** [Makefile:10: htslib/version.h] Error 127
</pre>


```bash
/data/data/com.termux/files/home/Biosoft/trinityrnaseq-v2.12.0/trinity-plugins/bamsifter/build_htslib.sh
```

Problem: in './trinity-plugins/bamsifter/htslib/Makefile' file, it assigned the `prefix = /usr/local`

```diff
- prefix    = /usr/local
+ prefix    = /data/data/com.termux/files/usr/
exec_prefix = $(prefix)
bindir      = $(exec_prefix)/bin
.
.
.
- $ENV{'SHELL'} = '/bin/sh' if ($^O eq 'dos');
- $ENV{'SHELL'} = '/data/data/com.termux/files/usr/bin/sh' if ($^O eq 'dos');
```
`/data/data/com.termux/files/home/Softwarw/autoconf-2.70/bin/autoheader`

This error actually comes form `autoheader` file:
`my $autom4te = $ENV{'AUTOM4TE'} || '/usr/local/bin/autom4te';`
We need to change it into:
`my $autom4te = $ENV{'AUTOM4TE'} || '/data/data/com.termux/files/home/Softwarw/autoconf-2.70/bin/autom4te'`

```bash
sed -i 's=/usr/local/bin/autom4te=/data/data/com.termux/files/home/Softwarw/autoconf-2.70/bin/autom4te='  /data/data/com.termux/files/home/Softwarw/autoconf-2.70/bin/autoheader|grep "{'AUTOM4TE'}"
```

<pre>

cd htslib
mkdir -p build
autoheader
autom4te: cannot open < /usr/local/share/autoconf/autom4te.cfg: No such file or directory
autoheader: '/data/data/com.termux/files/home/Softwarw/autoconf-2.69/bin/autom4te' failed with e
</pre>

`/data/data/com.termux/files/home/Softwarw/autoconf-2.69/bin/autom4te`

```diff
- my $pkgdatadir = $ENV{'autom4te_perllibdir'} || '/usr/local/share/autoconf';
+ my $pkgdatadir = $ENV{'autom4te_perllibdir'} || '/data/data/com.termux/files/home/Softwarw/autoconf-2.69/lib/';


```


<pre>
cd htslib
mkdir -p build
autoheader
autom4te: m4sugar/m4sugar.m4: no such file or directory
</pre>

`/data/data/com.termux/files/home/Softwarw/autoconf-2.69/bin/autom4te`
```diff
- my $pkgdatadir = $ENV{'AC_MACRODIR'} || '/usr/local/share/autoconf';
+ my $pkgdatadir = $ENV{'AC_MACRODIR'} || '/data/data/com.termux/files/home/Softwarw/autoconf-2.69/bin/';
```

<pre>
autoheader
autom4te: cannot open < /data/data/com.termux/files/home/Softwarw/autoconf-2.69/bin/autom4te.cfg: Not a directory
autoheader: '/data/data/com.termux/files/home/Softwarw/autoconf-2.69/bin/autom4te' failed with exit status: 1
mak
</pre>


`/data/data/com.termux/files/home/Softwarw/autoconf-2.69/bin/autom4te`

```diff
- load_configuration ($ENV{'AUTOM4TE_CFG'} || "$pkgdatadir/autom4te.cfg");
+ load_configuration ($ENV{'AUTOM4TE_CFG'} || "/data/data/com.termux/files/home/Softwarw/autoconf-2.69/lib/autom4te.cfg");
```

### autom4te.cfg
<pre>
autoheader
autom4te: error: cannot open /usr/local/share/autoconf/autom4te.cfg: No such file or directory
</pre>

```bash
sed  -i 's=/usr/local/share/autoconf=/data/data/com.termux/files/home/Softwarw/autoconf-2.70/lib=' /data/data/com.termux/files/home/Softwarw/autoconf-2.70/bin/autom4te |grep "/data/data/com."
```

's=/usr/local/share/autoconf=/data/data/com.termux/files/home/Softwarw/autoconf-2.69/lib='

### I finally installed 2.71

### perl doesn't support multithreads

```
./Configure -des -Dprefix=/data/data/com.termux/files/usr/local/perl
```
-Dusethreads -Uinstalluserbinperl

## R

```bash
apt install r-base
```

## miniconda

```bash
# download miniconda
wget -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh
```

##
```bash
# blast+
apt install blast2 bowtie bowtie2
```


## Hexo

Reference: [便当的梅开四度](https://wzk0.github.io/hx/)
```python
# update first or you'll got error
pkg upgrade && pkg update

# hexo is based on the nodejs
pkg install nodejs

```




