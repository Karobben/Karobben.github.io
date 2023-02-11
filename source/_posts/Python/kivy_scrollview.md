---
title: "kivy ScrollView"
ytitle: "Kivy, scrollview 自動調節大小"
description: "kivy widget: ScrollView | auto fit to the high of the widget"
date: 2021/02/10
url: kivy_scrollview
toc: true
excerpt: "How to insert widgets into ScrollView appropriately"
tags: [Python, Kivy]
category: [Python, Kivy]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.dpHEt6VNif2n2c4ULEqQ7gHaDJ'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
priority: 10000
covercopy: '© dotmodus'
---


[Official Document](https://kivy.org/doc/stable/api-kivy.uix.scrollview.html)

However, examples from the official document have shown the basics of this widget. But for newbies, it is easy to write an unworking widget due to a lack of understanding of it.

## Quick Start
```python
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
## Make sure the height is such that there is something to scroll.
layout.bind(minimum_height=layout.setter('height'))
for i in range(100):
    btn = Button(text=str(i), size_hint_y=None, height=40)
    layout.add_widget(btn)
root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)

runTouchApp(root)
```

## Why Am I failed to scroll my widget
The problem is that after you settled everything in your `kv` file, the sub-widget has the same size as the ScrollView widget by default. So, to have a functional scrolling behavior, you'd like to make sure the sub-widget is larger than the ScrollView widget. Let's go back to the example from the document:
```kv
ScrollView:
    do_scroll_x: False
    do_scroll_y: True

    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        padding: 10, 10
        text:
            'really some amazing text\n' * 100
```
In this `kv` file, two lines are important to redefine the height of this sub-widget.
```kv
size_hint_y: None
height: self.texture_size[1]
```
The problem is `self.texture_size[1]` is for text only. You'd like to replace it with an int, 1000, for example.

But of course, there is a better resolution from [@amd, 2015](https://stackoverflow.com/questions/32445341/kivy-scrollview-not-scrolling)
```kv
height: self.minimum_height
```

An example could show as:
```kv
ScrollView:
    size: 300, 20
    do_scroll_x: False
    do_scroll_y: True

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        padding: 10, 10

        MyButton:
          text: 'hit me 1'
        MyButton:
          text: 'hit me 2'
        MyButton:
          text: 'hit me 3'
        MyButton:
          text: 'hit me 4'
        MyButton:
          text: 'hit me 5'
        MyButton:
          text: 'hit me 6'
```

***Case closed!!!***
