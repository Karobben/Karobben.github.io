---
url: sxka47
---

# install package from source

install.packages("/data/data/com.termux/files/home/ggradar",repos = NULL)

<a name="function"></a>
# function
```R
myfunction <- function(arg1, arg2, ... ){
statements
return(object)
}
```
<a name="8f0e8288"></a>
## remove all variable
```R
rm(list = setdiff(ls(), lsf.str()))
```
<a name="45e3543f"></a>
## calculate "spend"  by Type
```R
A_radar = with(A[c(6,3)], tapply(spend, list(Type), sum))
```
<a name="match"></a>
# match
```R
c('aa','ab','c') %in% c('aa','c')
```
##system.time()
```R
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
```
<a name="logarithms"></a>
## logarithms
```R
exp(value)
```
<a name="3385a98a"></a>
## Split a column
```R
library(stringr)
str_split_fixed(before$type, "_and_", 2)
```
<a name="5f97668d"></a>
## Batter than cbind & rbind

[https://www.jianshu.com/p/a3277f29ed46](https://www.jianshu.com/p/a3277f29ed46)
```R
library(dplyr)
dplyr::bind_rows(data1,data2)
'''
namea value  nameb
1  海波  一波  
2  立波    接  
3  秀波  一波  
4    东去 柯震东
5      又 刘强东
6    东来 何盛东
'''

##weekdays
weekdays(as.Date('2018-3-1'))
```


---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
