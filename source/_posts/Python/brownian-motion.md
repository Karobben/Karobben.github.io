---
toc: true
url: brownian_motion
covercopy: © Karobben
priority: 10000
date: 2022-11-23 12:56:12
title: "Brownian Motion"
ytitle: "Brownian Motion"
description: "Brownian Motion"
excerpt: "Brownian motion is the random and erratic movement of small particles in a fluid or gas due to collisions with molecules in the surrounding medium. It was first observed and explained by Robert Brown in 1827, and is an important concept in the study of diffusion and stochastic processes. <a title='GhatGPT'>Who said this?</a>"
tags: [Python, Data]
category: [Python, Data]
cover: "https://s1.ax1x.com/2023/03/02/ppFi6mT.png"
thumbnail: "https://s1.ax1x.com/2023/03/02/ppFi6mT.png"
---

Codes from: [Tirthajyoti Sarkar](https://towardsdatascience.com/brownian-motion-with-python-9083ebc46ff0)

```python
import numpy as np
import matplotlib.pyplot as plt

class Brownian():
    """
    A Brownian motion class constructor
    """
    def __init__(self,x0=0):
        """
        Init class
        """
        assert (type(x0)==float or type(x0)==int or x0 is None), "Expect a float or None for the initial value"
        self.x0 = float(x0)
    def gen_random_walk(self,n_step=100):
        """
        Generate motion by random walk
        Arguments:
            n_step: Number of steps
        Returns:
            A NumPy array with `n_steps` points
        """
        # Warning about the small number of steps
        if n_step < 30:
            print("WARNING! The number of steps is small. It may not generate a good stochastic process sequence!")
        w = np.ones(n_step)*self.x0
        for i in range(1,n_step):
            # Sampling from the Normal distribution with probability 1/2
            yi = np.random.choice([1,-1])
            # Weiner process
            w[i] = w[i-1]+(yi/np.sqrt(n_step))
        return w

    def gen_normal(self,n_step=100):
        """
        Generate motion by drawing from the Normal distribution
        Arguments:
            n_step: Number of steps
        Returns:
            A NumPy array with `n_steps` points
        """
        if n_step < 30:
            print("WARNING! The number of steps is small. It may not generate a good stochastic process sequence!")
        w = np.ones(n_step)*self.x0
        for i in range(1,n_step):
            # Sampling from the Normal distribution
            yi = np.random.normal()
            # Weiner process
            w[i] = w[i-1]+(yi/np.sqrt(n_step))
        return w

    def stock_price(
                    self,
                    s0=100,
                    mu=0.2,
                    sigma=0.68,
                    deltaT=52,
                    dt=0.1
                    ):
        """
        Models a stock price S(t) using the Weiner process W(t) as
        `S(t) = S(0).exp{(mu-(sigma^2/2).t)+sigma.W(t)}`
        Arguments:
            s0: Iniital stock price, default 100
            mu: 'Drift' of the stock (upwards or downwards), default 1
            sigma: 'Volatility' of the stock, default 1
            deltaT: The time period for which the future prices are computed, default 52 (as in 52 weeks)
            dt (optional): The granularity of the time-period, default 0.1
        Returns:
            s: A NumPy array with the simulated stock prices over the time-period deltaT
        """
        n_step = int(deltaT/dt)
        time_vector = np.linspace(0,deltaT,num=n_step)
        # Stock variation
        stock_var = (mu-(sigma**2/2))*time_vector
        # Forcefully set the initial value to zero for the stock price simulation
        self.x0=0
        # Weiner process (calls the `gen_normal` method)
        weiner_process = sigma*self.gen_normal(n_step)
        # Add two time series, take exponent, and multiply by the initial stock price
        s = s0*(np.exp(stock_var+weiner_process))

        return s

b1 = Brownian()
b2 = Brownian()

x = b1.gen_normal(10000)
y = b2.gen_normal(10000)

colors = np.linspace(0, 1, len(x))

plt.plot(x,y, color = 'grey')
plt.scatter(x,y, c=colors, cmap='viridis')
xmax,xmin,ymax,ymin = x.max(),x.min(),y.max(),y.min()
scale_factor = 1.25
xmax,xmin,ymax,ymin = xmax*scale_factor,xmin*scale_factor,ymax*scale_factor,ymin*scale_factor
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
plt.show()
```

![network path find](https://s1.ax1x.com/2023/03/02/ppFic0U.png)

# Use Opencv to Show the Animation

```python
import cv2
import numpy as np

def Position_update(Point1):
    yi1 = np.random.normal()*10
    yi2 = np.random.normal()*10
    Point1[0] =  Point1[0] + int(yi1/np.sqrt(30))
    Point1[1] =  Point1[1] + int(yi2/np.sqrt(30))
    return Point1

MAP = np.zeros([1500, 1500, 3], dtype=np.uint8)
MAP[MAP==0] = 255

Point = {}
for i in range(1000):
    Point.update({i:[750,750]})

b1 = Brownian(1)
b2 = Brownian(1)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1080,1080))


while (True):
    MAP = np.zeros([1080, 1080, 3], dtype=np.uint8)
    MAP[MAP==0] = 255
    for i in range(1000):
        Point[i]=Position_update(Point[i])
        cv2.circle(MAP, Point[i], 3, [0,0,0], 2)
    cv2.imshow("video",MAP)
    out.write(MAP)
    if cv2.waitKey(25)&0xFF==ord('q'):
       cv2.destroyAllWindows()
       break
```


Detection

```python
import cv2
import numpy as np


# Map Edge detection

# Direction Reverse

Point1 = {
    "O":[200,200],
    "N":[20,10],
    "Dit":[0,0],
    "Sp": 1
}

def Map_bonce(Point, X, Y):
    if Point['N'][0] <0:
        Point['N'][0] *= -1
    if Point['N'][1] <0:
        Point['N'][1] *= -1
    if Point['N'][0] > X:
        Point['N'][0] = X - (Point['N'][0]- X)
    if Point['N'][1] > Y:
        Point['N'][1] = Y - (Point['N'][1]- Y)

    return(Point)

Point = {}

for i in range(10):
    Point.update({i:{
        "O":np.array([50,50]),
        "N":np.array([50,50]),
        "Dit":np.array([0,0]),
        "Sp": 1
    }})


while (True):
    MAP = np.zeros([100, 100, 3], dtype=np.uint8)
    MAP[MAP==0] = 255
    for i in range(10):
        Point[i]["O"] = np.array(Point[i]["N"])
        Point[i]["N"] = Position_update(Point[i]["N"])
        Point[i]= Map_bonce(Point[i], len(MAP[0]), len(MAP))
        # update old position and direction
        Point[i]["Dit"]=Point[i]["N"] - Point[i]["O"]
        cv2.circle(MAP, Point[i]["N"], 3, [0,0,0], 2)
        print(Point[i])

    cv2.imshow("video",MAP)
    if cv2.waitKey(25)&0xFF==ord('q'):
       cv2.destroyAllWindows()
       break
```


Collision by the center point

```python
import pandas as pd

# Overlap detection
def Map_bonce(Point, X, Y):
    if Point['N'][0] <0:
        Point['N'][0] *= -1
    if Point['N'][1] <0:
        Point['N'][1] *= -1
    if Point['N'][0] > X:
        Point['N'][0] = X - (Point['N'][0]- X)
    if Point['N'][1] > Y:
        Point['N'][1] = Y - (Point['N'][1]- Y)

    return(Point)

Point = {}
N_point = 300
for i in range(N_point):
    Point.update({i:{
        "O":np.array([50,50]),
        "N":np.array([50,50]),
        "Dit":np.array([0,0]),
        "Sp": 1
    }})

while (True):
    MAP = np.zeros([500, 500, 3], dtype=np.uint8)
    MAP[MAP==0] = 255
    for i in range(N_point):
        Point[i]["O"] = np.array(Point[i]["N"])
        Point[i]["N"] = Position_update(Point[i]["N"])
        # Check map-collision
        Point[i]= Map_bonce(Point[i], len(MAP[0]), len(MAP))
        # Particals Collision
        # update old position and direction
        Point[i]["Dit"]=Point[i]["N"] - Point[i]["O"]
    while True  in pd.DataFrame([Point[i]['N'] for i in Point]).duplicated().tolist():
        TMP = pd.DataFrame([Point[i]['N'] for i in Point])
        TMP2 = TMP[TMP.duplicated()]
        TMP == TMP2.iloc[0,:]
        INDEX = [i for i in Point if Point[i]['N'].tolist() == Point[TMP2.index[0]]['N'].tolist()]
        print(INDEX)
        for i in range(int(len(INDEX)/2)):
            INDEX_1 = INDEX[i*2]
            INDEX_2 = INDEX[i*2+1]
            Point[INDEX_1]['N'] +=Point[INDEX_2]['Dit']
            Point[INDEX_2]['N'] +=Point[INDEX_1]['Dit']
            Point[INDEX_1]["O"] = np.array(Point[INDEX_1]["N"])
            Point[INDEX_2]["O"] = np.array(Point[INDEX_2]["N"])
            if Point[INDEX_1]["O"].tolist() == Point[INDEX_1]["N"].tolist():
                Point[i]["N"] = Position_update(Point[i]["N"])
            if Point[INDEX_2]["O"].tolist() == Point[INDEX_2]["N"].tolist():
                Point[INDEX_2]["N"] = Position_update(Point[INDEX_2]["N"])
            Point[INDEX_1]["Dit"]=Point[INDEX_1]["N"] - Point[INDEX_1]["O"]
            Point[INDEX_2]["Dit"]=Point[INDEX_2]["N"] - Point[INDEX_2]["O"]
        # Check map-collision
        Point[INDEX_1]= Map_bonce(Point[INDEX_1], len(MAP[0]), len(MAP))
        Point[INDEX_2]= Map_bonce(Point[INDEX_2], len(MAP[0]), len(MAP))

    for i in range(N_point):
        cv2.circle(MAP, Point[i]["N"], 3, [0,0,0], 2)
    print(Point[i])

    cv2.imshow("video",MAP)
    if cv2.waitKey(25)&0xFF==ord('q'):
       cv2.destroyAllWindows()
       break
```

Collision based on the mask

mask circle

```python
# Circle Mask
def Cir_mas(Radian):
    x = np.arange(0, Radian *2 +1)
    y = np.arange(0, Radian *2 +1)
    arr = np.zeros((y.size, x.size))

    cx = Radian +1
    cy = Radian +1
    r = Radian

    # The two lines below could be merged, but I stored the mask
    # for code clarity.
    mask = (x[np.newaxis,:]-cx)**2 + (y[:,np.newaxis]-cy)**2 < r**2
    TMP = pd.melt(pd.DataFrame(mask).reset_index(), id_vars='index')
    MASK = TMP.iloc[:,:2][TMP.value==True].to_numpy()-[Radian+1,Radian+1]
    return
```

```python
def Map_bonce(Point, X, Y):
    if Point['N'][0] <0:
        Point['N'][0] *= -1
    if Point['N'][1] <0:
        Point['N'][1] *= -1
    if Point['N'][0] > X:
        Point['N'][0] = X - (Point['N'][0]- X)
    if Point['N'][1] > Y:
        Point['N'][1] = Y - (Point['N'][1]- Y)

    return(Point)


Point = {}
N_point = 50
for i in range(N_point):
    X = np.random.choice(range(500))
    Y = np.random.choice(range(500))
    Point.update({i:{
        "O":np.array([X,Y]),
        "N":np.array([X,Y]),
        "Dit":np.array([0,0]),
        "Ms": Cir_mas(3),
        "Sp": 1
    }})

def Point_TB(Point):
    TB = pd.DataFrame()
    for i in Point:
        tmp = pd.DataFrame(Point[i]['Ms'])  + Point[i]['N']
        tmp['index'] = i
        TB = pd.concat([TB, tmp])
    return TB

while (True):
    MAP = np.zeros([500, 500, 3], dtype=np.uint8)
    MAP[MAP==0] = 255
    for i in range(N_point):
        Point[i]["O"] = np.array(Point[i]["N"])
        Point[i]["N"] = Position_update(Point[i]["N"])
        # Check map-collision
        Point[i]= Map_bonce(Point[i], len(MAP[0]), len(MAP))
        # Particals Collision
        # update old position and direction
        Point[i]["Dit"]=Point[i]["N"] - Point[i]["O"]

    while True  in Point_TB(Point).iloc[:,:2].duplicated().tolist():
        TMP = Point_TB(Point)
        TMP2 = TMP[TMP.iloc[:,:2].duplicated()]
        INDEX = TMP[[i== TMP2.iloc[:,:2].to_numpy().tolist()[0] for i in TMP.iloc[:,:2].to_numpy().tolist()]]['index'].to_numpy()
        print(INDEX)
        for i in range(int(len(INDEX)/2)):
            INDEX_1 = INDEX[i*2]
            INDEX_2 = INDEX[i*2+1]
            Point[INDEX_1]['N'] +=Point[INDEX_2]['Dit']
            Point[INDEX_2]['N'] +=Point[INDEX_1]['Dit']
            Point[INDEX_1]["O"] = np.array(Point[INDEX_1]["N"])
            Point[INDEX_2]["O"] = np.array(Point[INDEX_2]["N"])
            if Point[INDEX_1]["O"].tolist() == Point[INDEX_1]["N"].tolist():
                Point[i]["N"] = Position_update(Point[i]["N"])
            if Point[INDEX_2]["O"].tolist() == Point[INDEX_2]["N"].tolist():
                Point[INDEX_2]["N"] = Position_update(Point[INDEX_2]["N"])
            Point[INDEX_1]["Dit"]=Point[INDEX_1]["N"] - Point[INDEX_1]["O"]
            Point[INDEX_2]["Dit"]=Point[INDEX_2]["N"] - Point[INDEX_2]["O"]
        # Check map-collision
        Point[INDEX_1]= Map_bonce(Point[INDEX_1], len(MAP[0]), len(MAP))
        Point[INDEX_2]= Map_bonce(Point[INDEX_2], len(MAP[0]), len(MAP))
        print(Point)

    for i in range(N_point):
        cv2.circle(MAP, Point[i]["N"], 3, [0,0,0], 1)

    cv2.imshow("video",MAP)
    if cv2.waitKey(25)&0xFF==ord('q'):
       cv2.destroyAllWindows()
       break

```















<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
