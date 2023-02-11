---
title: "R base"
excerpt: "Functions from R base; for the beginners"
date: 2020/05/01
url: rtricks2
toc: true
cover: 'https://www.r-project.org/Rlogo.png'
thumbnail: 'https://www.r-project.org/Rlogo.png'
priority: 10000
tags: [R]
category: [R, Beginner]
---

## Install R

### Ubuntu

source page: [linuxize 2020](https://linuxize.com/post/how-to-install-r-on-ubuntu-20-04/)

```bash
sudo apt install dirmngr gnupg apt-transport-https ca-certificates software-properties-common
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
sudo apt install r-base
```
## Packages Install

- Install from CRAN
```r
install.packages("ggplot2","repos" = c(CRAN="https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))
```
- Install from local fille

<code>
install.packages("/data/data/com.termux/files/home/ggradar",repos = NULL)
</code>

### Mirrors

## options函数就是设置R运行过程中的一些选项设置
`options("repos" = c(CRAN="https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))`

## Bioconductor
`options(BioC_mirror="https://mirrors.tuna.tsinghua.edu.cn/bioconductor")`

### Reading from Excel
```r
library("readxl")
A <- read_excel("Table.xlsx")
```

```r
library(tidyr)
library(dplyr)
df <- data.frame(x = c(NA, "a.b", "a.d", "b.c","a-b"))
df %>% separate(x, c("A", "B"),'-')
```

```R
'''
Base <- data.frame(Nodes =c("P1", "P1", "P1", "P2"), Targets=c("P2","P3","P4","P1"))
List <- c("P1", "P2", "P3")
Base <- read.table("DataBase/Mybase/AB_List")
List <- read.table("")[[1]]
'''
'''
Result without Annotation
'''

addPercent <- function(x){
percent <- round(x * 100, digits = 1)
result <- paste(percent, "%", sep = "")
return(result)
}

library(tidyr)
library(dplyr)
A <- Base
A <- A[which(match(A[[1]],List)!="NA"),]
A <- A[which(match(A[[2]],List)!="NA"),]
AVBA = paste(A[[2]],"_",A[[1]],sep='')
List = c(AVBA)
List = data.frame(X=List[duplicated(List)])
List = List %>% separate(X, c("A", "B"),'_')
ListVBA = paste(List[[2]],"_",List[[1]],sep='')
remove Lift == right
List = List[-which(match(ListVBA)-c(1: nrow(List))==0),]
List = List[match(ListVBA)-c(1: nrow(List))>0,]
A = A[-na.omit(match(ListVAB)),]
write.table(data.frame(A[1:2]),"Output",sep='\t',quote=F,col.names=F,row.names=F)
'''
for delete duplicates and combind rest of colums
'''
RM_du <-function(A){
AVBA = paste(A[[2]],"_",A[[1]],sep='')
##
Num=0
Num= Num+1
## Get the Duplicate list
i = unique(AVAB == AVBA == AVAB)[-1]){
Num= Num+1
## Get the Duplicate list
List1 = which(AVAB[1])
List1 = c(List1,which(AVAB[1]))
TMP = A[List1,]
TMP_R = data.frame(TMP[1,1:2],V3 = paste(unique(as.character(TMP[,3])), collapse='|'))
Result = rbind(Result,TMP_R)
A = A[-List1,]
print(Num)
}
return(Result)
}
```

```r
install package from source
install.packages("/data/data/com.termux/files/home/ggradar",repos = NULL)
function
myfunction <- function(arg1, arg2, ... ){
statements
return(object)
}
remove all variable
rm(list = setdiff(ls(), lsf.str()))
calculate "spend"  by Type
A_radar = with(A[c(6,3)], tapply(spend, list(Type), sum))
match
c('aa','ab','c') %in% c('aa','c')
###system.time()
I = 0
system.time(for(i in (1:1000000000)){I = I + i})
T1<- Sys.time()
ggplot() + geom_bar(aes(x=A,y=B),stat='identity')
T2<- Sys.time()
T2 - T1
Time_A = time.time()
plt.bar(A, B)
plt.show()
Time = time.time() - Time_A
print(Time)
logarithms
exp(value)
Split a column
library(stringr)
str_split_fixed(before$type, "and", 2)
Batter than cbind & rbind
https://www.jianshu.com/p/a3277f29ed46
library(dplyr)
dplyr::bind_rows(data1,data2)
'''
namea value  nameb
1  海波  一波   
2  立波    接   
3  秀波  一波   
4    东去 柯震东
5      又 刘强东
6    东来 何盛东
'''
###weekdays
weekdays(as.Date('2018-3-1'))
```


## Function
```r
Shrink <-  function(Data, P){
  Num = round(nrow(world)/P)
  Data = Data[c(1:Num)*P,]
}
```

```R
world <- map_data("world")
```

![123](https://i.loli.net/2020/06/18/Q68bCHiSALvYGNO.png)

## Connect to Jupyter NoteBook

[一窗星乱银河静1 2018](https://blog.csdn.net/ICERON/article/details/82743930)

```R
# dependents for IRkernel
install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'))

# Install IRkernel from github
devtools::install_github('IRkernel/IRkernel')

# Connect to Jupyter Notebook
IRkernel::installspec()
# 或者是在系统下安装
IRkernel::installspec(user = FALSE)
```


## Errors


<pre>
Package ‘XXX’ was installed before R 4.0.0: please re-install it
</pre>

Solution: [Amleto, 2020](https://stackoverflow.com/questions/63390194/package-xxx-was-installed-before-r-4-0-0-please-re-install-it)


1. check the lib path
```r
.libPaths()
```
<pre>
[1] "/home/ken/R/x86_64-pc-linux-gnu-library/4.2" "/usr/local/lib/R/site-library"              
[3] "/usr/lib/R/site-library"                     "/usr/lib/R/library"   
</pre>
2. grab old packages names and remove old packages
```r
for(i in .libPaths()[2:4]){
    old_packages <- installed.packages(lib.loc = i )
    old_packages <- as.data.frame(old_packages)
    list.of.packages <- unlist(old_packages$Package)
    remove.packages( installed.packages( priority = "NA" )[,1] )
}
```

Actually, it doesn't work to me. Then, I just deleted `/usr/local/lib/R/site-library`. Everything is fine, now.


### cannot create

<pre>
** byte-compile and prepare package for lazy loading
Fatal error: cannot create 'R_TempDir'
</pre>

Two possibles:
1. have no write right in /tmp file (not likely)
2. Out of storage space.
