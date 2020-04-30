---
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

![](https://cdn.nlark.com/yuque/__graphviz/b0f6ed473aa31f690d013d14d00e975d.svg#lake_card_v2=eyJjb2RlIjoiZGlncmFwaCBGIHtcbiAgICByYW5rZGlyID0gTFI7XG4gICAgZWRnZSBbc3R5bGU9c29saWRdO1xuICAgIG5vZGUgW3N0eWxlPWZpbGxlZCwgZm9udD1Db3VyaWVyXTtcblxuICAgIHN1YmdyYXBoIE0ge1xuICAgICAgICByYW5rID0gc2FtZTtcbiAgICAgICAgU3RhcnQgW2xhYmVsID0gXCJMYW1wIGRvZXNuJ3Qgd29ya1wiLCBjb2xvcj1ncmV5LCBzaGFwZSA9IGJveCwgZmlsbGNvbG9yID0gXCIjRkYwMDAwXCIgXTtcbiAgICAgICAgRW5kICAgW2xhYmVsID0gXCJSZXBhaXIgbGFtcFwiICAgICAgLCBzaGFwZSA9IGJveCwgY29sb3IgPSBjb3JhbF07XG5cbiAgICAgICAgQ29uMSBbbGFiZWwgPSBcIkxhbXAgcGx1Z2dlZCBpbj9cIiwgc2hhcGUgPSBkaWFtb25kLCBjb2xvciA9IGdyZWVuLCBzaXplID0gM107XG4gICAgICAgIENvbjIgW2xhYmVsID0gXCJCdWxiIGJ1cm5lZCBvdXQ_XCIsIHNoYXBlID0gZGlhbW9uZCwgY29sb3IgPSBncmVlbiwgc2l6ZSA9IDNdO1xuICAgIH1cblxuICAgIHN1YmdyYXBoIEMge1xuICAgICAgICByYW5rID0gc2FtZTtcbiAgICAgICAgUkIgW2xhYmVsID0gXCJSZXBsYWNlIGJ1bGJcIiwgc2hhcGUgPSBib3gsIGNvbG9yID0gZGVlcHNreWJsdWUxXTtcbiAgICAgICAgQVAgW2xhYmVsID0gXCJQbHVnIGluIGxhbXBcIiwgc2hhcGUgPSBib3gsIGNvbG9yID0gZGVlcHNreWJsdWUxXTtcbiAgICB9XG5cbiAgICBTdGFydCAtPiBDb24xO1xuICAgIENvbjEgLT4gQVAgICBbbGFiZWwgPSBcIk5vXCJdO1xuICAgIENvbjEgLT4gQ29uMiBbbGFiZWwgPSBcIlllc1wiXTtcblxuICAgIENvbjIgLT4gUkIgIFtsYWJlbCA9IFwiWWVzXCJdO1xuICAgIENvbjIgLT4gRW5kIFtsYWJlbCA9IFwiTm9cIl07XG5cdFx0XG5cdFx0QVAgLT4gRW5kXG5cdFx0UkIgLT4gRW5kXG59IiwidHlwZSI6ImdyYXBodml6IiwiaWQiOiI3cjJhTSIsInVybCI6Imh0dHBzOi8vY2RuLm5sYXJrLmNvbS95dXF1ZS9fX2dyYXBodml6L2IwZjZlZDQ3M2FhMzFmNjkwZDAxM2QxNGQwMGU5NzVkLnN2ZyIsImNhcmQiOiJkaWFncmFtIn0=)
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
![](https://cdn.nlark.com/yuque/__graphviz/b3ca26490c6e691b85da31eafb54446a.svg#lake_card_v2=eyJjb2RlIjoic3RyaWN0IGdyYXBoIHsgXG4gIGEgLS0gYlxuICBhIC0tIGJcbiAgYiAtLSBhIFtjb2xvcj1ibHVlXVxufSBcbiIsInR5cGUiOiJncmFwaHZpeiIsImlkIjoiWHEzZzEiLCJ1cmwiOiJodHRwczovL2Nkbi5ubGFyay5jb20veXVxdWUvX19ncmFwaHZpei9iM2NhMjY0OTBjNmU2OTFiODVkYTMxZWFmYjU0NDQ2YS5zdmciLCJjYXJkIjoiZGlhZ3JhbSJ9)


<a name="UebHR"></a>
# Official Documentation
Source: [http://graphviz.org/documentation/](http://graphviz.org/documentation/)

<a name="EvAhI"></a>
## Nodes,edges ...
Souce: [https://graphviz.gitlab.io/_pages/doc/info/attrs.html](https://graphviz.gitlab.io/_pages/doc/info/attrs.html)

Node shapes

Source: [https://graphviz.gitlab.io/_pages/doc/info/shapes.html](https://graphviz.gitlab.io/_pages/doc/info/shapes.html)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579665933905-28e49dbc-a8fa-44d1-9ce1-14070da1fa2c.png#align=left&display=inline&height=419&name=image.png&originHeight=419&originWidth=496&size=33022&status=done&style=none&width=496)<br />

<a name="L3B7Z"></a>
## Edge shapes
Source: [https://graphviz.gitlab.io/_pages/doc/info/arrows.html](https://graphviz.gitlab.io/_pages/doc/info/arrows.html)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579665992380-0291ce61-d6a1-491d-8b9c-4ea956752b7b.png#align=left&display=inline&height=281&name=image.png&originHeight=281&originWidth=493&size=17329&status=done&style=none&width=493)

<a name="MndZU"></a>
## Color


Source: [https://graphviz.gitlab.io/_pages/doc/info/colors.html](https://graphviz.gitlab.io/_pages/doc/info/colors.html)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579665861574-d083d8a3-6d2b-46bc-bbf8-63d458e9abb5.png#align=left&display=inline&height=685&name=image.png&originHeight=685&originWidth=880&size=177015&status=done&style=none&width=880)

<a name="lu47q"></a>
# For more
please visit: 

使用graphviz绘制流程图（2015版）<br />[http://icodeit.org/2015/11/using-graphviz-drawing/](http://icodeit.org/2015/11/using-graphviz-drawing/)




<br />--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
