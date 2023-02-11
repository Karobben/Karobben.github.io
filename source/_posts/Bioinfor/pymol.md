---
toc: true
url: pymol
covercopy: <a href="https://pymol.org/2/">© pymol</a>
priority: 10000
date: 2021-09-17 13:57:09
title: "Pymol: the best protein structure viewer"
ytitle: "Pymol"
description: 'Pymol: the best protein structure viewer'
excerpt: "Pymol: the best protein structure viewer"
tags: [Software]
category: [Biology, Bioinformatics, Software]
cover: "https://pymol.org/2/img/screenshot2.png"
thumbnail: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/PyMOL_logo.svg/64px-PyMOL_logo.svg.png"
---

## View and Themes

### background color
```bash
bg_color grey30
```

## Add something

### Add Hydrogen bonds

Add Hydrogen bonds: [PyMOL tutorial](http://www.protein.osaka-u.ac.jp/rcsfp/supracryst/suzuki/jpxtal/Katsutani/en/hydrogenbond.php)

**Action → find → polar contacts → select from menu**

|![Add Hydrogen bonds](http://www.protein.osaka-u.ac.jp/rcsfp/supracryst/suzuki/jpxtal/Katsutani/figure/hydrogenbond1.png)|
|:-:|
|[&copy; PyMOL tutorial](http://www.protein.osaka-u.ac.jp/rcsfp/supracryst/suzuki/jpxtal/Katsutani/en/hydrogenbond.php)|

## Remove something
cite: [&copy; Jan-Philip Gehrcke; 2011](https://gehrcke.de/2011/06/pymol-remove-hydrogens-and-water/)
```bash
# removing hydrogens
remove (hydro)
remove hydrogens

# removing water
remove resn hoh

# removing solvent
remove solvent
```


## Strcture align

|![Protein Structure Align](https://pymolwiki.org/images/thumb/6/6e/After_alignment.png/400px-After_alignment.png)|
|:-:|
|[&copy; Pymol](https://pymolwiki.org/index.php/Align)|


```bash
fetch 1oky 1t46, async=0

# 1) default with outlier rejection
align 1oky, 1t46

# 2) with alignment object, save to clustalw file
align 1oky, 1t46, object=alnobj
save alignment.aln, alnobj

# 3) all-atom RMSD (no outlier rejection) and without superposition
align 1oky, 1t46, cycles=0, transform=0
```

### Partial structure align

Cite: [Queen's University](http://pldserver1.biochem.queensu.ca/~rlc/work/teaching/pymol/alignment/)

```bash
align 5cha and resi 1-100, 2xxl and resi 300-400
# or in short form:
align structure2 & i. 1-100, structure 1 & i. 300-400

# Furthermore, you may wish to restrict the alignment to just the backbone atoms, so you can say:

align structure2 and resi 1-100 and name n+ca+c+o, structure1 and resi 300-400 and name n+ca+c+o

# or in short form:

align structure2 & i. 1-100 & n. n+ca+c+o, structure1 & i. 300-400 & n. n+ca+c+o
```

### Align chains

```bash
align 5cha and chain A+B+C, 2xxl and chain A
```

## Atom

### Atom color

```bash
## change the whole proteins color
color grey90, 2xxl
color grey80, 2xxl 5cha # 2 proteins
```

### Select Atom

[Select Properties](https://pymolwiki.org/index.php/Property_Selectors)

```PyMol PyMol
select aas, resn ASP+GLU in 2xxl
```

Create a variate ass which contain all ASP and GLU residues.
