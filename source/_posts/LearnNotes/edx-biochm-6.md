---
toc: true
url: edx_biochm_6
covercopy: <a href="https://naturalnews.com/2019-04-05-coagulating-toxic-canola-oil-ingredient-labeling-trick-explained.html">© S.D. Wells</a>
priority: 10000
date: 2021-03-31 11:27:23
title: "Principles of Biochemistry 6 |Blood Coagulation| Class Notes |HarvardX"
ytitle: "基礎生物化學筆記 6 |凝血| 哈佛 edx網課"
description: "Blood Coagulation; Class notes for biochemistry"
excerpt: "Blood Coagulation; Class notes for biochemistry"
tags: [Classes, Biology, Biochemistry]
category: [Notes, Class, Biochemistry]
cover: "https://naturalnews.com/wp-content/uploads/sites/91/2019/04/blood-clotting.jpg"
thumbnail: "https://courses.edx.org/asset-v1:harvardx+MCB63X+1T2021+type@thumbnail+block@course_image-375x200.jpg"
---

## Blood Clot

```graphviz
digraph F {
  rankdir = "LR"

  subgraph cluster_0{
    label = "Human Blood Clot"
    Platelets
    Fibrin
    Platelets -> Platelets_E
    Fibrin -> Fibrin_E
    subgraph A {
      rank = 1
      Fibrin
      Fibrin_E
    }
    subgraph B {
      rank = 2
      Platelets
      Platelets_E
    }
    Platelets_E [shape = box, label= "form a soft plug"]
    Fibrin_E [shape = box, label = "fibrous protein forms a mesh"]
  }
}
```

```graphviz
digraph F {
  rankdir = "LR"
  subgraph cluster_1{
    node [shape= none]
    label ="Three Phases of Blood Coagulation"
    Initiation [label = "1. Initiation"]
    Extension [label = "2. Extension"]
    Stabilization [label = "3. Stabilization"]
    Cascade [label = "Coagulation Cascade", fontcolor = "red"]
  }

  subgraph cluster_2 {
    node [shape = box]
    In_1 [label = "Von Willebrand factor (vWF) attaches to the collagen fibers."]
    In_2 [label = "unfolding of the fiber and expose the bind sites of the vWF"]
    In_3 [label = "attach the surface of the platelets"]
    In_4 [label = "platelets started to attach the lesion site"]
    label = "Initiation"
    In_1 -> In_2 -> In_3 -> In_4
    subgraph A {
      rank = same
      In_4
      In_3
      In_2
      In_1
    }
  }
  Initiation -> In_1

  subgraph cluster_3 {
    label = "Extension"
    Extension_1 [shape = none,
                label = "Consistant the recruitment of addition platelets.
                        It was contributed by the fibrinogen,
                        which has two binding sites for intergins.
                        The release of ADP and thromboxane
                         A2 by activate platelets attached.
                         to form a soft plug"]
  }
  Extension -> Extension_1

  subgraph cluster_4 {
    label = "Stabilization"
    Stabilization_Ex   [shape = none,
                        label = "Conversion of fibrinogen into fibrin
                                  and the polymerization of the fibrin
                                  into a network of fibers"]
    subgraph cluster_4_1{
      node  [shape =underline]
      ssub1 [label = "1. collagen"]
      ssub2 [label = "2. Thrombin: initiate"]
      ssub3 [label = "3. ADP/TxA: \n initiate pyhsical respons"]
      ssub4 [laebl = "5. Platelets Shell"]
      label = "Four molecules"
      fontcolor = "blue"
    }
  }
  Stabilization -> ssub1
}
```

<details>

### Initiation

*[vWF]: von Willebrand factor
- Von Willebrand factor attaches to the collagen fibers.
- unfolding of the fiber and expose the bind sites of the vWWF
- attach the surface of the platelets
- platelets started to attach the lesion site.

### Extension
consistant the recruitment of addition platelets.
It was contributed by the fibrinogen, which has two binding sites for intergins.

The release of ADP and thromboxane A2 by activate platelets attached.
-> soft plug

### Stabilization
Conversion of fibrinogen into fibrin and the polymerization of the fibrin into a network of fibers.
Stabilize anchored by thrombin.


Four molecules:
  - collagen
  - Thrombin: initiate
  - ADP/TxA: initiate pyhsical respons
  - platelets shell

</details>


### Fibrinogen
The third most abundant protein in blood plasma, consisting of two C-terminal domains.

*[thrombin]: 凝血酶

From fibrinogen to fibrin:
  - controlled by the activation of the thrombin.
  - cleave a small portion (18~20) to release 2 binding sites.
  - binding sites could react with other fibrin's C-terminal
  - turned into a meshwork of fibers.
  - meshwork extended from the base of the platelet plug into the lesion
  - which tenses the platelet plug

### A positive feedback process

|![Blood Vessel Layers](https://sphweb.bumc.bu.edu/otlt/MPH-Modules/PH/PH709_Heart/BloodVessel-structure.png)|
|:-:|
|[© Wayne W. LaMorte; 2016](https://sphweb.bumc.bu.edu/otlt/MPH-Modules/PH/PH709_Heart/PH709_Heart2.html)|

As shown above, the blood vessel has a few layers. Surrounding the endothelium, cells in the second layer of the vessel are characterized by expression **tissue factors** that could trigger blood coagulation.

The lesion would expose the second layer and release the tissue factors.

### Two pathway of the coagulation cascade
- Extrinsic (first)
- Intrinsic: activated plates.

<details> <summary>
Two pathway of the coagulation cascade
</summary>

#### Extrinsic

VII: coagulation factor VII
VII~a~: **activated** coagulation factor VII
TF + VII ->  TF - VII~a~ (composite)
VII~a~: IX -> IX~a~
IX~a~: X -> X~a~
X~a~ + V~a~  + TF
X~a~ + V~a~ + TF: pro-thrombin -> thrombin
thrombin: fibrinogen -> fibrin

thrombin: V~a~
trhombin -> VIII~a~
VIII~a~: X -> X~a~
thrombin: XIII~a~
XIII~a~: polymerization

#### Intrinsic path
Initiated when some hazer or foreign be recognized.

XII -> XII~a~
XII~a~: XI -> XI~a~
like above.

Misbehavior of the Intrinsic pathway could cause blood clots to cause disease.
</details>

```graphviz

digraph F {
  "marr0001" [shape=diamond,style=filled,label="",height=.1,width=.1] ;
  "marr0002" [shape=diamond,style=filled,label="",height=.1,width=.1] ;
  "marr0003" [shape=diamond,style=filled,label="",height=.1,width=.1] ;
  "marr0004" [shape=diamond,style=filled,label="",height=.1,width=.1] ;
  "marr0005" [shape=diamond,style=filled,label="",height=.1,width=.1] ;
  "marr0006" [shape=diamond,style=filled,label="",height=.1,width=.1] ;
  "marr0007" [shape=diamond,style=filled,label="",height=.1,width=.1] ;
  "marr0008" [shape=diamond,style=filled,label="",height=.1,width=.1] ;
  "marr0009" [shape=diamond,style=filled,label="",height=.1,width=.1] ;

  TF [label ="tissue factor"]
  TF_VII [label = "{<f2>Xa|<f3>Va}|{<f0>TF|<f1>VII}"
           shape = record]
  Pthrombin [label = "Pro-thrombin"]
  Polymerization [shape = box]

  TF ->  "marr0001"
  VII-> "marr0001" -> TF_VII

  TF_VII:f0 ->  marr0002 [style = dotted]
  IX -> marr0002 [dir = none]
  marr0002 -> IXa
  IXa -> marr0003 [style = dotted]
  marr0003 -> Xa
  X -> marr0003 [dir = none]
  Xa -> marr0004 -> TF_VII:f2
  Va -> marr0004 -> TF_VII:f3


  TF_VII:f3 -> marr0005 [style = dotted]
  Pthrombin -> marr0005 [dir = none]
  marr0005 -> thrombin
  thrombin -> marr0006 [style = dotted]
  marr0006 -> fibrin
  fibrinogen -> marr0006 [dir = none]

  thrombin -> XIIIa [style = dotted]
  XIIIa -> marr0007 [style = dotted]
  marr0007 -> Polymerization
  fibrin -> marr0007 [dir =none]
  subgraph cluster_0 {
    label = "Extrinsic Pathway"
    TF
    VII
    TF_VII
    IXa
    IX
    X
    Xa
    Va
    Pthrombin
    thrombin
    marr0001
    marr0002
    marr0003
    marr0004
    marr0005
    marr0006
    marr0007
    fibrin
    fibrinogen
    XIIIa
    Polymerization
    fibrin
  }

  subgraph cluster_i {
    label = "Intrinsic Pathway"
    XII -> marr0008 ->  XIIa
    XIIa -> marr0009 [style= dotted]
    XI -> marr0009 [dir = none]
    marr0009 -> XIa
  }
  XIa -> marr0002 [style = dotted]
}

```



### The stop of the coagulation

*[thrombomodulin]: ~~~~~~~~~~~~~ 血栓调节蛋白； 血栓调节素； 凝血酶调节素

Thrombin: control **the size** of the blood clot.

Thrombin + Protein S complexes -> bind to thrombomodulin: form a ternary complex

ternary complex -> Protein C
Protein C: Inactivation of IX and X to stop the clot.

#### Two additional levels of inhibition:
1. TFPIa binds and inactivates the ternary complexes (TF, VIIa, and Xa)
2. Antithrombin 3 binds irreversibly to thrombin. It also responds to the inactivation of the IX, X, XI, and XII.


## Thrombus Detection

### Thrombus

|![blood clots](https://www.acs.org/content/acs/en/pressroom/newsreleases/2015/august/blood-clots/_jcr_content/newsReleaseContent/columnsbootstrap/column1/image.img.jpg/1439813216602.jpg)|
|:-:|
|[(c) Peter Caravan, Ph.D. ](https://www.acs.org/content/acs/en/pressroom/newsreleases/2015/august/blood-clots.html)|

- Blood clot that forms in the arteries or veins of the body
- Can cause stroke, coronary artery disease, pulmonary embolism, deep vein thrombosis
- Affects millions of people and costs billions of dollars worldwide.
- Developing new imaging tools is essential for diagnosis and monitoring disease progression

#### Fibrin imaging

- Fibrin is an attractive target for thrombus image
  - only present in blood clots and wound hearling
  - not found in circulating blood
- High density for disease, no background.

#### Phage Display

1. Phage library filter:
    - incubate the phage with fibrin and collect the phage which bind with it.
2. Phage proliferation:
    - Incubate the phage with E. coli to proliferate them.
3. Improve the affinity:
    - Repeat the phase 1 and 2 over and over again.
4. Characterize those phage
5. Magnetic Resonance Imaging (MRI)
    - Need large magnetic field and radiofrequency energy for detection


#### Magnetic Resonance Imaging (MRI)

1. It is able to detect the Hydrogen molecules and mobile molecules, which are mainly water and fats.
2. Metal is another important resource, Gadolinium ion, especially.


|![Gd DTPA-BMA](https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid=24847884&t=l)|![Thrombus Detection](https://www.researchgate.net/profile/Borislav-D-Dimitrov/publication/221921782/figure/fig2/AS:305329989537799@1449807750898/MRI-of-Sinus-ThrombosisIn-Panel-A-a-T1-weighted-MRI-scan-obtained-with-the-spin-echo.png)|
|:-:|:-:|
|<nobr>[(c) pubchem:24847884](https://pubchem.ncbi.nlm.nih.gov/compound/Gadolinium-DTPA-BMA)</nobr>|[(c) Penka A Atanassova](https://www.researchgate.net/publication/221921782_Cerebral_Venous_Sinus_Thrombosis_-_Diagnostic_Strategies_and_Prognostic_Models_A_Review)|


- Label with radioactive isotope
    - Positron Emission Tomography
- Label with fluorescent dye
    - Fluorescent microscopy
- Label with ==EP-2014R==:
    - Fibrin-binding peptide coupled to 4 Gadolinium chelates.
    - Binds reversibly and specifically to fibrin
    - Low affinity for fibrinogen, albumin and other components of plasma
    - High relaxivity: makes clots bright.
