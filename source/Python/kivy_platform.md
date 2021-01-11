---
title: "Kivy: import android"
description: "Kivy, import android in PC"
date: 2021/01/01
url: kivy_platform
---

# Kivy: import android

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
