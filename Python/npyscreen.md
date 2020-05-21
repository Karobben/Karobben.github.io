---
url: npyscreen2
---
# npyscreen

**![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579621190752-8dd1e3a6-6d7a-41cc-9f7b-1713b84027ae.png#align=left&display=inline&height=811&name=image.png&originHeight=811&originWidth=1549&size=98271&status=done&style=none&width=1549)**<br />**<br />开发terminal平台软件<br />Developing terminal platform apps

<a name="N356a"></a>
# 1 Quick Start

```python
#!/usr/bin/env python3.7
# encoding: utf-8

import npyscreen
class TestApp(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "Welcome to Npyscreen",)
        t  = F.add(npyscreen.TitleText, name = "Text:",)
        fn = F.add(npyscreen.TitleFilename, name = "Filename:")
        fn2 = F.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
        s  = F.add(npyscreen.TitleSlider, out_of=12, name = "Slider")
        ml = F.add(npyscreen.MultiLineEdit,
               value = """try typing here!\nMutiline text, press ^R to reformat.\n""",
               max_height=5, rely=9)
        ms = F.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One",
                values = ["Option1","Option2","Option3"], scroll_exit=True)
        ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, value = [1,], name="Pick Several",
                values = ["Option1","Option2","Option3"], scroll_exit=True)
        # This lets the user interact with the Form.
        F.edit()
        print(ms.get_selected_objects())

if __name__ == "__main__":
    App = TestApp()
    App.run()
```

效果：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581064715450-01d0d9ad-d166-426d-bcf3-ad466a1146b4.png#align=left&display=inline&height=706&name=image.png&originHeight=706&originWidth=1184&size=51158&status=done&style=none&width=1184)

<a name="vvtzJ"></a>
# Features
<a name="TVnYP"></a>
##
<a name="CyyAV"></a>
## Input
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581064799262-4fa84aec-2ccc-4c9b-bf19-300329862f74.png#align=left&display=inline&height=43&name=image.png&originHeight=39&originWidth=274&size=3346&status=done&style=none&width=300)


<a name="Vwq2t"></a>
## Path segestion

<a name="hxo9y"></a>
### Path1:
Tab 键激活<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581064879908-f5b4e50b-5f96-4b11-853d-54c8d989fdc4.png#align=left&display=inline&height=212&name=image.png&originHeight=223&originWidth=631&size=31048&status=done&style=none&width=600)

<a name="S2ZQy"></a>
### Path2:
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581064978756-b42a6fdf-d7c0-4065-98fb-2f0204111233.png#align=left&display=inline&height=312&name=image.png&originHeight=614&originWidth=1179&size=98015&status=done&style=none&width=600)


<a name="Gih3Z"></a>
## Date
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581065105442-64be7d4d-0b0f-4c98-8e7b-64320ca74fb9.png#align=left&display=inline&height=244&name=image.png&originHeight=263&originWidth=378&size=23148&status=done&style=none&width=350)

<a name="FqeOj"></a>
## Slide
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581065130180-8c66dd14-9a28-4184-97a0-8e7cef43defd.png#align=left&display=inline&height=37&name=image.png&originHeight=37&originWidth=1153&size=4847&status=done&style=none&width=1153)

<a name="Nvocx"></a>
## Selection
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581065160715-6e7d92ea-fc6d-4b1f-8d11-50d7e2f9823b.png#align=left&display=inline&height=179&name=image.png&originHeight=149&originWidth=291&size=11505&status=done&style=none&width=350)<br />**see **[**ptop**](https://github.com/darxtrix/ptop)** as npyscreen apps **<br />**
