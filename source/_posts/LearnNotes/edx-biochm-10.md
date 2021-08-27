---
toc: true
url: edx_biochm_10
covercopy: <a href="https://www.researchgate.net/figure/Proposed-distribution-of-phospholipids-in-human-red-blood-cells-put-forward-by-Verkleij_fig1_276067418">© Verkleij, et al.</a>
priority: 10000
date: 2021-04-14 15:45:00
title: "Principles of Biochemistry 10 |Lipids Related Membrane-Function and Pathology| Class Notes |HarvardX"
ytitle: "基礎生物化學筆記 10 |脂质相关的膜功能与疾病| 哈佛 edx網課"
description: "Functions and related diseases of the lipids on cell membrane| Class notes for biochemistry"
excerpt: "Functions and related diseases of the lipids on cell membrane| Class notes for biochemistry"
tags: [Classes, Biology, Biochemistry]
category: [Notes, Class, Biochemistry]
cover: "https://www.researchgate.net/profile/Georg-Pabst/publication/276067418/figure/fig1/AS:294532152348672@1447233345197/Proposed-distribution-of-phospholipids-in-human-red-blood-cells-put-forward-by-Verkleij.png"
thumbnail: "https://www.researchgate.net/profile/Georg-Pabst/publication/276067418/figure/fig1/AS:294532152348672@1447233345197/Proposed-distribution-of-phospholipids-in-human-red-blood-cells-put-forward-by-Verkleij.png"
---

## Lipids for Membrane Functions
- Membrane **Curvature**
- Bilayer **Asymmetry**
- Membrane **Fluidity**

### Membrane Curvature

The **conical shape** of lipids was more prefer the inner layer which means the two layers of the membrane are **asymmetrical**.

- Exp:
  - ***Phosphatidylcholine*** - cylindrical shape
  - ***Phosphatidylethanolamine*** - Conical shape

#### Human Red Blood Cells

The lipid asymmetry of the membrane of the red blood cell:
|![Proposed distribution of phospholipids in human red blood cells put forward by Verkleij et al[^1]](https://www.researchgate.net/profile/Georg-Pabst/publication/276067418/figure/fig1/AS:294532152348672@1447233345197/Proposed-distribution-of-phospholipids-in-human-red-blood-cells-put-forward-by-Verkleij.png)|
|:-:|
|(c) Verkleij et al[^1] |

In <u>aged</u> red blood cells, the composition of the leaflet is changed. The phosphatidylserine appears on the surface of red blood cells and becomes predominant. This gives a signal to the macrophages to <u>clear them out</u>.

#### Maintain the asymmetry

Lipid transport proteins are responsible for maintaining asymmetry.

***Flipase***: outer into inner
***Floppase***: Inner into outer
***Scramblase***: Both directions


The lipids composition of the ER, Golgi apparatus and the cell membrane are very similar.


### The Fluidity of the Membrane

Situation 1: Full of Saturated, long fatty acid tails:
 - The membrane was packed much denser
 - It has low fluidity
 - It is called a **Paracrystalline state**
 - Situation 2: The membrane with shorter and unsaturated tails:
 - Packing much looser
 - More fluid
 - It is called a **fluid state**
 - Situation 3: Cholesterol
 - During the Golgi transport, a part of sphingolipids and cholesterol are transported into the cell membrane.
 - Intercalate between fatty acid tails
 - Disturb the tight packing
 - improve fluidity and maintain the rigidity of the **Paracrystalline state**

At a physiological Tm, a membrane existed between these two states.

## Protein and lipids in the membrane

Exp: lipid draft

### ***FRAP***

***FRAP***: Fluorescence Recovery After Photobleaching
|![Fluorescence Recovery After Photobleaching](http://zeiss-campus.magnet.fsu.edu/articles/livecellimaging/images/techniquesfigure9.jpg)|
|:-:|
|[(c) zeiss-campus](http://zeiss-campus.magnet.fsu.edu/articles/livecellimaging/techniques.html)|
1. Label of lipids
2. Make a small dark spot with laser
3. Measure the time the dark became fluorescence again.

**Fluorescence recovery is due to the near lipids diffusion.**

So, we can make a graph to show how long it takes to determine the ==diffusion-coefficient==.

$$
s = \sqrt{ 4Dt}
$$

$s$: Average distance traveled
$D$: Diffusion Coefficient
$t$: Time


### Membrane proteins

|![t](https://teaching.ncl.ac.uk/bms/wiki/images/6/6d/Membrane_Protein.png)|
|:-:|
|[(c) teaching.ncl.ac.uk](https://teaching.ncl.ac.uk/bms/wiki/index.php/Membrane_protein)|

#### Protein Diffusion

The diffusion velocity of the protein is variable.

- Similar to lipids: Photoreceptor.
- Very slow: chloride bicarbonate in red blood cell, which has interaction in the intracellular region of other protein networks, membrane skeleton.


#### Protein Functions

The total **concentration** and **composition** of the protein are **highly variable**.


#### Protein Position

- Integral membrane protein: fully embedded in the lipid.
- Peripheral protein: with lipids that are inserted into the lipid bilayer.

#### Functions

- Signal Transduction
- Molecular transportation (Pumps / Channels)
  - Ion
  - Glucose
  - Water

## Signal Role of the lipids

Both too little and too many lipids were causing pathologies.

Lipid droplets:
  - Few:
    Lipodystrophy & Cachexia

### Lipids Maintain

```graphviz
digraph F {
    rankdir = UD;
    edge [style=solid];
    node [style=filled, font=Courier];

    subgraph cluster_0{
      subgraph A {
        rank = "same";        
        Adipocyte
        Padipocyte [label = "Pre-adipocyte"]
      }
      MAdipocyte [label = "Mature Adipocyte"]

      style=filled;
  		color=lightgrey;
  		node [style=filled,color=white];
  		label = "Differentiation";
    }
    CDeath [label = "Cell Death"]

    Adipocyte -> MAdipocyte
    Padipocyte -> Adipocyte  [label ="Insulin and Cortisol|AKT2, PPARr"]
    MAdipocyte -> CDeath [label="Lamin A, ZMPSTE24"]
    MAdipocyte -> Adipocyte
}
```


### The fate of lipid droplets

The form of the lipid droplets is controlled by the rate of ==triacylglycerol synthesis== and the rate of ==mobilization by lipolysis==

**High energy state**:
  - ***GPAT***, ***AGPAT***, and ***MGAT*** catalyze the addition of fatty acids to glycerol or to monoacylglycerol to produce diacylglycerol
  - ***DGAT1*** and ***DGAT2*** contributed to the final synthesis of triacylglycerol
  - triacylglycerol stored in the endoplasmic reticulum
  - triacylglycerol will then accumulate between the two leaflets of the ER to form a small bump
  - Finally buds off and became a lipid droplet.

Genetic mutation reducing the activity of the ***AGPAT*** is implicated in over 50% of congenital generalized lipodystrophy.

**Low energy state**:

```graphviz
digraph F {
  node [style=filled,color=white, shape =box];
  rankdir ="UD"
  subgraph cluster_0{
    subgraph A {
      rank = "same";
      Catecholamine
      GP
      AD
    }


    Catecholamine
    GP [label ="trimeric G protein"]
    AD [label ="adenylyl cyclase"]

    style=filled;
		color= darkorange;
		label = "Cell Membrane";

  }

  subgraph cluster_1{

    ABAT [ label = "<f1> ABHD5 |<f2> ATGL"
              shape = "record"
              ];
    perilipin

    marr0002 [ label = "<f1> HSL |<f2> FABP4"
              shape = "record"
              ] ;
    LD [label = "lipid droplet", shape = plain]


    style=filled;
		color=deepskyblue3;
		label = "Surface of lipid droplet";

  }

  subgraph B {
    rank = "same";
    marr0001 [ shape=diamond,style=filled,label="",height=.1,width=.1] ;
    ATP
    cAMP [label ="cyclic AMP"]
  }

  subgraph C {
    rank = "same";
    ABHD5
    PKA
    ATGL
  }


  Catecholamine -> GP [label = "active"]
  GP -> AD [label = "active"]
  AD -> marr0001 [label = "catalytic"]
  ATP -> marr0001 [dir =none]
  marr0001 -> cAMP
  cAMP -> PKA [label = "active"]
  PKA -> perilipin  [label = "phosphate"]
  PKA -> HSL [label = "activate"]
  perilipin -> ABHD5 [label = "activate"]
  perilipin -> LD [label = "remodeling the surface of the droplets"]
  ABHD5 -> ATGL [label = "recruit"]
  HSL -> marr0002 [dir = none]
  FABP4 -> marr0002 [dir = none]
  marr0002 -> LD
  ATGL -> ABAT:f0 -> LD
}
```


Any mutation leading to uncontrolled activation of lipolysis will also result in lipodystrophy.

**Exp**: mutations prevent perilipin inhibition of ***ABHD5*** binding to the ***lipase ATGL***, leading to constitutive activation of **lipolysis**, and ultimately to **lipodystrophy**.


### Acquired Lipodystrophy

**Exp**: Autoimmune reaction and drug treatment.

HIV-associated acquired lipodystrophy.
Nucleoside reverse transcriptase inhibitors: mitochondrial toxicity.
Protease inhibitors: inhibit a protein needed for the processing of the nuclear protein lamin A.


## High Body Fat Situation

Two diseases: **Neutral Lipid Storage Disease**; **Metabolic Syndrome**

### Neutral Lipid Storage Disease

**Adipocytes**: Very large lipid droplets; Dominated by the TAG.
**Monogenic Disease**

Two Types of NLSD:
- ***Cardiomyopathy***: Characterized by a type of **heart disorder**
- ***NLSD-M***: Characterized by ***Ichthyosis*** (Sin takes on fish-scale-like appearance)
- ***NLSD-I***

#### ***NLSD-M***

The associated gene is ***ATGL***, which catalyzes the first step of triacylglycerol.  
Mutation of this gene prevented its recruitment.

Connection with ***Cardiomyopathy***:
This mutation impairment the release of energy fuels and impacts the tissues such as the cardiac muscle.

#### ***NLSDI***

NLSD-I: Chanarin-Dorfman Syndrome

Associated gene: $\alpha/\beta$-hydrolase domain-containing protein 5 (ABHD5)

ABHD5: triacylglycerol to diacylglycerol

***Ichthyosis***:
  - "Ichthyo": Having to do with fish
  - "-osis": pathology, or abnormal.
  - The skin of the patient was dry and rough like fish scales

**Causes**:
  - Abundant abnormal lipid deposits in the skin, which could reduce the permeability of the skin.
  - The outer layer of the skin was made by lipid-based Extracellular Matrix
  - The permeability of this layer is functional when lipolysis is functional.
  - Impaired lipolysis leads abnormal deposition of triacylglycerol.
  - Result: breakdown of the mortar holding the bricks; makes the skin taking on a dry, rough, and scale-like appearance.

## Metabolix Syndrome

Metabolix Syndrome is characterized by a cluster of pathologies: high blood level of triacylglycerol, cholesterol, and LDL, hyperglycemia, and insulin resistance.

Polygenic disease.

Ectopic fat deposition -[Lipotoxity; inflammation]-> insulin resistance -> Type 2 diabetes

```graphviz

digraph F {
    rankdir = LR;
    edge [style=solid];
    node [style=filled, font=Courier];

    subgraph M {
        rank = same;
        Start [label = "Ectopic Fat Deposition", shape = box, fillcolor = "#FF0000" ];
        End   [label = "Type 2 diabetes"      , shape = box, color = coral];

        Con1 [label = "Insulin Resistance", shape = diamond, color = green, size = 3];
    }

    Start -> Con1 [label = "Lipotoxity; inflammation" ]
    Con1 -> End
}


```

perilipin: control the size of the lipid droplets. (by initiating a chain reaction to lipid degradation.)

inflammation: <l>lipid gives the extra ATP in a muscle which recruits more adipocytes and attracts the macrophages.</l>
















[^1]: Verkleij, A.J.; Zwaal, R.F.A.; Roelofsen, B.; Comfurius, P.; Kastelijn, D.; van Deenen, L.L.M.The asymmetric distribution of phospholipids in the human red cell membrane. A combinedstudy using phospholipases and freeze-etch electron microscopy. Biochim. Biophys. Acta 1973,323, 178–193
