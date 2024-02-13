---
toc: true
url: pchm_vibr
covercopy: © Karobben
priority: 10000
date: 2024-02-13 11:01:57
title:
ytitle:
description:
excerpt:
tags:
category:
cover:
thumbnail:
---

## 

Tell the motion of the molecular without the fluorescent: Viboration 

- **One atom**: 3 independent degrees of freedom. (x, y, z)
- **2 unconnected atoms**: have 6 degrees if freedom. (x, y, z are independent)
- **2 bounded atom** (diatomic molecule): have 6 degrees if freedom
    - 3 translational for the entire molecule
    - 2 rotational about axes perpendicular to the bond
    - 1 vibrational 

As a result: Total number of degrees of freedom: 3N (N is the number of atoms in a molecule)
If we considerate the whole molecular as a whole: 3 rotational degrees of motion

- General case: for a molecule with N atoms, there are **3N-6** (nonlinear molecule) or **3N-5** (linear molecule) vibrational degrees of freedom


!!! note Normal mode: A pattern of motion in which all the parts move with the same sinusoidal time-dependence and with fixed phase
    - Each mode has a resonance frequency.
    - Each mode can be stimulated independently of all the other modes.
    - General oscillatory motion is described by a sum of motions of normal modes 

Molecules with many atoms have many vibrational degrees of freedom
- Symmetric stretch
- Asymmetric stretch
- Bend

### Molecular Vibrations

Covalent bonds vibrate only at certain allowable frequencies (like a spring)

![](https://imgur.com/qd2RuG7.png)

## Quantum Mechanical Harmonic Oscillator

# Schrödinger equation

The Schrödinger equation is represented as:

$$
\hat{H}\psi = (E_{kin} + E_{pot})\psi = E\psi
$$

Where $\hat{H}$ is the Hamiltonian operator, $\psi$ is the wavefunction, $E_{kin}$ is the kinetic energy, $E_{pot}$ is the potential energy, and $E$ is the total energy.

## Set of wave functions

The energy levels for a quantum harmonic oscillator are given by:

$$
E_n = \left(n + \frac{1}{2}\right)\hbar\omega_o \quad n = 0,1,2,3...
$$

$n$ represents the quantum number, $\hbar$ is the reduced Planck's constant, and $\omega_o$ is the angular frequency.

## Energy Diagram

The energy diagram on the right illustrates the difference between the Harmonic and Morse potentials. The Harmonic potential is an approximation that is valid only for small displacements from the equilibrium position $r_e$.

### Harmonic Oscillator

The potential energy of a harmonic oscillator is given by:

$$
E_{pot}(x) = \frac{1}{2}kx^2
$$

$k$ is the force constant and $x$ is the displacement from equilibrium.

### Morse Potential

The Morse potential is a more accurate model that accounts for the dissociation of a diatomic molecule. The dissociation energy $D_e$ is the energy required to break the bond.

### Energy Levels

The quantized energy levels are shown for both potentials. For the Harmonic oscillator, the energy levels are evenly spaced, while for the Morse potential, the spacing decreases with increasing energy.

### Vibrational Frequencies

The allowable frequencies for a quantum harmonic oscillator are given by:

$$
\omega_o = \sqrt{\frac{k}{m_r}} = 2\pi\nu_o
$$

K is a constant. 
$m_r$ is the reduced mass of the diatomic molecule, and $\nu_o$ is the fundamental frequency of vibration.

![](https://imgur.com/QQ2Qpj7.png)

the system is considerated by the change of the nuclear. To considerate the nuclear situaiton, we write the nuclear energy. The energy perform a U shape (Harmonic oscillator). Morse shape could describe the dissociation well when you got to much of energy.  

Here we use the viboration frequency to describe the energy.

Increase the S, you stretch the molecule
Decrease the S, you press the molecule, increasing the potential energy.

In the class, we only considerate teh Harmonic oscillation (in low energy state)

## Transition energies for vibrational spectroscopy


!!! note For electronic transitions in the visible spectrum: Energy from S0 → S1
    - Wavelength: $\lambda = 500 \text{ nm} = 0.5 \text{ }\mu\text{m}$
    - Wavenumber: $\tilde{\nu} = \frac{1}{\lambda} = 20,000 \text{ cm}^{-1}$
    - Energy change: $\Delta E \approx 60 \text{ kcal/mol}$ (about 100-times thermal energy, $RT$, at 298K)

!!! For vibrational transitions in the infrared spectrum: Energy from V0 → V1
    - Wavelength: $\lambda = 5,000 \text{ nm} = 5 \text{ }\mu\text{m}$
    - Wavenumber: $\tilde{\nu} = \frac{1}{\lambda} = 2,000 \text{ cm}^{-1}$
    - Energy change: $\Delta E \approx 6 \text{ kcal/mol}$ (about 10-times thermal energy, $RT$, at 298K)

The diagram illustrates the various energy levels:
- $S_0$: Ground electronic state with vibrational levels $V_0$, $V_1$, etc.
- $S_1$, $S_2$, $S_3$: Excited electronic states with their own vibrational levels.


Different energy (situation?) wave? to use different types of spectrum?
- absorb spectrum
- visible spectrum
- IR spectrum
- NMR spectrum


### IR-Active and IR-Inactive vibrational modes

Not all vibrational could cause IR spectrum: only the dipole change, the IR spectrum could be changed. (stretch the molecular asymmetric to change the dipole)

Exp, to compare the C-H, C-D, and C-C, the m~r~ is not the same, m~t~ should be considerated mainly

C-C, C=C, and C≡C: C≡C has more potential energy and the frequency would be higher because this time, the m~r~ are all the same.

## Water has a broad IR absorbance overlapping with the protein bands 

|![water absorbance spectrum](https://water.lsbu.ac.uk/water/images/d2o_vibrations.gif)|
|:-:|
|[lsbu.ac.uk](https://water.lsbu.ac.uk/water/water_vibrational_spectrum.html)|


Traditional wave scan take very long and it is not practical to most of samples.

1. Shine all frequencies of IR light through the sample (broad band source)
2. Do not disperse the light either prior to or after passing through the sample
3. Decode the absorbance vs frequency spectrum from the signal at the detector

Huge advantage is that you don’t need to use slits to cut down light intensity either before or after passing through the sample

Pass all the light to the sample and calculating the spectrum later with mathmetic knowledge (Fourier Transform).



**Detector signal for monochromatic light (single color, only one frequency \(\nu\)):**

$$
I(p) = I(\tilde{\nu})\cos(2\pi\tilde{\nu}p)
$$

**Detector signal with light of all frequencies will be the sum:**

$$
I(p) = \int_0^\infty I(\tilde{\nu})\cos(2\pi\tilde{\nu}p)d\tilde{\nu}
$$

**\(I(p)\) is called an Interferogram**

$$
I(tulde{\vu}) = \int_0^\infty I(p)\cos(2\pi\tilde{\nu}p)dp
$$




<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
