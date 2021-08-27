---
title: "Kivy examples: smooth line"
ytitle: "Kivy: 添加一條折線"
description: "Kivy examples: smooth line adding lines on kivy canvas"
date: 2020/12/13
url: kivy_examples_lines
toc: true
excerpt: "Kivy examples: smooth line adding lines on kivy canvas"
tags: [Python, Kivy]
category: [Python, Kivy]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.dpHEt6VNif2n2c4ULEqQ7gHaDJ'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
priority: 10000
covercopy: '© dotmodus'
---


![Kivy lines](https://kivy.org/doc/stable/_images/canvas__lines__py1.png)

[Document](https://kivy.org/doc/stable/examples/gen__canvas__lines__py.html)

## Quick Start
By copy the codes from the document, you are supposed being able to show the  line on the screen and adjust the alpha, width, etc of the line.

```python
ListProperty([(500, 500),
                          [300, 300, 500, 300],
                          [500, 400, 600, 400]])
```
As you can see above, you can envelope the points by `()` or `[]`, you can line the points one by one or line them all together if you wish (The examples show down below).

```python
ListProperty([(500, 500),
                          [300, 300], [500, 300],
                          [500, 400], [600, 400]])
```python
or
```python
ListProperty([500, 500, 300, 300, 500, 300, 500, 400, 600, 400])
```

The minimal codes you've to keep is:

```python
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_string('''
<LinePlayground>:
    # assign a list variate as point so it could be easliy handled in later
    point: [0,0, 200, 100]
    canvas:
        Color:
            rgba: .4, .4, 1, 1
        Line:
            # recall the variate 'point' above
            points: self.point
'''
)

class LinePlayground(FloatLayout):
    pass

class TestLineApp(App):
    def build(self):
        return LinePlayground()

if __name__ == '__main__':
    TestLineApp().run()
```

## updating the line

If you are not satisfied with drawing a line and want to create an animation, than like do some thing cool.



***updating....***

```python
from kivy.app import App
from kivy.properties import  ListProperty

from kivy.uix.floatlayout import FloatLayout


from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import ObjectProperty


## Remove unnecessary codes from this class
class LinePlayground(FloatLayout):
    pass

class Main_app(Widget):
    # assign a numeric variate
    i = 0
    # connect the class in kv file: line -> line_ground -> LinePlayground

    line = ObjectProperty(None)

    def update(self, dt):
        self.i +=1
        # update the point
        self.line.point = [[0,0,], [self.i,self.i]]
        print(self.line.point)
        print(self.line)
        print("1")


class TestLineApp(App):
    def build(self):
        Main = Main_app()
        # update the result with 60 fps (1/60)
        Clock.schedule_interval(Main.update,1/60)
        return Main


if __name__ == '__main__':
    TestLineApp().run()
```

`testline.kv` file:
```kv
<LinePlayground>:
    # assign a list variate as point so it could be easliy handled in later
    point: [0,0, 200, 100]
    canvas:
        Color:
            rgba: .4, .4, 1, 1
        Line:
            # recall the variate 'point' above
            points: self.point


<Main_app>:
    # assign the id which could be recall later
    line: line_ground


    LinePlayground:
        id: line_ground
        point: [0,10, 100,200]
```

![Line animation in Kivy](https://s3.ax1x.com/2020/12/13/rebSLq.gif)
