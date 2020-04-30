---
url: vci6o7
---

# Python 用 urwid 快速搭建 terminal TUI 交互应用

更多资料：[https://www.yuque.com/liuwenkan/python/urwid](https://www.yuque.com/liuwenkan/python/urwid)<br />本文主要用到了urwid 库， 更多关于TUI库介绍请看：[https://www.yuque.com/liuwenkan/python/nff2r2](https://www.yuque.com/liuwenkan/python/nff2r2)

<a name="UjumW"></a>
# Hollow world

```python
import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue'),]

txt = urwid.Text(('banner', u" Hello World "), align='center')
map1 = urwid.AttrMap(txt, 'streak')
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, 'bg')
loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)
loop.run()
```

<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581164700297-78ae20da-332c-43eb-99ff-6d3fb776e3c2.png#align=left&display=inline&height=184&name=image.png&originHeight=245&originWidth=533&size=8749&status=done&style=none&width=400)<br />
<br />

<a name="CHIs1"></a>
# 加上 按钮

Text，Button 等， 在Pile中排序， 然后添加入 Filler， 再丢进loop中

[代码地址](https://www.yuque.com/liuwenkan/python/urwid#S8n5a)
```python
# button function
def on_exit_clicked(button):
    raise urwid.ExitMainLoop()

# button Name
button = urwid.Button(u'Exit')

# align button and Text
fill = urwid.Pile([map1, button])

# Connect the signal
urwid.connect_signal(button, 'click', on_exit_clicked)
```

完全代码：
```python
import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue'),]

button = urwid.Button(u'Exit')
def on_exit_clicked(button):
    raise urwid.ExitMainLoop()

txt = urwid.Text(('banner', u" Hello World "), align='center')
map1 = urwid.AttrMap(txt, 'streak')
fill = urwid.Pile([map1, button])
fill = urwid.Filler(fill)

urwid.connect_signal(button, 'click', on_exit_clicked)
loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)
loop.run()
```
其实我挺讨厌这个背景色的 2333<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581176705348-fee6bb1d-a119-4f2d-b940-2027bee6fa26.png#align=left&display=inline&height=206&name=image.png&originHeight=276&originWidth=537&size=183805&status=done&style=none&width=400)<br />成功加入 退出

<a name="WIxwr"></a>
# 干脆添加一个菜单吧～
菜单代码地址





<br />--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
