---
title: "Kivy: Screen Communication"
ytitle: "Kivy: 不同屏幕之間的參數傳遞"
toc: true
date: 2021-03-09 11:26:45
description: "Sharing　the argument among different screens, manager.get_screen"
url: kivy_screen_commu
excerpt: "Sharing　the argument among different screens, `manager.get_screen`"
tags: [Python, Kivy]
category: [Python, Kivy]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.dpHEt6VNif2n2c4ULEqQ7gHaDJ'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
priority: 10000
covercopy: '© dotmodus'
---

## Quick view
|![Kivy screen arguments sharing](https://s3.ax1x.com/2021/03/09/61xWZV.gif)|
|:--:|
|(c) Karobben|


This work originated from @一个哲学家[^一个哲学家_2021]

[^一个哲学家_2021]: 一个哲学家; 2021; 今日头条; [kivy教程：实现屏幕切换、数据传递和函数绑定](https://www.toutiao.com/i6936906683163820557/)

Here is the `main.py`

```python main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from kivy.core.text import LabelBase

class NewGameScreen(Screen):
    class Gao(Widget):
        label = ObjectProperty(None)
        def btn(self,label):
            label.text='AFTER PROCESSING'+label.text

class OptionScreen(Screen):
    pass

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(NewGameScreen())
        sm.add_widget(OptionScreen())
        return sm

if __name__ == '__main__':
    TestApp().run()
```

here is the `test.kv`
```kv test.kv
<NewGameScreen>:
    name: 'newgame'
    label:label_id
    BoxLayout:
        orientation: 'vertical'

        TextInput:
            id:label_id
            text:'INPUT'
            on_text:
                root.manager.get_screen('options').label.text = str(self.text)

        Button:
            text: 'SUBMIT'
            on_press:
                root.Gao.btn(self,label_id)
                root.manager.transition.direction = 'left'
                root.manager.current = 'options'
                root.manager.current = 'options' if label_id.text == '123' else "newgame" #输入为 123 时才跳转

<OptionScreen>:
    label: label_id
    name: 'options'
    orientation: 'vertical'
    BoxLayout:
        Button:
            text: 'BACK'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'newgame'

        Label:
            id: label_id
            text: '1'
```

### Similar Resolution

This script was also communicate the different classes by using `manager.get_screen` @Nykakin[^Nykakin_2015]

[^Nykakin_2015]: [Psionman; 2015; How to update label text on second kivy screen; StackOverflow](https://stackoverflow.com/questions/33498120/how-to-update-label-text-on-second-kivy-screen)

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

Builder.load_string('''
<MainScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Goto strategy'
            on_press: root.manager.current = 'strategy'
        Button:
            text: 'Set text'
            on_press: root.SetText()

<StrategyScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: root.labelText
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'main'
''')

class MainScreen(Screen):
    def SetText(self):
        text = 'Total=' + str(17*21)
        self.manager.get_screen('strategy').labelText = text

class StrategyScreen(Screen):
    labelText = StringProperty('My label')

class TestApp(App):
    def build(self):
        # Create the screen manager
        screenManager = ScreenManager()
        screenManager.add_widget(MainScreen(name='main'))
        screenManager.add_widget(StrategyScreen(name='strategy'))
        return screenManager

if __name__ == '__main__':
    TestApp().run()
```

## Another Example:
@Taher Kawantwala[^ikolim_2018]

[^ikolim_2018]: [Taher Kawantwala; 2018; Kivy Change Label widget Text from another class; StackOverflow](https://stackoverflow.com/questions/49505616/kivy-change-label-widget-text-from-another-class)

`main.py`

```python main.py
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


class ConfirmPopup(BoxLayout):

    def __init__(self, **kwargs):
        self.register_event_type('on_answer')
        super(ConfirmPopup, self).__init__(**kwargs)
        self.total_images = 0

    def on_answer(self, filename, JKMain):
        self.total_images = 8
        print("JKMain=", JKMain)
        JKMain.change_text(self.total_images)


class JKMain(AnchorLayout):
    def __init__(self, **kwargs):
        super(JKMain, self).__init__(**kwargs)

    def change_text(self, layers):
        self.the_time.text = "Total Layers : " + str(layers)
        print("Total Layers = " + str(layers))

    def popup_func(self):

        content = ConfirmPopup()
        content.bind(on_answer=self._on_answer)
        self.popup = Popup(title="Select .zip file",
                           content=content,
                           size_hint=(None, None),
                           size=(500, 500),
                           auto_dismiss=False)
        self.popup.open()

    def _on_answer(self, instance, answer, obj):
        self.popup.dismiss()


class Main(App):

    def build(self):
        return JKMain()


if __name__ == "__main__":
    Main().run()
```

`main.ky`
```kv main.kv
#: kivy 1.10.0

<JKmain>:
    the_time: _id_lbl_time
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'
        BoxLayout:

            orientation: 'vertical'
            id: _tool_box
            size_hint: None,0.75
            width: 300

            Label:
                id: _id_lbl_time
                text: "Total Layers : "

    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'top'
        GridLayout:
            rows:2
            BoxLayout:
                orientation: 'horizontal'
                Button:
                    on_release: app.root.current = "main"
                    text: "SELECT"
                    size_hint: 1,0.2
                    background_color: (1.0, 1.0, 0.0, 1.0)
                    on_release: root.popup_func()
                Button:
                    text: "START"
                    size_hint: 1,0.2
                    background_color: (1.0, 0.0, 1.0, 1.0)
                    on_release: root.change_text(100)
                Button:
                    text: "EXIT"
                    size_hint: 1,0.2
                    background_color: (1.0, 0.0, 1.0, 1.0)
                    on_release: root.exit_app(self)

<ConfirmPopup>:
    BoxLayout:
        orientation: 'vertical'
        FileChooserIconView:
            id: filechooser
            filters: ['*.zip']

        GridLayout:
            cols: 2
            size_hint: 1,0.2
            Button:
                text: 'OK'
                on_release: root.dispatch('on_answer', filechooser.selection, app.root)
                size_hint: 1,0.2
            Button:
                text: 'Cancel'
                on_release: root.dispatch('on_answer', 'Cancel')
                size_hint: 1,0.2
```
