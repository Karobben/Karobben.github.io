---
title: "ggalluvial (Picture needed)"
description: "ggalluvial (Picture needed)"
url: ggalluvial2
date: 2020/06/19
toc: true
excerpt: "alluvial plot package for ggplot"
tags: [R, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: 'https://s1.ax1x.com/2020/06/19/NuhKsS.gif'
thumbnail: 'https://s1.ax1x.com/2020/06/19/NuhKsS.gif'
priority: 10000
---

## ggalluvial (Picture needed)


```r
vignette(topic = "ggalluvial", package = "ggalluvial")
library(ggalluvial)
titanic_wide <- data.frame(Titanic)
ggplot(data = titanic_wide,
aes(axis1 = Class, axis2 = Sex, axis3 = Age,
weight = Freq)) +
scale_x_discrete(limits = c("Class", "Sex", "Age"), expand = c(.1, .05)) +
geom_alluvium(aes(fill = Survived)) +
geom_stratum() + geom_text(stat = "stratum", label.strata = TRUE) +
theme_minimal() +
ggtitle("passengers on the maiden voyage of the Titanic",
"stratified by demographics and survival")
ggplot(as.data.frame(UCBAdmissions),
aes(weight = Freq, axis1 = Gender, axis2 = Dept)) +
geom_alluvium(aes(fill = Admit), width = 1/12) +
geom_stratum(width = 1/12, fill = "black", color = "grey") +
geom_label(stat = "stratum", label.strata = TRUE) +
scale_x_continuous(breaks = 1:2, labels = c("Gender", "Dept")) +
scale_fill_brewer(type = "qual", palette = "Set1") +
ggtitle("UC Berkeley admissions and rejections, by sex and department")
ggplot(as.data.frame(Titanic),
aes(weight = Freq,
axis1 = Survived, axis2 = Sex, axis3 = Class)) +
geom_alluvium(aes(fill = Class),
width = 0, knot.pos = 0, reverse = FALSE) +
guides(fill = FALSE) +
geom_stratum(width = 1/8, reverse = FALSE) +
geom_text(stat = "stratum", label.strata = TRUE, reverse = FALSE) +
scale_x_continuous(breaks = 1:3, labels = c("Survived", "Sex", "Class")) +
coord_flip() +
ggtitle("Titanic survival by class and sex")
5. 绘制非等高冲击图
library('alluvial')
data(Refugees, package = "alluvial")
country_regions <- c(
Afghanistan = "Middle East",
Burundi = "Central Africa",
Congo DRC = "Central Africa",
Iraq = "Middle East",
Myanmar = "Southeast Asia",
Palestine = "Middle East",
Somalia = "Horn of Africa",
Sudan = "Central Africa",
Syria = "Middle East",
Vietnam = "Southeast Asia")
Refugeescountry]
ggplot(data = Refugees,
aes(x = year, weight = refugees, alluvium = country)) +
geom_alluvium(aes(fill = country, colour = country),
alpha = .75, decreasing = FALSE) +
scale_x_continuous(breaks = seq(2003, 2013, 2)) +
theme(axis.text.x = element_text(angle = -30, hjust = 0)) +
scale_fill_brewer(type = "qual", palette = "Set3") +
scale_color_brewer(type = "qual", palette = "Set3") +
facet_wrap(~ region, scales = "fixed") +
ggtitle("refugee volume by country and region of origin")
###6. 等高非等量关系
data(majors)
majorscurriculum)
ggplot(majors,
aes(x = semester, stratum = curriculum, alluvium = student,
fill = curriculum, label = curriculum)) +
scale_fill_brewer(type = "qual", palette = "Set2") +
geom_flow(stat = "alluvium", lode.guidance = "rightleft",
color = "darkgray") +
geom_stratum() +
theme(legend.position = "bottom") +
ggtitle("student curricula across several semesters")
7. 工作状态时间变化图
data(vaccinations)
levels(vaccinationsresponse))
ggplot(vaccinations,
aes(x = survey, stratum = response, alluvium = subject,
weight = freq,
fill = response, label = response)) +
geom_flow() +
geom_stratum(alpha = .5) +
geom_text(stat = "stratum", size = 3) +
theme(legend.position = "none") +
ggtitle("vaccination survey responses at three points in time")
8. 分类学门水平相对丰度实战
df=data.frame(
Phylum=c("Ruminococcaceae","Bacteroidaceae","Eubacteriaceae","Lachnospiraceae","Porphyromonadaceae"),
GroupA=c(37.7397,31.34317,222.08827,5.08956,3.7393),
GroupB=c(113.2191,94.02951,66.26481,15.26868,11.2179),
GroupC=c(123.2191,94.02951,46.26481,35.26868,1.2179),
GroupD=c(37.7397,31.34317,222.08827,5.08956,3.7393)
)
数据转换长表格
library(reshape2)
melt_df = melt(df)
绘制分组对应的分类学，有点像circos
ggplot(data = melt_df,
aes(axis1 = Phylum, axis2 = variable,
weight = value)) +
scale_x_discrete(limits = c("Phylum", "variable"), expand = c(.1, .05)) +
geom_alluvium(aes(fill = Phylum)) +
geom_stratum() + geom_text(stat = "stratum", label.strata = TRUE) +
theme_minimal() +
ggtitle("Phlyum abundance in each group")
```

<a name="FG8Ad"></a>
## More






