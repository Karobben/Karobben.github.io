---
title: "npyscreen | An python TUI lib for development"
ytitle: "npyscreen | 一個簡單的Python  TUI 庫的簡單介紹"
description: "npyscreen"
url: npyscreen2
date: 2020/09/12
toc: true
excerpt: "Npyscreen is a python widget library and application framework for programming terminal or console applications. It is built on top of ncurses, which is part of the standard library."
tags: [Python, TUI lib]
category: [Python, TUI, others]
cover: 'https://s1.ax1x.com/2020/06/22/NYNrZj.png'
thumbnail: 'https://s1.ax1x.com/2020/06/22/NYNrZj.png'
priority: 10000
---
## npyscreen

![NYNciq.png](https://s1.ax1x.com/2020/06/22/NYNciq.png)
开发terminal平台软件<br />Developing terminal platform apps

<a name="N356a"></a>
## 1 Quick Start

```python
##!/usr/bin/env python3.7
## encoding: utf-8

import npyscreen
class TestApp(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "Welcome to Npyscreen",)
        t  = F.add(npyscreen.TitleText, name = "Text:",)
        fn = F.add(npyscreen.TitleFilename, name = "Filename:")
        fn2 = F.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
        s  = F.add(npyscreen.TitleSlider, out_of=12, name = "Slider")
        ml = F.add(npyscreen.MultiLineEdit,
               value = """try typing here!\nMutiline text, press ^R to reformat.\n""",
               max_height=5, rely=9)
        ms = F.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One",
                values = ["Option1","Option2","Option3"], scroll_exit=True)
        ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, value = [1,], name="Pick Several",
                values = ["Option1","Option2","Option3"], scroll_exit=True)
        # This lets the user interact with the Form.
        F.edit()
        print(ms.get_selected_objects())

if __name__ == "__main__":
    App = TestApp()
    App.run()
```

效果：
![NYNsds.png](https://s1.ax1x.com/2020/06/22/NYNsds.png)

<a name="vvtzJ"></a>
## Features
<a name="TVnYP"></a>
###
<a name="CyyAV"></a>
### Input
![NYNyon.png](https://s1.ax1x.com/2020/06/22/NYNyon.png)


<a name="Vwq2t"></a>
### Path segestion

<a name="hxo9y"></a>
#### Path1:
Tab 键激活<br />
![NYNrZj.png](https://s1.ax1x.com/2020/06/22/NYNrZj.png)

<a name="S2ZQy"></a>
#### Path2:
![NYNgJ0.png](https://s1.ax1x.com/2020/06/22/NYNgJ0.png)


<a name="Gih3Z"></a>
### Date
![NYN0sg.png](https://s1.ax1x.com/2020/06/22/NYN0sg.png)

<a name="FqeOj"></a>
### Progress bar
![NYNwQS.png](https://s1.ax1x.com/2020/06/22/NYNwQS.png)

<a name="Nvocx"></a>
### Selection
![NYNBLQ.png](https://s1.ax1x.com/2020/06/22/NYNBLQ.png)
[ptop](https://github.com/darxtrix/ptop) is npyscreen apps
