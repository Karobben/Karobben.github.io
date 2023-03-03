---
toc: true
url: fruchterman_reingold
covercopy: <a href="https://www.sciencedirect.com/science/article/pii/B9780123822291000114">© Bernie Hogan</a>
priority: 10000
date: 2023-02-20 21:44:24
title: "Fruchterman Reingold layout"
ytitle: "Fruchterman Reingold layout"
description: "Fruchterman Reingold"
excerpt: "The Fruchterman-Reingold layout is a force-directed layout algorithm, which treats edges like springs that move vertices closer or further from each other in an attempt to find an equilibrium that minimizes the 'energy' of the system. <a href='https://www.sciencedirect.com/science/article/pii/B9780123822291000072#c0007'>© Bernie Hogan</a>"
tags: ['Statistic', 'Network']
category:  ['Notes', 'Statistic', 'others']
cover: "https://ars.els-cdn.com/content/image/3-s2.0-B9780123822291000114-f11-05-9780123822291.jpg"
thumbnail: "https://ars.els-cdn.com/content/image/3-s2.0-B9780123822291000114-f11-05-9780123822291.jpg"
---


## Fruchterman–Reingold

> Fruchterman-Reingold is an algorithm used for force-directed graph drawing, which is a way of visualizing graph structures in a 2D or 3D space. The algorithm was first introduced by Thomas M. Fruchterman and Edward M. Reingold in 1991.
>
> The Fruchterman-Reingold algorithm works by simulating a physical system in which the nodes of a graph are treated as objects with electrical charges and the edges of the graph are treated as springs. The nodes are initially placed at random positions in the 2D or 3D space, and then the algorithm iteratively adjusts the position of the nodes based on the repulsion between the nodes and the attraction between the connected nodes. The nodes that are connected by an edge are pulled closer together, while the nodes that are not connected are pushed apart.
> 
> The Fruchterman-Reingold algorithm aims to minimize the total energy of the system by finding an equilibrium state where the forces between the nodes and edges are balanced. The algorithm iteratively adjusts the positions of the nodes until it reaches the equilibrium state. The result is a visually pleasing graph layout that allows the viewer to easily see the connections and relationships between the nodes.
> 
> The Fruchterman-Reingold algorithm is widely used in many fields such as social network analysis, information visualization, and bioinformatics. It has been implemented in many software packages, including Gephi, Cytoscape, and NetworkX.
> Fruchterman–Reingold is a type of layout which widely be used in the network, social network and protein-protein interaction network for instance, analysis. 
> <a title='ChatGPT'> Who sad this?</a>


So, imagine that all the nodes are electrons that carry the same charge. As a result, they prefer to stay away from each other and distribute evenly in a limited space. However, the connections (edges) work like springs that pull two nodes together. If two groups have connections that frequently occur within the group, those nodes would prefer to be close to each other and form two large clusters because of the "springs". The two groups would be away from each other because no/or a few of spring pulls them together, and the two huge groups of nodes would push the nodes outside the cluster. If a new node is added that has connections to both clusters and the number is significant enough, it could form an hourglass-like structure. And if there are a few other connections between two clusters at the same time, it would merge the two groups into a single one.

Harel–Koren Fast Multiscaling layout


## Want to know more?

This algorithm was published in 1991 by Fruchterman & Reingold[^1]. It is a undirected layout and modified from the spring-embedder model and VLSI technique called force-directed placement.

By this methoud, it is mainly concerned about:
1. Distribute the vertices evenly in the frame. 
2. Minimize edge crossings. 
3. Make  edge lengths uniform. 
4. Reflect inherent symmetry. 
5. Conform to the  frame. 

[^1]: Fruchterman, Thomas MJ, and Edward M. Reingold. "Graph drawing by force‐directed placement." Software: Practice and experience 21.11 (1991): 1129-1164.


- Repulsive forces
$
f _{rep}(u,v) = \frac{c _{rep}}{||p _v - p _u||^ 2} × \overrightarrow{p _vp _u}
$

- Attractive forces
$
f _{spring}(u,v) = c _{spring} × log\frac{||p _v - p _u||}{\ell} × \overrightarrow{p _vp _u}
$

$
f_{attr}(u,v) = f _spring(u,v)-f _{rep}(u,v)
$

- Resulting displacement vector
$
F _u =  \sum _{v \in V} f _{rep}(u, v) + \sum _{uv \in E} f _{attr} (u,v) 
$

More Details and example you can find at [Philipp Kindermann's Youtobe Video (2021) ](https://www.youtube.com/watch?v=JAe7Oscsp98)

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
