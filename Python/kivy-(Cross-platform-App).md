---
url: kivy
---

# kivy (Cross-platform App)

<a name="2rtOx"></a>
# Quick Start

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579676243909-181d73d2-08fb-429f-ba49-97241f943039.png#align=left&display=inline&height=335&name=image.png&originHeight=335&originWidth=818&size=75474&status=done&style=none&width=818)

Kivy - Open source Python library for rapid development of applications that make use of innovative user interfaces, such as multi-touch apps.<br />

```python
# Creat a Hello.kv file in the path you run your script
vim Hello.kv

## this is for Hello.kv
BoxLayout:
    Label:
        text: "Hello"
```

```python
#!/usr/bin/python3.6

from kivy.app import App

class HelloApp(App):
    pass

if __name__ == '__main__':
    HelloApp().run()

```


<a name="cvtyF"></a>
## Text layout
```bash
# hello.kv file

BoxLayout:
    Label:
        text: "Hello"
    Label:
        text: "Beautiful"
    Label:
        text: "World"

```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579684472652-cb4aeadb-6103-41c8-b554-a3235f09e481.png#align=left&display=inline&height=530&name=image.png&originHeight=530&originWidth=647&size=51819&status=done&style=none&width=647)


<a name="Ak5Qi"></a>
## Button Layout
```bash
# hello.kv file
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

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579685096878-cce85f2a-af38-4d49-bf17-392f552fe31a.png#align=left&display=inline&height=339&name=image.png&originHeight=339&originWidth=824&size=76604&status=done&style=none&width=824)

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

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579685674530-2ef5fb0d-d1b6-42a9-8010-eeda15920c88.png#align=left&display=inline&height=337&name=image.png&originHeight=337&originWidth=846&size=119687&status=done&style=none&width=846)

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579684669733-8de7c333-bffc-4f07-be64-42b6882cef45.png#align=left&display=inline&height=335&name=image.png&originHeight=335&originWidth=843&size=91376&status=done&style=none&width=843)



<a name="lQqQJ"></a>
# Events

<a name="H5ps8"></a>
## Responding to Input
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
			id: search_box	# Assign an ID
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

main.py:
```python
#!/usr/local/bin/python3.7

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        print("The user searched for '{}'".format(self.search_input.text))
#
#
class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()

```

Image left: GUI Layout;    Image right: result was printed in terminal after clicked the button search. <br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579746354233-b05b0cf6-2e2c-48a6-92b5-040f18b771be.png#align=left&display=inline&height=200&name=image.png&originHeight=295&originWidth=493&size=32035&status=done&style=none&width=334)![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579746413033-7532438c-8296-426d-8aef-f7bb1ecf5f66.png#align=left&display=inline&height=200&name=image.png&originHeight=159&originWidth=307&size=7138&status=done&style=none&width=386)

In the current version Kivy1.11.1,<br />The function ListView is not is not supported.  <br />Use Recycle As instead.

Take this as example:<br />from: [https://stackoverflow.com/questions/56601384/kivy-unknown-class-listview-error-code](https://stackoverflow.com/questions/56601384/kivy-unknown-class-listview-error-code)<br />main.py
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

