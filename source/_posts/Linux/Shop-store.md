---
title: "Package Managers For linux"
description: "Package Manager For linux"
url: shop_store2
date: 2020/06/26
toc: true
excerpt: "Packages managers like atp, snap, npm, apm, and flatpak"
tags: [Linux, Software]
category: [Linux, Software]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=465&h=180'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=180&h=180'
priority: 10000
---

## Package Managers For linux

<a name="oOuU3"></a>
## apt



<a name="is6uQ"></a>
## snap
website: [https://snapcraft.io/store](https://snapcraft.io/store)

```bash
systemctl restart snapd

sudo snap install **
```

获得下载链接:

```bash
curl -H 'Snap-Device-Series: 16' http://api.snapcraft.io/v2/snaps/info/anbox
```

ulr 在结果中(页面查找download可以迅速定位):<br />"download":{"deltas":[],"sha3-384":"76f4f975d6e465f7362f176a9c4ab49067224157d0d611d243596b82cd24c78f51c3d2a29f382882967bb5ae5fbf1858","size":81797120,"url":"https://api.snapcraft.io/api/v1/snaps/download/M7yvgnqOvyQj64bolfpawIAEwHv7dQ5G_202.snap"}
```bash
{"channel-map":[{"channel":{"architecture":"amd64","name":"stable","released-at":"2020-01-01T22:39:50.563736+00:00","risk":"stable","track":"latest"},"created-at":"2020-01-01T22:38:31.952619+00:00","download":{"deltas":[],"sha3-384":"f385d44ecfdfa9268a2be6b2fd98f29ac5d38d80d374e92cdc45ba07eac16c6fe9e178dbf675f579d0256cf52a483cb7","size":81793024,"url":"https://api.snapcraft.io/api/v1/snaps/download/M7yvgnqOvyQj64bolfpawIAEwHv7dQ5G_204.snap"},"revision":204,"type":"app","version":"v1.12"},
{"channel":{"architecture":"i386","name":"stable","released-at":"2020-01-01T22:42:08.624199+00:00","risk":"stable","track":"latest"},"created-at":"2020-01-01T22:41:21.457669+00:00","download":{"deltas":[],"sha3-384":"201b9a486e02fa8b06b7a1b1fad002757cc64b3982ba1fff5e5b11a82802fba31a0389d0aa5affba986d2400df273d31","size":82841600,"url":"https://api.snapcraft.io/api/v1/snaps/download/M7yvgnqOvyQj64bolfpawIAEwHv7dQ5G_205.snap"},"revision":205,"type":"app","version":"v1.12"},
{"channel":{"architecture":"amd64","name":"beta","released-at":"2020-01-18T07:04:58.924188+00:00","risk":"beta","track":"latest"},"created-at":"2020-01-18T07:03:58.524875+00:00","download":{"deltas":[],"sha3-384":"f608e1c8bc2fee937a1dead15ece1be4cc79fbb06804e3f405410a69933b1282967ce138454b92c6c6f15fd135b78e3c","size":85434368,"url":"https://api.snapcraft.io/api/v1/snaps/download/M7yvgnqOvyQj64bolfpawIAEwHv7dQ5G_208.snap"},"revision":208,"type":"app","version":"v1.12.1-1-g31bd950"},
{"channel":{"architecture":"armhf","name":"beta","released-at":"2020-01-18T08:02:17.160034+00:00","risk":"beta","track":"latest"},"created-at":"2020-01-18T08:01:25.981004+00:00","download":{"deltas":[],"sha3-384":"f44ce790760d736855c078b5679737cc6bf013ee91d28860fc9fb5cade2e0bf57ae4c81d987b2081e7874a7027c97f5a","size":73723904,"url":"https://api.snapcraft.io/api/v1/snaps/download/M7yvgnqOvyQj64bolfpawIAEwHv7dQ5G_210.snap"},"revision":210,"type":"app","version":"v1.12.1-1-g31bd950"},
{"channel":{"architecture":"i386","name":"beta","released-at":"2020-01-18T07:05:48.607438+00:00","risk":"beta","track":"latest"},"created-at":"2020-01-18T07:04:34.542649+00:00","download":{"deltas":[],"sha3-384":"8a330eb9981ef9957556515cda2ee8b8f4ae2a458d93488d62182fe5a4a60d0fb888e3d18ea420fe0dbf0e4ec39381f2","size":86736896,"url":"https://api.snapcraft.io/api/v1/snaps/download/M7yvgnqOvyQj64bolfpawIAEwHv7dQ5G_209.snap"},"revision":209,"type":"app","version":"v1.12.1-1-g31bd950"},
{"channel":{"architecture":"amd64","name":"edge","released-at":"2019-12-10T00:14:49.361567+00:00","risk":"edge","track":"latest"},"created-at":"2019-12-10T00:12:26.588992+00:00","download":{"deltas":[],"sha3-384":"76f4f975d6e465f7362f176a9c4ab49067224157d0d611d243596b82cd24c78f51c3d2a29f382882967bb5ae5fbf1858","size":81797120,"url":"https://api.snapcraft.io/api/v1/snaps/download/M7yvgnqOvyQj64bolfpawIAEwHv7dQ5G_202.snap"},"revision":202,"type":"app","version":"v1.12-1-g71df317"}],"default-track":null,"name":"scrcpy","snap":{"license":"Apache-2.0","name":"scrcpy","prices":{},"publisher":{"display-name":"sisco311","id":"jQgc0rEVirS9Mk0Ud0UWWPFSwlGF3yVu","username":"sisco311","validation":"unproven"},"snap-id":"M7yvgnqOvyQj64bolfpawIAEwHv7dQ5G","store-url":"https://snapcraft.io/scrcpy","summary":"Display and control your Android device","title":"scrcpy"},"snap-id":"M7yvgnqOvyQj64bolfpawIAEwHv7dQ5G"}
```



<a name="kYhNx"></a>
## npm
We're npm, Inc., the company behind Node package manager, the npm Registry, and npm CLI. We offer those to the community for free, but our day job is building and selling useful tools for developers like you. --[npm](https://www.npmjs.com/)<br />
<br />Reference:[https://blog.csdn.net/chenjh213/article/details/45692987](https://blog.csdn.net/chenjh213/article/details/45692987)<br />
<a name="BOK4s"></a>
### Install
```bash
npm install <registry-name>

## With mirror site
npm install <registry-name> --registry https://registry.npm.taobao.org

'''
Other Mirrows

https://registry.npmjs.org
https://r.cnpmjs.org
https://registry.npm.taobao.org
'''
```

<a name="jEM3l"></a>
### Mirrors
2.永久设置:
```bash
npm config set registry https://registry.npmjs.org  
npm config list #查看更新后的config设置
```



<a name="7uFqK"></a>

## apm
Atom pakcages manager

### mirror
```bash
apm config set registry http://registry.npm.taobao.org
```
reference: [提辖鲁](https://blog.csdn.net/lj402159806/article/details/76862981)
### install
```bash
apm install atom-latex
```


## flatpak

<a name="8tiox"></a>
### What is flatpak?
Flatpak is a next-generation technology for building and distributing desktop applications on Linux. Flatpak is developed by an independent community, made up of contributors, volunteers and supporting organizations. It is a true upstream open source project, dedicated to providing technology and services that can be used by all, with no vendor lock-in. We have strong links to other Free Software projects, including the Freedesktop project. --[Flatpck](https://www.flatpak.org/)

<a name="tI1qp"></a>
### Install flatpak
```bash
apt install flatpak
apt install gnome-software-plugin-flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

To complete setup, restart your system. Now all you have to do is install some apps!

<a name="sbeDx"></a>
### Install and run apps from flatpak

```bash
## isntall OBS
flatpak install flathub com.obsproject.Studio

## run OBS
flatpak run com.obsproject.Studio
```
