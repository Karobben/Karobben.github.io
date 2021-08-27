---
title: "pynput --Moniter your keybaord"
description: "pynput --Moniter your keybaord"
url: pynput2
date: 2020/01/22
toc: true
excerpt: "read your email through python"
tags: [Python, email]
category: [Python, Scripting, Module]
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
covercopy: '© getcodify.com'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## pynput --Moniter your keybaord

<a name="kC35U"></a>
## 1. Mouse

<a name="gxkG3"></a>
### 1.1 Mouse Controller
```python
from pynput.mouse import Button, Controller

mouse = Controller()

## Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

## Set pointer position
mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(mouse.position))

## Move pointer relative to current position
mouse.move(5, -5)

## Press and release
mouse.press(Button.left)
mouse.release(Button.left)

while True:
    mouse.press(Button.left)

## Double click; this is different from pressing and releasing
## twice on Mac OSX
mouse.click(Button.left, 2)

## Scroll two steps down
mouse.scroll(0, 2)
```


<a name="CYpoY"></a>
### 1.2 Mouse Monitor

```python
##监控鼠标事件
from pynput import mouse

def on_move(x, y ):
    print('Pointer moved to {o}'.format(
        (x,y)))
def on_click(x, y , button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        return False
def on_scroll(x, y ,dx, dy):
    print('scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
while True:
    with mouse.Listener( no_move = on_move,on_click = on_click,on_scroll = on_scroll) as listener:
        listener.join()
```


<a name="4QKL2"></a>
## 2. Keybaord

<a name="CEgBC"></a>
### 2.1 Keyboard Controller

```python
##键盘输入用法

from pynput.keyboard import Key, Controller

keyboard = Controller()

##Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)

keyboard.press(Key.left)
keyboard.release(Key.left)

##Type a lower case A ;this will work even if no key on the physical keyboard  is labelled 'A'
keyboard.press('a')
keyboard.release('a')

##Type two  upper case As
keyboard.press('A')
keyboard.release('A')
## or
with keyboard .pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')

##type 'hello world '  using the shortcut type  method
keyboard.type('hello world')
```


<a name="k1b09"></a>
### 2.2 Keyboard Monitor

```python
##键盘监听

from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key  {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False

while True:
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()
```
