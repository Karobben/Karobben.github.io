---
title: "Kivy, Examples of Action bar"
description: "Kivy, Examples of Action bar| Kivy ,下拉菜单"
date: 2020/10/28
url: kivy_actionbar
toc: true
excerpt: "Some tips for kivy"
tags: [Python, Kivy]
category: [Python, Kivy]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.dpHEt6VNif2n2c4ULEqQ7gHaDJ'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
priority: 10000
covercopy: '© dotmodus'
---


## Kivy Action bar

Origin from: [ikolim 2019](https://stackoverflow.com/questions/55482899/how-to-add-an-action-bar-in-kivy-using-screenmanager-widget)

![B1LWJP.png](https://s1.ax1x.com/2020/10/28/B1LWJP.png)

`main.py`

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


class WelcomeScreen(Screen):
    pass


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ScreenManager(ScreenManager):
    pass


class CrimePrevention(BoxLayout):
    pass


Builder.load_file("main.kv")


class TestApp(App):
    title = 'Kivy ScreenManager & ActionBar Demo'

    def build(self):
        return CrimePrevention()


if __name__ == '__main__':
    TestApp().run()
```

main.kv
```kv
##:kivy 1.11.0
##:import sp kivy.metrics.sp
##:import dp kivy.metrics.dp

<CrimePrevention>:
    orientation: 'vertical'

    canvas.before:
        Color:
            rgb: .6, .6, .6
        Rectangle:
            pos: self.pos
            size: self.size
            # source: 'data/background.png'

    SomeMenu_ActionBar:
        id: ActionBar

    ScreenManager:
        id: sm
        WelcomeScreen:
        FirstScreen:
        SecondScreen:

<SomeMenu_ActionBar@ActionBar>:

    ActionView:
        id: ActionView

        HiddenIcon_ActionPrevious:

        ActionGroup:
            id: App_ActionGroup
            mode: 'spinner'
            text: 'Jump to Screen'

            ActionButton:
                text: 'Crime Prediction'
                on_release: app.root.ids.sm.current = 'second'
            ActionButton:
                text: 'Forum'
                on_release:  app.root.ids.sm.current = 'second'
            ActionButton:
                text: 'Probable Suspect'
                on_release:  app.root.ids.sm.current = 'second'

        ActionGroup:
            id: App_ActionGroup
            mode: 'spinner'
            text: 'App'

            ActionButton:
                text: 'Settings'
                on_press: app.open_settings()
            ActionButton:
                text: 'Quit'
                on_press: app.get_running_app().stop()

        ActionGroup:
            id: File_ActionGroup
            mode: 'spinner'
            text: 'File'

            ActionButton:
                text: 'Open'
            ActionButton:
                text: 'Save'

<HiddenIcon_ActionPrevious@ActionPrevious>:
    title: ''   # app.title if app.title is not None else 'Action Previous'
    with_previous: False
    app_icon: ''
    app_icon_width: 0
    app_icon_height: 0
    size_hint_x: None
    width: len(self.title) * 10

<WelcomeScreen>:
    name: 'welcome'
    Label:
        text: 'Welcome Screen'
        font_size: sp(50)

<FirstScreen>:
    name: 'first'
    Label:
        text: 'First Screen'

<SecondScreen>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Predict Crime'
            font_size: 50

        BoxLayout:
            Button:
                text: 'Back to Main Menu'
                font_size: 30
                on_release: app.root.ids.sm.current = 'first'
            Button:
                text: 'get random colour screen'
                font_size: 30
                on_release: app.root.ids.sm.current = 'first'
```
