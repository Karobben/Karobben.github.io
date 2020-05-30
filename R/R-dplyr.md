---
url: bms4pv
---

# R-dplyr

```R
library(tidyr)<br />
library(dplyr)

df <- data.frame(x = c(NA, "a.b", "a.d", "b.c","a-b"))<br />
df %>% separate(x, c("A", "B"),'-')
```
---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
