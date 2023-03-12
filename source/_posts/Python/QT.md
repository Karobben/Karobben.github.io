---
title: "QT"
description: "QT"
url: qt2
date: 2020/01/22
toc: true
excerpt: "Qt for Python is the project that provides the official set of Python bindings (PySide2) that will supercharge your Python applications. While the Qt APIs are world renowned, there are more reasons why you should consider Qt for Python."
tags: [Python]
category: [Python, GUI, others]
cover: 'https://realpython.com/cdn-cgi/image/width=960,format=auto/https://files.realpython.com/media/Building-a-Python-Calculator-With-PyQt_Watermarked.e4c1a5cf2018.jpg'
covercopy: '<a href="https://realpython.com/python-pyqt-gui-calculator/">© realpython</a>'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## QT



```python
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel('Hello World!')
label.show()
app.exec_()
```


<a name="FlhjN"></a>
### 无边窗, 初始位点设定, 透明
```python
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import *

app = QApplication([])
My_Window = QLabel('Hello World!')
My_Window.setWindowFlags(Qt.WA_TranslucentBackground|Qt.WindowStaysOnBottomHint|Qt.SubWindow)
My_Window.move(1920, 100)
##背景颜色
My_Window.setStyleSheet("QLabel{color:rgb(225,22,173,255);font-size:50px;font-weight:normal;font-family:Arial;}")
My_Window.setWindowOpacity(0.5)
My_Window.show()
app.exec_()
```
<a name="X6BCX"></a>
#### 添加按钮(接上)
```python
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import *
import os

def btnPress1_clicked():
    os.system("google-chrome &")

app = QApplication([])
btnPress1=QPushButton('显示文本')
btnPress1.setWindowFlags(Qt.FramelessWindowHint|Qt.WA_TranslucentBackground|Qt.WindowStaysOnBottomHint|Qt.SubWindow)
btnPress1.clicked.connect(btnPress1_clicked)
btnPress1.move(1920, 100)
btnPress1.show()

```


<a name="Rxpq8"></a>
## 多个元素
```python
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui

app = QApplication([])
window = QWidget()
window.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnBottomHint|Qt.SubWindow)
window.setAutoFillBackground(False)
window.setAttribute(Qt.WA_TranslucentBackground, True)
window.repaint()


layout = QVBoxLayout()
btn = QPushButton('Top')
## 无边框
##btn.setFlat(True)
layout.addWidget(btn)
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()
```
