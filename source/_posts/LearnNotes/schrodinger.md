---
toc: true
url: schrodinger
covercopy: <a href="https://facts.net/science/physics/10-astounding-facts-about-schrodingers-cat">© Rosalie Mcneely</a>
priority: 10000
date: 2024-01-25 15:15:01
title: "Schrodinger Function"
ytitle: "Schrodinger Function"
description: "To develop a quantitative understanding of macromolecules in biological systems."
excerpt: "Schrodinger Function"
tags: []
category: []
cover: "https://facts.net/wp-content/uploads/2023/09/10-astounding-facts-about-schrodingers-cat-1694218667.jpg"
thumbnail: "https://facts.net/wp-content/uploads/2023/09/10-astounding-facts-about-schrodingers-cat-1694218667.jpg"
---

## Energy Momentum Relation

$E^2 = (m_ 0 C ^2) ^2 + (pc)^ 2$

For Energy with rest mess: $E = m_0c^2$
For Energy with no rest mess: $E = pc$

Introducing Bacground:
- Light is a ruler; molecules are objects to be measured.
- Visible light is a coarse ruler (300 nm resolution)
- Molecules, on the other hand, are fine objects (0.1 nm)
- How can we measure such a fine object with a coarse ruler?
    - Use a finer ruler (electron microscopy)
    - Use indirect evidence to infer the information (today’s focus)

How to infer? What indirect evidence?
- Use a language to describe the matter (molecule).
- Find information that is related to the size of a molecule.
- Hopefully that information can be obtained by measurement (using light).
- Infer the information about the molecule to be studied.
- Here is one way to do this:
    - Use the Schrödinger equation to describe the system (molecule, atoms, electrons).
    - Find out that energy of electrons is related to the size of the molecule.
    - Measure the energy of the system using light.
    - Infer the size of the molecule by interpreting the energy information.


## Use the Schrödinger Equation to Describe the System

$$
-\frac{\hbar}{2m} \frac{d^2 \Psi (x)}{dx^ 2} + V(x)\Psi(x) = E\Psi(x)
$$

- V(x): Potential energy provides the constraints
- E: Solve for Energy(also called eigenvalues)
- $\Psi(x)$: Solve for wavefunctions (also called eigenvectors or eigenfunctions)

We will end up with a series of wavefunctions with associated energies:
$$\Psi(x) \leftrightarrow E_ n $$

The Schrödinger Equation is a fundamental equation in quantum mechanics that describes how the quantum state of a physical system changes over time. It was formulated by Erwin Schrödinger in 1925. There are two forms of the Schrödinger Equation: the time-dependent and the time-independent forms.

### The Meaning of &Phi;(x)

$$
 P(x_0, t_0)dx = \Psi^ * (x_0, t_0)\Psi(x_0, t_0)dx = |\Psi (x_0, t_0)|^2 dx 
$$

***P(x~0~, t~0~)***: *Probability** of finding the particle (e.g. electron) within an interval
of *dx* of position *x~0~* at time *t~0~*

### Properties of &Phi;(x);

$$
 \int_{-\infty}^{\infty} \Psi^* (x, t) \Psi (x, t)dx = 1
$$

Average value of f(x) over all space 

$$
\left \langle  f(x) \right \rangle = \frac{ \int_{-\infty}^{\infty} \Psi^* (x) \Psi (x)f(x)dx }{\int_{-\infty}^{\infty} \Psi^* (x) \Psi (x)dx}
$$


## Find Out That Energy of Electrons Is Related to the Size of the Molecule.

### 1-d particle in a box


Here **Particle = electrons in a molecule**
**Layman language**: Potential energy outside the box is infinite.
**Mathematical language**: Boundary condition

![](https://bouman.chem.georgetown.edu/S02/lect13/piab.gif)

***V(x) = 0 for L > x > 0***
***V(x) = ∞ for x ≥ L, x ≤ 0***

$$
\frac{d^ 2 \Psi(x)}{dx^ 2} = \frac{2m} {\hbar^ 2} [V(x)-E]\Psi(x)
$$

1. Since ***V(x)*** is infinite outside the box, ***Ψ(x)*** must be zero outside the box
    (otherwise $\frac{d^2 Ψ(x)}{dx^2}$ would be infinite: not allowed)

2. Since ***Ψ(x)*** must be continous, ***Ψ(x)*** inside the box must connect smoothly to ***Ψ(x)*** outside the box
    Hence, $Ψ(0)= Ψ(L) = 0$

$$ \Psi_ n (x) = \sqrt{\frac{2}{L}}  sin(\frac{n\pi x}{L}) $$
- $ E_ n= \frac{h^2 n ^2}{8ma ^ 2} $
- $ where n = 1, 2, 3, 4... $
- Energy of the electron (***E***) is related to the size of the molecule (***L***).


With this theory, we could measure the energy of the system using light
- Pi-electrons behave as a “particle in a box: Molecules has different absorb peak when they as different number of conjugation bounds.

!!! Note The electrons and its orbitals
    4 pi electrons => 2 orbitals
    8 pi electrons => 4 orbitals


## Estimate bond length from the transition energy

$$
\Delta E = \frac{(n_ 3 ^ 2 - n_ 2^ 2) h^ 2 }{8mL^ 2}
$$

For this compound, There are **4 pi electrons**. Two each in the n=1 and n=2 orbitals. (This is due to electron spin, which we will see later).
The absorption is due to promoting an electron from the n=2 to the n=3 orbital.

- Infinite potential: infinite number of solutions
- Finite potential:
    1. A finite number of solutions (5 in this example)
    2. Wavefunctions are not zero at the boundary of the box
    3. The wavefunctions have finite amplitude outside the box.
    Finite chance the particle can be outside the box even though ***E<V~0~***

!!! note TUNNELING effect in Quantum Mechanics
    ![Quantum Tunneling](https://www.ntmdt-si.com/data/media/images/spm_basics/scanning_tunnel_microscopy_stm/stm_physical_backgrounds/tunneling_effect/img04.gif) [© ntmdt-si](https://www.ntmdt-si.com/resources/spm-theory/theoretical-background-of-spm/1-scanning-tunnel-microscopy-%28stm%29/11-stm-physical-backgrounds/111-tunneling-effect)
    
    a particle can go "through" an energy barrier instead of needing to have sufficient energy to go over the barrier
    When the wave go through the energy barrier, the exponential decay occurred inside of the energy barrier.


## Predict the Energy and Optical Property

If we know the structure of the molecule, can we predict the energy and optical property of the molecule?
Take the **hydrogen atom** as example.

- $V( r ) = \frac{e^ 2}{4\pi \epsilon_ 0 r}$
- ***e*** = electron charge
- ***&epsilon;~0~*** = permittivity of free space

### Predicted the Energy

Here we only need 3 quantum number: ***n***, ***l***, and ***m~l~***
- the principal quantum number: ***n***  = 1, 2, 3, 4...
- the angular momentum quantum number: ***l*** = 0, 1, 2, ... (n -1)
- the magnetic quantum number: ***m~l~*** = 0, ±1, ±2, … ± ***l***

As you can see, the energy only depends on ***n***:
$E_ n = - \frac{m_ e e^ 4}{8 \epsilon_ 0^ 2 h^2 n^ 2} = - \frac{2.179 × 10 ^ {-18}}{n^ 2}Joule = -\frac{13.6}{n^ 2}eV\ \ \ n = 1, 2, 3... $

|![](https://imgur.com/Kwx6VEm.png)|
|:-:|
|© Atkins, The Elements of Physical Chemistry|


## Cheat Sheet

- Energy: kcal/mol, kJ/mol
- Wavelength: nm
- Frequency: Hz
- $E = h\nu = \frac{hc}{\lambda}$
- Planck constant (***h***) = 6.62607015 × 10^-34^ J∙s
- Speed of light (***c***) = 299 792 458 m/s ~ 3 × 10^8^ m/s

!!! Note Calculate the energy of one photon of green light (532 nm)
    $ E = h\nu = \frac{hc}{\lambda} = \frac{hc}{532 × 10^ {-9}m} = 3.823×10^ {-19}J$
    

!!! note Convert J to Hz
    $ \nu = \frac{E}{h} = \frac{3.823×10^ {-19}J}{h} = 5.8 × 10^ {14} Hz$

!!! note Convert kJ/mol and kcal/mol
    $E_ {total} = N_ A × E = 6.02 × 10^ {23} \frac{1}{mol} × 3.823 × 10^ {-19} J$
    
    $= 230226 J/mol ~ 230 kJ/mol $
    
    $= 55 kcal/mol$

<br>
<br>
<br>
<br>
<br>
<br>
<br>

## Extra Reading

1. **Time-Dependent Schrödinger Equation:**
   $$
   i\hbar\frac{\partial}{\partial t}\Psi(\mathbf{r}, t) = \hat{H}\Psi(\mathbf{r}, t)
   $$
   Here, $\Psi(\mathbf{r}, t)$ is the wave function of the system, $i$ is the imaginary unit, $\hbar$ is the reduced Planck constant, $t$ represents time, $\mathbf{r}$ is the position vector, and $\hat{H}$ is the Hamiltonian operator which represents the total energy of the system.

2. **Time-Independent Schrödinger Equation:**
   $$
   \hat{H}\psi(\mathbf{r}) = E\psi(\mathbf{r})
   $$
   In this form, $\psi(\mathbf{r})$ is the time-independent wave function, $E$ represents the energy of the system, and other symbols have the same meaning as in the time-dependent equation.

The Schrödinger Equation is a cornerstone of quantum mechanics, providing a mathematical framework for understanding and predicting the behavior of quantum systems. It's important to note that these equations are usually accompanied by specific boundary conditions or potentials, depending on the physical situation being modeled.






















<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
