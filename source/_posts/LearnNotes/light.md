---
toc: true
url: light
covercopy: © Karobben
priority: 10000
date: 2024-01-18 21:30:37
title: "Light in Physics"
ytitle: "Light in Physics"
description: "Light in Physics"
excerpt: "Light in Physics"
tags: []
category: []
cover: ""
thumbnail: ""
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

### Example 1: Single Location Position

Let's set the $\lambda$ as 1, T as 10, and x = 0. Then, the equation could be simplified as $E(0, t) = sin[2\pi(0 - \frac{t}{10})]$.
And the change of the E^0^ with T could be show as the animation below.

|The E^0^ corresponded with the t | Static View by using x axis as t|
|:-:| :-:|
|![Observing the wave in single position](https://imgur.com/WvAIY5p.gif)|![Spread the observed points](https://imgur.com/Ct71NCk.png)|

### Example 2: Multiple Observation Locations

If we observe more positions, let's say, 0 to 10, and using the full function, we could get an animation like below. This is the propagating wave we could observe in 10 different locations.

![The propagating wave](https://imgur.com/KdWk5PU.gif)

## Direction of the Wave

When t increases, x increases => "+" direction on x;
When t increases, x decreases => "-" direction on x.

## Speed of the Wave

$velocity = \frac{\lambda}{T} = \lambda \nu$

- $\nu$ id frequency ($\frac{1}{T}$) of the wave.

So, the light of the wave is:
  - $c = \lambda \nu$

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
