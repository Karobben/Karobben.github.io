---
title: "Kivy, Input Methods"
description: "Kivy, Input Methods| Kivy, 输入法, 中文输入问题"
date: "2020/10/31"
url: kivy_chinese
toc: true
excerpt: "Kivy, Input Methods| Kivy, 输入法, 中文输入问题"
tags: [Python, Kivy]
category: [Python, Kivy]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.dpHEt6VNif2n2c4ULEqQ7gHaDJ'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
priority: 10000
covercopy: '© dotmodus'
---

## Kivy, Input Methods


<span style="background:salmon">Thank for the help of 毛毛虫 from a Kivy QQ Group</span>

Add the codes below at the begin of your `main.py`

```python

from kivy.uix.dropdown import DropDown
from kivy.core.window import WindowBase
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
## Custmer Functions
### Crawler for DB

resource_add_path("./font")
LabelBase.register(DEFAULT_FONT, 'FZYanZQKSJF.ttf')

WindowBase.softinput_mode = "below_target"
```

And for doing so, make sure you are
**not using Gboard!**
**not using Gboard!**
**not using Gboard!**

![BakAx0.png](https://s1.ax1x.com/2020/10/31/BakAx0.png)
