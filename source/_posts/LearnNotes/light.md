---
toc: true
url: light
covercopy: <a href = "https://www.eoas.ubc.ca/courses/atsc113/sailing/met_concepts/08-met-waves/8b-wave-characteristics/index.html">© eoas</a> 
priority: 10000
date: 2024-01-18 21:30:37
title: "Light in Physics"
ytitle: "Light in Physics"
description: "Light in Physics"
excerpt: "Light in Physics"
tags: []
category: []
cover: "https://www.eoas.ubc.ca/courses/atsc113/sailing/met_concepts/08-met-waves/8b-wave-characteristics/img-8b/8-wave-characteristics.gif"
thumbnail: "https://www.eoas.ubc.ca/courses/atsc113/sailing/met_concepts/08-met-waves/8b-wave-characteristics/img-8b/8-wave-characteristics.gif"
---


## Mathmatic Description of the Light

In the equation you've provided:

$$
E(x,t) = E^0 \sin\left[2\pi \left(\frac{x}{\lambda} - \frac{t}{T}\right)\right]
$$

This represents a sinusoidal wave function, where $E(x,t)$ is the electric field of the light wave at a position $x$ and at time $t$. Here's what the terms mean:

- $E^0$ is the amplitude of the wave, which indicates the maximum strength of the electric field.
- $\lambda$ (lambda) is the wavelength of the light, which is the distance over which the wave's shape repeats.
- $T$ is the period of the wave, which is the time it takes for one complete cycle of the wave to pass a point. ($\frac{1}{T} = \nu$)

The reason both $\lambda$ and $T$ are present in the equation is because they describe different aspects of the wave:

- $\lambda$ describes the spatial repetition of the wave along the $x$-axis.
- $T$ describes the temporal repetition of the wave along the $t$-axis (time).

The term $\frac{x}{\lambda} - \frac{t}{T}$ is the phase of the wave, which determines the position of the peaks and troughs of the wave at any given time $t$ and position $x$. It's not meant to equal zero; instead, it changes with time and position to represent the propagation of the wave through space and time.

The phase changes as time goes by, indicating that the peaks and troughs of the wave are moving. If $\frac{x}{\lambda} - \frac{t}{T}$ were always zero, it would imply a stationary wave, not a propagating one.

The product $2\pi$ times the phase gives you the argument of the sine function in radians, which is necessary because the sine function is periodic with a period of $2\pi$. This means that the wave repeats itself every $2\pi$ radians, which corresponds to one wavelength in space and one period in time.


![Wave Function](https://imgur.com/D0t8uGs.png)

<details><summary>Plot codes</summary>

```python
import matplotlib.pyplot as plt
import numpy as np

def waveFun(x, t = 0, lamb = 1, pi = np.pi, T = 1, E0 = 1):
    E = E0 * np.sin(2 * pi * (x/lamb - t/T))
    return E     

Y = range(-50,50)
X = range(0,100)
Points = []
for x in X:
    for y in Y:
        Dis = np.sqrt((x/10)**2 + (y/10)**2)
        Points += [[x, y, waveFun(Dis)]]

Points = np.array(Points)

plt.figure(figsize=(7, 5))
plt.scatter(Points[:, 0], Points[:, 1] + 0.5, c= Points[:, 2], marker='o', cmap=plt.cm.coolwarm,)
plt.show()
```
</details>

### Example 1: Single Location Position

Let's set the $\lambda$ as 1, T as 10, and x = 0. Then, the equation could be simplified as $E(0, t) = sin[2\pi(0 - \frac{t}{10})]$.
And the change of the E^0^ with T could be show as the animation below.

|The E^0^ corresponded with the t | Static View by using x axis as t|
|:-:| :-:|
|![Observing the wave in single position](https://imgur.com/WvAIY5p.gif)|![Spread the observed points](https://imgur.com/Ct71NCk.png)|

### Example 2: Multiple Observation Locations

If we observe more positions, let's say, 0 to 10, and using the full function, we could get an animation like below. This is the propagating wave we could observe in 10 different locations.

![The propagating wave](https://imgur.com/KdWk5PU.gif)

|![Wave Motion in Time and Space](https://www.acs.psu.edu/drussell/Demos/wave-x-t/wave-x-t.gif)|
|:-:|
|[© psu](https://www.acs.psu.edu/drussell/Demos/wave-x-t/wave-x-t.html)|

## Direction of the Wave

When t increases, x increases => "+" direction on x;
When t increases, x decreases => "-" direction on x.

## Speed of the Wave

$velocity = \frac{\lambda}{T} = \lambda \nu$

- $\nu$ id frequency ($\frac{1}{T}$) of the wave.

So, the light of the wave is:
  - $c = \lambda \nu$


## Energy of the Wave

Energy of a wave is proportional to the square of the amplitude (in classical mechanics)

$\rho(\nu)$: energy per unit volume

$$
\rho(\nu) = constant\ x (E^ o)^ 2
$$

- ==Classic==: Energy is dependent on amplitude
- ==QM==: Energy is dependent on frequency

## Commonly used notation

1. **Wave Vector ($k$)**: The wave vector is defined as $\frac{2\pi}{\lambda}$, where $\lambda$ is the wavelength of the wave. The wave vector points in the direction of the wave's propagation and has a magnitude equal to the number of wave cycles per unit distance. The notation $\hat{k}$ represents a unit vector in the direction of $k$, so the wave vector $k$ is sometimes written as $\frac{2\pi}{\lambda} \hat{k}$, emphasizing its direction.

2. **Angular Frequency ($\omega$)**: This is defined as $2\pi\nu$, where $\nu$ is the frequency of the wave. It represents how many radians the wave cycles through per unit time.

3. **Phase ($\phi$)**: The phase is a term that allows us to specify where in its cycle the wave is at $t = 0$ and $x = 0$. It lets us define **the "zero point" or starting point** of the wave at a place other than the origin of our coordinate system.

$$E(x,t) = E^0 \sin(kx - \omega t + \phi)$$
$$H(x,t) = H^0 \sin(kx - \omega t + \phi)$$

!!! Question Why Standard Form?
    The first function form expresses the wave in terms of its wavelength λ and period T, which are perhaps more intuitive when you're first learning about waves.  It makes it very clear that the wave repeats itself every wavelength λ in space and every period T in time.
    
    The second function is the standard form. It's particularly useful in more advanced topics like wave interference, diffraction, and quantum mechanics, where the concept of phase space and the relationship between position and momentum (or wavelength and frequency) are crucial.
    
    For example, when you want to mimic the interference of the wave, the previous function could became extreamly complcated because the only difference between two wave is phase.

<details> <summary>More descriptions</summary>
These equations describe how the electric and magnetic fields oscillate as a function of space and time, which is characteristic of electromagnetic waves such as light. The quantities $E^0$ and $H^0$ are the maximum strengths of the electric and magnetic fields, respectively.

In an electromagnetic wave, the electric and magnetic fields are perpendicular to each other and to the direction of wave propagation. The equations show that both fields oscillate in sync (they have the same phase $\phi$) but are described by separate equations since they are perpendicular components.

The term $kx - \omega t$ indicates that the wave is moving in the positive $x$-direction. If the wave were moving in the negative $x$-direction, the sign in front of $\omega t$ would be positive.

The factor $\sin(kx - \omega t + \phi)$ varies between \(-1\) and \(1\), causing the electric and magnetic field strengths to oscillate between $-E^0$ to $E^0$ and $-H^0$ to $H^0$, respectively. The wave thus carries energy and, if it is light, can be observed as it interacts with matter.
</details>


## Huygen’s Principle (1678)

Waves spread as if each region of space is behaving as a source of new waves of the ==same frequency and phase==.
So, Huygen’s principle applied to light showing a wave front.


## Diffraction

![Wave Diffraction](https://imgur.com/vtuefhO.png)

When we konw d, D, X, and &theta; we could calcualate the &lambda; (wave length):
- When the light patten shows the dark point, we know that the phase between two waves is $n\frac{\lambda}{2}$
- So the $\Delta \phi$ of the first dark spot would be $\frac{\lambda}{2}$
- According to the plot, the &lambda; would be (path4 - path3) * 2 $ = \frac{d}{2}sin\theta$
- When the angle is very small, we have $sin\theta \approx tan\theta = \frac{X}{2}\frac{1}{D}$
- So finally, we could get: $\frac{d}{2}\frac{X}{2D} = \frac{\lambda}{2}$
    - $\lambda = \frac{dX}{2D}$

|![Two wave interference](https://imgur.com/qiLpQ7c.png)|![Three wave interference](https://imgur.com/1Cqo89a.png)|
|:-:|:-:|
|Two wave interference (center: y~1~ = -15, y~2~ = 15)| Three wave interference (y~1~ = 10, y~2~ = 0, y~3~ = -10)|

|![Double Slit](http://hyperphysics.phy-astr.gsu.edu/hbase/phyopt/imgpho/muls2.png)|
|:-:|
|[© gsu](http://hyperphysics.phy-astr.gsu.edu/hbase/phyopt/mulslid.html)|
|![Double Slit](https://myslu.stlawu.edu/~jmil/physics/labs/152_lab/setup_manual/blackboard/img/double_slit.gif)|
|stlawu.edu|

$$
n\lambda = d sin\theta_n \approx d tan\theta_n = d \frac{x_ n }{D}
$$

- Each photon is represented as a plane wave at the slits.
- The square of the amplitude of the recombined wave is proportional to the probability of finding the photon at this point

<details><summary>Plot code</summary>

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Y = range(-50,50)
X = range(0,100)

def waveFun(x, t = 0, lamb = 1, pi = np.pi, T = 1, E0 = 1):
    E = E0 * np.sin(2 * pi * (x/lamb - t/T))
    return E     

def WaveE(X, Y, dy = 0):
    Points = []
    for x in X:
        for y in Y:
            Dis = np.sqrt((x/10)**2 + (y/10)**2)
            Points += [[x, y + dy, waveFun(Dis)]]
    Points = np.array(Points)
    return Points

P1 = WaveE(X, Y, 0)
P2 = WaveE(X, Y, 10)
P3 = WaveE(X, Y, -10)

P1 = pd.DataFrame(P1, columns = ['x', 'y', "E1"])
P2 = pd.DataFrame(P2, columns = ['x', 'y', "E2"])
P3 = pd.DataFrame(P3, columns = ['x', 'y', "E3"])

TB = pd.merge(P1, P2)
TB = pd.merge(TB, P3)
TB['E'] = TB.E1 + TB.E2  + TB.E3

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(6,6))
ax.plot_trisurf(TB.x, TB.y, TB.E, vmin=TB.E.min() * 2, cmap=cm.coolwarm)
plt.show()

#plt.figure(figsize=(5, 5))
#plt.scatter(TB.x, TB.y, c= TB.E, marker='o', cmap=plt.cm.coolwarm,)
#plt.show()
```
</details>



## Principle of Superposition

At the beginning of the story, let's say there are two same waves with different $\phi$ which: $\phi_2 - \phi_1 = \pi$

In this case, the Intensity of this two wave is:
- $E^2_{sum} = (E_1 + E_2 )^2 = 0$
- ps: ==Not== $E^2_{sum} = E_1^2 + E_2^2 \neq 0$

(Destructive interference)

### For Two Traveling Waves

- Two sine waves with the same amplitude but slightly different frequencies traveling at the same velocity in the same direction

$ E(x,t) = E^o sin(k_1 x - \omega _1 t) +E^o sin(k_2 x - \omega _2 t) $
$ = 2 E^o cos [\frac{[k_1 - k_2]}{2}x - \frac{\omega _1 - \omega _2}{2}t] sin[\frac{[k_1 - k_2]}{2}x - \frac{\omega _1 - \omega _2}{2}t] $

## Direction

$$ 𝑛_1 \cdot sin 𝜃_1 = 𝑛_2 \cdot sin 𝜃_2 $$
 

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>

## Extra Explore

Becuase we konw:
- $E(x,t) = E^0 \sin\left[2\pi \left(\frac{x}{\lambda} - \frac{t}{T}\right)\right]$

So, when we move to the 2D wave, we could have function:
- $E(x, y, t) = E^0 \sin\left[2\pi \left(\frac{\sqrt{x^2 - y^2}}{\lambda} - \frac{t}{T}\right)\right]$

In order to calcualte the 2D wave from the different emission location, we need to introduce the initial point b=(b~x~, b~y~) 
- $E(x, y, b_x, b_y, t) = E^0 \sin\left[2\pi \left(\frac{\sqrt{(x-b_x)^2 - (y-b_y)^2}}{\lambda} - \frac{t}{T}\right)\right]$



<details><summary>Plot codes</details>

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pyvista as pv

def waveFun(x, y, bx =0, by = 0, t = 0, lamb = 1, pi = np.pi, T = 1, E0 = 1):
    E = E0 * np.sin(2 * pi * ((np.sqrt((x-bx)**2+(y-by)**2))/lamb - t/T))
    return E     


X = np.arange(100, step = .1)
Y = np.arange(-50,50, step = .1)
X, Y = np.meshgrid(X, Y)
Points = waveFun(X,X)

X = np.arange(-50, 50, step = .1)
Y = np.arange(-50, 50, step = .1)
X, Y = np.meshgrid(X, Y)
Points += waveFun(X,Y, lamb = .7, T = .7)

plt.imshow(Points)
plt.show()

for i in range(200):
    i = (i-100)/20  
    X = np.arange(100, step = .1)
    Y = np.arange(-50 + i,50 + i, step = .1)
    X, Y = np.meshgrid(X, Y)
    Points += waveFun(X,Y)


#plt.scatter(points_array[:, 0], points_array[:, 1] + 0.5, c= points_array[:, 2], marker='o', cmap=plt.cm.coolwarm,)
#plt.show()
# Create a PyVista point cloud
point_cloud = pv.PolyData(points_array)
point_cloud['point_color'] = point_cloud.points[:, 2]
point_cloud.plot(point_size=5,scalars='point_color', cmap="jet", show_bounds=True)






Y = range(-100,100)
X = range(0,200)
Points = []
for x in X:
    x /=10
    for y in Y:
        y /=10
        E = 0
        for by in np.arange(-10,11, .1):
            E += waveFun(x, y, 0, by)
        Points += [[x, y, E] ]

points_array = np.array(Points)
#plt.scatter(points_array[:, 0], points_array[:, 1] + 0.5, c= points_array[:, 2], marker='o', cmap=plt.cm.coolwarm,)
#plt.show()
# Create a PyVista point cloud
point_cloud = pv.PolyData(points_array)
point_cloud['point_color'] = point_cloud.points[:, 2]
point_cloud.plot(point_size=5,scalars='point_color', cmap="jet", show_bounds=True)



point_cloud = pv.PolyData(Points)
volume = point_cloud.delaunay_3d(alpha = 5)
shell = volume.extract_geometry()
shell.plot(show_edges=True)

TB = pd.DataFrame(Points, columns = ['x', 'y', 'E'])

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(6,6))
P = ax.plot_trisurf(TB.x, TB.y, TB.E, vmin=TB.E.min() * 2, cmap=plt.cm.coolwarm)
plt.show()


from scipy.interpolate import griddata

df =TB
x1 = np.linspace(df['x'].min(), df['x'].max(), len(df['x'].unique()))
y1 = np.linspace(df['y'].min(), df['y'].max(), len(df['y'].unique()))
"""
x, y via meshgrid for vectorized evaluation of
2 scalar/vector fields over 2-D grids, given
one-dimensional coordinate arrays x1, x2,..., xn.
"""
x2, y2 = np.meshgrid(x1, y1)
# Interpolate unstructured D-dimensional data.
z2 = griddata((df['x'], df['y']), df['E'], (x2, y2), method='cubic')



# Ready to plot
fig = plt.figure()
ax = fig.subplots(subplot_kw = {"projection":'3d'})

surf = ax.plot_surface(x2, y2, z2, rstride=1, cstride=1, cmap=plt.cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('Meshgrid Created from 3 1D Arrays')

plt.show()

```
</details>
