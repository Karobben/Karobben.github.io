---
toc: true
url: fluorescence
covercopy: © Karobben
priority: 10000
date: 2024-02-06 01:22:42
title: "FLUORESCENCE SPECTROSCOPY"
ytitle: "FLUORESCENCE SPECTROSCOPY"
description: "FLUORESCENCE SPECTROSCOPY"
excerpt: "FLUORESCENCE SPECTROSCOPY"
tags: []
category: []
cover: ""
thumbnail: ""
---

## FLUORESCENCE SPECTROSCOPY

!!! note What happens after the molecule is excited?
    ![](https://imgur.com/nD2T2sw.png)
    Fluorescence properties depend on what happens to the molecule during the ~10-8 sec during which it is excited

### What are the processes of non-radiative decay?

||Unit: sec^-1^|
|:-:|:-|
|![](https://imgur.com/uYOhyLM.png)|Black = Non-radiative<br> Red = Radiative (photon)<br> ABS = absorption (10^15^)<br>**IC** = internal conversion <br> (k~IC~ ≈ 10^11~12^)<br> **Q** = quenching<br>**IX**=intersystem crossing<br>S~1~→T~0~: 10^8^; T~1~→S~0~: 10^2^<br> **Chem**=photochemistry<br>k~f~ ≈ 10^8^; k~p~ ≈ 10^2^<br> **F** = fluorescence<br> **P** = phosphorescence<br> Trans = energy transfer<br>k~collision~ ≈ 10^10^ M^-1^sec^-1^|


- Internal Conversion: energy loss due to collisions with solvent molecules
    - collision rate = k~coll~ [solvent]
        - k~coll~ ~10^10^M^-1^sec^-1^
        - [slovent]: 55M for water
        - The rate of collision of a single molecule is ≈ 10^11^-10^12^sec^-1^
    - ==S1-S2==: Heat. Fast IC (10^-11^sec): heat loss to solvent, **all excited molecules are in the lowest vibrational state** of S~1~
    - ==S0-S1==: Heat. Slow IC (10^-8^sec): due to larger energy gap, therefore fluorescence is possible.

!!! note What is the concentration of pure water?
    <li> 1 L water = 1000 g
    <li> water molecule = 18 g/mol
    <li> So 1 L water = 1000/18 =55 mol
    <li> [M] = 55 mol/1 L = 55 M


#### Solvent reorganization and the Stokes Shift

Measure fluorescence at fixed λ~ex~ as a function of ***λ~em~***
**Stokes shift**: Emission spectrum is always red-shifted (lower energy) compared to the absorption spectrum

|Vibrational relaxation|Solvent reorganization|
|:-:|:-:|
|![](https://chem.libretexts.org/@api/deki/files/79075/%253DScreen_shot_2011-03-14_at_11.08.58_AM.png?revision=1&size=bestfit&width=224&height=274)|![](https://upload.wikimedia.org/wikipedia/commons/f/fc/Stokes_shift_diagram.svg)|
|[© libretexts.org](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Spectroscopy/Electronic_Spectroscopy/Jablonski_diagram)|[© wikipedia](https://en.wikipedia.org/wiki/Stokes_shift)|
||Franck-Condon Overlap Factors<br>Prob (0’→2’) ≅ Prob (2’←0’) etc|

![](https://imgur.com/3c7E6y8.png)

Absorption: ~ 10^-15^ sec
Solvent reorganization (relaxation): ~ 10^-10^ sec
Fluorescence: ~ 10^-8^ sec
Step 1: Permanent Dipoles of solvent re-orient to adjust to the altered dipole of the excited fluorophore.
Step 2: The dipole-dipole interaction in turn stabilizes S1 and destabilizes S0. 
**Requires**:
    1. solvent polarity (dielectric constant, ε)
    2. mobility of solvent (reorientation of solvent dipoles)

### How long can a molecule stay in its excited state?

Excite some molecules to $ S_1 $ with a brief pulse of light at $ t = 0 $, $ N_0^* $ excited state molecules
Decay of the excited state population is exponential: $ \frac{dN^*(t)}{dt} = -(k_f + k_{NR})N^*(t) $
So: $ N^ *(t) = N_0^ * e ^ {-(k_f+k_{NR})t} = N_0^ * e^ {-t/\tau} \quad$ where $N^* (t)$ is the number of excited molecules at time ***t***.

Define: lifetime $ \tau $
    $ \tau = \frac{1}{k_f + k_{NR}} $
Hence, the equation for the decay of the excited state population:
    $ N^*(t) = N_0^* e^ {-t/\tau} $


!!! note The meaning of the fluorescence lifetime
    ***τ*** has units of time (seconds) <br>
    $[N_ {t=\tau}^ *] = \frac{N_ 0^ *}{e} \approx 0/37N_ 0^ *$<br>
    After one lifetime following excitation, the probability of a molecule still being in the excited state is about 37%

#### How bright can a molecule be?

Rate up: $S_0 \rightarrow S_1 = I_0$, unit: [# of photons absorbed/sec]
Rate down: $S_1 \rightarrow S_0 = -(k_f + k_{NR}) \cdot N^*(t)$
Unit: [1/sec][# of photons]

$N^*(t)$ = concentration of excited state molecules at any time, $t$
$k_{NR}$ = sum of all non-radiative rate constants
$N^*(t) = [S_1(t)]$, [# of molecules]

Steady state: rate up = rate down
$0 = \frac{dN^*(t)}{dt} = I_0 - (k_f + k_{NR}) N^*(t)$

In the steady state $N^*(t)$ is constant $= N^*_{SS}$
$I_0 = (k_f + k_{NR}) N^*_{SS}$

#### Fluorescence quantum yield (QY)

$Q_f$ (QY): fraction of excited-state molecules that relax to the ground state by emitting a photon.

photons/sec emitted in steady state

$Q_f = \frac{k_f N^*_{SS}}{I_0} = \frac{k_f N^*_{SS}}{(k_f + k_{NR})N^*_{SS}}$

Since $I_0 = (k_f + k_{NR})N^*_{SS}$

photons/sec absorbed in steady state

$Q_f = \frac{k_f}{(k_f + k_{NR})} = k_f \times \tau$

Recall $\tau = \frac{1}{(k_f + k_{NR})}$


### What are the fluorophores in biological systems?

- Intrinsic Fluorescence of Proteins

Absorption spectra Fluorescence spectra of amino acids in water “About 300 papers per year abstracted in Biological Abstracts report work that exploits or studies tryptophan (Trp) fluorescence in proteins…”
Vivian et al. Biophysical Journal 2001

|               | Lifetime (nsec) | Absorption                   |               | Fluorescence    |           |
|---------------|-----------------|------------------------------|---------------|-----------------|-----------|
|               |                 | Wavelength (nm)              | Absorptivity (ε, M^-1cm^-1) | Wavelength (λmax, nm) | Quantum Yield (25°C) |
| Tryptophan    | 2.6             | 280                          | 5,600         | 348             | 0.20      |
| Tyrosine      | 3.6             | 274                          | 1,400         | 303             | 0.14      |
| Phenylalanine | 6.4             | 257                          | 200           | 282             | 0.04      |


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
