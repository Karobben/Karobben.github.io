---
toc: true
url: tools
covercopy: <a href="https://www.shutterstock.com/image-vector/programming-software-interface-on-device-by-1095220634">© aurielaki</a>
priority: 10000
date: 2021-10-16 23:30:43
title: "Tools/Softwares collection, technology changes your life"
ytitle: "各种软件收集"
description: "Different kinds of apps/software collection for Linux mainly, you may never know that Linux can't down so much of things!"
excerpt: "Different kinds of apps/software collection for Linux mainly, you may never know that Linux can't down so much of things!"
tags: [Software, Linux]
category: [others, Blog, Sharing]
cover: "https://image.shutterstock.com/z/stock-vector-programming-software-interface-on-device-by-engineers-application-for-company-project-a-space-of-1095220634.jpg"
thumbnail: "https://image.shutterstock.com/image-vector/programming-windows-600w-526837729.jpg"
---

## Software

|Name|Platform|Discription|
|:-|:-|:-|
|Xmind| Windows/ Mac / Linux||
|Edraw| Windows/ Mac / Linux/ Android||
|[Flameshot](#Flameshot)| Linux/ Mac| The best, open source, cross platform Screen Shot App.|
|Adobe PDF Reader|(Linux)|Installation scripts show below|
| Other PDF reader| Linux||

### Biology

|Name|Platform|Discription|
|:-|:-|:-|
|[Alignment software List](https://en.wikipedia.org/wiki/List_of_sequence_alignment_software)|Linux|= = To many tools = =|
|[Phylogeny Programs List](https://evolution.genetics.washington.edu/phylip/software.pars.html)|Linux or more|More than 40 different kinds for sorftawres|


### Chemistry

|Name|Platform|Discription|
|:-|:-|:-|
|[Chemdoodle 2D](https://www.chemdoodle.com/#trial)|Win/Mac/Linux (15$/Mon)|One of the most powerful chemical structures drawer|
|[Chemdoodle 3D](https://www.chemdoodle.com/3d)|Win/Mac/Linux (15$/Mon)|One of the most powerful chemical structures drawer|

## Online Tools

Free Copyright Pictures:
  - [shutterstock](https://www.shutterstock.com/)
  - [Adobe Stock](https://stock.adobe.com/)

## Software

### Adobe PDF Reader
Reference: [Lubos Rendek; 2020](https://linuxconfig.org/how-to-install-adobe-acrobat-reader-on-ubuntu-20-04-focal-fossa-linux)

```bash
wget -O ~/adobe.deb ftp://ftp.adobe.com/pub/adobe/reader/unix/9.x/9.5.5/enu/AdbeRdr9.5.5-1_i386linux_enu.deb

## add i386 requirment for dpkg
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install libxml2:i386 libcanberra-gtk-module:i386 gtk2-engines-murrine:i386 libatk-adaptor:i386

sudo dpkg -i ~/adobe.deb
```

### Other PDF Reader

Reference: [Swapnil Tirthakar; 2017](https://linuxhint.com/top-10-pdf-readers-on-linux/)


Evince is ==recommended==

```bash
sudo apt-get install evince
```

More :
```bash
## okular
sudo apt-get install okular
## zathura
sudo apt-get install zathura
## GNU GV
sudo apt-get install gv
## MuPDF
sudo apt-get install mupdf
## ePDF Viewer
## Foxit Reader
  ### Download the Foixt first
cd /tmp
gzip –d FoxitReader_version_Setup.run.tar.gz
tar –xvf FoxitReader_version_Setup.run.tar
./FoxitReader_version_Setup.run

## Atril
sudo apt-get install atril

## Xpdf
sudo apt-get install xpdf

```

## Pictures

<span id="Flameshot"></span>
[Flameshot](https://flameshot.org/): The best, open source screen shot App cross platform. ([Github](https://github.com/flameshot-org/flameshot))

|![](https://flameshot.org/media/animatedUsage.gif)|
|:-:|
|[© Flameshot](https://flameshot.org/)|

### Biology

- [Biologic Models](https://biologicmodels.com/)
- [Science Photo Library](https://www.sciencephoto.com/)
