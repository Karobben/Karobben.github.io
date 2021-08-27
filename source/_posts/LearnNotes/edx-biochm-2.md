---
toc: true
url: edx_biochm_2
covercopy: © Slawomir Walkowski
priority: 10000
date: 2021-03-23 13:49:04
title: "Principles of Biochemistry 2 |Entropy| Class Notes |HarvardX"
ytitle: "基礎生物化學筆記 2 | 自由能， 熵 | 哈佛 edx網課"
description: "Free energy and Entropy; Delta G;Class notes for biochemistry"
excerpt: '''Free energy and Entropy; $\Delta G = \Delta H - T\Delta$ ; Class notes for biochemistry'''
tags: [Classes, Biology, Biochemistry]
category: [Notes, Class, Biochemistry]
cover: "https://www.researchgate.net/profile/Janusz-Szymas/publication/51047721/figure/fig4/AS:195339794554884@1423584044453/Contrast-and-entropy-formulas-N-is-the-size-of-GLCM-Pij-are-probabilities-calculated.png"
thumbnail: "https://courses.edx.org/asset-v1:harvardx+MCB63X+1T2021+type@thumbnail+block@course_image-375x200.jpg"
---

## What is life?

Carbon is the base of life. But organisms are not only a piece of carbon.
Living life constantly carries a series of energy exchange processes.

```graphviz
digraph F {
    rankdir = DU;

    subgraph cluster_1 {
        rank = UD
        minerals [label = "minerals", shape = box, fillcolor = "#FF0000" ];
        O2 [label = "O2", shape = diamond, color = green, size = 2];
        CO2 [label = "CO2", shape = diamond, color = green, size = 2];
        organics   [label = "organics"      , shape = box, color = coral];

    }

    subgraph cluster_0 {
        Food [label = "Food", shape = box, color = deepskyblue1];
        Sun [label = "Sun", shape = box, color = deepskyblue1];
    }
    subgraph cluster_2 {
      Metabolism [label = "Metabolism", shape = circle, color = pink, size = 3];
      Catabolism [label = "Use for variety bio-activities"]
      Anabolism [label = "Build body component"]
      Metabolism -> Anabolism [label = Anabolism];
      Metabolism -> Catabolism [label = Catabolism];
    }

    subgraph cluster_0 {
  		style=filled;
  		color=lightgrey;
  		node [style=filled,color=white];
  		label = "Potential Energy";
  	}


    subgraph cluster_1 {
  		node [style=filled];
  		label = "Surrounding Energy";
  		color=blue
  	}

    subgraph cluster_2{
      node [style=filled];
  		label = "Living Cell";
  		color= red
    }
    Food -> Metabolism [ label = "Catabolism" ];
    Sun ->  Metabolism;
    minerals -> Metabolism;
    organics -> Metabolism;
    O2 -> Metabolism;
    CO2 -> Metabolism;
}
```

## Types of Metabolism

```graphviz
digraph F {

  NSunlight [label = "Not Sunlight"];
  Organisms -> Sunlight -> Phototrophs;
  Organisms -> NSunlight -> Chemotrophs;
  Phototrophs -> Food;
  Phototrophs -> CO2;
  Chemotrophs -> Food -> Heterotrophs;
  Chemotrophs -> CO2 -> Autotrophs;

  subgraph cluster_0{
    node [style=filled];
    label = "Energy source";
    color= blue
    Sunlight;
    NSunlight;
    Phototrophs;
    Chemotrophs;
  }

  subgraph cluster_1{
    node [style=filled];
    label = "Carbon Source";
    color= pink;
    Food;
    CO2;
  }

  subgraph cluster_2{
    node [style=filled];
    label = "Metabolic type";
    color= red;
    Autotrophs;
    Heterotrophs;
  }

  {rank="same"; Heterotrophs; Autotrophs}
  Heterotrophs -> Autotrophs [label = CO2; color= red];
  Heterotrophs -> H2O ->  Autotrophs [ color= red];
  Autotrophs ->  O2 ->  Heterotrophs [ color= blue];
  Autotrophs -> organics ->  Heterotrophs [ color= blue];
}
```

## Entropy and reaction

### Gibb's free energy equation
$$
G = H - TS
$$
*G*: Free engergy
*H*: Enthalpy
*T*: Temperature
*S*: Entropy

Enthalpy (H): Total energy of the system (Energy in bonds)
Entropy (S): Quantitative expression for the randomness of the system; (the disorder of the system, the amount of energy that cannot do work)
Temperature (T): Temperature; Degrees Kelvin
$TS$: Increased temperature intensifies random molecular motion, leading to increased disorder.
Free Energy (G): The only portion of the energy that is able to do work.

In a cell that carries reactions, the amount of energy lost as heat, which contributes to random motion, increased entropy, and the reaction was irreversible.

### Spontaneous Reaction
In a spontaneous reaction, the free energy is decreased,
therefor:
$\Delta G < 0$
Because:
$\Delta G = \Delta H - T\Delta S$
As a result:
$\Delta H < T \Delta S$

So,
$\Delta H$ is negative: $(-)\Delta H$, the heat is release, it is a ==exothermic reaction==.
$\Delta H$ is positive: $(+)\Delta H$, the heat is absorbed, it is a ==endothermic reaction==.

The parameters of the reaction:
- Spontaneous or not;
- Equilibrium constant;
- Directionality;
- Velocity;

### Equilibrium

1. A reaction can occur spontaneously only if $\Delta G$ is negative. (exergonic)
2. A system is at *equilibrium* and no net change can take place if $\Delta G = 0$
3. A reaction can not occur spontaneously, only input of free energy to lead it happens when the $\Delta G <0$ . (endergonic)

Equilibrium constant
$S \rightleftharpoons  P$

The concentration of S and P constantly changes.

This ration is called: Equilibrium constant ($K_{eq}$)
$K_{eq} = \frac{[P]_ {eq} } { [S]_{eq}}$


Significant: most chemical reactions are reversible. By knowing the $K_{eq}$ and the initial the concentration, we can predict the direction of reaction.

### Calculating Exp. 1:

![Entropy calculating Exp1](https://z3.ax1x.com/2021/03/23/67Wh79.png)
Dihydroxyacetone phosphate (DHAP)
Glyceraldehyde 3-phosphate (G3P)

$$DHAP \rightleftharpoons  G3P$$

$K_{eq} = \frac{[G3P]}{[DHAP]}$
$\ \ \ \ \ \ \ = 0.475$

Stabdard free energy change ($\Delta G^{\circ}$):
$$\Delta G^{\circ} = -RTln(K_{eq})$$

*R*: gas constant
*T*: temperature expressed in degrees Kelvin.

So, a standard condition is a condition that the reaction proceeds at a constant temperature-- *T* equals 298 Kelvin or $25^{\circ}$C:

$$T = 298K = 25^{\circ}C$$
Reactants and products = $1M$
$R = 1.98 \times 10^{-3} kcal^1 mol^{-1} deg^{-1}$

$\Delta G^{\circ} = -RTln(K_{eq})$
$\ \ \ \ \ \ \ \ = - (1.98 \times 10^{-3}) \times 298 \times ln(0.0475)$
$\ \ \ \ \ \ \ \ = 1.80 kcal/mol$

So, the $\Delta G^{\circ}$ is positive.


==But== the thing that determines the property spontaneously is the free energy change. It gives a function
$$\Delta G = \Delta G^{\circ}+ RTln(K)$$

Here, K is the actual ratio of glyceraldehyde 3-phosphate and dihydroxyacetone phosphate concentrations in the cell. In this example, the concentration of the DHAP is $2 \times 10^{-4}M$ and the G3P's concentration is $3 \times 10^{-6}M$ (the initial of the concentration).
Under this condition, We now have:

$\Delta G = \Delta G^{\circ}+ RTln(K)$
$\ \ \ \ \ \ \ = 1.80 + RTln(\frac{[G3P]}{[DHAP]})$
$\ \ \ \ \ \ \ = 1.80 + (1.98 \times 10^{-3}) \times 298 \times ln(\frac{3 \times 10^{-6}}{2 \times 10^{-4}})$
$\ \ \ \ \ \ \ = - 0.7 kcal/mol$

As a result, the $\Delta G < 0$
==That's means, it is a spontaneous reaction!==



### Delta G
We already know that:
$\Delta G = \Delta G^{\circ}+ RTln(K)$

When there are no works is down, then, $\Delta G = 0$:
$0 = \Delta G^{\circ} + RTln(K_{eq})$
$\Delta G^{\circ} = - RTln(K_{eq})$


### Calculating Exp. 2:
In the following reaction:
$S \longrightarrow P $
$K_{eq}=4$
Initial concentration of *P* and *S*: $[P]= 10M;[S]=1M$
The forward reaction is ?:

- Standard Calculation:
$\Delta G = \Delta G^{\circ} + RTln(K)$
$\Delta G = - RTln(K_{eq}) + RTln(K)$
$\Delta G = RT(RTln(K) - ln(K_{eq}))$
$\Delta G = RT(ln(10) - ln(K_{4}))$
$\Delta G = 1.98 \times 10^{-3} \times 298 \times (ln(10) - ln(4))$
$\Delta G = 0.5406482kcal/mol$
- or can avoid the calculation:
$\Delta G = \Delta G^{\circ} + RTln(K)$
$\Delta G = - RTln(K_{eq}) + RTln(K)$
$\Delta G = RT(ln(K) - ln(K_{eq}))$
$\Delta G = RT(ln(10) - ln(K_{4}))$
$\because RT > 0$
$\because ln(10) - ln(K_{4}) > 0$
$\therefore RT \times ( ln(10) - ln(K_{4}) ) > 0$
$\therefore \Delta G > 0$

- Another way:
$\because K_{eq} = \frac{[P_{eq}]}{[S_{eq}]} = 4$
$\because K = \frac{P}{S} = 10$
$\therefore K_{eq} < K$
$\therefore ln(K) - ln(K_{eq}) > 0$
$\because RT > 0$
$\therefore RT \times ( ln(10) - ln(K_{4}) ) > 0$
$\therefore \Delta G >0$


---
Cover: [Walkowski, Slawomir & Szymas, Janusz. (2011). Quality evaluation of virtual slides using methods based on comparing common image areas. Diagnostic pathology. 6 Suppl 1. S14. 10.1186/1746-1596-6-S1-S14. ](https://www.researchgate.net/publication/51047721_Quality_evaluation_of_virtual_slides_using_methods_based_on_comparing_common_image_areas)
