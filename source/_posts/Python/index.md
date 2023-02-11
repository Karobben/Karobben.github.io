---
title: "index"
description: "index"
date: 2020/01/22
excerpt: "Don't Click"
priority: 100000
---

- # Introduction
	- [pip](pip.html)
	- [base](base.html)
	- [Encode_decode](Encode_decode.html)
	- [FTP Server](ftp)

- # library for Scripts
  - [argparse](argparse.html)
  - [itchat](itchat.html)
  - [json](json.html)
  - [Matplotlib](Matplotlib.html)
  - [multyprocesser](multyprocesser.html)
  - [numpy](numpy.html)
  - [OpenCV](OpenCV.html)
  - [Pandas](Pandas.html)
  - [PDF](PDF.html)
  - [PIL_np.array](PIL_np.array.html)
  - [Plot-in-the-Terminal](Plot-in-the-Terminal.html)
  - [popmail](popmail.html)
  - [pynput](pynput.html)
  - [Tensorflow](Tensorflow.html)
  - [wordcloud](wordcloud.html)

- # Biology
  - [Biopython](Biopython.html)
  - [Sanger Sequencing Plot](Bio_SSP.html)

- # Developer
  - ## TUI
    - [TUI-libs](TUI-libs.html)
    - [npyscreen](npyscreen.html)
    - [urwid](urwid.html)
  - ## GUI
    - [QT](QT.html)
    - # [kivy_Cross-platform-App](kivy_Cross-platform-App.html)
    - [kivy-Buildozer](kivy-Buildozer.html)
    - Learn Kivy from Sent
      - [1. Hello World](Kivy_sent1.html)
      - [3. Screen Manager](Kivy_sent3.html)
    - Kivy widgets
      - [Draw Lines](Kivy_sline.html)
      - [import android](kivy_platform.html)
      - [ScrollView](kivy_scrollview.html)
      - [Bubble](Kivy_bubble.html)
    - [Kivy: Filechooser](kivy_filechooser.html)
    - [Kivy tips & tricks](kivy_tips.html)
- # Blogs
  - [Opencv_Vedio_reverse.py](Vedio_reverse.py.html)
  - [Opencv_VedioSlice.py](VedioSlice.py.html)
  - [Opencv_Lightening-Img](Lightening-Img.html)
  - [Opencv_gif](Opencv_gif.html)
  - [Tensorflow-Numbers-k](Tensorflow-Numbers-k.html)
  - [Transfer_Learning](Transfer_Learning.html)
  - [Crawler](Crawler.html)
  - [BaseMap](BaseMap.html)
  - [HTML-server](HTML-server.html)
  - [Animation-Text](Animation-Text.html)
  - [Others](Others.html)

```bash
ls | awk '{print "["$1"]("$i")"}'| sed 's/\.md]/]/;s/\.md)/\.html)/;/yuque.yml/d;/(summary.html)/d' > P-index.md
```
