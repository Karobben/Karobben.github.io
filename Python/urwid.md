---
url: urwid2
---

# urwid

Reference：[http://urwid.org/tutorial/index.html](http://urwid.org/tutorial/index.html)

[Urwid Tutorial](http://urwid.org/tutorial/index.html#)<br /> [Minimal Application](http://urwid.org/tutorial/index.html#minimal-application)<br /> [Global Input](http://urwid.org/tutorial/index.html#global-input)<br /> [Display Attributes](http://urwid.org/tutorial/index.html#display-attributes)<br />[ High Color Modes](http://urwid.org/tutorial/index.html#high-color-modes)<br />[ Question and Answer](http://urwid.org/tutorial/index.html#question-and-answer)<br />[ Signal Handlers](http://urwid.org/tutorial/index.html#signal-handlers)<br />[ Multiple Questions](http://urwid.org/tutorial/index.html#multiple-questions)<br /> [Simple Menu](http://urwid.org/tutorial/index.html#simple-menu)<br />[ Cascading Menu]()<br /> [Horizontal Menu](http://urwid.org/tutorial/index.html#horizontal-menu)<br />[ Adventure Game](http://urwid.org/tutorial/index.html#adventure-game)

Main tutorial: [http://urwid.org/manual/index.html](http://urwid.org/manual/index.html)

- [Library Overview](http://urwid.org/manual/overview.html)
- [Main Loop](http://urwid.org/manual/mainloop.html)
  - [Widgets Displayed](http://urwid.org/manual/mainloop.html#widgets-displayed)
  - [Event Loops](http://urwid.org/manual/mainloop.html#event-loops)
- [Display Modules](http://urwid.org/manual/displaymodules.html)
  - [Raw and Curses Display Modules](http://urwid.org/manual/displaymodules.html#raw-and-curses-display-modules)
  - [Other Display Modules](http://urwid.org/manual/displaymodules.html#other-display-modules)
  - [Setting a Palette](http://urwid.org/manual/displaymodules.html#setting-a-palette)
- [Widgets](http://urwid.org/manual/widgets.html)
  - [Widget Layout](http://urwid.org/manual/widgets.html#widget-layout)
  - [Box, Flow and Fixed Widgets](http://urwid.org/manual/widgets.html#box-flow-and-fixed-widgets)
  - [Included Widgets](http://urwid.org/manual/widgets.html#included-widgets)
  - [Decoration Widgets](http://urwid.org/manual/widgets.html#decoration-widgets)
  - [Container Widgets](http://urwid.org/manual/widgets.html#container-widgets)
  - [ListBox Contents](http://urwid.org/manual/widgets.html#listbox-contents)
  - [Custom Widgets](http://urwid.org/manual/widgets.html#custom-widgets)
  - [Widget Metaclass](http://urwid.org/manual/widgets.html#widget-metaclass)
- [User Input](http://urwid.org/manual/userinput.html)
  - [Keyboard Input](http://urwid.org/manual/userinput.html#keyboard-input)
  - [Mouse Input](http://urwid.org/manual/userinput.html#mouse-input)
- [Text Layout](http://urwid.org/manual/textlayout.html)
  - [Custom Text Layouts](http://urwid.org/manual/textlayout.html#custom-text-layouts)
  - [Text Layout Structures](http://urwid.org/manual/textlayout.html#text-layout-structures)
- [Encodings Supported](http://urwid.org/manual/encodings.html)
  - [Unicode Support](http://urwid.org/manual/encodings.html#unicode-support)
  - [Pass-through Support](http://urwid.org/manual/encodings.html#pass-through-support)
  - [Future Work](http://urwid.org/manual/encodings.html#future-work)
- [Display Attributes](http://urwid.org/manual/displayattributes.html)
  - [Using Display Attributes](http://urwid.org/manual/displayattributes.html#using-display-attributes)
  - [Foreground and Background Settings](http://urwid.org/manual/displayattributes.html#foreground-and-background-settings)
  - [Recommended Combinations](http://urwid.org/manual/displayattributes.html#recommended-combinations)
- [Canvas Cache](http://urwid.org/manual/canvascache.html)
  - [Composite Canvases](http://urwid.org/manual/canvascache.html#composite-canvases)
  - [Cache Lifetime](http://urwid.org/manual/canvascache.html#cache-lifetime)
  - [Future Work](http://urwid.org/manual/canvascache.html#future-work)

<a name="zxt1G"></a>
# Quick Start:

```python
import urwid

txt = urwid.Text(u"Hello World")
fill = urwid.Filler(txt, 'top') #'top', 'middle', 'bottom'
loop = urwid.MainLoop(fill)
loop.run()
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581068500177-66f08b8a-9559-473d-a5c5-d1d3c23a431c.png#align=left&display=inline&height=277&name=image.png&originHeight=277&originWidth=568&size=9085&status=done&style=none&width=568)<br />
<br />

<a name="byFqh"></a>
# Global Input

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

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581068757974-519973e0-09ff-48fe-b169-80f66417ea93.png#align=left&display=inline&height=267&name=image.png&originHeight=267&originWidth=555&size=9999&status=done&style=none&width=555)<br />
<br />

<a name="XKE08"></a>
# Display Attributes

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

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581164700297-78ae20da-332c-43eb-99ff-6d3fb776e3c2.png#align=left&display=inline&height=110&name=image.png&originHeight=245&originWidth=533&size=8749&status=done&style=none&width=239)![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581164906179-996e709c-e443-4c49-8fd6-8839624550e2.png#align=left&display=inline&height=110&name=image.png&originHeight=246&originWidth=536&size=218056&status=done&style=none&width=240)![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581164961271-9aa033d2-1725-4d9d-881e-9daf63973969.png#align=left&display=inline&height=110&name=image.png&originHeight=247&originWidth=537&size=233129&status=done&style=none&width=239)<br />原图                                           去掉‘bg’                                            去掉‘streak’

<a name="pManZ"></a>
## 解释：
txt， 最顶层，标签是‘banner’，获取palette中‘banner’的设置<br />map1， 和txt 一个道理。<br />txt 丢到map1， map1丢到 fill， fill丢到map2， 一层盖一层。
<a name="tc2tt"></a>
# Question and Answer

```python
import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

class QuestionBox(urwid.Filler):
    def keypress(self, size, key):
        if key != 'enter':
            return super(QuestionBox, self).keypress(size, key)
        self.original_widget = urwid.Text(
            u"Nice to meet you,\n%s.\n\nPress Q to exit." %
            edit.edit_text)

edit = urwid.Edit(u"What is your name?\n")
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581166593939-391cb761-5e8e-4926-9752-bdfb83b3975d.png#align=left&display=inline&height=184&name=image.png&originHeight=247&originWidth=536&size=222973&status=done&style=none&width=400)



<a name="S8n5a"></a>
# Signal Handlers

```python
import urwid

palette = [('I say', 'default,bold', 'default', 'bold'),]
ask = urwid.Edit(('I say', u"What is your name?\n"))
reply = urwid.Text(u"")
button = urwid.Button(u'Exit')
div = urwid.Divider()
pile = urwid.Pile([ask, div, reply, div, button])
top = urwid.Filler(pile, valign='top')

def on_ask_change(edit, new_edit_text):
    reply.set_text(('I say', u"Nice to meet you, %s" % new_edit_text))

def on_exit_clicked(button):
    raise urwid.ExitMainLoop()

urwid.connect_signal(ask, 'change', on_ask_change)
urwid.connect_signal(button, 'click', on_exit_clicked)

urwid.MainLoop(top, palette).run()
```

![deepin-screen-recorder_deepin-terminal_20200208205839.gif](https://cdn.nlark.com/yuque/0/2020/gif/691897/1581166736809-5e8ee982-0865-464a-b4d1-45534d9286fd.gif#align=left&display=inline&height=417&name=deepin-screen-recorder_deepin-terminal_20200208205839.gif&originHeight=417&originWidth=540&size=243822&status=done&style=none&width=540)



<a name="eFB75"></a>
# Simple Menu

```python
import urwid

choices = u'Chapman Cleese Gilliam Idle Jones Palin'.split()

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', item_chosen, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
    response = urwid.Text([u'You chose ', choice, u'\n'])
    done = urwid.Button(u'Ok')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([response,
        urwid.AttrMap(done, None, focus_map='reversed')]))

def exit_program(button):
    raise urwid.ExitMainLoop()

main = urwid.Padding(menu(u'Pythons', choices), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
    align='center', width=('relative', 60),
    valign='middle', height=('relative', 60),
    min_width=20, min_height=9)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581167098962-166da259-b6b5-436e-85bd-4d92d84900f7.png#align=left&display=inline&height=183&name=image.png&originHeight=246&originWidth=538&size=204388&status=done&style=none&width=400)



<a name="kT6yB"></a>
# Pop-up Menu

```python
import urwid

def menu_button(caption, callback):
    button = urwid.Button(caption)
    urwid.connect_signal(button, 'click', callback)
    return urwid.AttrMap(button, None, focus_map='reversed')

def sub_menu(caption, choices):
    contents = menu(caption, choices)
    def open_menu(button):
        return top.open_box(contents)
    return menu_button([caption, u'...'], open_menu)

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    body.extend(choices)
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button):
    response = urwid.Text([u'You chose ', button.label, u'\n'])
    done = menu_button(u'Ok', exit_program)
    top.open_box(urwid.Filler(urwid.Pile([response, done])))

def exit_program(button):
    raise urwid.ExitMainLoop()

menu_top = menu(u'Main Menu', [
    sub_menu(u'Applications', [
        sub_menu(u'Accessories', [
            menu_button(u'Text Editor', item_chosen),
            menu_button(u'Terminal', item_chosen),
        ]),
    ]),
    sub_menu(u'System', [
        sub_menu(u'Preferences', [
            menu_button(u'Appearance', item_chosen),
        ]),
        menu_button(u'Lock Screen', item_chosen),
    ]),
])

class CascadingBoxes(urwid.WidgetPlaceholder):
    max_box_levels = 4
	#
    def __init__(self, box):
        super(CascadingBoxes, self).__init__(urwid.SolidFill(u'/'))
        self.box_level = 0
        self.open_box(box)
	#
    def open_box(self, box):
        self.original_widget = urwid.Overlay(urwid.LineBox(box),
            self.original_widget,
            align='center', width=('relative', 80),
            valign='middle', height=('relative', 80),
            min_width=24, min_height=8,
            left=self.box_level * 3,
            right=(self.max_box_levels - self.box_level - 1) * 3,
            top=self.box_level * 2,
            bottom=(self.max_box_levels - self.box_level - 1) * 2)
        self.box_level += 1
	#
    def keypress(self, size, key):
        if key == 'esc' and self.box_level > 1:
            self.original_widget = self.original_widget[0]
            self.box_level -= 1
        else:
            return super(CascadingBoxes, self).keypress(size, key)

top = CascadingBoxes(menu_top)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581167392737-0af2b839-764b-4405-9a33-5abe6b466c9f.png#align=left&display=inline&height=253&name=image.png&originHeight=340&originWidth=537&size=369461&status=done&style=none&width=400)


<a name="xc41N"></a>
# Horizontal Menu

```python
import urwid

class MenuButton(urwid.Button):
    def __init__(self, caption, callback):
        super(MenuButton, self).__init__("")
        urwid.connect_signal(self, 'click', callback)
        self._w = urwid.AttrMap(urwid.SelectableIcon(
            [u'  \N{BULLET} ', caption], 2), None, 'selected')

class SubMenu(urwid.WidgetWrap):
    def __init__(self, caption, choices):
        super(SubMenu, self).__init__(MenuButton(
            [caption, u"\N{HORIZONTAL ELLIPSIS}"], self.open_menu))
        line = urwid.Divider(u'\N{LOWER ONE QUARTER BLOCK}')
        listbox = urwid.ListBox(urwid.SimpleFocusListWalker([
            urwid.AttrMap(urwid.Text([u"\n  ", caption]), 'heading'),
            urwid.AttrMap(line, 'line'),
            urwid.Divider()] + choices + [urwid.Divider()]))
        self.menu = urwid.AttrMap(listbox, 'options')
	#
    def open_menu(self, button):
        top.open_box(self.menu)

class Choice(urwid.WidgetWrap):
    def __init__(self, caption):
        super(Choice, self).__init__(
            MenuButton(caption, self.item_chosen))
        self.caption = caption
	#
    def item_chosen(self, button):
        response = urwid.Text([u'  You chose ', self.caption, u'\n'])
        done = MenuButton(u'Ok', exit_program)
        response_box = urwid.Filler(urwid.Pile([response, done]))
        top.open_box(urwid.AttrMap(response_box, 'options'))

def exit_program(key):
    raise urwid.ExitMainLoop()

menu_top = SubMenu(u'Main Menu', [
    SubMenu(u'Applications', [
        SubMenu(u'Accessories', [
            Choice(u'Text Editor'),
            Choice(u'Terminal'),
        ]),
    ]),
    SubMenu(u'System', [
        SubMenu(u'Preferences', [
            Choice(u'Appearance'),
        ]),
        Choice(u'Lock Screen'),
    ]),
])

palette = [
    (None,  'light gray', 'black'),
    ('heading', 'black', 'light gray'),
    ('line', 'black', 'light gray'),
    ('options', 'dark gray', 'black'),
    ('focus heading', 'white', 'dark red'),
    ('focus line', 'black', 'dark red'),
    ('focus options', 'black', 'light gray'),
    ('selected', 'white', 'dark blue')]
focus_map = {
    'heading': 'focus heading',
    'options': 'focus options',
    'line': 'focus line'}

class HorizontalBoxes(urwid.Columns):
    def __init__(self):
        super(HorizontalBoxes, self).__init__([], dividechars=1)
	#
    def open_box(self, box):
        if self.contents:
            del self.contents[self.focus_position + 1:]
        self.contents.append((urwid.AttrMap(box, 'options', focus_map),
            self.options('given', 24)))
        self.focus_position = len(self.contents) - 1

top = HorizontalBoxes()
top.open_box(menu_top.menu)
urwid.MainLoop(urwid.Filler(top, 'middle', 10), palette).run()
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581167671183-8f436087-01c8-4a17-861e-09a13c7514cb.png#align=left&display=inline&height=225&name=image.png&originHeight=358&originWidth=636&size=74807&status=done&style=none&width=400)<br />
<br />

<a name="9vcI2"></a>
# Frames
<a name="6G3ti"></a>
##  urwid.Text

![](https://cdn.nlark.com/yuque/__puml/999a2529ac590e4c560985eb8111d10a.svg#lake_card_v2=eyJjb2RlIjoiZGlncmFwaCBGIHtcbiAgICByYW5rZGlyID0gTFI7XG4gICAgZWRnZSBbc3R5bGU9c29saWRdO1xuICAgIG5vZGUgW3N0eWxlPWZpbGxlZCwgZm9udD1Db3VyaWVyXTtcblxuICAgIHN1YmdyYXBoIEEge1xuICAgICAgICByYW5rID0gc2FtZTtcbiAgICAgICAgVGV4dCBbbGFiZWwgPSBcIlRleHRcIiwgc2hhcGUgPSBib3gsIGZpbGxjb2xvciA9IGRlZXBza3libHVlMSBdO1xuICAgICAgICBUZXh0MiBbbGFiZWwgPSBcIlRleHRcIiwgc2hhcGUgPSBib3gsIGZpbGxjb2xvciA9IGRlZXBza3libHVlMSBdO1xuXHRcdH1cbiAgICBzdWJncmFwaCBCIHtcbiAgICAgICAgcmFuayA9IHNhbWU7XG4gICAgICAgIFBpbGUgW2xhYmVsID0gXCJQaWxlXCIsIHNoYXBlID0gYm94LCBmaWxsY29sb3IgPSBkZWVwc2t5Ymx1ZTEgXTtcbiAgICAgICAgUGlsZTIgW2xhYmVsID0gXCJQaWxlXCIsIHNoYXBlID0gYm94LCBmaWxsY29sb3IgPSBkZWVwc2t5Ymx1ZTEgXTtcblx0XHR9XG4gICAgc3ViZ3JhcGggQyB7XG4gICAgICAgIHJhbmsgPSBzYW1lO1xuICAgICAgICBBdHRyTWFwIFtsYWJlbCA9IFwiQXR0ck1hcFwiLCBzaGFwZSA9IGJveCwgZmlsbGNvbG9yID0gZGVlcHNreWJsdWUxIF07XG4gICAgICAgIEF0dHJNYXAyIFtsYWJlbCA9IFwiQXR0ck1hcFwiLCBzaGFwZSA9IGJveCwgZmlsbGNvbG9yID0gZGVlcHNreWJsdWUxIF07XG4gICAgICAgIEZpbGxlciBbbGFiZWwgPSBcIkZpbGxlclwiLCBzaGFwZSA9IGJveCwgZmlsbGNvbG9yID0gZGVlcHNreWJsdWUxIF07XG4gICAgICAgIENvbHVtbnMgW2xhYmVsID0gXCJDb2x1bW5zXCIsIHNoYXBlID0gYm94LCBmaWxsY29sb3IgPSBkZWVwc2t5Ymx1ZTEgXTtcblx0XHR9XG4gICAgc3ViZ3JhcGggRCB7XG4gICAgICAgIHJhbmsgPSBzYW1lO1xuICAgICAgICBGcmFtZSBbbGFiZWwgPSBcIkZyYW1lXCIsIHNoYXBlID0gYm94LCBmaWxsY29sb3IgPSBkZWVwc2t5Ymx1ZTEgXTtcblx0XHR9XG5cblx0XG5cblx0XHR7VGV4dCxUZXh0Mn1cdC0-IFBpbGU7XG5cdFx0e1BpbGUsUGlsZTJ9IC0-IENvbHVtbnMgW2Fycm93aGVhZD1cIm5vbmVcIl07XG5cdFx0e1BpbGUsRmlsbGVyIENvbHVtbnN9XHQtPiBBdHRyTWFwO1xuXHRcdHtBdHRyTWFwLENvbHVtbnN9XHQtPiBGaWxsZXI7XG5cdFx0e0F0dHJNYXAsQXR0ck1hcDJ9XHQtPiBGcmFtZSAgW2Fycm93aGVhZD1cIm5vbmVcIl07XG5cdFxufSIsInR5cGUiOiJwdW1sIiwiaWQiOiJRZnNLWCIsInVybCI6Imh0dHBzOi8vY2RuLm5sYXJrLmNvbS95dXF1ZS9fX3B1bWwvOTk5YTI1MjlhYzU5MGU0YzU2MDk4NWViODExMWQxMGEuc3ZnIiwiY2FyZCI6ImRpYWdyYW0ifQ==)
不能:<br />{Column, AttrMap} --> Mainloop 

可:<br />{Filler, Frame } -> Mainloop 

Column -> Filler  -> Mainloop<br />Text -> Filler  -> Mainloop<br />Column -> Filler -> AttrMap -> Mainloop<br />Text -> Filler -> AttrMap -> Mainloop

<a name="QCusj"></a>
## Frame
> Frame(header=hdr, body=map2)
> Text -> *AttrWrap > header
> Columns -> *Filler -> *AttrMap -> body


<a name="U3Yzd"></a>
## ListBox
> x    Filler -> ListBox
> x    Padding -> SimpleListWalker -> ListBox
>
> [Text, Pile, Columns] -> SimpleListWalker -> ListBox
> [Text, Pile, Columns]-> SimpleListWalker -> ListBox -> *AttrWrap -> Frame


<a name="7dOh6"></a>
# Exampels
Source: [https://github.com/urwid/urwid/tree/master/examples](https://github.com/urwid/urwid/tree/master/examples)

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581170201460-f3dbc86f-af7c-42bf-bcf3-094bc7ae3d88.png#align=left&display=inline&height=200&name=image.png&originHeight=301&originWidth=351&size=20757&status=done&style=none&width=233)            ![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581170274321-1052c9a7-7b6e-4e4f-a6e4-5c329cb700ad.png#align=left&display=inline&height=200&name=image.png&originHeight=306&originWidth=386&size=36404&status=done&style=none&width=252)            ![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581171943127-d1a61ac4-c0be-4f41-81a8-aabce3646854.png#align=left&display=inline&height=200&name=image.png&originHeight=272&originWidth=199&size=9189&status=done&style=none&width=146)<br />                  browse.py                                                 bigtext.py                                        treesample.py

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581170387594-f2167445-aeca-4e08-b7e3-82365e1984fc.png#align=left&display=inline&height=200&name=image.png&originHeight=287&originWidth=598&size=29203&status=done&style=none&width=417)        ![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581171871938-ddf4380d-a574-445b-b101-7da155f3ac1f.png#align=left&display=inline&height=200&name=image.png&originHeight=436&originWidth=561&size=73529&status=done&style=none&width=257)<br />                                       calc.py                                                                                tour.py

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581170609398-8d7ac96d-32b9-4152-9e7c-1f98eebb29a3.png#align=left&display=inline&height=200&name=image.png&originHeight=239&originWidth=302&size=15764&status=done&style=none&width=253)![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581170737037-e933ab89-e467-4257-8603-91097d1bbcf8.png#align=left&display=inline&height=200&name=image.png&originHeight=361&originWidth=533&size=31259&status=done&style=none&width=295)<br />edit.py                                                                        fib.py

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581170810366-560eaabb-a071-4424-9831-aa452b060390.png#align=left&display=inline&height=200&name=image.png&originHeight=289&originWidth=533&size=13543&status=done&style=none&width=369)![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581171544560-ec8131c5-2b93-4c13-b208-0aebcc7f448e.png#align=left&display=inline&height=200&name=image.png&originHeight=391&originWidth=615&size=398332&status=done&style=none&width=315)<br />graph.py                                                                  terminal.py

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581170867897-2d0c87c8-eff6-469a-b095-5c0d002464c6.png#align=left&display=inline&height=200&name=image.png&originHeight=345&originWidth=630&size=80141&status=done&style=none&width=365)![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581171040048-3395d491-8cc0-4dc3-b4de-67a2e2b733f0.png#align=left&display=inline&height=200&name=image.png&originHeight=197&originWidth=372&size=15724&status=done&style=none&width=378)<br />input_test.py                                                                    pop_up.py

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581171009374-18c34c91-533c-4af9-be35-2a2c13afe306.png#align=left&display=inline&height=321&name=image.png&originHeight=642&originWidth=706&size=351387&status=done&style=none&width=353)<br />palette_test.py


more examples: [https://www.programcreek.com/python/example/12128/urwid.MainLoop](https://www.programcreek.com/python/example/12128/urwid.MainLoop)

<a name="jee6m"></a>
## pop_up.py

P-raw
```python
#!/usr/bin/env python

import urwid

class PopUpDialog(urwid.WidgetWrap):
    """A dialog that appears with nothing but a close button """
    signals = ['close']
    def __init__(self):
        close_button = urwid.Button("that's pretty cool")
        urwid.connect_signal(close_button, 'click',
            lambda button:self._emit("close"))
        pile = urwid.Pile([urwid.Text(
            "^^  I'm attached to the widget that opened me. "
            "Try resizing the window!\n"), close_button])
        fill = urwid.Filler(pile)
        self.__super.__init__(urwid.AttrWrap(fill, 'popbg'))


class ThingWithAPopUp(urwid.PopUpLauncher):
    def __init__(self):
        self.__super.__init__(urwid.Button("click-me"))
        urwid.connect_signal(self.original_widget, 'click',
            lambda button: self.open_pop_up())

    def create_pop_up(self):
        pop_up = PopUpDialog()
        urwid.connect_signal(pop_up, 'close',
            lambda button: self.close_pop_up())
        return pop_up

    def get_pop_up_parameters(self):
        return {'left':0, 'top':1, 'overlay_width':32, 'overlay_height':7}


fill = urwid.Filler(urwid.Padding(ThingWithAPopUp(), 'center', 15))
loop = urwid.MainLoop(
    fill,
    [('popbg', 'white', 'dark blue')],
    pop_ups=True)
loop.run()
```

原来程序:<br />![12.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/691897/1581859443674-2565cd29-ca05-4a45-9563-1adcd7dd0fbc.jpeg#align=left&display=inline&height=289&name=12.jpg&originHeight=289&originWidth=400&size=11350&status=done&style=none&width=400)<br />
<br />再 pop up 的框里面加一个退出按钮<br />结构解析:<br />

```python
close_button = urwid.Button("that's pretty cool")			#定义一个button 名称
urwid.connect_signal(close_button, 'click',					# button 的作用
                     lambda button:self._emit("close"))
pile = urwid.Pile([urwid.Text(								#一段文字,加上前面的button
    "^^  I'm attached to the widget that opened me. "			#pile 在一起
    "Try resizing the window!\n"), close_button])
fill = urwid.Filler(pile)									#封装
self.__super.__init__(urwid.AttrWrap(fill, 'popbg'))		#完成
```
可以看出基本结构为, Button -> Pile + Button  ->  Filler<br />因此, 除了加入button title和 signal 外, 还需要在 pile处, 一起打包.<br />测试:

```python
        esc_button = urwid.Button("Esc")
        urwid.connect_signal(esc_button, 'click',
            lambda button:self._emit("close"))
        pile = urwid.Pile([urwid.Text(
            "^^  I'm attached to the widget that opened me. "
            "Try resizing the window!\n"), close_button,esc_button])
```

直接加的话, 按键会依次排列:<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581860379136-f251d0b2-4d42-48ea-a24a-98ab369233ca.png#align=left&display=inline&height=45&name=image.png&originHeight=45&originWidth=304&size=2974&status=done&style=none&width=304)


<a name="mjICH"></a>
### Button 位置等属性
用 urwid.Padding(close_button, 'left', 18) 参数 调整button 位置, 结果一个上左, 一个右下<br />注: 18 为字符数<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581862070198-8c5f0de5-5f15-4849-a4a7-d0c4bc34cc07.png#align=left&display=inline&height=129&name=image.png&originHeight=129&originWidth=288&size=10386&status=done&style=none&width=288)

这里用到一个新函数 ,参考来源:[https://stackoverflow.com/questions/52252730/how-do-you-make-buttons-of-the-python-library-urwid-look-pretty](https://stackoverflow.com/questions/52252730/how-do-you-make-buttons-of-the-python-library-urwid-look-pretty)

<a name="TjLXz"></a>
### urwid.Columns
基本用法:  urwid.Columns([button1, button2])

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581863098176-7b7356fe-ab8c-477e-a698-a5b1356b5086.png#align=left&display=inline&height=143&name=image.png&originHeight=143&originWidth=289&size=9922&status=done&style=none&width=289)<br />

```python
def on_exit_clicked(button):
    raise urwid.ExitMainLoop()

# button, 加在上文 p-raw 的 9~11行之间
button = urwid.Button(u'Exit')
urwid.connect_signal(button, 'click', on_exit_clicked)

# button的排序, 加载urwid.Pile() 里面
urwid.Columns([
    urwid.Padding(close_button, 'left'),
    urwid.Padding(button, 'right', 8),
]),


```

完整代码:<br />pop-2
```python
#!/usr/bin/env python

import urwid

def on_exit_clicked(button):
    raise urwid.ExitMainLoop()

class PopUpDialog(urwid.WidgetWrap):
    """A dialog that appears with nothing but a close button """
    signals = ['close']

    def __init__(self):
        close_button = urwid.Button("that's NOT COOL")
        urwid.connect_signal(close_button, 'click',
            lambda button:self._emit("close"))

        button = urwid.Button(u'Exit')
        urwid.connect_signal(button, 'click', on_exit_clicked)

        pile = urwid.Pile([urwid.Text(
            "^^  I'm attached to the widget that opened me. "
            "Try resizing the window!\n"),
            urwid.Columns([
                urwid.Padding(close_button, 'left'),
                urwid.Padding(button, 'right', 8),
            ]),
            ])
        fill = urwid.Filler(pile)
        self.__super.__init__(urwid.AttrWrap(fill, 'popbg'))


class ThingWithAPopUp(urwid.PopUpLauncher):
    def __init__(self):
        self.__super.__init__(urwid.Button("click-me"))
        urwid.connect_signal(self.original_widget, 'click',
            lambda button: self.open_pop_up())

    def create_pop_up(self):
        pop_up = PopUpDialog()
        urwid.connect_signal(pop_up, 'close',
            lambda button: self.close_pop_up())
        return pop_up

    def get_pop_up_parameters(self):
        return {'left':0, 'top':1, 'overlay_width':32, 'overlay_height':7}


button = urwid.Button(u'Exit')
urwid.connect_signal(button, 'click', on_exit_clicked)

pile = urwid.Pile([urwid.Padding(ThingWithAPopUp(), 'center', 15),button])
fill = urwid.Filler(pile)
loop = urwid.MainLoop(
    fill,
    [('popbg', 'white', 'dark blue')],
    pop_ups=True)
loop.run()
```

<a name="Jbejz"></a>
### pop window size

修改这里就好了~
```python
def get_pop_up_parameters(self):
    return {'left':0, 'top':1, 'overlay_width':32, 'overlay_height':7}
```

![123.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/691897/1581864427590-354a9886-3040-4cf7-84b9-4224396841c1.jpeg#align=left&display=inline&height=117&name=123.jpg&originHeight=117&originWidth=400&size=5446&status=done&style=none&width=400)
<a name="cxS2V"></a>
### 魔改
左右各一个list:<br />将pile 放入column中<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581870602504-8ab5ff9b-0686-4ced-9a07-2bc81821d0a5.png#align=left&display=inline&height=203&name=image.png&originHeight=203&originWidth=535&size=190390&status=done&style=none&width=535)

把pop-2 的 51,52行改成
```python
pile = urwid.Pile(body_A)
col = urwid.Columns([pile,urwid.Text("│"),('fixed',14,pile)])
fill = urwid.Filler(col)
```


<a name="KcNTC"></a>
## bigtext.py
非常靓的一个<br />![123.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/691897/1581865775886-4205a6de-9e6e-4a32-826c-cb86cea7a0b0.jpeg#align=left&display=inline&height=223&name=123.jpg&originHeight=223&originWidth=400&size=17579&status=done&style=none&width=400)<br />
<br />排版区
```python
        # Create chars_avail
        cah = urwid.Text("Characters Available:")
        self.chars_avail = urwid.Text("", wrap='any')
        ca = urwid.AttrWrap(self.chars_avail, 'chars')

        chosen_font_rb.set_state(True) # causes set_font_event call

        # Create Edit widget
        edit = self.create_edit("", "Urwid "+urwid.__version__,
            self.edit_change_event)

        # ListBox
        chars = urwid.Pile([cah, ca])
        fonts = urwid.Pile([urwid.Text("Fonts:")] + self.font_buttons,
            focus_item=1)
        col = urwid.Columns([fonts,('fixed',16,chars)], 3,
            focus_column=1)
        bt = urwid.Pile([bt, edit], focus_item=1)
        l = [bt, urwid.Divider(), col]
        w = urwid.ListBox(urwid.SimpleListWalker(l))

        # Frame
        w = urwid.AttrWrap(w, 'body')
        hdr = urwid.Text("Urwid BigText example program - F8 exits.")
        hdr = urwid.AttrWrap(hdr, 'header')
        w = urwid.Frame(header=hdr, body=w)
```

<br />Frame 排版结构
![](https://cdn.nlark.com/yuque/__puml/a40369f5eba72bffebffe2c1de91f0e3.svg#lake_card_v2=eyJjb2RlIjoiZGlncmFwaCBGIHtcbiAgICByYW5rZGlyID0gTFI7XG4gICAgZWRnZSBbc3R5bGU9c29saWRdO1xuICAgIG5vZGUgW3N0eWxlPWZpbGxlZCwgZm9udD1Db3VyaWVyXTtcblxuICAgIHN1YmdyYXBoIEEge1xuICAgICAgICByYW5rID0gc2FtZTtcbiAgICAgICAgRW5kIFtsYWJlbCA9IFwid19GcmFtXCIsIHNoYXBlID0gYm94LCBmaWxsY29sb3IgPSBcIiNGRjAwMDBcIiBdO1xuXHRcdH1cblxuICAgIHN1YmdyYXBoIEIge1xuICAgICAgICByYW5rID0gc2FtZTtcbiAgICAgICAgaGRyIFtsYWJlbCA9IFwiaGRyX0F0dHJXcmFwXCIsIHNoYXBlID0gYm94LCBjb2xvciA9IGRlZXBza3libHVlMV07XG4gICAgICAgIHcgW2xhYmVsID0gXCJ3X0F0dHJXcmFwXCIsIHNoYXBlID0gYm94LCBjb2xvciA9IGRlZXBza3libHVlMV07XG5cdFx0XHRcdHcyIFtsYWJlbCA9IFwid19MaXN0Qm94XCIsIHNoYXBlID0gYm94LCBjb2xvciA9IGRlZXBza3libHVlMV07XG4gICAgfVxuXG5cbiAgICBzdWJncmFwaCBEIHtcbiAgICAgICAgcmFuayA9IHNhbWU7XG5cdFx0XHRcdGNoYSBbbGFiZWwgPSBcImNoYV9UZXh0XCIsIHNoYXBlID0gYm94LCBjb2xvciA9IGRlZXBza3libHVlMV07XG5cdFx0XHRcdGNoIFtsYWJlbCA9IFwiY2hfQXR0cldyYXBcIiwgc2hhcGUgPSBib3gsIGNvbG9yID0gZGVlcHNreWJsdWUxXTtcblx0XHR9XG5cbiAgICBzdWJncmFwaCBEIHtcbiAgICAgICAgcmFuayA9IHNhbWU7XG5cdFx0XHRcdGNoYXJzIFtsYWJlbCA9IFwiY2hhcnNfUGlsZVwiLCBzaGFwZSA9IGJveCwgY29sb3IgPSBkZWVwc2t5Ymx1ZTFdO1xuXHRcdFx0XHRmb250cyBbbGFiZWwgPSBcImZvbnRzX1BpbGVcIiwgc2hhcGUgPSBib3gsIGNvbG9yID0gZGVlcHNreWJsdWUxXTtcblx0XHR9XG4gICAgc3ViZ3JhcGggRiB7XG4gICAgICAgIHJhbmsgPSBzYW1lO1xuXHRcdFx0XHRoZHIyIFtsYWJlbCA9IFwiaGRyX1RleHRcIiwgc2hhcGUgPSBib3gsIGNvbG9yID0gZGVlcHNreWJsdWUxXTtcblx0XHRcdFx0RGl2aWRlciBbbGFiZWwgPSBcIkRpdmlkZXJcIiwgc2hhcGUgPSBib3gsIGNvbG9yID0gZGVlcHNreWJsdWUxXTtcblx0XHRcdFx0Y29sIFtsYWJlbCA9IFwiY29sX0NvbHVtbnNcIiwgc2hhcGUgPSBib3gsIGNvbG9yID0gZGVlcHNreWJsdWUxXTtcblx0XHRcdFx0YnQgW2xhYmVsID0gXCJidF9QaWxlXCIsIHNoYXBlID0gYm94LCBjb2xvciA9IGRlZXBza3libHVlMV07XG5cdFx0fVxuXHRcblxuXHRcdHtjaGEsIGNofSAtPiBjaGFycyBbbGFiZWw9XCLlt6bkuItsaXN0XCJdIDtcblx0XHR7Zm9udHMsY2hhcnN9IC0-IGNvbCBbbGFiZWw9XCLlj7PkuIvpgInmi6noj5zljZVcIl07XG5cbiAgICB7YnQsRGl2aWRlcixjb2x9XHQtPiB3MiBbbGFiZWwgPSBcIm91dHB1dOS7peS4i-mDqOWIhlwiXTtcblxuICAgIHcyXHRcdC0-IHcgIFtsYWJlbCA9IFwiXCJdO1xuICAgIGhkcjJcdC0-IGhkciBbbGFiZWwgPSBcIlwiXTtcblx0XHRcblx0XHRoZHJcdC0-IEVuZFxuXHRcdHdcdFx0LT4gRW5kXG59IiwidHlwZSI6InB1bWwiLCJpZCI6IllObU5jIiwidXJsIjoiaHR0cHM6Ly9jZG4ubmxhcmsuY29tL3l1cXVlL19fcHVtbC9hNDAzNjlmNWViYTcyYmZmZWJmZmUyYzFkZTkxZjBlMy5zdmciLCJjYXJkIjoiZGlhZ3JhbSJ9)
继续魔改. 首先发现一个bug, 虽然说按F8 退出, 但是按完以后, 只出来一个 pop window, 写着quit, 然后,,, 就没有然后了. 所以我们先来加一个Esc 按钮吧~ (以后再说)<br />
<br />

<a name="QvFMc"></a>
## Refresh
Eample

```python
import urwid
import time
import sys

'''
https://github.com/bavanduong/urwid-example/blob/master/clock.py
'''
class Clock:

    def keypress(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    def setup_view(self):
        self.clock_txt = urwid.BigText(
            time.strftime('%H:%M:%S'), urwid.font.HalfBlock5x4Font())
        self.view = urwid.Padding(self.clock_txt, 'center', width='clip')
        self.view = urwid.AttrMap(self.view, 'body')
        self.view = urwid.Filler(self.view, 'middle')

    def main(self):
        self.setup_view()
        loop = urwid.MainLoop(
            self.view, palette=[('body', 'dark cyan', '')],
            unhandled_input=self.keypress)
        loop.set_alarm_in(1, self.refresh)
        loop.run()

    def refresh(self, loop=None, data=None):
        self.setup_view()
        loop.widget = self.view
        loop.set_alarm_in(1, self.refresh)


if __name__ == '__main__':
    clock = Clock()
    sys.exit(clock.main())

```

<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581873976196-5e9e2176-fc5f-4491-96c8-2cebf343f4e2.png#align=left&display=inline&height=125&name=image.png&originHeight=125&originWidth=337&size=45541&status=done&style=none&width=337)<br />
<br />

<a name="e5hwH"></a>
# 實戰
<a name="lttQ1"></a>
## [Todolist](https://www.yuque.com/liuwenkan/blog/urwid_todolist)

<br />![deepin-screen-recorder_Select area_20200314002713.gif](https://cdn.nlark.com/yuque/0/2020/gif/691897/1584116870885-9493e05a-004d-43c5-a105-3cbd527048c0.gif#align=left&display=inline&height=333&name=deepin-screen-recorder_Select%20area_20200314002713.gif&originHeight=333&originWidth=662&size=152669&status=done&style=none&width=662)<br />

<a name="ATtSJ"></a>
## [Bilibili 信息板](https://www.yuque.com/liuwenkan/blog/suxiv3)

<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581879501970-2a9c010a-9801-461e-88e1-74a6f9ab9f15.png#align=left&display=inline&height=156&name=image.png&originHeight=156&originWidth=598&size=38295&status=done&style=none&width=598)
