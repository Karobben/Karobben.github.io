---
url: rtricks2
---

# Base and tricks (maintain needed)


<a name="osNch"></a>
# Packages Install

- Install from CRAN
```r
Install.packages("ggplot2","repos" = c(CRAN="https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))
```
- Install from local fille
```R
Install.packages("/data/data/com.termux/files/home/ggradar",repos = NULL)
```

<a name="Bg1g4"></a>
## Reading from Excel
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
#
Num=0
Num= Num+1
# Get the Duplicate list
i = unique(AVAB == AVBA == AVAB)[-1]){
Num= Num+1
# Get the Duplicate list
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
##system.time()
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
##weekdays
weekdays(as.Date('2018-3-1'))
```

# Data frame


```R
Shrink <-  function(Data, P){
  Num = round(nrow(world)/P)
	Data = Data[c(1:Num)*P,]
}
```

```R
world <- map_data("world")
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580007783801-b9ff0a91-0801-49f0-959f-16830969c90e.png#align=left&display=inline&height=264&name=image.png&originHeight=264&originWidth=236&size=22009&status=done&style=none&width=236)<br />





---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
