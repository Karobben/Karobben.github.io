---
title: "Kivy: FileChooser on Android"
ytitle: "Kivy: 安卓手機選擇文件或文件夾"

description: "A kivy example of fileChoose from github. It can run smoothly on your Android phone."
date: 2021/01/02
url: kivy_filechooser
toc: true
excerpt: "A kivy example of fileChoose from github. It can run smoothly on your Android phone."
tags: [Python, Kivy]
category: [Python, Kivy]
cover: 'https://s3.ax1x.com/2021/03/12/6aAbHx.md.png'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
priority: 10000
covercopy: '© Karobben'
---

## Quick Start

Because of lacking the knowledge of android, I made very slow progress on running filechooser on android.

But thanks the post in [GitHub issue](https://github.com/kivy/plyer/issues/512), I finally made it. ([original codes](https://github.com/kivy/plyer/files/5014975/android_filechooser.zip) from [Sirfanas](https://github.com/Sirfanas))

And this is the codes below which could substitude the photos on the background by choosing the photo in your phone.

<details>
  <summary><span style="font-size:20px"> <code>main.py</code></span> </summary>
  ```python main.py
  from kivy.app import App
  from kivy.uix.widget import Widget
  from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
  from kivy.vector import Vector
  from kivy.clock import Clock
  from random import randint
  from kivy.lang import Builder
  from kivy.uix.image import AsyncImage

  from plyer import filechooser
  from kivy.properties import ListProperty
  from kivy.uix.button import Button


  class Main(Widget):

      selection = ListProperty([])

      def choose(self):
          '''
          Call plyer filechooser API to run a filechooser Activity.
          '''
          filechooser.open_file(on_selection=self.handle_selection)

      def handle_selection(self, selection):
          '''
          Callback function for handling the selection response from Activity.
          '''
          self.selection = selection
          #print(str(selection))


      def on_selection(self, *a, **k):
          '''
          Update TextInput.text after FileChoose.selection is changed
          via FileChoose.handle_selection.
          '''
          self.b_t.ii = self.selection[0]
          self.box.ii = self.selection[0]

  class RunApp(App):
      def build(self):
          game = Main()
          return game

  if __name__ == '__main__':
      RunApp().run()
  ```
</details>

<details>
  <summary><span style="font-size:20px"> <code>run.kv</code></span> </summary>
  ```kv run.kv
  <Main@BoxLayout>:
      box: box_img
      b_t: b_t
      orientation: " vertical"
      BoxLayout:
          id: box_img
          ii: '1.png'
          canvas:
              Rectangle:
                  source: self.ii
                  pos: root.pos
                  size: root.size
      BoxLayout:
          width: root.width
          Button:
              size_hint_x:1
              pos: self.pos
              text: 'Switch'
              on_release: root.choose()
          Label:
              size_hint_x:9
              id: b_t
              ii: '123'
              text: self.ii
              haling: 0
  ```
</details>

<details>
  <summary><span style="font-size:20px"><code>buildozer.spec</code></span> </summary>

  ```txt buildozer.spec
  [app]

  # (str) Title of your application
  title = FileChooser

  # (str) Package name
  package.name = filechooser

  # (str) Package domain (needed for android/ios packaging)
  package.domain = org.sirfanas.filechooser

  # (str) Source code where the main.py live
  source.dir = .

  # (list) Source files to include (let empty to include all the files)
  source.include_exts = py,png,jpg,kv,atlas

  # (list) List of inclusions using pattern matching
  #source.include_patterns = assets/*,images/*.png

  # (list) Source files to exclude (let empty to not exclude anything)
  #source.exclude_exts = spec

  # (list) List of directory to exclude (let empty to not exclude anything)
  #source.exclude_dirs = tests, bin

  # (list) List of exclusions using pattern matching
  #source.exclude_patterns = license,images/*/*.jpg

  # (str) Application versioning (method 1)
  version = 0.5

  # (str) Application versioning (method 2)
  # version.regex = __version__ = ['"](.*)['"]
  # version.filename = %(source.dir)s/main.py

  # (list) Application requirements
  # comma separated e.g. requirements = sqlite3,kivy
  requirements =
    plyer,
    android,
    kivy, kivymd,
    python3==3.7.5,
    Pillow

  # (str) Custom source folders for requirements
  # Sets custom source for any requirements with recipes
  # requirements.source.kivy = ../../kivy

  # (list) Garden requirements
  # garden_requirements =

  # (str) Presplash of the application
  #presplash.filename = %(source.dir)s/data/presplash.png

  # (str) Icon of the application
  #icon.filename = %(source.dir)s/data/icon.png

  # (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
  orientation = all

  # (list) List of service to declare
  #services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

  #
  # OSX Specific
  #

  #
  # author = © Copyright Info

  # change the major version of python used by the app
  osx.python_version = 3

  # Kivy version to use
  osx.kivy_version =  1.9.1

  #
  # Android specific
  #

  # (bool) Indicate if the application should be fullscreen or not
  fullscreen = 0

  # (string) Presplash background color (for new android toolchain)
  # Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
  # red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
  # darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
  # olive, purple, silver, teal.
  #android.presplash_color = #FFFFFF

  # (list) Permissions
  android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

  # (int) Target Android API, should be as high as possible.
  android.api = 27

  # (int) Minimum API your APK will support.
  android.minapi = 21

  # (str) Android NDK version to use
  android.ndk = 19b

  # (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
  android.ndk_api = 21

  # (bool) Use --private data storage (True) or --dir public storage (False)
  #android.private_storage = True

  # (str) Android NDK directory (if empty, it will be automatically downloaded.)
  #android.ndk_path =

  # (str) Android SDK directory (if empty, it will be automatically downloaded.)
  #android.sdk_path =

  # (str) ANT directory (if empty, it will be automatically downloaded.)
  #android.ant_path =

  # (bool) If True, then skip trying to update the Android sdk
  # This can be useful to avoid excess Internet downloads or save time
  # when an update is due and you just want to test/build your package
  android.skip_update = False

  # (bool) If True, then automatically accept SDK license
  # agreements. This is intended for automation only. If set to False,
  # the default, you will be shown the license when first running
  # buildozer.
  android.accept_sdk_license = True

  # (str) Android entry point, default is ok for Kivy-based app
  #android.entrypoint = org.renpy.android.PythonActivity

  # (list) Pattern to whitelist for the whole project
  #android.whitelist =

  # (str) Path to a custom whitelist file
  #android.whitelist_src =

  # (str) Path to a custom blacklist file
  #android.blacklist_src =

  # (list) List of Java .jar files to add to the libs so that pyjnius can access
  # their classes. Don't add jars that you do not need, since extra jars can slow
  # down the build process. Allows wildcards matching, for example:
  # OUYA-ODK/libs/*.jar
  #android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

  # (list) List of Java files to add to the android project (can be java or a
  # directory containing the files)
  #android.add_src =

  # (list) Android AAR archives to add (currently works only with sdl2_gradle
  # bootstrap)
  #android.add_aars =

  # (list) Gradle dependencies to add (currently works only with sdl2_gradle
  # bootstrap)
  #android.gradle_dependencies =

  # (list) Java classes to add as activities to the manifest.
  #android.add_activites = com.example.ExampleActivity

  # (str) python-for-android branch to use, defaults to master
  #p4a.branch = master

  # (str) OUYA Console category. Should be one of GAME or APP
  # If you leave this blank, OUYA support will not be enabled
  #android.ouya.category = GAME

  # (str) Filename of OUYA Console icon. It must be a 732x412 png image.
  #android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

  # (str) XML file to include as an intent filters in <activity> tag
  #android.manifest.intent_filters =

  # (str) launchMode to set for the main activity
  #android.manifest.launch_mode = standard

  # (list) Android additional libraries to copy into libs/armeabi
  #android.add_libs_armeabi = libs/android/*.so
  #android.add_libs_armeabi_v7a = libs/android-v7/*.so
  #android.add_libs_x86 = libs/android-x86/*.so
  #android.add_libs_mips = libs/android-mips/*.so

  # (bool) Indicate whether the screen should stay on
  # Don't forget to add the WAKE_LOCK permission if you set this to True
  #android.wakelock = False

  # (list) Android application meta-data to set (key=value format)
  #android.meta_data =

  # (list) Android library project to add (will be added in the
  # project.properties automatically.)
  #android.library_references =

  # (list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tag
  #android.uses_library =

  # (str) Android logcat filters to use
  #android.logcat_filters = *:S python:D

  # (bool) Copy library instead of making a libpymodules.so
  #android.copy_libs = 1

  # (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
  android.arch = armeabi-v7a

  #
  # Python for android (p4a) specific
  #

  # (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
  #p4a.source_dir =

  # (str) The directory in which python-for-android should look for your own build recipes (if any)
  #p4a.local_recipes =

  # (str) Filename to the hook for p4a
  #p4a.hook =

  # (str) Bootstrap to use for android builds
  # p4a.bootstrap = sdl2

  # (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
  #p4a.port =


  #
  # iOS specific
  #

  # (str) Path to a custom kivy-ios folder
  #ios.kivy_ios_dir = ../kivy-ios
  # Alternately, specify the URL and branch of a git checkout:
  ios.kivy_ios_url = https://github.com/kivy/kivy-ios
  ios.kivy_ios_branch = master

  # Another platform dependency: ios-deploy
  # Uncomment to use a custom checkout
  #ios.ios_deploy_dir = ../ios_deploy
  # Or specify URL and branch
  ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
  ios.ios_deploy_branch = 1.7.0

  # (str) Name of the certificate to use for signing the debug version
  # Get a list of available identities: buildozer ios list_identities
  #ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

  # (str) Name of the certificate to use for signing the release version
  #ios.codesign.release = %(ios.codesign.debug)s


  [buildozer]

  # (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
  log_level = 2

  # (int) Display warning if buildozer is run as root (0 = False, 1 = True)
  warn_on_root = 1

  # (str) Path to build artifact storage, absolute or relative to spec file
  build_dir = ../.buildozer

  # (str) Path to build output (i.e. .apk, .ipa) storage
  # bin_dir = ./bin

  #    -----------------------------------------------------------------------------
  #    List as sections
  #
  #    You can define all the "list" as [section:key].
  #    Each line will be considered as a option to the list.
  #    Let's take [app] / source.exclude_patterns.
  #    Instead of doing:
  #
  #[app]
  #source.exclude_patterns = license,data/audio/*.wav,data/images/original/*
  #
  #    This can be translated into:
  #
  #[app:source.exclude_patterns]
  #license
  #data/audio/*.wav
  #data/images/original/*
  #


  #    -----------------------------------------------------------------------------
  #    Profiles
  #
  #    You can extend section / key with a profile
  #    For example, you want to deploy a demo version of your application without
  #    HD content. You could first change the title to add "(demo)" in the name
  #    and extend the excluded directories to remove the HD content.
  #
  #[app@demo]
  #title = My Application (demo)
  #
  #[app:source.exclude_patterns@demo]
  #images/hd/*
  #
  #    Then, invoke the command line with the "demo" profile:
  #
  #buildozer --profile demo android debug
  ```
</details>

<br>
<img src="https://s3.ax1x.com/2021/01/02/sSdtHg.gif" style="height:40%;" alt="Kivy file chooser">



## Choose files or directorys

Whit this script, it can print the absolute path of the file/directory you piked at the button.

`filechooser.open_file` works fine. But `filechooser.choose_dir` works only in my PC, not on Android. No idea why.
<details>
  <summary> <code>main.py</code> </summary>
  ```py main.py
  from kivy.app import App
  from kivy.uix.widget import Widget
  from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
  from kivy.vector import Vector

  from kivy.clock import Clock
  from random import randint
  from kivy.lang import Builder
  from kivy.uix.image import AsyncImage

  from plyer import filechooser
  from kivy.properties import ListProperty
  from kivy.uix.button import Button


  class Main(Widget):
      selection = ListProperty([])

      def choose(self):
          '''
          Call plyer filechooser API to run a filechooser Activity.
          '''
          filechooser.open_file(on_selection=self.handle_selection)

      def choose_d(self):
          '''
          Call plyer filechooser API to run a filechooser Activity.
          '''
          filechooser.choose_dir(on_selection=self.handle_selection)

      def handle_selection(self, selection):
          '''
          Callback function for handling the selection response from Activity.
          '''
          self.selection = selection
          #print(str(selection))

      def on_selection(self, *a, **k):
          '''
          Update TextInput.text after FileChoose.selection is changed
          via FileChoose.handle_selection.
          '''
          self.b_t.ii = self.selection[0]

  class RunApp(App):
      def build(self):
          game = Main()
          return game

  if __name__ == '__main__':
      RunApp().run()
  ```
</details>

<details>
  <summary> <code>run.kv</code> </summary>
  ```kv run.kv
  <FileChoose>:

  <Main@BoxLayout>:
      box: box_img
      b_t: b_t
      orientation: " vertical"
      BoxLayout:
          id: box_img
          ii: '1.png'
          canvas:
              Rectangle:
                  source: self.ii
                  pos: root.pos
                  size: root.size
      BoxLayout:
          width: root.width
          BoxLayout:
              orientation: 'vertical'
              size_hint_x:1
              Button:
                  pos: self.pos
                  text: 'Pick file'
                  on_release: root.choose()
              Button:
                  pos: self.pos
                  text: 'Directory'
                  on_release: root.choose_d()
          Label:
              color: 0, 0, 0, 1
              size_hint_x:9
              id: b_t
              ii: 'The thing you choosed'
              text: self.ii
              haling: 0
  ```
</details>

<br>

![Kivy file chooser](https://s3.ax1x.com/2021/03/12/6aAbHx.png)

## For android

This example makes you are able to choose a filer/directory in Android phone.

```python main.py
from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.utils import platform


KV = '''
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: "MDFileManager"
        left_action_items: [['menu', lambda x: None]]
        elevation: 10

    FloatLayout:

        MDRoundFlatIconButton:
            text: "Open manager"
            icon: "folder"
            pos_hint: {'center_x': .5, 'center_y': .6}
            on_release: app.file_manager_open()
'''


class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            #preview=True
        )

    def build(self):
        return Builder.load_string(KV)

    def file_manager_open(self):
        PATH ="."
        if platform == "android":
          from android.permissions import request_permissions, Permission
          request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
          app_folder = os.path.dirname(os.path.abspath(__file__))
          PATH = "/storage/emulated/0" #app_folder
        self.file_manager.show(PATH)  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


Example().run()
```


## Official Document

[Kivy](https://kivy.org/doc/stable/api-kivy.uix.filechooser.html)

Add this to the requirements
```kv
requirements = kivy, python3==3.7.5, docutils, android
```

```py main.py
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.utils import platform

import os

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        PATH = "."
        if platform == "android":
          from android.permissions import request_permissions, Permission
          request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
          app_folder = os.path.dirname(os.path.abspath(__file__))
          PATH = "/storage/emulated/0" #app_folder
        content.ids.filechooser.path = PATH

        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        PATH = "."
        if platform == "android":
          from android.permissions import request_permissions, Permission
          request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
          app_folder = os.path.dirname(os.path.abspath(__file__))
          PATH = "/storage/emulated/0" #app_folder
        content.ids.filechooser.path = PATH
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()


class Editor(App):
    pass


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
    Editor().run()
```

`editor.kv`

```kv editor.kv
#:kivy 1.1.0

Root:
    text_input: text_input

    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: 'Load'
                on_release: root.show_load()
            Button:
                text: 'Save'
                on_release: root.show_save()

        BoxLayout:
            TextInput:
                id: text_input
                text: ''

            RstDocument:
                text: text_input.text
                show_errors: True

<LoadDialog>:
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserListView:
            id: filechooser
            path: "."

        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                id: test
                text: "Cancel"
                on_release: root.cancel()

            Button:
                text: "Load"
                on_release: root.load(filechooser.path, filechooser.selection)

<SaveDialog>:
    text_input: text_input
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserListView:
            id: filechooser
            on_selection: text_input.text = self.selection and self.selection[0] or ''

        TextInput:
            id: text_input
            size_hint_y: None
            height: 30
            multiline: False

        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "Cancel"
                on_release: root.cancel()

            Button:
                text: "Save"
                on_release: root.save(filechooser.path, text_input.text)
```
