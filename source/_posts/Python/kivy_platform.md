---
title: "Kivy: import android Onlu on android"
ytitle: "Kivy: 導入安卓庫，僅在安卓設備情況下"
description: "Kivy, import android in only when on android devices"
date: 2021/01/01
url: kivy_platform
toc: true
excerpt: "Import android in kivy when it runs on Android devices"
tags: [Python, Kivy]
category: [Python, Kivy]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.dpHEt6VNif2n2c4ULEqQ7gHaDJ'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
priority: 10000
covercopy: '© dotmodus'
---


You may see error code below when you try to `import android` in your PC.
<pre>
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    from android.permissions import request_permissions, Permission
ModuleNotFoundError: No module named 'android'
</pre>

For solving this, you can import `platform` like below:

```python
from kivy.utils import platform

if platform == "android":
  from android.permissions import request_permissions, Permission
  request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
```
