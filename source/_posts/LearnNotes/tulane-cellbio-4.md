---
toc: true
url: tulane_cellbio_4
covercopy: <a href="https://sitn.hms.harvard.edu/art/2015/actin-four-ways/"> © Anna Maurer and DWP </a>
priority: 10000
date: 2021-09-16 12:13:29
title: "4 Cytoskeleton|Advanced Cell Biology|Tulane"
ytitle: "4 细胞骨架|高等细胞生物学|杜兰"
description: "Classes notes of the Advanced Cell Biology"
excerpt: "Classes 4,  Cytoskeleton"
tags: [Classes, Cell Biology, Tulane Classes]
category: [Notes, Class, Tulane, Cell Biology]
cover: "https://i2.wp.com/sitn.hms.harvard.edu/wp-content/uploads/2015/10/BPAE-Warhol-REAL.png?resize=1024%2C819&ssl=1"
thumbnail: "https://www.researchgate.net/profile/Callixte-Yadufashije/publication/324543378/figure/fig26/AS:616049695285249@1523889101090/Onion-cell-before-staining.png"
---

## Cytoskeleton


### Type

Intermediate filament; microtubule; Actin filament

- Geometry of the cell
- Fix the position of organelles
- Moves the compounds (cargos)
- Facilitate movement of the whole cells

|Cytoskeletal Element|Diameter|Composition|
|:-|:-|:-|
|Microfilament (MF)| thin (6-7nm)| Actin+ associated protein
|Microtubules (MT)|tubular structures (25nm)| tubline + associated proteins |
|Intermediate filaments (IF)|rope-like fibers (~10)|No associated proteins|

## Actin and Microfilaments
- **G-actin** Highly globular protein
- **F-actin** Polymerizes into microfilaments (exhibits polarity)
- Filaments stabilized by other proteins

### Polymerization

- Requires nucleation (activation)
  - 3 actins
- Elongation primarily at "+" end (barbed end)
- ATP/ADP
  - G-actin has bound ATP
  - ADP-actin more likely to dissociate
- Actin-binding proteins
  - monomer sequestration (profilin)
  - trimeric G-proteins
- Celluar regulation
  - hro family (ras-like G-proteins)
  - trimeric G-proteins
- Drugs
  - cytochalasins (prevent assembly)
  - phalloidin (prevent disassembly)

$$
G-actin \to F-actin
$$

### Nucleation factors

|||
|:-|:-|
|<blockquote>==Initial== dimer and trimer formation is energetically ==unfavorable==.</blockquote>| Assemble automatically is unfavorable|
|<blockquote>==Tandem== monomer-binding ==nucleators== bring together actin monomers through tandem G-actin-binding motifs to form an actin nucleus.|Tandem: initial a pointed end (-)|
|<blockquote>A ==formin== FH2-domain dimer associates with the ==barbed end== of an actin filament and the FH1 domains recruit and deliver profilin-bound actin to the barbed end.|Formins helping elongate by binding the barbed ends|
|<blockquote>==Arp2/3 with NPF (WASp)== nucleates a new filament from the side of an existing filament, causing branching at a 70°angle.|Arp2/3 for forming a branch|

### Examples of Actin-Binding Proteins

| Tight bundles | Loose bundles  | 3-D Gels | Dick shape |
| :-----------: | :------------: | :------: | :--------: |
| fimbrin       | alpha actinin  | filamin  | Spectrin (Red blood cell)|


### Actin Microfilament (MF) Bundles

*[microvillus]: 微絨毛

> - Tight bundles (e.g., microvilli)
>   - MFs having the same polarity
>   - (+) ends point toward the microvillus tip
>   -  Fimbrin bundling proteins
>      - Two ABD of the monomer holding two MFs together

> - Loose bundles (e.g., contractile ring); which could interacted with myosine
>   - MFs loosely spaced for myosin binding for contraction
>   - &alpha;-actinin bundling proteins
>     - Two ABD of the dimer holding two MFs together


### Actin Microfilament (MF) networks

*[orthogonal]: 直角的，正交的，垂直的

>  Filamin is a dimer
>    -  Forming a flexible V-shaped molecule
>    - Crosslinking MFs into orthogonal networks

## Submembrane cortical MF in RBC

*[cortical]: 皮质的
*[spectrins]: 血影
*[Ankyrin]: 锚蛋白

> RBC spectrin, a tetramer of &alpha; and &beta; chains
>  - Two chains join laterally to form a dimer and head-to-head to form a tetramer
>  - ABDs of the &beta; chain are separated by ~200 nm
>  - Spectrins associate with short MFs (yellow ball) to form the network.
>  - Protein 4.1 (pink) links MFs to PM-embedded glycophorin
>  - Ankyrin (green) links spectrins to PM-embedded Band 3

### Stress Fibers at Focal Adhesions

> Focal adhesions: ECM attachment regions of the cell
> Stress fibers: &alpha;-actinin-linked contractile bundles of MFs
>  - Attached to the plasma membrane at focal adhesions via interactions with integrin.
>  - Mediated by talin and vinculin
>    - Talin and &alpha;-actinin bind to the cytoplasmic domains of integrins. (out cell)
>    - Talin also binds to vinculin, which in turn interacts with actin. (inner cell)


### MFs at Adherens Junctions

*[integrin]:  整合素
*[Cadherins]: 钙粘素


> - Adherens junctions are regions of ==cell-cell contact==.
> - In epithelial cells, the AJs form a ==belt-like structure==
> - Contractile bundle of MFs is linked to the PM
>     - MFs associate with cytoplasmic &alpha;/&beta; catenins (connect to ==Cadherins==), which form a complex with PM-embedded cadherins
>     - Cadherins (membrane protein) mediate contact between cells

### Myosin and Force Generation (in loos connection)
>- large family of proteins (16)
>- actin-activated ATPase
>- converts chemical energy into mechanical energy

### Cell Locomotion-1

*[lamellipodia]: 片状伪足

>- Step 1: Movement begins with extension of one or more ==lamellipodia== from the leading edge of the cell.
>- Step 2: Some lamellipodia adhere to the substratum via ==focal adhesions==.
>- Step 3: Then the bulk of the cytoplasm in the cell body ==flows forward==.
>- Step 4: The trailing edge of the cell remains attached to the substratum until the tail eventually ==detaches== and retracts into the cell body.

Proline leading the actin assembly

```graphviz
digraph F {
  rankdir = "LR"
  node [style=filled, font=Courier, color = "salmon",  shape = "box"];

  A [label="Lamellipodia\nFormation"]
  B [label="Focal Adhesion\nDormation"]
  C [label="Cytoplasm\nTransportation"]
  D [label="Old Focal\nAdhesion Detach"]

  A -> B -> C -> D
}
```

### Cell Locomotion-2
>What propels the membrane forward?
>- The polymerization of actin filaments at the (+) end, stimulated by ==profilin== located at the ==leading-edge== membrane, pushes the membrane outward.
>- ==Vasp (MF elongator) and Arp2/3== may participate in directing assembly.
>- ==Myosin I== links actin filaments to the leading-edge plasma membrane
>- ==Arp2/3 and actin cross-linking proteins== stabilize the actin filaments into networks and bundles.
>- ==Cofilin induces the loss== of subunits fromthe (−) ends of filaments.



## Microtubules (MT)

|![Microtubules](https://www.researchgate.net/profile/Linda-Amos-2/publication/227991141/figure/fig1/AS:302246198824960@1449072517316/Structure-of-microtubules-a-Atomic-structure-of-the-ab-tubulin-heterodimer-shown-as.png)|
|:-:|
|[&copy; Linda A Amos](https://www.researchgate.net/publication/227991141_Tubulin_and_Microtubules)|

### Major Roles:
1. Mechanical/Cell Shape
2. in Cilia(lung)/Flagella(bone)
3. Mitotic Spindle (divide)


> **Tubulin**:
> - highly conserved
> - heterodimer (&alpha;, &beta;)
> - in vivo MT assembly starting from MT organization center

13 &beta; subunits on the top only.
two subunits (one unit) added at a time

### Microtubule Organizing Center (MTOC)

*[Amorphous]: 無定形


> Centrioles of animal cell
>  - aka basal bodies of flagella
>  - Barrel-shaped (triplets of MT)
>
> Centrosome of plant cell
>  - Amorphous protein matrix + two centrioles
>  - Organizes cytoplasmic MT array
>  - Forms spindle poles during cell division in animal
>
> Spindle pole bodies of fungi
>  - Not contain centrioles
>  - Located on nuclear membrane
>  - Forms mitotic spindle in many lower eukaryotes

### &gamma;-Tublin and MT Nucleation

==&gamma;-Tublin: nucleation center==

> - MT nucleation in vivo requires &gamma;-tubulin and associated proteins (&gamma;Tu ring complex)
>    - Caps minus end
>    - Anchored near MTOC
>    - Tubulin &alpha;/&beta;-dimers added to plus end

### Flagellar Movement-1

|![microtubules](https://www.researchgate.net/profile/Linda-Amos-2/publication/227991141/figure/fig3/AS:302246198824962@1449072517576/a-Cross-section-through-a-typical-axoneme-viewed-from-the-tip-ie-from-the-plus.png)|
|:-:|
|[&copy; Linda A Amos](https://www.researchgate.net/publication/227991141_Tubulin_and_Microtubules)|

> Axoneme cytoskeleton of cilia and flagella
> - Nine outer doublets MTs
> - A central pair of singlet MTs
> - A and B tubules in each MT doublet
>    - 13 protofilaments in A tubule
>    - 10 protofilaments in B tubule
>    - Inner and outer dynein arms in A tubule

### Flagellar Movement-2

> **Sliding forces generated by dynein arms**:
> The dynein arms on the A tubule of 1^st^ doublet "walk" along the adjacent 2^nd^ doublet’s B tubule toward its base, the (−) end, moving the 2^nd^ doublet toward the (+) end.

### Flagellar Movement-3

> Axonemal bending:
> - Each doublet slides down only one of its two neighboring doublets,
> - Active sliding in a portion of the axoneme produces bending toward one side
> - Active sliding in the opposite portion produces bending toward the opposite side.


## Motor Proteins

> **MF associated**
> - myosin
>
> **MT associated**
> - dynein
>     - cilia/flagella
>     - cytoplasmic
> - Kinesin

|![Kinesins & Dynein](https://www.researchgate.net/profile/Jason-Duncan-4/publication/6784713/figure/fig1/AS:280842044755971@1443969369196/Cytoplasmic-Dynein-and-Kinesin-Power-Axonal-Transport-Schematic-diagram-of-the.png)|
|:-:|
|[&copy; Jason Duncan](https://www.researchgate.net/publication/6784713_The_Genetics_of_Axonal_Transport_and_Axonal_Transport_Disorders)|


### Kinesins

|![Kinesins](https://www.researchgate.net/profile/Nancy-Forde/publication/312170092/figure/fig3/AS:667843909660695@1536237804605/Kinesin-crystal-structure-and-walking-schematic-Top-crystal-structure-of-kinesin-I.ppm)|
|:-:|
|[&copy; Chapin Korosec](https://www.researchgate.net/publication/312170092_Engineering_Nanoscale_Biological_Molecular_Motors)|

> - Large superfamily of proteins (45)
>    - defined by 'motor' domain
> - Tail regions are highly divergent (cargo binding function)
> - Chemomechanical cycle
>   - similarities to myosin
>   - two motors needed (?)

Structure:
|Moto Domain | Stalk Region | Tail region|
|:-|:-|:-|
|&mu;T binding ATPase| Coiled-coil| accessory proteins specific functions|


### Kinesins in Mitosis

> - Reorganization of MT during mitosis
>     - disassembly of cytoplasmic MT
>     - assembly of spindle apparatus
> - Duplication of centrosome to initiate spindle apparatus formation
> - Several kinesins implicated
>     - separation of poles
>     - migration of chromosomes

## Intermediate Filaments

|![Intermediate Filaments](https://www.researchgate.net/profile/Gareth-Mckinley/publication/51216027/figure/fig2/AS:484692890787841@1492571198274/Deformation-of-intermediate-filaments-networks-like-the-ones-shown-here-result-in-a.png)|
|:-:|
|[&copy; Douglas Fudge, et al.](https://www.researchgate.net/publication/51216027_From_ultra-soft_slime_to_hard_-keratins_The_many_lives_of_intermediate_filaments)|

> - Rope-like fibers extending from nucleus periphery
> - Extremely stable
>     - resistant to detergent extraction
> - Only in metazoa
> - Subunits are part of large multigene family
>     - related to nuclear lamins
>     - tissue specific expression


GFAP: Glial fibrillary acidic protein

### Intermediate Filament Proteins

&alpha;-helical rod domain
C-terminus domain

> - IF protein types distinguished by N- and C-termini
> - Central region composed of ==heptad repeats==
>     - Forms coiled-coil structure (a-helices that twist around each other)


### IF Proposed Structure

> - Tetramer believed to be fundamental subunit
> - Mechanism of assembly and disassembly not known
> - Form stable structures $\to$ mechanical support

### IF Role in Mechanical Support
> - abundant in cells/structures under mechanical stress (e.g., epithelial, muscle)
> - links to membranes and other cytoskeletal elements
