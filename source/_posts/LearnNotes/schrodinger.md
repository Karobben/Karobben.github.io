---
toc: true
url: schrodinger
covercopy: © Karobben
priority: 10000
date: 2024-01-25 15:15:01
title: "Schrodinger Function"
ytitle: "Schrodinger Function"
description: "To develop a quantitative understanding of macromolecules in biological systems."
excerpt: "Schrodinger Function"
tags: []
category: []
cover: ""
thumbnail: ""
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


$$
-\frac{\hbar}{2m} \frac{d^2 \Psi (x)}{dx^ 2} + V(x)\Psi(x) = E\Psi(x)
$$

- V(x): Potential energy provides the constraints
- E: Solve for Energy(also called eigenvalues)
- $\Psi(x)$: Solve for wavefunctions (also called eigenvectors or eigenfunctions)

We will end up with a series of wavefunctions with associated energies:
$$\Psi(x) \leftrightarrow E_ n $$

The Schrödinger Equation is a fundamental equation in quantum mechanics that describes how the quantum state of a physical system changes over time. It was formulated by Erwin Schrödinger in 1925. There are two forms of the Schrödinger Equation: the time-dependent and the time-independent forms.

1. **Time-Dependent Schrödinger Equation:**
   \[
   i\hbar\frac{\partial}{\partial t}\Psi(\mathbf{r}, t) = \hat{H}\Psi(\mathbf{r}, t)
   \]
   Here, \( \Psi(\mathbf{r}, t) \) is the wave function of the system, \( i \) is the imaginary unit, \( \hbar \) is the reduced Planck constant, \( t \) represents time, \( \mathbf{r} \) is the position vector, and \( \hat{H} \) is the Hamiltonian operator which represents the total energy of the system.

2. **Time-Independent Schrödinger Equation:**
   \[
   \hat{H}\psi(\mathbf{r}) = E\psi(\mathbf{r})
   \]
   In this form, \( \psi(\mathbf{r}) \) is the time-independent wave function, \( E \) represents the energy of the system, and other symbols have the same meaning as in the time-dependent equation.

The Schrödinger Equation is a cornerstone of quantum mechanics, providing a mathematical framework for understanding and predicting the behavior of quantum systems. It's important to note that these equations are usually accompanied by specific boundary conditions or potentials, depending on the physical situation being modeled.






















<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
