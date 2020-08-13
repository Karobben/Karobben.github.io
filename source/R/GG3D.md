---
title: "GG3D"
description: "GG3D"
url: gg3d2
---

# GG3D

<a name="2iMCl"></a>
# 1. 安装
```r
install.packages('devtools')
devtools::install_github("AckerDWM/gg3D")
```

<a name="YNFtv"></a>
## Quick Start
<a name="JmVtJ"></a>
### 看图
```r
library(gg3D)
library(ggplot2)
theta=1 #方位角的度数
phi=50 # 渐近线
ggplot(iris, aes(x=Petal.Width, y=Sepal.Width, z=Petal.Length, color=Species)) +
    axes_3D(theta=theta, phi=phi) + stat_3D(theta=theta, phi=phi) +
    axis_labs_3D(theta=theta, phi=phi, size=3, hjust=c(1,1,1.2,1.2,1.2,1.2), vjust=c(-.5,-.5,-.2,-.2,1.2,1.2)) +
    labs_3D(theta=theta, phi=phi, hjust=c(1,0,0), vjust=c(1.5,1,-.2),labs=c("Petal width", "Sepal width", "Petal length")) +theme_void()

```

<a name="xqVEd"></a>
### theta & phi的关系

```r
# 查看theta
for(i in c(0:100)){
theta=i #方位角的度数
phi=1 # 渐近线
p <- ggplot(iris, aes(x=Petal.Width, y=Sepal.Width, z=Petal.Length, color=Species)) +
    axes_3D(theta=theta, phi=phi) + stat_3D(theta=theta, phi=phi) +
    axis_labs_3D(theta=theta, phi=phi, size=3, hjust=c(1,1,1.2,1.2,1.2,1.2), vjust=c(-.5,-.5,-.2,-.2,1.2,1.2)) +
    labs_3D(theta=theta, phi=phi, hjust=c(1,0,0), vjust=c(1.5,1,-.2),labs=c("Petal width", "Sepal width", "Petal length")) +theme_void()+
    labs(title =paste("theta=",i))
print(p)
#ggsave(paste(i,'.png',sep=""))
}
#convert $(ls  *.png| sort -n) theta.gif

#查看phi
for(i in c(0:100)){
theta=1 #方位角的度数
phi=i # 渐近线
p <- ggplot(iris, aes(x=Petal.Width, y=Sepal.Width, z=Petal.Length, color=Species)) +
    axes_3D(theta=theta, phi=phi) + stat_3D(theta=theta, phi=phi) +
    axis_labs_3D(theta=theta, phi=phi, size=3, hjust=c(1,1,1.2,1.2,1.2,1.2), vjust=c(-.5,-.5,-.2,-.2,1.2,1.2)) +
    labs_3D(theta=theta, phi=phi, hjust=c(1,0,0), vjust=c(1.5,1,-.2),labs=c("Petal width", "Sepal width", "Petal length")) +theme_void()+
    labs(title =paste("phi=",i))
print(p)
#ggsave(paste(i,'.png',sep=""))
}
#convert $(ls  *.png| sort -n) phi.gif

```
|Theta|Phi|
|:---:|:---:|
|![NuhKsS.gif](https://s1.ax1x.com/2020/06/19/NuhKsS.gif)|![NuhMqg.gif](https://s1.ax1x.com/2020/06/19/NuhMqg.gif)|

# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)


---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
