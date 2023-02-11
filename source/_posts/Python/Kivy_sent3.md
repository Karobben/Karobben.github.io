---
title: "Learn Kivy from Sant: 3"
ytitle: "Sant 的kivy視頻筆記 3"
description: "Learn Kivy from Sant: 3"
date: 2020/11/12
url: kivy_sent_3
toc: true
excerpt: "Some notes from sant's kivy video tutorial"
tags: [Python, Kivy]
category: [Python, Kivy]
cover: 'https://s3.ax1x.com/2021/03/12/6UBcCT.gif'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
priority: 10000
covercopy: '© Karobben'
---


Introduction of kivy:
[Youtube Vedio](https://www.youtube.com/watch?v=sJmkhV02lnM)
[Text Tutorial](https://pythonprogramming.net/screen-manager-pages-screens-kivy-application-python-tutorial/)

As you can see, I skipped lesson 2 which is introducing how to add and join a button.
Besides, he showed us how to get the input texts from the `TextInput`

In this video, Sant introduced the module of `screenmanager` from `kivy.uix`.

Main skeleton of the codes:
```python
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
## to use buttons:
from kivy.uix.button import Button
## to screen
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require("1.10.1")

class EpicApp(App):

class ConnectPage(GridLayout):

class InfoPage(GridLayout):


if __name__ == "__main__":
    chat_app = EpicApp()
    chat_app.run()
```

### EpicApp()

As you can see, there are three classes. In the first class, `EpicApp`, is the class which manager different screens.  

```python
class EpicApp(App):
    def build(self):
        # We are going to use screen manager, so we can add multiple screens
        # and switch between them
        self.screen_manager = ScreenManager()
        # Initial, connection screen (we use passed in name to activate screen)
        # First create a page, then a new screen, add page to screen and screen to screen manager
        self.connect_page = ConnectPage()
        screen = Screen(name='Connect')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)
        # Info page
        # Info page was below
        self.info_page = InfoPage()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager
```
After assigned the `screen_manger`, we need to assign the **"name"** and **"widget"** on each screen; and then, add them into `screen_manager`

As we can see, it loaded the `ConnectPage` first, and <span style="background:salmon">named it as *'Connect'*</span> which was used to switch the screen later.

<span style="background:salmon">Who loaded first would be the Home Page.<span>


### ConnectPage
```python
class ConnectPage(GridLayout):
    # runs on initialization
    # Our Main Screen
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1  # used for our grid

        self.add_widget(Label(text='Hello World'))  # widget #1, top left
        #self.add_widget(self.ip) # widget #2, top right

        # add our button.
        self.join = Button(text="Try me")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())  # just take up the spot.
        self.add_widget(self.join)

    def join_button(self, instance):
        #print(f"Joining {ip}:{port} as {username}")
        # Create info string, update InfoPage with a message and show it
        info = f"You found me"
        chat_app.info_page.update_info(info)
        chat_app.screen_manager.current = 'Info'
```
The layout of this page was clearly explained by Sant. And for practicing, I simplified it and remained a line of text and button only. The button is the key to join another screen. The trick of it is create a brand new screen.

### InfoPage

```python
class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Just one column
        self.cols = 1

        # And one label with bigger font and centered text
        self.message = Label(halign="center", valign="middle", font_size=30)

        # By default every widget returns it's side as [100, 100], it gets finally resized,
        # but we have to listen for size change to get a new one
        # more: https://github.com/kivy/kivy/issues/1044
        self.message.bind(width=self.update_text_width)

        # Add text widget to the layout
        self.add_widget(self.message)

        # add our button.
        # Add an return button
        self.join = Button(text="return")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())  # just take up the spot.
        self.add_widget(self.join)

    def join_button(self, instance):
        #print(f"Joining {ip}:{port} as {username}")
        chat_app.screen_manager.current = 'Connect'

    # Called with a message, to update message text in widget
    def update_info(self, message):
        self.message.text = message

    # Called on label width update, so we can set text width properly - to 90% of label width
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)
```

In this page, Sant add a function which could update the texts in the screen. So we can print the texts by running `chat_app.info_page.update_info(info)` before switch to the screen 'Info'

And personally, I add a return button to back to the home page.
![Kivy screen manager](https://s3.ax1x.com/2020/11/12/BzT4at.gif)

<details>
  <summary><span style="font-size:20px"> Click to see the full version of the code</span> </summary>
  ```python
  import kivy
  from kivy.app import App
  from kivy.uix.label import Label
  from kivy.uix.gridlayout import GridLayout
  # to use buttons:
  from kivy.uix.button import Button
  # to screen
  from kivy.uix.screenmanager import ScreenManager, Screen

  kivy.require("1.10.1")

  class EpicApp(App):
      def build(self):
          # We are going to use screen manager, so we can add multiple screens
          # and switch between them
          self.screen_manager = ScreenManager()
          # Initial, connection screen (we use passed in name to activate screen)
          # First create a page, then a new screen, add page to screen and screen to screen manager
          self.connect_page = ConnectPage()
          screen = Screen(name='Connect')
          screen.add_widget(self.connect_page)
          self.screen_manager.add_widget(screen)
          # Info page
          # Info page was below
          self.info_page = InfoPage()
          screen = Screen(name='Info')
          screen.add_widget(self.info_page)
          self.screen_manager.add_widget(screen)
          return self.screen_manager

  class ConnectPage(GridLayout):
      # runs on initialization
      # Our Main Screen
      def __init__(self, **kwargs):
          super().__init__(**kwargs)

          self.cols = 1  # used for our grid

          self.add_widget(Label(text='Hello World'))  # widget #1, top left
          #self.add_widget(self.ip) # widget #2, top right

          # add our button.
          self.join = Button(text="Try me")
          self.join.bind(on_press=self.join_button)
          self.add_widget(Label())  # just take up the spot.
          self.add_widget(self.join)

      def join_button(self, instance):
          #print(f"Joining {ip}:{port} as {username}")
          # Create info string, update InfoPage with a message and show it
          info = f"You found me"
          chat_app.info_page.update_info(info)
          chat_app.screen_manager.current = 'Info'


  # Simple information/error page
  class InfoPage(GridLayout):
      def __init__(self, **kwargs):
          super().__init__(**kwargs)

          # Just one column
          self.cols = 1

          # And one label with bigger font and centered text
          self.message = Label(halign="center", valign="middle", font_size=30)

          # By default every widget returns it's side as [100, 100], it gets finally resized,
          # but we have to listen for size change to get a new one
          # more: https://github.com/kivy/kivy/issues/1044
          self.message.bind(width=self.update_text_width)

          # Add text widget to the layout
          self.add_widget(self.message)

          # add our button.
          # Add an return button
          self.join = Button(text="return")
          self.join.bind(on_press=self.join_button)
          self.add_widget(Label())  # just take up the spot.
          self.add_widget(self.join)

      def join_button(self, instance):
          #print(f"Joining {ip}:{port} as {username}")
          chat_app.screen_manager.current = 'Connect'

      # Called with a message, to update message text in widget
      def update_info(self, message):
          self.message.text = message

      # Called on label width update, so we can set text width properly - to 90% of label width
      def update_text_width(self, *_):
          self.message.text_size = (self.message.width * 0.9, None)


  if __name__ == "__main__":
      chat_app = EpicApp()
      chat_app.run()
  ```
<details>
