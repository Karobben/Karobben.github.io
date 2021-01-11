---
title: "Kivy, Input Methods"
description: "Kivy, Input Methods| Kivy, 输入法, 中文输入问题"
date: "2020/10/31"
url: Kivy_Chinese
---

# Kivy, Input Methods


<span style="background:salmon">Thank for the help of 毛毛虫 from a Kivy QQ Group</span>

Add the codes below at the begin of your `main.py`

```python

from kivy.uix.dropdown import DropDown
from kivy.core.window import WindowBase
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
# Custmer Functions
## Crawler for DB

resource_add_path("./font")
LabelBase.register(DEFAULT_FONT, 'FZYanZQKSJF.ttf')

WindowBase.softinput_mode = "below_target"
```

And for doing so, make sure you are
**not using Gboard!**
**not using Gboard!**
**not using Gboard!**

[![BakAx0.png](https://s1.ax1x.com/2020/10/31/BakAx0.png)](https://imgchr.com/i/BakAx0)
