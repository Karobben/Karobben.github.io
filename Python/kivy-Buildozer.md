---
url: buildozer
---

# kivy-Buildozer


<a name="Z0CZY"></a>
# 1 install Buildozer

```bash
sudo pip3.7  install -i https://pypi.tuna.tsinghua.edu.cn/simple 
```

链接安卓手机, 开启USB debug模式;<br />进入 kivy 项目目录<br />测试项目:[https://github.com/sevvalbrt/Todolist](https://github.com/sevvalbrt/Todolist)
```bash
buildozer init
buildozer android deploy run
```
手机有什么提示, 记得选择

可能会下一些东西. 等一下就好了<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1584001227762-8df00de8-b6f9-4790-b414-0c319bf06d3a.png#align=left&display=inline&height=230&name=image.png&originHeight=230&originWidth=507&size=200065&status=done&style=none&width=507)<br />
<br />更多参考:<br />[https://cycleuser.gitbooks.io/kivy-guide-chinese/content/15-Kivy-Pack-Android.html](https://cycleuser.gitbooks.io/kivy-guide-chinese/content/15-Kivy-Pack-Android.html)
