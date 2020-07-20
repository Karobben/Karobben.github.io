---
title: "用Python管理邮件 -- Python TUI 邮箱"
description: "用Python管理邮件 -- Python TUI 邮箱"
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

![Nskcrj.png](https://s1.ax1x.com/2020/06/26/Nskcrj.png)
<br />

<a name="mezds"></a>
### 2 cannot import name 'gpgme' from 'gpg'


+  +<br />出不来  - - 放弃了- - 日后再来 




---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
