---
toc: true
url: par_wave_dual
covercopy: <a hreh="https://www.livescience.com/24509-light-wave-particle-duality-experiment.html">© Clara Moskowitz</a>
priority: 10000
date: 2024-01-23 09:57:26
title: "PARTICLE-WAVE DUALITY"
ytitle: "PARTICLE-WAVE DUALITY"
description: "PARTICLE-WAVE DUALITY"
excerpt: "PARTICLE-WAVE DUALITY"
tags: []
category: []
cover: "https://cdn.mos.cms.futurecdn.net/gyuT23ZwvfNoevmxW6XMte-650-80.jpg.webp"
thumbnail: "https://cdn.mos.cms.futurecdn.net/gyuT23ZwvfNoevmxW6XMte-650-80.jpg.webp"
---

## Failure of Classical Mechanics 

### Black Body Radiation

- **Experiment**: measure the radiation intensity as a function of frequency of the radiation emitted from a black body (a physical body that absorbs all incident electromagnetic radiation) at thermal equilibrium
- **Model**: Emitted radiation is classically due to oscillating electric dipoles within the material, acting like broadcast antennas.
- **Classical expectation**: higher temperature should result in a large increase in the radiation emitted at high frequencies (fast oscillation at high T)

!!! note Gustav Kirchhoff
    The blackbody is an idealized physical body that absorbs all incident electromagnetic radiation (such as light), regardless of frequency or angle of incidence.
    
    A black body can also emit black-body radiation, which is solely determined by its temperature.

    [![Gustav Robert Kirchhoff](https://upload.wikimedia.org/wikipedia/commons/f/fe/Gustav_Robert_Kirchhoff.jpg)](https://en.wikipedia.org/wiki/Gustav_Kirchhoff)

###  Black-body Radiation Spectrum: Intensity vs. Wavelength

|![Relationship between radiational intensity vs. wavelength](https://i.stack.imgur.com/f4xki.gif)|
|:-:|

Notic: the "Cold" object also emit "light" as long as its above the absolute zero (-273.15 °C). And it would appear "blakc" because the peak wavelength is in infrared range, which human eye cannot recognize.

According to this theory, we could astimate the temperature of stars based on its color.

|![](https://stsci-opo.org/STScI-01G7RQ0CRCSNKZNX18HNNAQRV0.jpg)|![](https://www.astronomy.com/wp-content/uploads/sites/2/2023/02/ScreenShot20210420at3.19.16PM.jpg)|
|:-:|:-:|
|[webbtelescope](https://webbtelescope.org/contents/media/images/01F8GF8WYBCQVKTGPX3MA58182?Type=Infographics&Tag=Spectroscopy)|[astronomy.com](https://www.astronomy.com/astronomy-for-beginners/color-coding-stars/)|

### Wien’s Displacement Law

$ \lambda _{max} = \frac{W}{T} $
- $  \lambda _{max} $: Peak wavelength
- W: Wien's constant = 2.9 e^-3^ m Kelvin
- T: Surfave temperature

Exp:

When &lambda;~max~ = 500nm:
$T = \frac{W}{\lambda_ {max}} = \frac{2.9 e^ {-3} mK}{500e^ {-9}m } = 5800K$

### Rayleigh-Jeans law (Classical description of light)

- Predict the spectral irradiance (or spectral density) of a black body radiation as a function of wavelength or frequency for a fixed temperature.
- Spectrum Density (&nu;, T) = $\frac{8\pi\nu^2}{ c^3 }k_BT$
    - c: speed of light
    - k~B~ = Boltzmann constant = 1.380649 × 10^-23^ J/K
    - T: temperature
    - &nu;: frequency

### Spectral density

- Density = radiance
    The power of radiation (W) passing a unit area (m^2^) within a unit solid angle (sr), within a unit time
(s). It has the unit of W/(m^2^ × sr × s)
- Spectral density = Spectral radiance
    The radiance per unit wavelength (um) or per unit frequency (Hz), depending on if the power is measured over wavelength or frequency. Therefore, spectral density has the unit of W/(m^2^ × sr × s × um) or W/(m^2^ × sr × s × Hz).

### Unexpected Black Body Radiation: UV Catastrophe

!!! note Conflict between observation and expectation
    - **Observation** :
        Spectral density does not monotonically increase as the frequency increases.
    - **Classical expectation**:
        According to the Rayleigh-Jean law, spectral density should increase as the frequency increases

Reason: ==The classic oscillating field from electromagnetic radiation drives the motion of a spring==
    - faster oscillation → higher frequency → higher energy

For fix this conflict, a propportional model was given: E = nhν (==Max Planck==)
- n = 1, 2, 3...
- Planck’s constant (h) = 6.626×10^−34^ Js

$$
\rho (\nu, T) = \frac{8\pi\nu^2 h \nu}{ c^3 } \frac{1}{e^{\frac{hv}{k_ BT}} - 1 }
$$

Explained:
    - energy of photon (with frequent &nu;): h&nu;
    - weight if photon population (&nu;): g(&nu;) = $\frac{8\pi \nu ^2 }{c^ 3}$
    - averagy number of photon (&nu;): n(&num;, T) = $\frac{1}{exp(\frac{h\nu}{k_BT})-1}$
    - &rho; (&nu;T)d&nu; = h&nu; × g(&nu;) × n(&num;, T) 
        = $h\nu × \frac{8\pi \nu ^2 }{c^ 3} × \frac{1}{exp(\frac{h\nu}{k_BT})-1}$
        = $\frac{8\pi h \nu^3}{ c^3 } \frac{1}{e^{\frac{hv}{k_ BT}} - 1 }$

In Planck Low, it show either high temperature or low frequency would case the "Ultralviolet catastrophe":

![planck Law](https://imgur.com/rWBTB6C.png)
- From the left to the right:
    - $\frac{8\pi \nu ^2 }{c^ 3}$
    - $\frac{1}{exp(\frac{h\nu}{k_BT})-1}$
    - $\frac{8\pi h \nu^3}{ c^3 } \frac{1}{e^{\frac{hv}{k_ BT}} - 1 }$

<details><summary>Plot Codes</summary>

```python
import numpy as np
import matplotlib.pyplot as plt

def Rayleigh_Jeans(v, T):
    kB = 1.380649 * 10**(0-23)
    c = 3 * 10**8
    return (v**2) * 8 * np.pi * kB * T / (c**3)

def Planck(v, T):
    h = 6.626*10**(0-34)
    kB = 1.380649 * 10**(0-23)
    return 1 /( np.e ** (h*v / (kB * T) ) - 1 )

def Merged(v, T):
    h = 6.626e-34
    kB = 1.380649e-23
    c = 3 * 10 **8
    return 8 * np.pi * h * v**3 / c**3 / np.e**(h *v /(kB * T))

# Constants
h = 6.62607015e-34  # Planck's constant (m^2 kg / s)
c = 299792458       # Speed of light in vacuum (m / s)
k_B = 1.380649e-23  # Boltzmann constant (J / K)

# Planck's law function
def planck_law(frequency, temperature):
    """
    Calculate the spectral radiance of a black body at thermal equilibrium.  
    Parameters:
    frequency (float): frequency of the electromagnetic radiation (Hz)
    temperature (float): absolute temperature of the body (K)
    Returns:
    float: spectral radiance (W / (m^2 * sr * Hz))
    """
    exponent = (h * frequency) / (k_B * temperature)
    spectral_radiance = (8 * np.pi * h * frequency**3) / (c**3) * (1 / (np.exp(exponent) - 1))
    return spectral_radiance

# Example usage: Calculate the spectral radiance for a frequency of 1e14 Hz at 5000 K
frequency_example = 1e14  # Hz
temperature_example = 5000  # K
radiance_example = planck_law(frequency_example, temperature_example)

# Plot the graphs above
X = [i /10 for i in  range(1,100)]
fig, axs = plt.subplots(1, 3)
axs[0].plot(X, [Planck(i * 1e14, 3000) for i in X])
axs[1].plot(X, [Rayleigh_Jeans(i * 1e14, 3000) for i in X])
axs[2].plot(X, [h *(i *1e14)* Rayleigh_Jeans(i*1e14, 3000) * Planck(i*1e14, 3000)  for i in X])
plt.tight_layout()
plt.show()

# plot the mergerd function
plt.plot(X, [Merged(i*1e14/10, 3000)  for i in X])
plt.show()
```
</details>

So, both Rayleigh-Jean law and Planck law agree with the observation very well in very low frequency.
But only Plank law could fit the decreasing of the intensity in high frequency situation.

## Light is Particle

### Einstein’s Contribution: Photoelectric Effect

$$
E = nhν
$$

By using the light to eject electrons from a copper, they found the ==kinetic energy of ejected electrons depends on light frequency==

$$
E_{light} = \beta\nu_{light}
$$

### The Photoelectric Effect

Conservation of energy

|![](https://imgur.com/DSOpstj.png)|
|:-:|
|..?unknow|

$$
E_{elec} + \Phi= \beta \nu
$$
- E~elec~: (Measured) Electron kinetic energy
- &\Phi; Work to remove electron from target (independently determined)
- &nu;: Determine the value of &\beta;

!!! note Einstein concluded that light must be behaving like a particle in this experiment: PHOTON
    E = *h&nu;*

### Duality in partical with mass

- **Electron diffraction**: This is a typical diffraction pattern of a beam of electrons diffracted by a crystalline solid

from Planck's equation to Einstein's equestion:
- *E = h&nu* → *E = mc^2^*

$v = h\nu$
$mv = P = m\lambda\nu$
$v = \frac{P}{m\lambda}$
$E = h\nu = \frac(hP){m\lambda} → E = \frac{p^2 }{m}$

De Broglie Equation:
$\lambda = \frac{h}{p} = \frac{h}{m\nu}$

### About Weight Terms in Spectral Density

$g(\nu) = \frac{N(E)}{V} = \frac{Number of States (E)}{Volumne}$
 

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
