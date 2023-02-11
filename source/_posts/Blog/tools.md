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
tags: [Software, Linux, Tools]
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

## Videos tools

For linux:
Video Editor: [Kdenlive](https://kdenlive.org/en/)
![© Kdenlive](https://kdenlive.org/wp-content/uploads/2022/05/photo_2022-05-28_01-11-01.jpg)

Video mate information: mediainfo
```bash
sudo apt install mediainfo
mediainfo test.mp4
```

<pre>
General
Complete name                            : 20210613_Desat1-V330035-Hnf4-HA-29C_8d_OR_5d_.MP4
Format                                   : MPEG-4
Format profile                           : Base Media
Codec ID                                 : isom (isom/iso2/avc1/mp41)
File size                                : 131 MiB
Duration                                 : 18 min 10 s
Overall bit rate                         : 1 004 kb/s
Writing application                      : Lavf58.29.100

Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 4 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 4 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 18 min 10 s
Bit rate                                 : 1 000 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 30.000 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.016
Stream size                              : 130 MiB (100%)
Writing library                          : x264 core 155 r2917 0a84d98
Encoding settings                        : cabac=1 / ref=3 / deblock=1:0:0 / analyse=0x3:0x113 / me=hex / subme=7 / psy=1 / psy_rd=1.00:0.00 / mixed_ref=1 / me_range=16 / chroma_me=1 / trellis=1 / 8x8dct=1 / cqm=0 / deadzone=21,11 / fast_pskip=1 / chroma_qp_offset=-2 / threads=12 / lookahead_threads=2 / sliced_threads=0 / nr=0 / decimate=1 / interlaced=0 / bluray_compat=0 / constrained_intra=0 / bframes=3 / b_pyramid=2 / b_adapt=1 / b_bias=0 / direct=1 / weightb=1 / open_gop=0 / weightp=2 / keyint=250 / keyint_min=25 / scenecut=40 / intra_refresh=0 / rc_lookahead=40 / rc=abr / mbtree=1 / bitrate=1000 / ratetol=1.0 / qcomp=0.60 / qpmin=0 / qpmax=69 / qpstep=4 / ip_ratio=1.40 / aq=1:1.00
Codec configuration box                  : avcC
</pre>

### Biology

- [Biologic Models](https://biologicmodels.com/)
- [Science Photo Library](https://www.sciencephoto.com/)
