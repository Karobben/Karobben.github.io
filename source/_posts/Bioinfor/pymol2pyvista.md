---
toc: true
url: pymol2pyvista
covercopy: © Karobben
priority: 10000
date: 2023-12-06 13:46:30
title: "Visualize the Protein Mesh with pyvista"
ytitle: "Visualize the Protein Mesh with pyvista"
description: "seamlessly bridges PyMOL and Python: read PyMOL result to python"
excerpt: "The main idea of this work is to use PyMOL for calculating the surface information/mesh structure, and then employ Python to read that information for visualization and other complex/advanced calculations. In other words, it seamlessly bridges PyMOL and Python."
tags: [3D, Software, Protein, PyMol, Pyvista]
category: [Biology, Bioinformatics, Protein Structure]
cover: "https://imgur.com/CvCh8So.png"
thumbnail: "https://imgur.com/CvCh8So.png"
---

## Prerrequirement

<pre>
pymol
collada
pyvista
</pre>

All libraries could be installed by `pip`

## Save the Mesh Information with Pymol

after loaded your model:

Example file: 2a6d
Target: Extract the mesh information of CDR region from a antibody
PS: output may takes a while.
```pymol
bg_color white
color deepblue, 2a6d

select CDR1, 2a6d and chain B and resi 31-35
select CDR2, 2a6d and chain B and resi 50-66
select CDR3, 2a6d and chain B and resi 99-110
create cdr, CDR1 CDR2 CDR3

show mesh, cdr
color hotpink, cdr

hide all
show surface, cdr
save object.stl, cdr
```

![Select a target area from pymol](https://imgur.com/bNjPfcD.png)


## Load It with pyvista

```python
import pyvista as pv
mesh = pv.read('object.stl')

mesh.plot()

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh)
plotter.show(screenshot="myscreenshot.png")
```

![stl file visualize by pyvista](https://imgur.com/kH46OTm.png)


## Model Manipulation

### Rotate the Model

```python
# Rotate the mesh
angle = 45  # Angle in degrees

mesh.rotate_x(angle)  # Rotate 45 degrees around the x-axis
# mesh.rotate_y(angle)  # Rotate around the y-axis
# mesh.rotate_z(angle)  # Rotate around the z-axis

# For rotation around an arbitrary axis (e.g., [1, 1, 1]), use:
# mesh.rotate_vector([1, 1, 1], angle)

# Now you can plot the rotated mesh
plotter = pv.Plotter()
plotter.add_mesh(mesh)
plotter.show()
```

### Move the Model

```python
import pyvista as pv

# Assume 'mesh' is your PyVista mesh
# ...

# Translate the mesh
translation_vector = [10, 0, 0]  # This will move the mesh 10 units along the x-axis
mesh.translate(translation_vector)

# Now you can plot the translated mesh
plotter = pv.Plotter()
plotter.add_mesh(mesh)
plotter.show()
```

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
