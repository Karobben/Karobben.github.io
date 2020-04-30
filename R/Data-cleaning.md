---
url: dataclean
---

# Data cleaning

<a name="07z5w"></a>
# Date

```r
as.Date("Aug_24_2019",  "%B_%d_%Y")
as.Date("08_24_2019", "%m_%d_%y")
as.Date("08月24日2019年", "%m月%d日%y年")
```

<a name="8T9kT"></a>
# Split column by str

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

