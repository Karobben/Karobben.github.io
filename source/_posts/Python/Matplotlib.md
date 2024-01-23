---
title: "Matplotlib"
description: "Matplotlib"
url: matplotlib2
date: 2020/01/22
toc: true
excerpt: "Matplotlib is a Python library used for data visualization, including creating graphs, charts, and plots. It offers a wide range of customization options and supports various output formats, including PDF, PNG, and SVG. <a title='GhatGPT'>Who said this?</a>"
tags: [Python, Plot, matplotlib]
category: [Python, Plot]
cover: 'https://s1.ax1x.com/2020/06/22/NYYKFx.png'
thumbnail: 'https://s1.ax1x.com/2020/06/22/NYYKFx.png'
priority: 10000
---

## Matplotlib


<a name="XWWUc"></a>
## 1. Quick Start


<a name="Fsumh"></a>
### 1.1 Quick hit
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

![NYYKFx.png](https://s1.ax1x.com/2020/06/22/NYYKFx.png)
<a name="1dYBV"></a>
### 1.2 Adding layers

```python
## Showing change of each movements  
plt.ion()
plt.show()

np.random.seed(2000)
y = np.random.standard_normal((20,2)).cumsum(axis=0)

plt.figure(figsize=(7, 4))  # adding a canves figsize=(width, height)
plt.plot(y.cumsum(), 'm',lw=1.5)  # adding a line
plt.plot(y.cumsum(), 'ro')  # adding dots
plt.grid(True)  # adding grid on panals
plt.axis('tight')  # adding... I don't know
plt.xlabel('index')  # adding a title x
plt.ylabel('value')  # addint a title y
plt.title('A Simple Plot') # adding a title

```

![NYYMY6.png](https://s1.ax1x.com/2020/06/22/NYYMY6.png)<a name="l8Gj5"></a>
### 1.3 Facet(subplot)

```python
plt.ion()
plt.show()

## Data set
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
![NYY1SO.png](https://s1.ax1x.com/2020/06/22/NYY1SO.png)



<a name="KJDOy"></a>
## 2. Main Plot

<a name="bCizs"></a>
### 2.1 Dot plot

```python
plt.plot(y[:, 0], 'ro')
```

<a name="of4aN"></a>
### 2.2 Scatter plot

<a name="4KKFK"></a>
#### 2.2.1 plot()
```python
y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7, 5))
plt.plot(y[:, 0], y[:, 1], 'ro')
plt.grid(True)
plt.title('Scatter Plot')
```

![NYY3lD.png](https://s1.ax1x.com/2020/06/22/NYY3lD.png)

<a name="x9oul"></a>
#### 2.2.2 scatter()

```python
plt.figure(figsize=(7, 5))
plt.scatter(y[:, 0], y[:, 1], marker='o')
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')
```

<a name="7F9HK"></a>
#### 2.2.3 Adding color: c = c

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
![NYYakt.png](https://s1.ax1x.com/2020/06/22/NYYakt.png)

#### Edge of the Scatter Points

```python
# default plot
plt.scatter(x= TB_Sp.Frame, y = TB_Sp.value, color = 'black', alpha = .1)
# Adding color to the edge
plt.scatter(x= TB_Sp.Frame, y = TB_Sp.value, color = 'black', alpha = .1, edgecolors = 'steelblue')
# remove the edges from each point
plt.scatter(x= TB_Sp.Frame, y = TB_Sp.value, color = 'black', alpha = .1, linewidths= 0 )
```

| Default | Edge with Color | No Edge |
| :-: | :-: | :-: |
| ![matplotlib: default scatter plot](https://imgur.com/QFB71uS.png)| ![matplotlib: scatter plot, change edge color](https://imgur.com/L7gFVkp.png)   | ![matplotlib: scatter plot, remove edge](https://imgur.com/NSYWGGk.png)|

### 2.3 Line plot

```python
y = np.random.standard_normal(20)
x = range(len(y))
plt.plot(y, lw=1.5, label='1st')
```

<a name="m1hbr"></a>
### 2.4 Bar plot

<a name="9RhWD"></a>
### 2.4.1 Bar plot
```python
y = np.random.standard_normal(20)
x = range(len(y))
plt.bar(np.arange(len(y)), y, width=0.5, color='g', label='2nd')
```
![NYYNTI.png](https://s1.ax1x.com/2020/06/22/NYYNTI.png)

<a name="IoN7c"></a>
### 2.4.2 Histogram
<a name="cZrhm"></a>
##### 1. Align as "dodge"
```python
plt.figure(figsize=(7, 4))
plt.hist(y, label=['1st', '2nd'], bins=25)
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')
```

![NYYQfK.png](https://s1.ax1x.com/2020/06/22/NYYQfK.png)
<a name="xUpAg"></a>
##### 2. Align as 'stack'<br />
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
![NYY86e.png](https://s1.ax1x.com/2020/06/22/NYY86e.png)




<a name="bes3v"></a>
### 2.5 Box polt

```python
fig, ax = plt.subplots(figsize=(7,4))
plt.boxplot(y)
plt.grid(True)
plt.setp(ax, xticklabels=['1st', '2nd'])
plt.xlabel('data set')
plt.ylabel('value')
plt.title('Boxplot')
```

![NYYGOH.png](https://s1.ax1x.com/2020/06/22/NYYGOH.png)

<a name="HUUBd"></a>
### 2.6  Adding Text/Formula
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

![NYYdtP.png](https://s1.ax1x.com/2020/06/22/NYYdtP.png)
Result


## 3. Plot 3D

#### 3.1 

```python
## Preparing for Data set
strike = np.linspace(50, 150, 24)
ttm = np.linspace(0.5, 2.5, 24)
strike, ttm = np.meshgrid(strike, ttm)
iv = (strike - 100) ** 2 / (100 * strike) / ttm

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(strike, ttm, iv, rstride=2, cstride=2, cmap=plt.cm.coolwarm, linewidth=0.5, antialiased=True)
ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')
fig.colorbar(surf, shrink=0.5, aspect=5)
```

![matplotlib, 3D surface plot](https://s1.ax1x.com/2020/06/22/NYYYmd.png)


#### 3.2 From Surface data to Dot

```python
fig = plt.figure(figsize=(8, 5))

ax = fig.add_subplot(111, projection='3d')

ax.view_init(30, 60)
ax.scatter(strike, ttm, iv, zdir='z', s=25, c='b', marker='^')
ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')
plt.show()
```

![matplotlib, 3D dots plot](https://s1.ax1x.com/2020/06/22/NYYwff.png)

#### From 3D Dots into Surface Plot

Cite: [Adobe, 2014](https://stackoverflow.com/questions/12423601/simplest-way-to-plot-3d-surface-given-3d-points)

```python
from matplotlib.ticker import MaxNLocator

X = range(10)
Y = range(10)
Points = []
for x in X:
    for y in Y:
        Points += [[x*10, y*10, x**y]]

Points = np.array(Points)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(6,6))
surf = ax.plot_trisurf(Points[:, 0], Points[:, 1], Points[:,2])

ax.xaxis.set_major_locator(MaxNLocator(5))
ax.yaxis.set_major_locator(MaxNLocator(6))
ax.zaxis.set_major_locator(MaxNLocator(5))
plt.show()
```

|![Matplotlib, 3D dots plot](https://imgur.com/FQdH74C.png)|![Matplotlib, from 3D dots into surface plot](https://imgur.com/RurDloP.png)|
|:-:|:-:|
|Raw 3D dots plot| Converte the 3D dots plot into surface plot|

## Save
```python
## Assignment the size of the picture
plt.figure(figsize=(12*3, 8*3))
## Save
plt.savefig(OUTPUT)
```

## plot a circle (ring)

[Yann, 2012](https://stackoverflow.com/questions/9215658/plot-a-circle-with-pyplot)

```python
import matplotlib.pyplot as plt

circle1 = plt.Circle((0, 0), 0.2, color='r')
circle2 = plt.Circle((0.5, 0.5), 0.2, color='blue')
circle3 = plt.Circle((1, 1), 0.2, color='g', clip_on=False)

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)

fig.savefig('plotcircles.png')
```

|![Matplotlib, circle plot](https://i.stack.imgur.com/6Wq0M.png)|
|:-:|
|[© Yann](https://stackoverflow.com/questions/9215658/plot-a-circle-with-pyplot)|

Others for 3D
- [Delaunay Triangulation to fill the mesh by **mayavi**](https://stackoverflow.com/questions/12423601/simplest-way-to-plot-3d-surface-given-3d-points)
- [calculate the ball like mesh by **pyvista**](https://stackoverflow.com/questions/54898657/i-want-to-generate-a-mesh-from-a-point-cloud-in-python)

## arrow

from point `(0, 0)`, `(2, 2)`

```python
plt.arrow(0, 0, 2, 2, width = 0.05)
```

4 points for 2 arrows:

```python
plt.arrow(P1[0], P1[1], P2[0]-P1[0], P2[1]-P1[1], width = 1)
plt.arrow(P3[0], P3[1], P4[0]-P3[0], P4[1]-P3[1], width = 1)
```

## Animation

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

y = []
for t in range(100):
    y += [np.sin(2*math.pi * (0 - t/100))]

x = np.array([0] * 100)
y = np.array(y)

fig, ax = plt.subplots()
line, = ax.plot(x, y, 'o')

def update(num, x, y, line):
    line.set_data(x[num], y[num])
    return line,

ani = animation.FuncAnimation(fig, update, len(x), interval=10,
                              fargs=[x, y, line], blit=True)
ani.save('animation_drawing.gif', writer='imagemagick', fps=60)

plt.plot(np.array(range(100))/10, y, 'o')
plt.savefig('wave.png')
plt.show()
```

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

frame = 100 
Y = []
for x in range(10):
    y = []
    for t in range(frame):
        y += [np.sin(2*math.pi * (x/10 - t/10/10))]
    Y += [np.array(y)]

Y = np.array(Y)
X = np.array([[i] * frame for i in range(len(Y))])

fig, ax = plt.subplots()
line, = ax.plot([0, 10], [-1, 1], 'o')
ax.set_ylim(-1)

def update(num, x, y, line):
    line.set_data(x[:,num], y[:,num])
    return line,

ani = animation.FuncAnimation(fig, update, frame, interval=100,
                              fargs=[X, Y, line], blit=True )
ani.save('animation_drawing.gif', writer='imagemagick', fps=60)

plt.plot(np.array(range(100))/10, y, 'o')
plt.savefig('wave.png')
plt.show()
`
