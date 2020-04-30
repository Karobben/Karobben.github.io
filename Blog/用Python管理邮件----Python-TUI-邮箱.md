---
url: ikckgy
---

# 用Python管理邮件 -- Python TUI 邮箱


```bash
git clone https://github.com/pazz/alot.git

cd alot

python3.7 setup.py install
```

<a name="k35MJ"></a>
## 错误：

<a name="27jVX"></a>
### 1 libgpgme
error: Setup script exited with Could not find gpgme-config.  Please install the libgpgme development package.

```bash
Writing /tmp/easy_install-jevj4foo/gpg-1.10.0/setup.cfg
Running gpg-1.10.0/setup.py -q bdist_egg --dist-dir /tmp/easy_install-jevj4foo/gpg-1.10.0/egg-dist-tmp-qpuy_731
error: Setup script exited with Could not find gpgme-config.  Please install the libgpgme development package.

```

```bash
sudo apt install libgpgme-dev
python3.7 setup.py install
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581144571265-5d2f86a9-b305-4358-a5df-74bda8ead81a.png#align=left&display=inline&height=162&name=image.png&originHeight=162&originWidth=476&size=21043&status=done&style=none&width=476)<br />
<br />

<a name="mezds"></a>
### 2 cannot import name 'gpgme' from 'gpg'


+  +<br />出不来  - - 放弃了- - 日后再来 




--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
