---
toc: true
url: kivy_inaction_tb_7
priority: 10000
date: 2021-05-10 01:26:53
title: "Kivy for android in action: Web Service"
ytitle: "Kivy安卓实战:7 |网页浏览器| 寫個工具箱把7"
excerpt: "Write a kivy toolbox for yourselves."
description: "Write a kivy toolbox for yourselves."
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

Because I was using my blog project to doing the test with this server, so I called it as `Blog.py`

Function `run_sever` is for starting the http server so you can render CSS and applying `js`, `close_blog` could close the server and back to home directory.

```python Blog.py
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.utils import platform
import os
import webbrowser, time
import threading

class FunctionWidget():

    def main(self):
        Builder.unload_file("Layout/Blog.kv")
        self.Function_page = Builder.load_file("Layout/Blog.kv")
        self.Function_page.ids.buton_start.on_release = self.open_blog
        self.Function_page.ids.buton_close.on_release = self.close_blog
        return self.Function_page

    def run_sever(self):
        import http.server
        import socketserver
        PORT = 5500
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", PORT), Handler) as self.httpd:
            print("serving at port", PORT)
            self.httpd.serve_forever()

    def close_blog(self):
        PATH = os.path.abspath(__file__).split("libWidget")[0].replace("appc","app")
        print(PATH)

        try:
            self.httpd.shutdown()
            os.chdir(PATH)
        except:
            os.chdir(PATH)

    def open_blog(self, *args):
        if platform == "android":
            from libs.webview import WebView
        os.chdir("Blog")
        PATH = os.path.abspath(__file__).split("libWidget")[0].replace("appc","app")
        URL = 'file://'+PATH+'/demo/clustal/123.html',
        URL = 'http://127.0.0.1:5500/'
        print("URL = ", URL)
        x = threading.Thread(target=self.run_sever, args=())
        x.start()
        print("Started, test")
        if platform == "android":
            self.browser = None
            self.browser = WebView(URL,
                                   enable_javascript = True,
                                   enable_downloads = True,
                                   enable_zoom = True)
        else:
            try:
                webbrowser.open('http://127.0.0.1:5500/')
            except:
                pass
```

## Layout

`Blog.py`

```kv Blog.kv
MDBoxLayout:
    MDRectangleFlatButton:
        id: buton_start
        text: "Start Server"
        on_release: None
        pos_hint: {"center_x": .5, "center_y": .5}
    MDRectangleFlatButton:
        id: buton_close
        text: "Close Server"
        on_release: None
        pos_hint: {"center_x": .5, "center_y": .5}
```


## Functions for webview
This function was written by [RobertFlatt](https://github.com/RobertFlatt) and published in [ RobertFlatt /Android-for-Python ](https://github.com/RobertFlatt/Android-for-Python/tree/main/webview). He also contributed lots of other awesome functions and examples of widgets.

I copied his `webview.py` to `libs` directory. An example of using it:
```python
if platform == "android":
    from libs.webview import WebView
    self.browser = None
    self.browser = WebView(URL,
                           enable_javascript = True,
                           enable_downloads = True,
                           enable_zoom = True)
```  
