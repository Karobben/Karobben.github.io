---
title: "Data cleaning"
url: dataclean
date: 2020/05/01
toc: true
excerpt: "Tricks for Data cleaning in R"
tags: [R, Statistic]
category: [R, Data, Data Clean ]
cover: 'https://www.r-project.org/Rlogo.png'
thumbnail: 'https://www.r-project.org/Rlogo.png'
priority: 10000
---

## Data cleaning


## Date

```r
as.Date("Aug_24_2019",  "%B_%d_%Y")
as.Date("08_24_2019", "%m_%d_%y")
as.Date("08月24日2019年", "%m月%d日%y年")
```

<a name="8T9kT"></a>
## Split column by str

```r
## Split a column
library(stringr)
str_split_fixed(before$type, "_and_", 2)
```

```r
r$> print(TB)                                       
        Date Words Words_Wrong  MisRate MisRateT
1 2020-08-24   525         165 1559.486   31.43%
2 2020-08-25   449         138 1525.069   30.73%
3 2020-08-27   338          96 1409.325    28.4%
4 2020-08-28   446         131 1457.448   29.37%
5 2020-08-29   423         102 1196.511   24.11%
6 2020-08-30   368         104 1402.304   28.26%

r$> str_split_fixed(TB$Date, "-", 2)               
     [,1]   [,2]   
[1,] "2020" "08-24"
[2,] "2020" "08-25"
[3,] "2020" "08-27"
[4,] "2020" "08-28"
[5,] "2020" "08-29"
[6,] "2020" "08-30"
```


## reshape2
Raw matrix:`head(longImage)`
```R
  Var1 Var2 Var3     value
1    1    1    1 1.0000000
2    2    1    1 0.9921569
3    3    1    1 0.9882353
4    4    1    1 0.9725490
5    5    1    1 0.9686275
6    6    1    1 0.9803922
```

Reshape
```R
reshape(longImage, timevar='Var3',idvar=c('Var1','Var2'), direction='wide')
```

```R
  Var1 Var2   value.1   value.2   value.3
1    1    1 1.0000000 0.9960784 1.0000000
2    2    1 0.9921569 0.9921569 1.0000000
3    3    1 0.9882353 1.0000000 1.0000000
4    4    1 0.9725490 0.9960784 0.9960784
5    5    1 0.9686275 1.0000000 1.0000000
6    6    1 0.9803922 1.0000000 1.0000000
```

## R-dplyr

```R
library(tidyr)<br />
library(dplyr)

df <- data.frame(x = c(NA, "a.b", "a.d", "b.c","a-b"))<br />
df %>% separate(x, c("A", "B"),'-')
```


## Expression matrix

Centralize the matrix for heatmap
This codes come from **Trinity-rnaseq**

```r
Exm_center <- function(primary_data){
  primary_data = as.matrix(primary_data)
  ##transformations
  data = log2(primary_data+1)
  data = as.matrix(data) # convert to matrix
  ## Centering rows
  data = data.frame(t(scale(t(data), scale=F)))
  return (data)
}
```


## String 

### remove numbers from str

```r
string_with_numbers <- "The quick brown fox 123 jumps over the lazy dog 456"
string_without_numbers <- gsub("\\d+", "", string_with_numbers)
print(string_without_numbers)
```

<pre>
[1] "The quick brown fox  jumps over the lazy dog "
</pre>

In this example, string_with_numbers is the original string that contains numbers. The \\d+ regular expression matches one or more digits, and the gsub() function replaces all matches with an empty string. The resulting string without numbers is stored in string_without_numbers. <a title='ChatCPT'>Who said this?</a>