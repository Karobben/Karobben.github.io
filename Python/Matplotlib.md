---
url: matplotlib2
---

# Matplotlib


<a name="XWWUc"></a>
# 1. Quick Start


<a name="Fsumh"></a>
## 1.1 Quick hit
```python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


np.random.seed(1000)
y = np.random.standard_normal(20)
x = range(len(y))
plt.plot(x, y)

plt.show()
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579661352291-90373740-f072-4c0f-8265-9c434858499d.png#align=left&display=inline&height=214&name=image.png&originHeight=240&originWidth=392&size=16529&status=done&style=none&width=350)

<a name="1dYBV"></a>
## 1.2 Adding layers

```python
# Showing change of each movements  
plt.ion()
plt.show()

np.random.seed(2000)
y = np.random.standard_normal((20,2)).cumsum(axis=0)

plt.figure(figsize=(7, 4))	# adding a canves figsize=(width, height)
plt.plot(y.cumsum(), 'm',lw=1.5)	# adding a line
plt.plot(y.cumsum(), 'ro')	# adding dots
plt.grid(True)	# adding grid on panals
plt.axis('tight')	# adding... I don't know
plt.xlabel('index')	# adding a title x
plt.ylabel('value')	# addint a title y
plt.title('A Simple Plot') # adding a title

```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579659267668-fd5097cc-cf1b-47cc-8941-6582a470f0ad.png#align=left&display=inline&height=196&name=image.png&originHeight=375&originWidth=670&size=24273&status=done&style=none&width=350)
<a name="l8Gj5"></a>
## 1.3 Facet(subplot)

```python
plt.ion()
plt.show()

# Data set
np.random.seed(2000)
y = np.random.standard_normal((20,2)).cumsum(axis=0)


plt.figure(figsize=(7,5))
plt.subplot(211)
'''
211:
2: 2 plot in a column;
1: 1 plot in a row
1: the 1sd
'''
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
plt.title('A Simple Plot')

plt.subplot(212) # the second
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
plt.plot(y[:, 1], 'ro')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579659303624-b42ac019-7e2b-418f-9505-11ee5b73af47.png#align=left&display=inline&height=244&name=image.png&originHeight=469&originWidth=673&size=42432&status=done&style=none&width=350)



<a name="KJDOy"></a>
# 2. Main Plot

<a name="bCizs"></a>
## 2.1 Dot plot

```python
plt.plot(y[:, 0], 'ro')
```

<a name="of4aN"></a>
## 2.2 Scatter plot

<a name="4KKFK"></a>
### 2.2.1 plot()
```python
y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7, 5))
plt.plot(y[:, 0], y[:, 1], 'ro')
plt.grid(True)
plt.title('Scatter Plot')
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579659559488-9bd7e62f-5cfa-4a4f-b86a-cd19d0583cf3.png#align=left&display=inline&height=256&name=image.png&originHeight=450&originWidth=615&size=46191&status=done&style=none&width=350)
<a name="x9oul"></a>
### 2.2.2 scatter()

```python
plt.figure(figsize=(7, 5))
plt.scatter(y[:, 0], y[:, 1], marker='o')
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')
```
<a name="VeB2w"></a>
##
<a name="7F9HK"></a>
### 2.2.3 Adding color: c = c

```python
c = np.random.randint(0, 10, len(y))
plt.figure(figsize=(7, 5))
plt.scatter(y[:, 0], y[:, 1], c=c, marker='o')
plt.colorbar()
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579659730619-6d3c24a4-1a14-48b1-a7d7-c928d29a17d8.png#align=left&display=inline&height=271&name=image.png&originHeight=471&originWidth=608&size=111149&status=done&style=none&width=350)
<a name="l20I2"></a>
## 2.3 Line plot

```python
y = np.random.standard_normal(20)
x = range(len(y))
plt.plot(y, lw=1.5, label='1st')
```

<a name="m1hbr"></a>
## 2.4 Bar plot

<a name="9RhWD"></a>
## 2.4.1 Bar plot
```python
y = np.random.standard_normal(20)
x = range(len(y))
plt.bar(np.arange(len(y)), y, width=0.5, color='g', label='2nd')
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579661634031-b3d48411-8bb1-4fa7-8143-5ab1d811f322.png#align=left&display=inline&height=265&name=image.png&originHeight=430&originWidth=567&size=9768&status=done&style=none&width=350)

<a name="IoN7c"></a>
## 2.4.2 Histogram
<a name="cZrhm"></a>
#### 1. Align as "dodge"
```python
plt.figure(figsize=(7, 4))
plt.hist(y, label=['1st', '2nd'], bins=25)
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579659780380-9970219d-104f-4966-b5bc-018ddbe83ce1.png#align=left&display=inline&height=203&name=image.png&originHeight=386&originWidth=666&size=16822&status=done&style=none&width=350)

<a name="xUpAg"></a>
#### 2. Align as 'stack'<br />
```python
y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7, 4))
plt.hist(y, label=['1st', '2nd'], color=['b', 'g'], stacked=True, bins=20)
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579659996121-4649044a-9724-4b2b-b0a8-ec3d73f20ef3.png#align=left&display=inline&height=206&name=image.png&originHeight=382&originWidth=648&size=16559&status=done&style=none&width=350)




<a name="bes3v"></a>
## 2.5 Box polt

```python
fig, ax = plt.subplots(figsize=(7,4))
plt.boxplot(y)
plt.grid(True)
plt.setp(ax, xticklabels=['1st', '2nd'])
plt.xlabel('data set')
plt.ylabel('value')
plt.title('Boxplot')
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579660079712-da317de0-5443-43c3-bf95-1d8d88cd6cd0.png#align=left&display=inline&height=209&name=image.png&originHeight=386&originWidth=645&size=14964&status=done&style=none&width=350)

<a name="HUUBd"></a>
## 2.6  Adding Text/Formula
```python
from matplotlib.patches import Polygon
def func(x):
    return 0.5 * np.exp(x) + 1
a, b = 0.5, 1.5
x = np.linspace(0, 2)
y = func(x)
fig, ax = plt.subplots(figsize=(7, 5))
plt.plot(x, y, 'b', linewidth=2)
plt.ylim(ymin=0)
Ix = np.linspace(a, b)
Iy = func(Ix)
verts = [(a, 0)] + list(zip(Ix, Iy)) + [(b, 0)]
poly = Polygon(verts, facecolor='0.7', edgecolor='0.5')
ax.add_patch(poly)
plt.text(0.5 * (a + b), 1, r"$\int_a^b fx\mathrm{d}x$", horizontalalignment='center', fontsize=20)
plt.figtext(0.9, 0.075, '$x$')
plt.figtext(0.075, 0.9, '$f(x)$')
ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks([func(a), func(b)])
ax.set_yticklabels(('$f(a)$', '$f(b)$'))
plt.grid(True)
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579660721746-07123b3b-eadd-4428-9ba7-81bae70ca82c.png#align=left&display=inline&height=219&name=image.png&originHeight=239&originWidth=382&size=11605&status=done&style=none&width=350)<br />Result


<a name="cyLz9"></a>
# 3. Plot 3D

<a name="Nk4gV"></a>
### 3.1 
```python
# Preparing for Data set
strike = np.linspace(50, 150, 24)
ttm = np.linspace(0.5, 2.5, 24)
strike, ttm = np.meshgrid(strike, ttm)
iv = (strike - 100) ** 2 / (100 * strike) / ttm

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(9,6))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(strike, ttm, iv, rstride=2, cstride=2, cmap=plt.cm.coolwarm, linewidth=0.5, antialiased=True)
ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')
fig.colorbar(surf, shrink=0.5, aspect=5)
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579661143348-6a513c35-23c8-4432-a33b-b5a53c54744b.png#align=left&display=inline&height=292&name=image.png&originHeight=507&originWidth=694&size=105915&status=done&style=none&width=400)


<a name="WVm3Q"></a>
### 3.2 switch to dot

```python
fig = plt.figure(figsize=(8, 5))

ax = fig.add_subplot(111, projection='3d')

ax.view_init(30, 60)
ax.scatter(strike, ttm, iv, zdir='z', s=25, c='b', marker='^')
ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579661176811-de328538-9db1-4ff9-8e7a-812cb7f98595.png#align=left&display=inline&height=368&name=image.png&originHeight=527&originWidth=573&size=158629&status=done&style=none&width=400)
