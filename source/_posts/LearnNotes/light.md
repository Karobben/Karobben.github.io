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


The image you've uploaded contains a set of equations that describe a wave, likely in the context of electromagnetic theory. Here is an explanation of the concepts:

1. **Wave Vector ($k$)**: The wave vector is defined as $\frac{2\pi}{\lambda}$, where $\lambda$ is the wavelength of the wave. The wave vector points in the direction of the wave's propagation and has a magnitude equal to the number of wave cycles per unit distance. The notation $\hat{k}$ represents a unit vector in the direction of $k$, so the wave vector $k$ is sometimes written as $\frac{2\pi}{\lambda} \hat{k}$, emphasizing its direction.

2. **Angular Frequency ($\omega$)**: This is defined as $2\pi\nu$, where $\nu$ is the frequency of the wave. It represents how many radians the wave cycles through per unit time.

3. **Phase ($\phi$)**: The phase is a term that allows us to specify where in its cycle the wave is at $t = 0$ and $x = 0$. It lets us define **the "zero point" or starting point** of the wave at a place other than the origin of our coordinate system.

$$E(x,t) = E^0 \sin(kx - \omega t + \phi)$$
$$H(x,t) = H^0 \sin(kx - \omega t + \phi)$$

<details> <summary>More descriptions</summary>
These equations describe how the electric and magnetic fields oscillate as a function of space and time, which is characteristic of electromagnetic waves such as light. The quantities $E^0$ and $H^0$ are the maximum strengths of the electric and magnetic fields, respectively.

In an electromagnetic wave, the electric and magnetic fields are perpendicular to each other and to the direction of wave propagation. The equations show that both fields oscillate in sync (they have the same phase $\phi$) but are described by separate equations since they are perpendicular components.

The term $kx - \omega t$ indicates that the wave is moving in the positive $x$-direction. If the wave were moving in the negative $x$-direction, the sign in front of $\omega t$ would be positive.

The factor $\sin(kx - \omega t + \phi)$ varies between \(-1\) and \(1\), causing the electric and magnetic field strengths to oscillate between $-E^0$ to $E^0$ and $-H^0$ to $H^0$, respectively. The wave thus carries energy and, if it is light, can be observed as it interacts with matter.
</details>


## Diffraction
















<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
