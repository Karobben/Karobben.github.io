---
url: zs2d12
---

# GGplot2 - 杂记

'''<br />0, ggsave<br />1.1, point chart<br />1.2, Box plot<br />1.3, Bar plot<br />1.4, Heatmap<br />1.5, Fan plot<br />'''

###################################################################################################<br />###################<br />###################  ggplot<br />###################<br />###################################################################################################

##########################

<a name="bcae3146"></a>
# 0 ggsave

##########################

ggsave(filename, plot = last_plot(), device = NULL, path = NULL, scale = 1, width = NA, height = NA, units = c("in", "cm", "mm"), dpi = 300, limitsize = TRUE, ...)

#########################

<a name="b1e3bd2a"></a>
# 1.1, point chart

#########################<br />Point gragh<br />ggplot(data = mpg) + geom_point(mapping = aes(x = displ, y = hwy, color = class))<br />ggplot(data = mpg) + geom_point(mapping = aes(x = V1, y = V2, color = V3, shape = V4, size=V5))

#########################

<a name="0340e9ac"></a>
# 1.2, Box plot

#########################<br />#box

ggplot(box,aes(x=box$variable,y=box$value))+geom_boxplot()

#########################

<a name="f1a6a24d"></a>
# 1.3, bar plot

#########################<br />#bar #barplot

- geom_bar(stat= 'identity')

<a name="237bed0d"></a>
## the number of the point

- geom_bar(aes(fill=group),stat="identity")

<a name="089b0219"></a>
## the mean of all point (stack togather)

- geom_bar(aes(fill=group),stat="summary",fun.y="mean",position = 'stack')

<a name="9b52f0c5"></a>
## dont stact

- geom_bar(aes(fill=group),stat="summary",fun.y="mean",position = 'dodge')

#########################

<a name="e82dea9e"></a>
# 1.4,   heatmap

#########################<br />#heatmap

ggplot(A, aes(x=Diet,y=A$Time)) + xlab("samples") + ylab(NULL) +theme_bw()+theme(panel.grid.major = element_blank()) +theme(legend.key=element_blank())+geom_tile(aes(fill=weight)) +scale_fill_gradient2(low="steelblue2",mid="white",high="red",midpoint =150)+scale_fill_gradient(low = "white", high = "red")

ggplot(A, aes(x=Diet,y=A$Time)) + xlab("samples") + ylab(NULL) +<br />theme_bw()+<br />theme(panel.grid.major = element_blank()) +<br />theme(legend.key=element_blank())+<br />geom_tile(aes(fill=weight)) +<br />scale_fill_gradient2(low="steelblue2",mid="white",high="red",midpoint =150)+<br />scale_fill_gradient(low = "white", high = "red")

#####################################################<br />library(DOSE)<br />library(RColorBrewer)<br />colorRampPalette(rev(brewer.pal(n = 7,<br />name = "RdYlBu"))) -> cc<br />simplot(d) + scale_fill_gradientn(colors=cc(100)) + theme()

#########################

<a name="33fea772"></a>
# 1, switch X and Y

#########################

- coord_flip()

###########################

<a name="4b0b9f17"></a>
# The region of the  aix

###########################

- coord_cartesian(ylim = c(100,200), expand = F)
- coord_fixed(ratio =2) #expand

###############

<a name="9d42bad0"></a>
# polar  aix

###############

- coord_polar(theta ="x", start = pi/3)
- coord_polar(theta ="y", start = pi/3)

##+ theme(panel.grid.major =element_line(color="grey"),axis.line = element_blank(),panel.background = element_blank(), axis.ticks=element_blank(),axis.text.y=element_blank())

ggplot(data, aes(x=as.factor(id), y=value)) +  geom_bar(stat="identity", fill=alpha("green", 0.3))<br />ylim(-100,120) +<br />theme_minimal() +<br />theme(<br />axis.text = element_blank(),<br />axis.title = element_blank(),<br />panel.grid = element_blank(),<br />plot.margin = unit(rep(-1,4), "cm")<br />) +<br />coord_polar(start = 0) +<br />geom_text(data=label_data, aes(x=id, y=value+10, label=individual, hjust=hjust), color="black", fontface="bold",alpha=0.6, size=2.5, angle= label_data$angle, inherit.aes = FALSE )

##################################

<a name="094956e5"></a>
## Change the name of the Stixs

##################################

<a name="35e047b6"></a>
# add the limits first and substitu...

- scale_x_discrete(name ="Dose (mg)", limits=c(1:119),labels=as.character(A$X1))

##############

<a name="255b59a8"></a>
# Add a line

##############

ggplot(data = mpg) + geom_point(mapping = aes(x = V1, y = V2)) + geom_smooth(mapping= aes(x=V1, y=V2))


<a name="sting"></a>
# sting

ggplot(mpg , aes(x = displ, y = hwy)) +<br />geom_point() +<br />geom_smooth(method = "lm")

###########

<a name="ggtitle"></a>
# ggtitle

###########

ggtitle("AAA")<br />theme(plot.title = element_text(hjust = 0.5))

#########

<a name="labs"></a>
## labs

#########<br />#labs

- labs(title="MPO", x="Basket", y="U/g")

##############

<a name="Facet"></a>
### Facet

##############<br />#facet

- facet_grid(Group ~ .)

<a name="8c063bca"></a>
# for GO enrichment

- facet_grid(. ~ Cate,scales = "free_x",space = "free")<br />
'''<br />
ggplot(GO3_ALL1[GO3_ALL1[[2]] >5,]) + geom_bar(aes(x=Description,y=Count,fill=group),stat='identity') + facet_grid(~group, ,scales = "free_x",space = "free") + theme(legend.position='none', panel.background=element_blank(),axis.line=element_line(color='black'), strip.background=element_blank(), strip.text.x=element_text(size=15,face='bold') ,axis.text.x =element_text(angle=45,hjust=1,size=8) )+ expand_limits(x=c(-0.5,0))<br />
'''
- facet_wrap(~ V3, nrow = NULL, ncol = NULL, scales = "free")

##############

<a name="Levels"></a>
## Levels

##############<br />#levels

table$X=factor(table$X, levels=table[[1]])

##############

<a name="text"></a>
## text

##############<br />#text<br />library(ggrepel)<br />geom_text_repel(aes(label=variable))

- geom_text(data=A,aes(x=V1,y=valuable,label=row.names(A4), colour =row.names(A4)),nudge_x = 0.5)

#############

<a name="legend"></a>
# legend

#############<br />#rm legend<br />+theme(legend.position='none') ("none", "left", "right", "bottom", "top", or two-element numeric vect

#############

<a name="smooth"></a>
# smooth

#############

+geom_smooth(data=Growth_p,aes(x=ID,y=log(value+20)/3,group=ALL,color='OD Curve'),se = FALSE,span=0.75)

#############

<a name="theme"></a>
# theme

#############<br />#theme

- theme(plot.title = element_text(hjust = 0.5),axis.text.x = element_text(angle = 45, hjust=1))

###########################

<a name="5b90e64d"></a>
# class by $V3 in different chart

ggplot(data = mpg) + geom_point(mapping = aes(x = V1, y = V2,))+ facet_wrap(~ V3)

########################

<a name="948e23f0"></a>
# Color patern

########################<br />scale_fill_brewer + (..., type = "seq", palette = 1, direction = 1, aesthetics = "colour")

'''<br />Palettes:<br />Diverging<br />BrBG, PiYG, PRGn, PuOr, RdBu, RdGy, RdYlBu, RdYlGn, Spectral<br />Qualitative<br />Accent, Dark2, Paired, Pastel1, Pastel2, Set1, Set2, Set3<br />Sequential<br />Blues, BuGn, BuPu, GnBu, Greens, Greys, Oranges, OrRd, PuBu, PuBuGn, PuRd, Purples, RdPu, Reds, YlGn, YlGnBu, YlOrBr, YlOrRd<br />'''<br />################

<a name="63396163"></a>
# cow plot

################<br />#cow #cowplot<br />library(cowplot)

ggdraw()+ draw_plot(p1,0,0.5,0.5,0.5)+draw_plot(p2,0.5,0.5,0.5)<br />+draw_plot(pheat,0.5,0,0.5,0.5)<br />+draw_plot_label(c("A", "B"), c(0,0.5), c(1, 1), size = 20)

'''<br />Xl,Xr,Yt,Yzoom<br />draw_plot(p1,Xl,Yb,Xzoom,Yzoom,Pzoom)<br />'''

##############

<a name="mapping"></a>
# mapping

##############<br />library(pacman)<br />p_load(tidyverse, gganomate, maps, ggthemes)

ggplot()+borders("world", color="black", fill="steelblue4")+geom_point(data = rladies, aes(lon, lat, size=followers), color="firebrick3", alpha=0.6)+scale_size_continuous(range = c(2,8), breaks = c(250, 500, 750, 1000))+labs(size="Followers", title="The development of R-Ladies'Twitter accounts",x=NULL,y=NULL)+theme(text = element_text(family = "Times New Roman", color = "deeppink"),plot.title = element_text(size=40,color = "#f9ba00"),plot.subtitle = element_text(size=14),axis.ticks = element_blank(),axis.text = element_blank(),panel.grid = element_blank(),panel.background = element_rect(fill="skyblue"),plot.background = element_rect(fill = "#333333"),legend.position = c(0.18,0.36),legend.background = element_blank(),legend.key = element_blank(),legend.text = element_text(size = 24),legend.title = element_text(size=28, color = "orangered3"))

##################

<a name="d40b80ab"></a>
# The colour Set

##################<br />library("ggthemes")<br />library("RColorBrewer")

<a name="Gradient"></a>
# Gradient

scale_fill_gradient() 允许分配一组双色连续渐变，low="white",high="red"<br />scale_fill_gradient2() 允许分配一组三色连续渐变，low="blue",mid="white",high="red"

<a name="b4b1d439"></a>
# sed a group of colour

scale_fill_manual(values=c("Linen","Peru","PeachPuff","SandyBrown","Chocolate"))

<a name="1f541ad9"></a>
# apply the Set on ggthemes

- scale_colour_XXX()  # Tab to see more

################

<a name="annotate"></a>
# annotate

################

annotate(geom, x = NULL, y = NULL, xmin = NULL, xmax = NULL,<br />ymin = NULL, ymax = NULL, xend = NULL, yend = NULL, ...,<br />na.rm = FALSE)

geom="text" |"rect"| "segment" | "pointrange"

- annotate("segment", x = 2, xend = 4, y = 15, yend = 25, colour = "pink", size=3, alpha=0.6, arrow=arrow())

################

<a name="geom_segment"></a>
# geom_segment

################

ggplot(data, aes(x=x, y=y)) + geom_segment( aes(x=y, xend=0, y=x, yend=0, color=mycolor), size=1.3, alpha=0.9) + theme_light()

#####################

<a name="90135a1b"></a>
# remove background

#####################<br />##rm ##background

- theme(panel.grid.major =element_blank(), panel.grid.minor = element_blank(),panel.background = element_blank(),axis.line = element_line(colour = "black"))
- theme(legend.position='none')<br />
theme(axis.ticks = element_blank()) +   ## 删去刻度线

#################

<a name="ce0636ba"></a>
# expand limits

#################

- expand_limits(y=c(-12,18))

<a name="927f9b4f"></a>
# slice the limits

- coord_cartesian(ylim=c(5, 7.5))

#########

<a name="c46b5e86"></a>
# error bar


- geom_errorbar(aes(ymin=len-sd, ymax=len+sd), width=.2， position=position_dodge(.9))<br />
##########################

<a name="981f393a"></a>
## Parameter of theme

##########################<br />line	#all line elements (element_line)<br />rect	#all rectangular elements (element_rect)<br />text	#all text elements (element_text)<br />title	#all title elements: plot, axes, legends (element_text; inherits from text)<br />aspect.ratio	#aspect ratio of the panel<br />axis.title	#label of axes (element_text; inherits from text)<br />axis.title.x	#x axis label (element_text; inherits from axis.title)<br />axis.title.y	#y axis label (element_text; inherits from axis.title)<br />axis.tex	#tick labels along axes (element_text; inherits from text)<br />axis.text.x	#x axis tick labels (element_text; inherits from axis.text)<br />axis.text.y	#y axis tick labels (element_text; inherits from axis.text)<br />axis.ticks	#tick marks along axes (element_line; inherits from line)<br />axis.ticks.x	#x axis tick marks (element_line; inherits from axis.ticks)<br />axis.ticks.y	#y axis tick marks (element_line; inherits from axis.ticks)<br />axis.ticks.length	#length of tick marks (unit)<br />axis.line	#lines along axes (element_line; inherits from line)<br />axis.line.x	#line along x axis (element_line; inherits from axis.line)<br />axis.line.y	#line along y axis (element_line; inherits from axis.line)<br />legend.background	#background of legend (element_rect; inherits from rect)<br />legend.margin	#extra space added around legend (unit)<br />legend.key	#background underneath legend keys (element_rect; inherits from rect)<br />legend.key.size	#size of legend keys (unit; inherits from legend.key.size)<br />legend.key.height	#key background height (unit; inherits from legend.key.size)<br />legend.key.width	#key background width (unit; inherits from legend.key.size)<br />legend.text	#legend item labels (element_text; inherits from text)<br />legend.text.align	#alignment of legend labels (number from 0 (left) to 1 (right))<br />legend.title	#title of legend (element_text; inherits from title)<br />legend.title.align	#alignment of legend title (number from 0 (left) to 1 (right))<br />legend.position	#the position of legends ("none", "left", "right", "bottom", "top", or two-element numeric vector)<br />legend.direction	#layout of items in legends ("horizontal" or "vertical")<br />legend.justification	#anchor point for positioning legend inside plot ("center" or two-element numeric vector)<br />legend.box	#arrangement of multiple legends ("horizontal" or "vertical")<br />legend.box.just	#justification of each legend within the overall bounding box, when there are multiple legends ("top", "bottom", "left", or "right")<br />panel.background	#background of plotting area, drawn underneath plot (element_rect; inherits from rect)<br />panel.border	#border around plotting area, drawn on top of plot so that it covers tick marks and grid lines. This should be used with fill=NA(element_rect; inherits from rect)<br />panel.margin	#margin around facet panels (unit)<br />panel.margin.x	#horizontal margin around facet panels (unit; inherits from panel.margin)<br />panel.margin.y	#vertical margin around facet panels (unit; inherits from panel.margin)<br />panel.grid	#grid lines (element_line; inherits from line)<br />panel.grid.major	#major grid lines (element_line; inherits from panel.grid)<br />panel.grid.minor	#minor grid lines (element_line; inherits from panel.grid)<br />panel.grid.major.x	#vertical major grid lines (element_line; inherits from panel.grid.major)<br />panel.grid.major.y	#horizontal major grid lines (element_line; inherits from panel.grid.major)<br />panel.grid.minor.x	#vertical minor grid lines (element_line; inherits from panel.grid.minor)<br />panel.grid.minor.y	#horizontal minor grid lines (element_line; inherits from panel.grid.minor)<br />panel.ontop	#option to place the panel (background, gridlines) over the data layers. Usually used with a transparent or blankpanel.background. (logical)<br />plot.background	#background of the entire plot (element_rect; inherits from rect)<br />plot.title	#plot title (text appearance) (element_text; inherits from title)<br />plot.margin	#margin around entire plot (unit with the sizes of the top, right, bottom, and left margins)<br />strip.background	#background of facet labels (element_rect; inherits from rect)<br />strip.text	#facet labels (element_text; inherits from text)<br />strip.text.x	#facet labels along horizontal direction (element_text; inherits from strip.text)<br />strip.text.y	#facet labels along vertical direction (element_text; inherits from strip.text)<br />strip.switch.pad.grid	#space between strips and axes when strips are switched (unit)<br />strip.switch.pad.wrap	#space between strips and axes when strips are switched (unit)

margin(t = 0, r = 0, b = 0, l = 0, unit = "pt")

element_blank()

element_rect(fill = NULL, colour = NULL, size = NULL,<br />linetype = NULL, color = NULL, inherit.blank = FALSE)

element_line(colour = NULL, size = NULL, linetype = NULL,<br />lineend = NULL, color = NULL, arrow = NULL,<br />inherit.blank = FALSE)

element_text(family = NULL, face = NULL, colour = NULL,<br />size = NULL, hjust = NULL, vjust = NULL, angle = NULL,<br />lineheight = NULL, color = NULL, margin = NULL, debug = NULL,<br />inherit.blank = FALSE)

rel(x)





<br />--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
