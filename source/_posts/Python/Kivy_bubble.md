---
title: "Kivy examples: bubble"
ytitle: "Kivy 案例: 複製黏貼按鈕彈窗"
description: "A kivy examples to build a bubble to pop out"
date: 2020/12/16
url: kivy_bubble
toc: true
excerpt: "A kivy examples to build a bubble to pop out"
tags: [Python, Kivy]
category: [Python, Kivy]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.dpHEt6VNif2n2c4ULEqQ7gHaDJ'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
priority: 10000
covercopy: '© dotmodus'
---


![kivy bubble](https://kivy.org/doc/stable/_images/bubble.jpg)
example from document

```python
'''
Bubble
======
Test of the widget Bubble.
'''
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.bubble import Bubble

Builder.load_string('''
<cut_copy_paste>
  size_hint: (None, None)
  size: (160, 120)
  pos_hint: {'center_x': .5, 'y': .6}
  BubbleButton:
    text: 'Cut'
  BubbleButton:
    text: 'Copy'
  BubbleButton:
    text: 'Paste'
''')

class cut_copy_paste(Bubble):
  pass

class BubbleShowcase(FloatLayout):

  def __init__(self, **kwargs):
    super(BubbleShowcase, self).__init__(**kwargs)
    self.but_bubble = Button(text='Press to show bubble')
    self.but_bubble.bind(on_release=self.show_bubble)
    self.add_widget(self.but_bubble)

  def show_bubble(self, *l):
    if not hasattr(self, 'bubb'):
      self.bubb = bubb = cut_copy_paste()
      self.add_widget(bubb)
    else:
      values = ('left_top', 'left_mid', 'left_bottom', 'top_left',
        'top_mid', 'top_right', 'right_top', 'right_mid',
        'right_bottom', 'bottom_left', 'bottom_mid', 'bottom_right')
      index = values.index(self.bubb.arrow_pos)
      self.bubb.arrow_pos = values[(index + 1) % len(values)]


class TestBubbleApp(App):

  def build(self):
    return BubbleShowcase()

if __name__ == '__main__':
  TestBubbleApp().run()
```


## Show bubble when touch the Input box

origin source: [ikolim, stackoverflow](https://stackoverflow.com/questions/47552735/kivy-python-textinput-display-bubble)
```python
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Clipboard = None
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock

import time
class CustomBubbleButton(BubbleButton):
    pass


class NumericKeyboard(Bubble):
    layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(NumericKeyboard, self).__init__(**kwargs)
        self.create_bubble_button()


    def create_bubble_button(self):
        numeric_keypad = [Clipboard.paste()]
        for x in numeric_keypad:
            if len(x) == 0:
                self.layout.add_widget(Label(text=""))
            else:
                bubb_btn = CustomBubbleButton(text=str(x))
                self.layout.add_widget(bubb_btn)
                #Clock.schedule_once(self.REMOVE, 1)
                #self.layout.add_widget(bubb_btn)



class BubbleShowcase(FloatLayout):
    text_input = ObjectProperty(None)
    def REMOVE(self, dt):
        self.remove_widget(self.bubb)
        #print('12')


    def show_bubble(self, *l):
        # If you annotate this line, the wedge would survive from self.REMOVE by clicking the bubble.
        if not hasattr(self, 'bubb'):
            self.bubb = bubb = NumericKeyboard()
            self.bubb.arrow_pos = "bottom_mid"
            self.add_widget(self.bubb)
            # close the bubble after 3s
            Clock.schedule_once(self.REMOVE, 3)
            #self.remove_widget(self.bubb)



Builder.load_file("test.kv")


class TestBubbleApp(App):
    title = "Numeric Key Pad - Using Bubble"

    def build(self):
        return BubbleShowcase()


if __name__ == '__main__':
    TestBubbleApp().run()
```
*test.kv*
```kv
##:kivy 1.10.0

<CustomBubbleButton>:
    on_release:
        app.root.text_input.text += self.text


<NumericKeyboard>:
    layout: layout

    size_hint: (None, None)
    size: (160, 120)
    pos_hint: {'center_x': .5, 'y': .6}

    GridLayout:
        id: layout
        cols: 3

<BubbleShowcase>:
    text_input: text_input

    canvas:
        Color:
            rgba: 0, 1, 1, 1
        Rectangle:
            size: self.width, self.height
    TextInput:
        id: text_input
        pos_hint: {'center_x': .5, 'y': .54}
        size_hint: (0.2, 0.06)
        cursor_blink: True
        font_size: 20
        multiline: False
        on_focus:
            root.show_bubble()
```
![Kivy bubble table](https://s3.ax1x.com/2020/12/16/r15BnJ.gif)

So, by setting the clock, it could automatically vanished.
