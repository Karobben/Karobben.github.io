---
toc: true
url: kivy_inaction_tb_9
priority: 10000
date: 2021-05-15 23:26:53
title: "Kivy for android in action:Show opencv result in Kivy desktop"
ytitle: "Kivy安卓实战:9 |Kivy现实opencv结果| 寫個工具箱把9"
excerpt: "An example of kivy show the result of OpenCV | Kivy for Android"
description: "An example of kivy show the result of OpenCV | Kivy for Android"
tags: [Python, Kivy]
category: [Python, Kivy, Toolbox]
cover: 'https://kivy.org/static/images/kivy-colorwheel-examples.jpg'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
covercopy: '<a href="https://kivy.org/">© kivy</a>'
---

```
CryptoWatch-Kivy          1.13
Kivy                      2.0.0
Kivy-Garden               0.1.4
kivy-garden.wordcloud     1.0.0
kivymd                    0.104.2.dev0
```

```graphviz
digraph{
  rankdir = "LR"
  mm1 [label ="", height = 0, width = 0, shape = none]
  mm2 [label ="", height = 0, width = 0, shape = none]
  mm3 [label ="", height = 0, width = 0, shape = none]
  mm4 [label ="", height = 0, width = 0, shape = none]
  mm5 [label ="", height = 0, width = 0, shape = none]
  mm6 [label ="", height = 0, width = 0, shape = none]
  mm7 [label ="", height = 0, width = 0, shape = none]
  mm8 [label ="", height = 0, width = 0, shape = none]
  mm9 [label ="", height = 0, width = 0, shape = none]

  Navigation [URL="/2021/04/26/Python/kivy-inaction-tb-1/#Navigation", fontcolor = "#3273DC"]
  Navigation_S [URL="/2021/04/26/Python/kivy-inaction-tb-1/#Separate-the-KV-and-PY", fontcolor = "#3273DC"]
  Tags [URL ="/2021/04/26/Python/kivy-inaction-tb-1/#Tags", fontcolor = "#3273DC"]
  FF [label="Font Switch"; URL ="/2021/04/26/Python/kivy-inaction-tb-1/#First-Function", fontcolor = "#3273DC"]
  FileChooser [label="File Chooser"; URL ="/2021/04/28/Python/kivy-inaction-tb-2/#Filechooser", fontcolor = "#3273DC"]
  Menu [label="Menu"; URL ="/2021/04/30/Python/kivy-inaction-tb-3/#Write-is-as-a-widget", fontcolor = "#3273DC"]
  Editor [label="Editor"; URL ="/2021/05/08/Python/kivy-inaction-tb-6/", fontcolor = "#3273DC"]

  node [shape = "box"]
  Navigation_S [label = "Separate the KV and PY"]
  Navigation -> mm2
  mm3 -> Navigation_S [dir=back]
  Tags -> mm4
  mm5 -> FF -> Slider[dir=back]
  FileChooser -> mm6
  mm7 -> Menu [dir=back]
  Menu -> FF
  mm8-> Editor [dir = back]
  subgraph A{
    rank = same
    mm1 -> mm2 -> mm3 -> mm4 -> mm5 -> mm6 -> mm7 -> mm8 -> mm9 [dir = "none"]
  }
}
```

## Quick Review
```bash
tree
```
<pre style= "color:#76EE00; background-color:#363636">
  .
  ├── 123.fa
  ├── 123.html
  ├── Karobben_logo_horizontal_800.png
  ├── LICENSE
  ├── Layout
  │   ├── Blog.kv
  │   ├── CV_cm.kv
  │   ├── CV_test.kv
  │   ├── Data_table.kv
  │   ├── Font.kv
  │   ├── Navigation_Draw.kv
  │   ├── Navigation_Tabs.kv
  │   ├── Seq.kv
  │   ├── editor.kv
  │   ├── filechooser.kv
  │   └── menu.kv
  ├── README.md
  ├── alipay.jpg
  ├── buildozer.spec
  ├── config
  │   ├── Navi.json
  │   └── home.json
  ├── custom_camera
  │   ├── __init__.py
  │   ├── custom_camera.kv
  │   └── custom_camera.py
  ├── demo
  │   ├── clustal
  │   └── echart
  ├── favicon.ico
  ├── font
  │   ├── ArtificialBox-WdD4.ttf
  │   ├── FangZhengHeiTiFanTi-1.ttf
  │   ├── FangZhengHeiTiJianTi-1.ttf
  │   ├── FangZhengKaiTiPinYinZiKu-1.ttf
  │   ├── FangzhenXiaozhuan.ttf
  │   ├── HuaKangXinZhuanTi-1.ttf
  │   ├── JingDianFanJiaoZhuan-1.ttf
  │   ├── heydings-controls-1.ttf
  │   ├── heydings-icons-1.ttf
  │   ├── heydings-icons-2.ttf
  │   └── icon-works-webfont-2.ttf
  ├── image_processing
  │   ├── __init__.py
  │   ├── cascades
  │   │   └── haarcascade_frontalface_default.xml
  │   └── image_processing.py
  ├── libWidget
  │   ├── Blog.py
  │   ├── CV_cm.py
  │   ├── CV_test.py
  │   ├── Data_table.py
  │   ├── Font.py
  │   ├── Seq.py
  │   ├── editor.py
  │   ├── filechooser.py
  │   ├── menu.py
  │   └── model.txt
  ├── libs
  │   ├── bio_seq.py
  │   ├── clustalo.py
  │   ├── clustalo.pytxt
  │   ├── web_open.py
  │   └── webview.py
  ├── logo.png
  ├── main.py
  └── wepay.png
</pre>

## Function for Close Tab

This script originally contributed by [okajun35](https://github.com/okajun35/kivy_show_opencv_pillow) in GitHub.

`CV_cm.py`

```python CV_test.py
# -*- coding: utf-8 -*
import numpy as np
import cv2
from kivy.uix.boxlayout import BoxLayout

from PIL import Image
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle


class FunctionWidget():

    def main(self):
        Builder.unload_file("Layout/test.kv")
        self.Function_page = Builder.load_file("Layout/test.kv")
        self.Function_page.ids.button_load.on_release= self.run
        return self.Function_page

    def run(self, *args):
        img = cv2.imread('logo.png')
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # 画像をグレイスケールに変換
        #gray_img = cv2.cvtColor(img,1)
        texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='rgb', bufferfmt='ubyte') # BGRモードで用意,ubyteはデフォルト引数なので指定なくてもよい
        texture.blit_buffer(img.tostring(),colorfmt='rgb', bufferfmt='ubyte')  # ★ここもBGRで指定しないとRGBになって色の表示がおかしくなる
        texture.flip_vertical()
        self.Function_page.show_pic  = texture
```

## Layout

`CV_cm.kv`
```kv CV_test.kv
BoxLayout:
    orientation: "vertical"
    show_pic: None
    BoxLayout:
        canvas:
            Rectangle:
                texture: root.show_pic
                pos: self.pos
                size: self.size
                #pos_hint: {'center_x': .5, 'center_y': .5}
                #color: 0, 0, 0, 1
    BoxLayout:
        orientation: "vertical"
        BoxLayout
            MDRaisedButton:
                id: button_load
                text: 'F'
                font_size: 30
                font_name: './font/heydings-icons-1'
                width: root.width * 0.5
                line_color: 1, 1, 1, 1
```

It works on PC not in androied. And I don't know why.
