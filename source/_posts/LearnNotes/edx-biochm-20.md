---
toc: true
url: edx_biochm_20
covercopy: <a href="https://www.researchgate.net/figure/The-metabolism-of-TG-in-the-liver-The-three-major-sources-of-FFAs-are-diet-peripheral_fig1_336685673">© Patrik Nasr</a>
priority: 10000
date: 2021-06-15 20:44:46
title: "Principles of Biochemistry 20 |Liver and Muscle Metabolism| Class Notes |HarvardX"
ytitle: "基礎生物化學筆記 20 |肝脏和肌肉的代谢| 哈佛 edx網課"
tags: [Classes, Biology, Biochemistry]
category: [Notes, Class, Biochemistry]
description: "Principles of Biochemistry 20 |Liver metabolism| Class Notes |HarvardX"
excerpt: "Liver metabolism, Edx classes, HarvardX"
cover: "https://www.researchgate.net/profile/Patrik-Nasr-3/publication/336685673/figure/fig1/AS:816341938356226@1571642493475/The-metabolism-of-TG-in-the-liver-The-three-major-sources-of-FFAs-are-diet-peripheral.png"
thumbnail: "https://www.researchgate.net/profile/Patrik-Nasr-3/publication/336685673/figure/fig1/AS:816341938356226@1571642493475/The-metabolism-of-TG-in-the-liver-The-three-major-sources-of-FFAs-are-diet-peripheral.png"
---

## Over view

glycolysis, citric acid cycle, and oxidative phosphorylation have significant effects on metabolism and catabolism. The substrates and products from metabolism could be used to synthesis nuclide acid, fatty acid, and protein. So, the processes of metabolism should be precisely regulated.

<br>

Allosteric regulation (e.g., PFK1)
- It's the quickest way to regulate the pathway.

Reversible covalent modification
- (interactive Enzyme phosphorylation) is slower than allosteric regulation.
- Common in reciprocal regulation of the catabolic and anabolic pathway.

Translation, transcriptional, and post-translational control
Compartmentalization
- Establishment of gradients across membranes


## Who all metabolic pathways are connected

Three main "Hubs" for metabolic pathways:
- Glucose-6-phosphate
- Pyruvate
- Acetyl-CoA

```graphviz
digraph{
  node [shape=box]
  G6P [label= "Glucose-6-P", color="red", shape="diamond", style="filled"]
  Pyruvate [color="green", shape="diamond", style="filled"]
  ACoA [label = "Acetyl-CoA", color="skyblue", shape="diamond", style="filled"]

  "Amino\nAcids" -> Glucose -> G6P  [color = "red"]
  G6P -> Pyruvate -> ACoA
  Lactate -> Glucose [color = "red"]
  Glycogen -> G6P [dir=both, color = "red"]
  G6P -> "Pentose phosphate\npathway" [color = "red"]

  Lactate -> Pyruvate [dir=both, color = "green"]
  Alanine -> Pyruvate [dir=both, label="deamination\ntransamination", color = "green"]

  "Fatty\nacids" -> ACoA [label = "β-oxidation", color = "skyblue"]
  "Amino\nAcids" -> ACoA [color = "skyblue"]
  "Ketone\nBodies" -> ACoA [dir = both, color = "skyblue" label = "to brain"]
  Cholesterol -> ACoA [color = "skyblue"]

  ACoA -> "Fatty acids" [color = "skyblue"]

  subgraph cluster_0{
    label = "Mitochondrial"
    fontsize = 20
    fontcolor = "red"
    ACoA, "Ketone\nBodies","Fatty\nacids"
  }

}
```

- Amino acid catabolism feeds the citric acid cycle
- Citric acid cycle intermediates feed amino acid synthesis
- Metabolic networks are a conduit for carbon backbones:
  - To build new molecules
  - To break them down for energy


## Metabolism adaptation

- Skeletal Muscle (motion):
  Fast ATP synthesis
- Red Blood cells (oxygen delivery):
  Minimal metabolism
- Brain cells (ion pumping):
  Neurotransmitter synthesis
- **Liver (metabolism)**:
  Regulator
  - Processes Toxins
  - Processes nutrients from digestion
  - Controls glucose homeostasis
    (Maintains [Glucose]~blood~ ~4mM)

High blood glucose level:
- Transport
  GLUT2 in the surface of the hepatocyte could transport glucose very efficiently.
- Transfer
  $Glucose + Pi  \overset{Glucokinase}{\longrightarrow} Glucose^{_ -}6^{_ -}P$
  Glucokinase is an isoform of hexokinase in the liver. It won't be prohibited by the products.
- Catabolism
  $Glucose^{_ -}6^{_ -}P \longrightarrow Glycogen$

Low blood glucose level:
- Glycogen broken-down:
$$
Glycogen + Pi \overset{Glycogen\ phosphorylase}{\longrightarrow} Glucose^{_ -}1^{_ -}P   \overset{Phosphogluco-mutase}{\longrightarrow} Glucose^{_ -}6^{_ -}P  \overset{Glucose 6-phosphatase}{\longrightarrow}
 Glucose
$$

### Fates of Fatty acids
- Incorporated int TAG, lipoproteins
- Bind to albumin, feed muscle
- Storage in lipid droplets (fatty liver)

### Fates of Amino acids
- Incorporated into liver proteins
- Incorporated into serum proteins
- Exported as free amino acids in the blood
- Precursors to other biomolecules
  - Nucleotides, hormones, porphyrins
  - Pyruvate, acetyl-ACoA
  - Glucose


## Muscle Metabolism

Muscle consumes 50% of oxygen and 90% during active works.

The skeletal muscle could carry anaerobic breath during the energy burst. But cardiac muscle can’t. It’ll cause cell death and/or heart attack.

**Cardiac muscle**:
- Aerobic metabolism
- Requires O~2~
- Sensitive to low pH
- Ion gradients disrupted by pH changes

### Phosphocreatine system

In cytoplasm
$$
Phosphocreatine + ADP + H^+ \overset{Creatine\ Kinase}{\rightleftharpoons} creatine + ADP
$$

This system is both common in skeletal and cardiac muscles.
H^+^ was consumed, the pH was Maintained. The recovery speed of phosphocreatine could be improved by exercise.

Creatine Kinase is distributed in the inner membrane, cytoplasm, and inter-membrane of the mitochondria.

limited of phosphocreatine system:
During the intense muscle contraction, the ATP and phosphocreatine power the muscle for **5 to 6 seconds**.

## short term, media term, and long term activities

The quickest speed of 100-meter racing is 9.58, the pH of the blood dropped from 7.4 to 7.2.
But the record of 1000 meter is 132.
If the sport keeps the speed like 100 meters, he can finish it with 95s, and the pH of the blood would drop to 6.8, and the cell would die. So, there are other metabolic pathways that get involved in the 1000 meter race compared with the 100-meter race. In this situation, glycogen was broken down.
In a much longer race, like a marathon, more energy was needed.

## Cori Cycle

```graphviz
digraph{
  rankdir = "LR"
  Glucose  [label="Glucose", color ="red", style ="filled"]
  Glucose2 [label="Glucose", color ="red", style ="filled"]
  Lactate  [label="Lactate", color ="green", style ="filled"]
  Lactate2 [label="Lactate", color ="green", style ="filled"]
  inter [label = "", width = 0, height =0]
  subgraph cluster_0{
    label ="Muscle"
    Glucose -> Lactate  [label ="Activity"]
    Glucose -> Glycogen [label ="Rest"]
    {rank=same; Lactate, Glucose}
  }
  Lactate -> Lactate2 [style=dotted, label="blood", color="red"]
  subgraph cluster_1{
    label ="Liver"
    Lactate2 -> inter [dir = none]
    ATP -> inter
    inter -> Glucose2
    {rank=same; Lactate2, inter, Glucose2}
  }
  Glucose2 -> Glucose [style=dotted, label="blood", color="red"]
}
```

## Glucose-alanine cycle Cycle

```graphviz
digraph{
  Glucose  [label="Glucose", color ="red", style ="filled", shape="hexagon"]
  Glucose2 [label="Glucose", color ="red", style ="filled", shape="hexagon"]
  Alanine  [label="Alanine", color ="green", style ="filled"]
  Alanine2 [label="Alanine", color ="green", style ="filled"]
  "NH"     [label="-NH₂", color ="skyblue", style ="filled"]
  "NH2"    [label="-NH₂", color ="skyblue", style ="filled"]
  Py       [label="Pyruvate", color = "pink", style = "filled"]
  Py2      [label="Pyruvate", color = "pink", style = "filled"]

  inter    [label="", width = 0, height =0]
  inter2   [label="", width = 0, height =0]

  subgraph cluster_0{
    label ="Muscle"
    Glucose
    "Amino\nacids" -> "NH" -> inter -> Alanine
    Py -> inter
    {rank=same;"Amino\nacids", "NH", inter, Alanine}
  }
  Alanine -> Alanine2 [label = "Blood", style = dotted, color =red]
  Glucose2 -> Glucose [label = "Blood", style = dotted, color =red]
  subgraph cluster_1{
    label ="Liver"
    Alanine2 -> inter2 -> NH2 -> "Urea"
    inter2 -> Py2 -> Glucose2
    Py2 -> "Citric acid\ncycle"
    {rank=same; Alanine2, inter2, Py2, Glucose2}
  }
}
```

## Type of Fibers

|Slow twitch Type I|Fast twitch Type IIa|Fast twitch Type IIb|
|:--|:--|:--|
|- fatty acid<br>- oxidation|- fatty acid<br>- glycolysis|- glycolysis<br>- fermentation|
|- mitochondria<br>- myoglobin|- mitochondria<br>- myoglobin<br>- glycogen|- glycogen|
|Marathon|1000 meter race|100 meter race|
