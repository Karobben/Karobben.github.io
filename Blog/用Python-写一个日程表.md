---
url: urwid_todolist
---

# 用Python 写一个日程表

依赖: urwid; 

<a name="6Fm19"></a>
# 1 基本框架
<a name="tRQdB"></a>
## main.py
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
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1583827242581-7f5b83b7-b2af-4928-9e2b-f332407260f7.png#align=left&display=inline&height=245&name=image.png&originHeight=245&originWidth=533&size=8749&status=done&style=none&width=533)
<a name="MuI57"></a>
## ToDolist
文本文件, 用tab分隔
```bash
语文	10	0
数学	10	0
英语	10	0
```

<a name="mEq1j"></a>
# 2 读取内容从ToDolist
加入下文的第一行, 并在上文的12行, 改成下文第二行
```python
TODO = open(sys.path[0]+"/ToDolist",'r').read()
txt = urwid.Text(('banner', TODO), align='center')
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1583827522181-22c0adcd-e0f8-4207-9f3a-222b3e770b92.png#align=left&display=inline&height=251&name=image.png&originHeight=251&originWidth=541&size=32920&status=done&style=none&width=541)<br />
<br />当然, 这不是想要效果, 2333. 最好的是用numpy或者pandas来读成表格, matrix 的数据结构, 但是我不想为这么点点东西来费这么大的力气, 所以我就全用list了.

```python
def Read_ToDolsit():
    TODO = open(sys.path[0]+"/ToDolist",'r').read().split('\n')[:-1]
    Result = []
    for i in TODO:
        Result += [i.split()]
    return Result
```

这样, 之前的 open, 就直接改成
```python
TODO = Read_ToDolsit()
```

输出的TODO变成了:

```python
[['语文', '10', '0'], ['数学', '10', '0'], ['英语', '10', '0']]
```

<a name="B3tnr"></a>
# 3 放入列表

写一个循环读取, 并放入columns, columns 叠入Pile
```python
def TODO_col(TODO):
    Column_list = []
    for Sub in TODO:
        Sub_list = []
        for i in Sub:
            Sub_list += [urwid.Text(i)]
        Column_list += [urwid.Columns(Sub_list)]
    A = urwid.Pile(Column_list)
    return A
```

这样的话, 自动读取结果就是:<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1583828927470-60e983f4-c5eb-41f0-87a6-c55eff529c7b.png#align=left&display=inline&height=253&name=image.png&originHeight=253&originWidth=544&size=237910&status=done&style=none&width=544)<br />
<br />增加修改按钮:<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1583829200825-8b08fd09-454e-4edd-89b4-9ce581d5988c.png#align=left&display=inline&height=246&name=image.png&originHeight=246&originWidth=538&size=232898&status=done&style=none&width=538)<br />
<br />如何做到按钮对应每一列的操作, 我想的解决方案是,按钮直接操作ToDolist, 然后刷新整个页面. 反正都是小文本, 整个过程都是毫秒级的.<br />

<a name="NHNUy"></a>
# 4 添加计数按钮

想了好久= = 么有好方法= =只好预写一堆的button signal 放在 另一个页面, 然后丢在list里面 调用= = 唉, 虽然蠢, 但是有效就好.<br />
<br />不管怎么样- - 反正, 我算是成功了- - 唉... 虽然代码很丑<br />
<br />![deepin-screen-recorder_Select area_20200310182420.gif](https://cdn.nlark.com/yuque/0/2020/gif/691897/1583835907967-61b54436-8b94-44d1-9588-7047160bb787.gif#align=left&display=inline&height=250&name=deepin-screen-recorder_Select%20area_20200310182420.gif&originHeight=250&originWidth=540&size=143878&status=done&style=none&width=540)<br />
<br />这个时候的代码: (非常丑= =)

```python
#!/usr/bin/env python3

import urwid, sys, buttons

# exit the program
def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


'''
bottons
'''

def bottons_1P(button):
    List = Read_ToDolsit()
    List[0][2] = str(int(List[0][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()
 #    loop.set_alarm_in(1,Setupview)

def bottons_1M(button):
    List = Read_ToDolsit()
    List[0][2] = str(int(List[0][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_2P(button):
    List = Read_ToDolsit()
    List[1][2] = str(int(List[1][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_2M(button):
    List = Read_ToDolsit()
    List[1][2] = str(int(List[1][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_3P(button):
    List = Read_ToDolsit()
    List[2][2] = str(int(List[2][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_3M(button):
    List = Read_ToDolsit()
    List[2][2] = str(int(List[2][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_4P(button):
    List = Read_ToDolsit()
    List[3][2] = str(int(List[3][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_4M(button):
    List = Read_ToDolsit()
    List[3][2] = str(int(List[3][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_5P(button):
    List = Read_ToDolsit()
    List[4][2] = str(int(List[4][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_5M(button):
    List = Read_ToDolsit()
    List[4][2] = str(int(List[4][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_6P(button):
    List = Read_ToDolsit()
    List[5][2] = str(int(List[5][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_6M(button):
    List = Read_ToDolsit()
    List[5][2] = str(int(List[5][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_7P(button):
    List = Read_ToDolsit()
    List[6][2] = str(int(List[6][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_7M(button):
    List = Read_ToDolsit()
    List[6][2] = str(int(List[6][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_8P(button):
    List = Read_ToDolsit()
    List[7][2] = str(int(List[7][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_8M(button):
    List = Read_ToDolsit()
    List[7][2] = str(int(List[7][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_9P(button):
    List = Read_ToDolsit()
    List[8][2] = str(int(List[8][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_9M(button):
    List = Read_ToDolsit()
    List[8][2] = str(int(List[8][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

Botton_listP = [bottons_1P,bottons_2P,bottons_3P]
Botton_listM = [bottons_1M,bottons_2M,bottons_3M]

def bottons_resbond(a):
    TODO = Read_ToDolsit()
    fill = urwid.Filler(urwid.Pile([TODO_col(TODO),Fresh]))
    loop.widget = fill

'''
Botton is done
'''

def List2str(List):
    Result2 = ""
    for i in List:
        Result2 += '\t'.join(i) + '\n'
    return Result2

# reading Task from ToDoList

def Read_ToDolsit():
    TODO = open(sys.path[0]+"/ToDolist",'r').read().split('\n')[:-1]
    Result = []
    for i in TODO:
        Result += [i.split()]
    return Result

#bottons_resbond = bottons_resbond("P_line1")
#A = urwid.Columns([urwid.Text(TODO[0][0]),urwid.Text(TODO[0][1]),urwid.Text(TODO[0][2])])
#A = urwid.Pile([A,A])
def TODO_col(TODO):
    Num = 0
    Column_list = []
    for Sub in TODO:
        Num += 1
        Sub_list = []
        for i in Sub:
            Sub_list += [urwid.Text(i)]
        # bottons:
        locals()["P_line"+str(Num)]= urwid.Button(u'+')
        locals()["M_line"+str(Num)]= urwid.Button(u'-')
        # resbond:
        urwid.connect_signal(locals()["P_line"+str(Num)], 'click', Botton_listP[Num-1])
        urwid.connect_signal(locals()["M_line"+str(Num)], 'click', Botton_listM[Num-1])
        #
        Sub_list += [locals()["P_line"+str(Num)],locals()["M_line"+str(Num)]]
        Column_list += [urwid.Columns(Sub_list)]
    A = urwid.Pile(Column_list)
    return A

palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue'),]

def Setupview():
    TODO = Read_ToDolsit()
    #Fresh = urwid.Button('fresh')
    fill = urwid.Filler(TODO_col(TODO))
    return fill
TODO = Read_ToDolsit()
fill = urwid.Filler(TODO_col(TODO))#Setupview()
loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_q)
loop.run()
```

<a name="iWnus"></a>
# 5 将数字改成长条
我们把按钮左移, 然后加一个10个单位的进度条, 底色为红色

```python
def Bar_line(Sub,Bar_Max=20):
    if int(Sub[2])<= int(Sub[1]):
        Bar_G = int(int(Sub[2])*Bar_Max/int(Sub[1]))
        Bar_R = Bar_Max - Bar_G
        Bar_B = 0
    elif int(Sub[2]) > int(Sub[1]):
        Bar_G = Bar_Max-1
        Bar_R = 1
        Bar_B = int((int(Sub[2])-int(Sub[1]))*Bar_Max/int(Sub[1]))
        #print(int((int(Sub[2])-int(Sub[1]))*Bar_Max/int(Sub[1])))
    Sub_bar  = [('fixed',40,urwid.Text([('Green_BG', " "* Bar_G),('Red_BG', " "*Bar_R),('Blue_BG', " "*Bar_B)]))]
    return Sub_bar
```

到此, 最简单的日程表, 就已经做好啦!

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1583841536233-9a51da37-00a9-4269-80f9-761d379524aa.png#align=left&display=inline&height=247&name=image.png&originHeight=247&originWidth=537&size=196464&status=done&style=none&width=537)<br />完全代码:

```python
#!/usr/bin/env python3

import urwid, sys, buttons

# exit the program
def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


'''
bottons
'''

def bottons_1P(button):
    List = Read_ToDolsit()
    List[0][2] = str(int(List[0][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()
 #    loop.set_alarm_in(1,Setupview)

def bottons_1M(button):
    List = Read_ToDolsit()
    List[0][2] = str(int(List[0][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_2P(button):
    List = Read_ToDolsit()
    List[1][2] = str(int(List[1][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_2M(button):
    List = Read_ToDolsit()
    List[1][2] = str(int(List[1][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_3P(button):
    List = Read_ToDolsit()
    List[2][2] = str(int(List[2][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_3M(button):
    List = Read_ToDolsit()
    List[2][2] = str(int(List[2][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_4P(button):
    List = Read_ToDolsit()
    List[3][2] = str(int(List[3][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_4M(button):
    List = Read_ToDolsit()
    List[3][2] = str(int(List[3][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_5P(button):
    List = Read_ToDolsit()
    List[4][2] = str(int(List[4][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_5M(button):
    List = Read_ToDolsit()
    List[4][2] = str(int(List[4][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_6P(button):
    List = Read_ToDolsit()
    List[5][2] = str(int(List[5][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_6M(button):
    List = Read_ToDolsit()
    List[5][2] = str(int(List[5][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_7P(button):
    List = Read_ToDolsit()
    List[6][2] = str(int(List[6][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_7M(button):
    List = Read_ToDolsit()
    List[6][2] = str(int(List[6][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_8P(button):
    List = Read_ToDolsit()
    List[7][2] = str(int(List[7][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_8M(button):
    List = Read_ToDolsit()
    List[7][2] = str(int(List[7][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_9P(button):
    List = Read_ToDolsit()
    List[8][2] = str(int(List[8][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_9M(button):
    List = Read_ToDolsit()
    List[8][2] = str(int(List[8][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

Botton_listP = [bottons_1P,bottons_2P,bottons_3P,bottons_4P,bottons_5P,bottons_6P,bottons_7P,bottons_8P,bottons_9P]
Botton_listM = [bottons_1M,bottons_2M,bottons_3M,bottons_4M,bottons_5M,bottons_6M,bottons_7M,bottons_8M,bottons_9M]


'''
Botton is done
'''

def List2str(List):
    Result2 = ""
    for i in List:
        Result2 += '\t'.join(i) + '\n'
    return Result2

# reading Task from ToDoList

def Read_ToDolsit():
    TODO = open(sys.path[0]+"/ToDolist",'r').read().split('\n')[:-1]
    Result = []
    for i in TODO:
        Result += [i.split()]
    return Result

def Bar_line(Sub,Bar_Max=20):
    if int(Sub[2])<= int(Sub[1]):
        Bar_G = int(int(Sub[2])*Bar_Max/int(Sub[1]))
        Bar_R = Bar_Max - Bar_G
        Bar_B = 0
    elif int(Sub[2]) > int(Sub[1]):
        Bar_G = Bar_Max-1
        Bar_R = 1
        Bar_B = int((int(Sub[2])-int(Sub[1]))*Bar_Max/int(Sub[1]))
        #print(int((int(Sub[2])-int(Sub[1]))*Bar_Max/int(Sub[1])))
    Sub_bar  = [('fixed',40,urwid.Text([('Green_BG', " "* Bar_G),('Red_BG', " "*Bar_R),('Blue_BG', " "*Bar_B)]))]
    return Sub_bar

def TODO_col(TODO):
    Num = 0
    Column_list = []
    for Sub in TODO:
        Num += 1
        Sub_list = []
        for i in Sub:
            Sub_list += [urwid.Text(i)]
        # bottons:
        locals()["P_line"+str(Num)]= urwid.Button(u'+')
        locals()["M_line"+str(Num)]= urwid.Button(u'-')
        # resbond:
        urwid.connect_signal(locals()["P_line"+str(Num)], 'click', Botton_listP[Num-1])
        urwid.connect_signal(locals()["M_line"+str(Num)], 'click', Botton_listM[Num-1])
        #
        Sub_list = [('fixed',5,locals()["P_line"+str(Num)]),('fixed',5,locals()["M_line"+str(Num)])] + Sub_list
        # Bar determination:
        Sub_bar  = Bar_line(Sub)
        Column_list += [urwid.Columns(Sub_list + Sub_bar)]
    A = urwid.Pile(Column_list)
    return A

def Setupview():
    TODO = Read_ToDolsit()
    #Fresh = urwid.Button('fresh')
    fill = urwid.Filler(TODO_col(TODO))
    return fill

palette = [
    ('banner', 'black', 'light gray'),
    ('Red_BG', 'dark red', 'dark red'),
    ('Green_BG', 'dark green', 'dark green'),
    ('Blue_BG', 'dark blue', 'dark blue'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue'),]


fill = Setupview()
loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_q)
loop.run()
```

<a name="VlQY3"></a>
# 6 加一個title＆ Clean 按鈕

```python
def BigTxt(TXT):
    txt = urwid.BigText(
                ('banner',TXT), urwid.font.HalfBlock5x4Font())
    view = urwid.Padding(txt, 'center', width='clip')
    view = urwid.AttrMap(view, 'Blue_BG')
    return view#urwid.Columns([view])

def Button_C():
    def Clean(botton):
        List = Read_ToDolsit()
        for i in List:
            i[2] = str(0)
        Str_list = List2str(List)
        F = open(sys.path[0]+"/ToDolist",'w')
        F.write(Str_list)
        F.close()
        # refresh
        loop.widget = Setupview()
    Button_clean = urwid.Button(u"Clear")
    urwid.connect_signal(Button_clean, 'click', Clean)
    return Button_clean
```

Setview改一下:

```python
def Setupview():
    Header = BigTxt("What's Next???")
    TODO = Read_ToDolsit()
    ToDOcol_list = TODO_col(TODO)
    Button_clean = Button_C()
    ToDoWidget = urwid.Pile([Header] + ToDOcol_list+[Button_clean])
    fill = urwid.Filler(ToDoWidget)
    return fill

```

![deepin-screen-recorder_Select area_20200314002713.gif](https://cdn.nlark.com/yuque/0/2020/gif/691897/1584116870885-9493e05a-004d-43c5-a105-3cbd527048c0.gif#align=left&display=inline&height=333&name=deepin-screen-recorder_Select%20area_20200314002713.gif&originHeight=333&originWidth=662&size=152669&status=done&style=none&width=662)<br />--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](https://karobben.github.io/) <br />R 语言画图索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)<br />

