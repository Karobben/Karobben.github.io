---
title: "Graphviz"
description: "Graphviz"
url: eddb3e
---

# Graphviz

<a name="XsnEk"></a>
# 1 Quick Start
```r
digraph F {
    rankdir = LR;
    edge [style=solid];
    node [style=filled, font=Courier];

    subgraph M {
        rank = same;
        Start [label = "Lamp doesn't work", shape = box, fillcolor = "#FF0000" ];
        End   [label = "Repair lamp"      , shape = box, color = coral];

        Con1 [label = "Lamp plugged in?", shape = diamond, color = green, size = 3];
        Con2 [label = "Bulb burned out?", shape = diamond, color = green, size = 3];
    }

    subgraph C {
        rank = same;
        RB [label = "Replace bulb", shape = box, color = deepskyblue1];
        AP [label = "Plug in lamp", shape = box, color = deepskyblue1];
    }

    Start -> Con1;
    Con1 -> AP   [label = "No"];
    Con1 -> Con2 [label = "Yes"];

    Con2 -> RB  [label = "Yes"];
    Con2 -> End [label = "No"];

		AP -> End
		RB -> End
}

```

![NrHdqH.png](https://s1.ax1x.com/2020/06/26/NrHdqH.png)

<a name="DshML"></a>
## More exemples:
[http://graphviz.org/gallery/](http://graphviz.org/gallery/)

<a name="gPUU1"></a>
# 2 Parameters

<a name="rv6r4"></a>
## 2.1 Structure
Source:[https://graphviz.gitlab.io/_pages/doc/info/lang.html](https://graphviz.gitlab.io/_pages/doc/info/lang.html)
```r
graph	:	[ strict ] (graph | digraph) [ ID ] '{' stmt_list '}'
stmt_list	:	[ stmt [ ';' ] stmt_list ]
stmt	:	node_stmt
|	edge_stmt
|	attr_stmt
|	ID '=' ID
|	subgraph
attr_stmt	:	(graph | node | edge) attr_list
attr_list	:	'[' [ a_list ] ']' [ attr_list ]
a_list	:	ID '=' ID [ (';' | ',') ] [ a_list ]
edge_stmt	:	(node_id | subgraph) edgeRHS [ attr_list ]
edgeRHS	:	edgeop (node_id | subgraph) [ edgeRHS ]
node_stmt	:	node_id [ attr_list ]
node_id	:	ID [ port ]
port	:	':' ID [ ':' compass_pt ]
|	':' compass_pt
subgraph	:	[ subgraph [ ID ] ] '{' stmt_list '}'
compass_pt	:	(n | ne | e | se | s | sw | w | nw | c | _)
```


A -> {B C}<br />is equivalent to<br />A -> B<br />A -> C

<a name="pYvmH"></a>
## color for edge

![NrHtxO.png](https://s1.ax1x.com/2020/06/26/NrHtxO.png)



<a name="UebHR"></a>
# Official Documentation
Source: [http://graphviz.org/documentation/](http://graphviz.org/documentation/)

<a name="EvAhI"></a>
## Nodes,edges ...
Souce: [https://graphviz.gitlab.io/_pages/doc/info/attrs.html](https://graphviz.gitlab.io/_pages/doc/info/attrs.html)

Node shapes

Source: [https://graphviz.gitlab.io/_pages/doc/info/shapes.html](https://graphviz.gitlab.io/_pages/doc/info/shapes.html)
![NrHUMD.png](https://s1.ax1x.com/2020/06/26/NrHUMD.png)

<a name="L3B7Z"></a>
## Edge shapes
Source: [https://graphviz.gitlab.io/_pages/doc/info/arrows.html](https://graphviz.gitlab.io/_pages/doc/info/arrows.html)
![NrHase.png](https://s1.ax1x.com/2020/06/26/NrHase.png)

<a name="MndZU"></a>
## Color


Source: [https://graphviz.gitlab.io/_pages/doc/info/colors.html](https://graphviz.gitlab.io/_pages/doc/info/colors.html)
![NrH0Zd.png](https://s1.ax1x.com/2020/06/26/NrH0Zd.png)

<a name="lu47q"></a>
# For more
please visit: 

使用graphviz绘制流程图（2015版）<br />[http://icodeit.org/2015/11/using-graphviz-drawing/](http://icodeit.org/2015/11/using-graphviz-drawing/)




---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
