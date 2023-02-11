---
title: "Kivy: hello world (Cross-platform GUI) for python"
ytitle: "Kivy | 跨平臺軟件開發"
description: "kivy A Cross-platform GUI for python; codes for newbies"
url: kivy2
date: 2020/12/16
toc: true
excerpt: "kivy A Cross-platform GUI for python; codes for newbies"
tags: [Python, Kivy]
category: [Python, Kivy]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.dpHEt6VNif2n2c4ULEqQ7gHaDJ'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
priority: 3
covercopy: '© dotmodus'
---


## Install
```bash
sudo add-apt-repository ppa:kivy-team/kivy-daily

sudo apt-get update

sudo apt-get install python-kivy
```
```python
sudo python3.7 -m pip install --upgrade pip wheel setuptools bcm

sudo python3.7 -m pip install docutils pygments  

sudo python3.7 -m pip install kivy.deps.gstreamer --extra-index-url https://kivy.org/downloads/packages/simple/

```
## Quick Start

![Kivy hello world](https://s1.ax1x.com/2020/06/22/NYEbGt.png)

Kivy - Open source Python library for rapid development of applications that make use of innovative user interfaces, such as multi-touch apps.<br />

```python
## Creat a Hello.kv file in the path you run your script
vim hello.kv

### this is for Hello.kv
BoxLayout:
    Label:
        text: "Hello"
```

```python
##!/usr/bin/python3.6

from kivy.app import App

class HelloApp(App):
    pass

if __name__ == '__main__':
    HelloApp().run()

```

You need to name the `kv` file as `hello.kv`.
This file is target by the function `HelloApp` in `main.py` automatically.

<a name="cvtyF"></a>
### Text layout
```bash
## hello.kv file

BoxLayout:
    Label:
        text: "Hello"
    Label:
        text: "Beautiful"
    Label:
        text: "World"

```

![Kivy boxlayout](https://s1.ax1x.com/2020/06/22/NYEjsS.png)


<a name="Ak5Qi"></a>
### Button Layout
```bash
## hello.kv file
AddLocationForm:

<AddLocationForm@BoxLayout>:
    orientation: "vertical"
    BoxLayout:
        TextInput:
        Button:
            text: "Search"
            size_hint_x: 1
            size_hint_y: 0.3
        Button:
            text: "Current Location"
            size_hint_x: 0.5

```
![Kivy input](https://s1.ax1x.com/2020/06/22/NYEXM8.png)

```bash
AddLocationForm:

<AddLocationForm@BoxLayout>:
    orientation: "vertical"
    BoxLayout:
        height: "40dp"
        size_hint_y: None
        TextInput:
            size_hint_x: 50
        Button:
            text: "Search"
            size_hint_x: 25
        Button:
            text: "Current Location"
            size_hint_x: 25
    BoxLayout:
        Label:
            text: "Palo Alto, MX\nPalo Alto, US"
```

![Kivy Recycle view](https://s1.ax1x.com/2020/06/22/NYELxf.png)
![Kivy weather app](https://s1.ax1x.com/2020/06/22/NYEqRP.png)


<a name="lQqQJ"></a>
## Events

<a name="H5ps8"></a>
### Responding to Input
In this section, We'd like to acquire the input information from the input box.<br />For respond the Input message, two things we need to done:

1. Assign an ID for TextInput
  1. line 5: Acquiring Input.
  1. line 10: Assign the ID "search_box" to  TextInput Box 
  1. line 15: active function search_location()
2. Assign an function for responding the text
  1. line 5: import the function
  1. line 11-12: assigning the function to acquire and respond the massage from TextInput

Weather.kv:
```bash
AddLocationForm:

<AddLocationForm@BoxLayout>:
    orientation: "vertical"
    search_input: search_box # Change one
    BoxLayout:
        height: "40dp"
        size_hint_y: None
        TextInput:
            id: search_box  # Assign an ID
            size_hint_x: 50
        Button:
            text: "Search"
            size_hint_x: 25
            on_press: root.search_location()
        Button:
            text: "Current Location"
            size_hint_x: 25
    BoxLayout:
        Label:
            text: "Palo Alto, MX\nPalo Alto, US"
```

`main.py`:
```python
##!/usr/local/bin/python3.7

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        print("The user searched for '{}'".format(self.search_input.text))
##
##
class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()

```

Image left: GUI Layout;    Image right: result was printed in terminal after clicked the button search. <br />
![Kivy weatehr app](https://s1.ax1x.com/2020/06/22/NYEHPI.png)
![Kivy weather app](https://s1.ax1x.com/2020/06/22/NYV6eg.png)
In the current version Kivy1.11.1,<br />The function ListView is not is not supported.  <br />Use Recycle As instead.

Take this as example:<br />from: [https://stackoverflow.com/questions/56601384/kivy-unknown-class-listview-error-code](https://stackoverflow.com/questions/56601384/kivy-unknown-class-listview-error-code)
`main.py`

### Light Weather App
```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder

import json


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()

    def search_location(self):
        search_template = "https://samples.openweathermap.org/data/2.5/find?q={}&appid=b6907d289e10d714a6e88b30761fae22"
        # search_template = "https://api.openweathermap.org/data/2.5/find?q={}&typle=like&appid=xyz"    # Replace 'xyz' with your API Key (APPID)
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        cities = ["{} ({})".format(d['name'], d['sys']['country']) for d in data['list']]
        self.search_results.data = [{'text': str(x)} for x in cities]
        print(f"self.search_results.data={self.search_results.data}")


class WeatherRoot(BoxLayout):
    pass


class TestApp(App):
    title = "Weather App"

    def build(self):
        return Builder.load_file("main.kv")


if __name__ == '__main__':
    TestApp().run()
```

mian.kv
```bash
WeatherRoot:

<WeatherRoot>:
    AddLocationForm:

<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (1, 0, 0, 1) if self.selected else (.0, 0.9, .1, .3)
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: (0, 0.9, .1, .3)
        Rectangle:
            pos: self.pos
            size: self.size

<AddLocationForm>:
    orientation: "vertical"

    search_input: search_input
    search_results: search_results_list

    BoxLayout:
        height: "40dp"
        size_hint_y:None

        TextInput:
            id: search_input
            size_hint_x: 50
            focus: True
            multiline: False
            hint_text: 'Your city name'
            on_text_validate: root.search_location()


        Button:
            text: "Search"
            size_hint_x: 25
            on_press: root.search_location()

        Button:
            text: "Current Location"
            size_hint_x: 25

    RecycleView:
        id: search_results_list

        viewclass: 'SelectableLabel'

        SelectableRecycleBoxLayout:
            default_size: None, dp(26)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            multiselect: True
            touch_multiselect: True
```

## Examples
### UrlRequest

Origin from:[coder.work](https://www.coder.work/article/2009103)
```python
from kivy.app import App
##kivy.require("1.9.1")
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest

class MyWidget(BoxLayout):
    def __init__(self,**kwargs):
        super(MyWidget,self).__init__(**kwargs)
        search_url = "http://api.openweathermap.org/data/2.5/forecast/daily?APPID=ef4f6b76310abad083b96a45a6f547be&q=new%20york"
        print search_url
        self.request = UrlRequest(search_url, self.res)
        print self.request
        print "Result: before success", self.request.result,"\n"


    def res(self,*args):
        print "Result: after success", self.request.result


class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()
```

## Some Awesome Blogs
[Build a Mobile Application With the Kivy Python Framework](https://realpython.com/mobile-app-kivy-python/#creating-a-kivy-application) Mike Driscoll  Nov 04, 2019

[Official Gallery](https://kivy.org/doc/stable/examples/gallery.html)
