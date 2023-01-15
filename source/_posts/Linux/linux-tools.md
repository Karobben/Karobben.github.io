---
toc: true
url: linux_tools
covercopy: <a href="https://pixabay.com/illustrations/developer-programmer-technology-3461405/">© kreatikar</a>
priority: 10000
date: 2022-06-22 12:14:24
title: 'fancy tools in linux'
ytitle: "Linux 好用的工具"
description: "For sharing some fancy tools for seeped up your work/or study"
excerpt: "For sharing some fancy tools for seeped up your work/or study"
tags: [Linux, Tools]
category: [Linux, Software]
cover: "https://cdn.pixabay.com/photo/2018/06/08/00/48/developer-3461405_1280.png"
thumbnail: "https://cdn.pixabay.com/photo/2018/06/08/00/48/developer-3461405_1280.png"
---

## Fancy Tools for Linux User

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>

- Office
- IDE
- System
- Media
- Bioinformatic


## Office

### Documents, Sheets, Powerpoints
- [WPS for Linux](https://www.wps.com/office/linux/)
![](https://website-prod.cache.wpscdn.com/img/slider_2.d1058e0.png)
- [ONLYOFFICE](https://www.onlyoffice.com/)
    <details><summary>snap shot for Gmonitor</summary>

    ![](https://static-www.onlyoffice.com/images/mainpage/dp-fscreen-bg-en.png)
    </details>

### Document format convert

- [Pandoc](https://pandoc.org/)
```bash
# HTML fragment:
pandoc MANUAL.txt -o example1.html
# Standalone HTML file:
pandoc -s MANUAL.txt -o example2.html
# HTML with table of contents, CSS, and custom footer:
pandoc -s --toc -c pandoc.css -A footer.html MANUAL.txt -o example3.html
# LaTeX:
pandoc -s MANUAL.txt -o example4.tex
```

## IDE

- [Vim](https://www.vim.org/)
![](https://files.realpython.com/media/vim-ide.90be624b30bf.png)
[© Real Python](https://realpython.com/vim-and-python-a-match-made-in-heaven/)
- [Atom](https://atom.io/)
![](https://opensource.com/sites/default/files/uploads/atom-31_days-atom-opensource.png)
[© Seth Kenlon](https://opensource.com/article/20/12/atom)
- [VScode](https://code.visualstudio.com/)
    <details><summary>snap shot for Gmonitor</summary>

    ![](https://code.visualstudio.com/assets/home/home-screenshot-linux-lg.png)
    </details>

## System

### Processes Monitor
#### CPU and RAM
- top
- htop
- gtop
- [gotop](https://github.com/cjbassi/gotop) (favorite)
![](https://github.com/cjbassi/gotop/raw/master/assets/demos/demo.gif)

#### GPU

- [nvtop](https://github.com/Syllo/nvtop) (favorite)
![](https://github.com/Syllo/nvtop/raw/master/screenshot/NVTOP_ex1.png)
- [gmonitor](https://github.com/mountassir/gmonitor)
    <details><summary>snap shot for Gmonitor</summary>

    ![](https://camo.githubusercontent.com/33950f77e2e496db3b225242ff0c560f372a4f47fc56750357327b43c2a6570f/68747470733a2f2f692e696d6775722e636f6d2f49747447346b622e706e67)
    </details>


## Media

### Audio
Play music in terminal
```bash
sudo apt-get install sox
sudo apt-get install sox libsox-fmt-all
play test.mp3
```
|![](https://www.unixmen.com/wp-content/uploads/2013/05/sox_play.png)|
|:-:|
|[© Enock Seth Nyamador](https://www.unixmen.com/how-to-play-music-from-command-line-terminal/)|

### Video

Print mate information of a Video
```bash
mediainfo test.mp4
```

<pre>
General
Complete name                            : test.mp4
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


- ffmpeg: Crop; stream etc.
Link [ffmpeg accelerate with NVIDA GPU](https://docs.nvidia.com/video-technologies/video-codec-sdk/ffmpeg-with-nvidia-gpu/)
The most awesome thing is ffmpeg support GPU accelerating which could make video cropping much faster than traditional way.  

- Kdenlive

```bash
libmovit-dev
libmovit8
```
