---
title: "urwid: control the mouse through touch board| 控制鼠标"
description: "Python 用 urwid 面板控制鼠标"
url: urwid_mouse
---

# Python 用 urwid 控制 鼠标位置

更多资料：[https://www.yuque.com/liuwenkan/python/urwid](https://www.yuque.com/liuwenkan/python/urwid)<br />本文主要用到了urwid 库， 更多关于TUI库介绍请看：[https://www.yuque.com/liuwenkan/python/nff2r2](https://www.yuque.com/liuwenkan/python/nff2r2)

# Hollow world

## Main function of touch board
```python
import urwid

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))

txt = urwid.Text(u"Hello World")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()
```
So, we can acquiring the position by key.
If you using mouse, we can accept mouse dragging moves.
But for touch screen, we can read press and release only.

![Mouse moves](https://s1.ax1x.com/2020/06/23/NtMrWQ.png)

so, we can get the touch position by:
```python
if key[0] == 'mouse release':
    X = key[2]
    Y = key[3]
```

Before calculating the relative position, we need access the resolution of the monitor first.

```python
# Access resolution of monitor
import pyautogui

W_X = pyautogui.size()[0]
W_Y = pyautogui.size()[1]

# access the size of the terminal
cols, rows = urwid.raw_display.Screen().get_cols_rows()
M_X = round((W_X/cols)*X)
M_Y = round((W_Y/rows)*Y*2)
```

# Move the mouse
Now, once we had the target position, we can move mouse by `pynput`
```python
from pynput.mouse import Button, Controller
mouse = Controller()

# Set pointer position
mouse.position = (M_X, M_Y)
```

ummmm... I just found this is the most useless script I have ever write...
When I test this script on cell phone and trying to control the mouse of computer... it failed. And I just realize it is impossible = =
